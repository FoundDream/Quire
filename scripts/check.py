#!/usr/bin/env python3
"""Quire design-system linter.

Scans Quire templates for violations of the 10 invariants.

Usage:
    python3 scripts/check.py                         # check all templates
    python3 scripts/check.py assets/templates/playbook-en.html
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "assets" / "templates"


# Patterns that indicate a violation. (regex, severity, message)
VIOLATIONS = [
    # 1. Pure white backgrounds
    (r"background\s*:\s*(#fff(fff)?|white)\b", "ERROR",
     "Pure white background — Quire uses cream #faf9f5"),

    # 2. RGBA usage (PDF rendering bug per anti-patterns.md #9)
    (r"background\s*:[^;]*rgba\s*\(", "WARN",
     "rgba() background — convert to solid hex (WeasyPrint double-rectangle bug)"),

    # 3. Drop shadows
    (r"box-shadow\s*:\s*(?!none)[^;]*[1-9]", "ERROR",
     "box-shadow detected — Quire uses rule lines, not shadows"),
    (r"text-shadow\s*:\s*(?!none)[^;]+", "ERROR",
     "text-shadow detected — forbidden"),
    (r"filter\s*:[^;]*(blur|drop-shadow)", "ERROR",
     "filter: blur / drop-shadow detected — forbidden"),

    # 4. Gradients
    (r":[^;]*linear-gradient\s*\(", "ERROR",
     "linear-gradient detected — Quire uses solid fills only"),
    (r":[^;]*radial-gradient\s*\(", "ERROR",
     "radial-gradient detected — Quire uses solid fills only"),

    # 5. Italic body
    (r"font-style\s*:\s*italic", "WARN",
     "font-style: italic — Quire forbids italic body. Use <strong> or .hl"),

    # 6. Heavy weights
    (r"font-weight\s*:\s*(700|800|900|bold)\b", "WARN",
     "font-weight 700+/bold — Quire uses 400/500 only"),

    # 7. Cool grays (Tailwind defaults)
    (r"#(e5e7eb|d1d5db|9ca3af|6b7280|4b5563|374151|1f2937|111827)\b", "WARN",
     "Tailwind cool-gray detected — use warm grays (R≥G>B)"),
    (r"#(f3f4f6|f9fafb)\b", "WARN",
     "Tailwind cool-gray surface — Quire surfaces are cream-tinted"),

    # 8. Emoji in source (rough check — flags any non-ASCII in a class= or content='')
    # Skipping this as too noisy; trust the writing.md rule
]


def check_file(path: Path) -> list[tuple[str, int, str, str]]:
    """Return list of (severity, line_num, message, snippet)."""
    issues = []
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    for pattern, severity, message in VIOLATIONS:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            # Find line number
            line_num = text.count("\n", 0, m.start()) + 1
            line = lines[line_num - 1].strip() if line_num <= len(lines) else ""
            snippet = line[:120]
            issues.append((severity, line_num, message, snippet))

    return issues


def main():
    if len(sys.argv) > 1:
        targets = [Path(arg) for arg in sys.argv[1:]]
    else:
        targets = sorted(TEMPLATES_DIR.glob("*.html"))

    if not targets:
        print("No templates found.", file=sys.stderr)
        sys.exit(1)

    total_errors = 0
    total_warns = 0

    for path in targets:
        if not path.exists():
            print(f"SKIP: {path} not found")
            continue

        issues = check_file(path)
        if not issues:
            print(f"✓ {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
            continue

        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"\n● {rel}")
        for severity, line_num, message, snippet in issues:
            marker = "✗" if severity == "ERROR" else "!"
            print(f"  {marker} L{line_num}  [{severity}]  {message}")
            print(f"        {snippet}")
            if severity == "ERROR":
                total_errors += 1
            else:
                total_warns += 1

    print(f"\n{total_errors} error(s), {total_warns} warning(s)")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
