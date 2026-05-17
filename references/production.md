# Quire · Production Runbook

How to take a Quire HTML template and ship it as a PDF, with embedded fonts and no rendering surprises.

Three parts: **HTML → PDF**, **Verify**, **Pitfalls**.

---

## Part 1 · HTML → PDF

Quire supports two export paths. Pick based on your environment.

### Path A · Headless Chrome (recommended)

Best fidelity, font-embedding handled automatically, works with the shared Google Fonts import in `assets/styles/quire-type.css`.

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf-no-header \
  --print-to-pdf="output.pdf" \
  "file://$(pwd)/playbook.html"
```

Linux equivalents:

```bash
google-chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="output.pdf" "file://$(pwd)/playbook.html"
```

The `@page { size: ...; margin: 0 }` block in the template controls paper size. Make sure it matches your intended paper:

```css
@page {
  size: 11in 8.5in;
  margin: 0;
} /* US-Letter landscape */
@page {
  size: A4;
  margin: 22mm 24mm;
} /* A4 portrait */
```

### Path B · WeasyPrint (when you need full control over @page rules)

Best for documents that need running headers, page-counter strings, or strict pagination control.

```bash
weasyprint playbook.html output.pdf
```

WeasyPrint requires `@font-face` declarations with `src: url(...)` pointing to local font files in `assets/fonts/`. It does not load Google Fonts links automatically.

```css
@font-face {
  font-family: "Fraunces";
  src: url("assets/fonts/Fraunces[opsz,SOFT,wght].woff2") format("woff2");
  font-weight: 100 700;
  font-style: normal;
}
```

Run `scripts/ensure-fonts.sh` before building to verify all required font files exist.

---

## Part 2 · Verify

After export, run these checks before delivery.

### 2.1 · Embedded fonts

```bash
pdffonts output.pdf
```

Expected: every font name should show `yes` under "emb" column. If any font shows `no`, it will fall back to a system substitute on machines without that font installed.

If Fraunces shows as not embedded, verify:

1. Web-font import URL is reachable
2. `font-display: swap` is set so headless Chrome waits for fonts before printing
3. For WeasyPrint, the `@font-face` `src: url()` path resolves at build time

### 2.2 · Accent surface ratio

There's no automated tool. Manual check: open the PDF, page through, and confirm no single page has the accent color on more than 15 % of its visible surface. Chapter dividers (using lightened tint) are exempt.

If a content page is over-using accent, the most likely culprits are:

- Tag pills clustering in one paragraph (split them)
- A run of `.hl` highlights in consecutive sentences (cut to 1–2 per page)
- Stat-anchor and pull-quote on the same page (split into two pages)

### 2.3 · Widow / orphan check

Page through and look for:

- A page that ends with a single line of a paragraph (orphan top of next page = widow)
- A page that begins with a single trailing line from the previous page

In CSS, the template sets `widows: 3; orphans: 3;` to prevent this — if it's still occurring, your content is likely too dense for the page size. Either tighten leading or move a paragraph break.

### 2.4 · Color-on-color contrast

For chapter dividers (text on tint background):

- Title in `--ink` (`#131b2a`) on `--accent-tint` (`#c8ebfa`) → contrast ratio ~ 13.6 ✓
- Body link in `--accent-deep` (`#02669e`) on `--canvas` (`#fcfbf8`) → contrast ratio ~ 4.6 ✓ (just over AA 4.5)
- Eyebrow in `--accent` (`#1cb2f5`) on `--canvas` → contrast ratio ~ 2.3 (does **not** pass WCAG — use only on `--accent-tint` chapter dividers, or accept the a11y tradeoff for decorative eyebrows)

If you've changed the accent or tint, run them through a WCAG contrast checker. Minimum: 4.5 for body text, 3.0 for large titles (≥ 18pt bold or ≥ 24pt regular). For body links, use `--accent-deep`.

---

## Part 3 · 11 known pitfalls

### Pitfall 1 · WeasyPrint double rectangle on rgba tags

**Symptom**: tag pills with `background: rgba(...)` render as two stacked rectangles in PDF, fine on screen.

**Fix**: convert all rgba backgrounds to solid hex. The `--accent-tint` token (`#c8ebfa`) is pre-computed as `--accent` 35 % over `--canvas` 65 %, and should be used everywhere a translucent accent fill is wanted.

### Pitfall 2 · Headless Chrome print margin defaults

**Symptom**: `--no-margins` not respected; PDF has 0.4-inch white border.

**Fix**: must combine `@page { margin: 0 }` in CSS **and** pass `--print-to-pdf` without `--margin` flags. Newer Chrome ignores `@page` margin if you also pass `--margin-*` flags.

### Pitfall 3 · Missing CJK fallback

**Symptom**: Chinese chapter title renders as "tofu boxes" (□□□) on machines without Source Han Serif.

**Fix**: every `font-family` declaration that may contain CJK must include a fallback chain:

```css
font-family:
  "Fraunces", "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC", "STSong",
  Georgia, serif;
```

Including `@page` footer text, `pre`, `code`, and SVG `<text>` labels.

### Pitfall 4 · Fraunces variable axis not applied

**Symptom**: titles look "soft" / dumpy at large sizes — Fraunces fell back to its default axis values.

**Fix**: set `font-variation-settings` explicitly on every display-size element:

```css
.cover-title {
  font-family: var(--font-serif);
  font-variation-settings:
    "opsz" 144,
    "SOFT" 30;
}
```

Browsers do not auto-pick optical sizes — you must set the axis.

### Pitfall 5 · Page break inside a callout

**Symptom**: an Exercise callout splits across two pages with the label on one page and body on the next.

**Fix**: add `break-inside: avoid` to `.callout` and `blockquote` rules.

### Pitfall 6 · Embedded font subset missing glyphs

**Symptom**: PDF embeds fonts but a specific glyph (em-dash, fancy quote) renders as a fallback.

**Fix**: subset embedding can drop rare glyphs. Either disable subsetting (larger file) or include a "test glyph" string at the end of the document with all expected punctuation, forcing them into the subset.

### Pitfall 7 · `position: fixed` page numbers

**Symptom**: page numbers from `position: fixed` show on the wrong page or duplicate.

**Fix**: use CSS Paged Media `@page` content counters, not `position: fixed`:

```css
@page {
  @bottom-right {
    content: counter(page);
    font-family: var(--font-sans);
  }
}
```

### Pitfall 8 · Long URLs breaking the layout

**Symptom**: a citation contains a long URL that doesn't break, pushing past the right margin.

**Fix**: add `overflow-wrap: anywhere` (or `word-break: break-word` for older engines) on `.citation` and `.note` classes. Or shorten URLs to a label form.

### Pitfall 9 · Mixed pt + px units

**Symptom**: at 100 % zoom on screen everything looks fine; at PDF page scale H1 is tiny relative to the page.

**Fix**: pick one unit per template. Quire fixed-page templates: `pt` for type, `mm` for margins. Quire flowing templates: `px` / `rem` throughout.

### Pitfall 10 · Stat-figure tabular-num not applied

**Symptom**: "$1,234,567" stat figure has uneven digit spacing.

**Fix**: add `font-variant-numeric: tabular-nums` on `.stat-figure` and any `<td>` containing numbers. Without this, proportional digits cause misalignment.

### Pitfall 11 · Cover page bleeding into TOC on small screens

**Symptom**: when previewing the HTML in browser at narrow widths, cover content overflows into TOC area.

**Fix**: covers and content pages must each be wrapped in `<section class="page">` with explicit `min-height: 100vh` (screen) or fixed page height (PDF). The `page-break-after: always` rule does the rest.

---

## Build script (skeleton)

A minimal `scripts/build.sh` for users on macOS:

```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:-playbook.html}"
OUTPUT="${INPUT%.html}.pdf"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || CHROME="$(command -v google-chrome || command -v chromium)"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$OUTPUT" \
  "file://$(pwd)/$INPUT"

echo "Built: $OUTPUT"
echo "Verifying fonts..."
pdffonts "$OUTPUT" | head -20

echo "Pages:"
pdfinfo "$OUTPUT" | grep Pages
```

---

## What gets shipped

A delivered Quire document is:

- One `.pdf` file (US-Letter or A4, embedded fonts)
- One `.html` source file (so the user can re-export after edits)
- Optionally: `assets/fonts/*.woff2` if the user needs the document to be self-contained without internet

That's it. No PowerPoint export, no editable Word doc, no Figma file. Quire is for shipping typeset PDFs, not for round-tripping through other tools.
