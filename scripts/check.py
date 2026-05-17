#!/usr/bin/env python3
"""Quire design-system linter.

Scans Quire templates and shared system CSS for violations of the 10 invariants.

Usage:
    python3 scripts/check.py                         # check all templates
    python3 scripts/check.py assets/templates/playbook.html
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "assets" / "templates"
TYPE_CSS = ROOT / "assets" / "styles" / "quire-type.css"


# Patterns that indicate a violation. (regex, severity, message)
VIOLATIONS = [
    # 1. Pure white backgrounds (invariant #1)
    (r"background\s*:\s*(#fff(fff)?|white)\b", "ERROR",
     "Pure white background — Quire uses cool canvas #f6f8fb (var(--canvas))"),

    # 2. Retired warm-cream surfaces (previous Quire era; now forbidden)
    (r"background\s*:\s*#(faf9f5|fffaf0|fdf6e3|fefae0|fdf5e6)\b", "ERROR",
     "Warm cream background — the cream era is retired; use cool canvas #f6f8fb"),

    # 3. RGBA usage (WeasyPrint double-rectangle bug per production.md #1)
    (r"background\s*:[^;]*rgba\s*\(", "WARN",
     "rgba() background — convert to solid hex (WeasyPrint double-rectangle bug)"),

    # 4. Shadows / blur / drop-shadow (invariant #8)
    (r"box-shadow\s*:\s*(?!none)[^;]*[1-9]", "ERROR",
     "box-shadow detected — Quire uses rule lines, not shadows"),
    (r"text-shadow\s*:\s*(?!none)[^;]+", "ERROR",
     "text-shadow detected — forbidden"),
    (r"filter\s*:[^;]*(blur|drop-shadow)", "ERROR",
     "filter: blur / drop-shadow detected — forbidden"),

    # 5. Gradients (invariant #8)
    (r":[^;]*linear-gradient\s*\(", "ERROR",
     "linear-gradient detected — Quire uses solid fills only"),
    (r":[^;]*radial-gradient\s*\(", "ERROR",
     "radial-gradient detected — Quire uses solid fills only"),

    # 6. Italic body (invariant #5)
    (r"font-style\s*:\s*italic", "WARN",
     "font-style: italic — Quire forbids italic body. Use <strong> or .hl"),

    # 7. Heavy weights (invariant #5: 400 / 500 only)
    (r"font-weight\s*:\s*(600|700|800|900|bold)\b", "WARN",
     "font-weight 600+ / bold — Quire uses 400 / 500 only"),

    # 8. Border-radius > 3pt or pill-shape (invariant #8: --r-md cap)
    (r"border-radius\s*:\s*([4-9]|\d{2,})(\.\d+)?\s*pt", "WARN",
     "border-radius > 3pt — Quire keeps radii ≤ --r-md (3pt). No pill chrome."),
    (r"border-radius\s*:\s*([5-9]|\d{2,})(\.\d+)?\s*px", "WARN",
     "border-radius > 4px (≈ 3pt) — Quire keeps radii ≤ --r-md (3pt)."),
    (r"border-radius\s*:\s*[1-9]\d*\s*%", "WARN",
     "border-radius with % — pill chrome; Quire keeps radii ≤ 3pt"),

    # 9. Tailwind gray hexes — these happen to be cool grays (invariant #3 allows that),
    # but using raw Tailwind values instead of Quire ink tokens is a fidelity break.
    (r"#(e5e7eb|d1d5db|9ca3af|6b7280|4b5563|374151|1f2937|111827|f3f4f6|f9fafb)\b", "WARN",
     "Tailwind gray hex — use Quire ink tokens (--ink, --ink-soft, --ink-muted, --ink-faint)"),

    # 10. Warm grays (R > B) — invariant #3 requires cool grays (B ≥ G ≥ R)
    (r"#(78716c|57534e|44403c|292524|1c1917|fafaf9|f5f5f4|e7e5e4|d6d3d1|a8a29e)\b", "ERROR",
     "Warm gray detected (R > B) — invariant #3 requires cool grays (B ≥ G ≥ R)"),
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
        if TYPE_CSS.exists():
            targets.append(TYPE_CSS)

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
