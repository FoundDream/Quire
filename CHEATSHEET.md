# Quire · Cheatsheet

One-page quick reference. Scan before filling a template. Full spec in `references/design.md`.

## The 10 invariants

1. Cream canvas `#faf9f5`, never pure white
2. One accent color per document, ≤ 5 % surface area
3. All grays warm-toned (yellow-brown undertone), no cool blue-grays
4. One serif family carries hierarchy; sans-serif only for UI chrome (eyebrows, page numbers, headers)
5. Two weights only: 400 / 500. No bold (600+), no italic body
6. Line-height: titles 1.05–1.20, body 1.55–1.70
7. Letter-spacing: titles `-0.02em ~ -0.03em`; eyebrows `+0.04em ~ +0.08em`; body 0
8. Chapter dividers use lightened tints, not full-saturation fills
9. No drop shadows, no gradients, no blur — depth via rule lines and tints
10. Every callout has a label; unlabelled blockquotes drift into decoration

## Page archetypes

| Type             | When to use                 | Visual signal                                          |
| ---------------- | --------------------------- | ------------------------------------------------------ |
| Cover            | Page 1 only                 | Full-bleed accent or cream + oversized title           |
| TOC              | Page 2                      | Eyebrow + numbered list with leader dots               |
| Chapter divider  | Start of each chapter       | Lightened-accent tint, chapter number + title, no body |
| Standard content | Most pages                  | h1 + lead + h2/h3 + paragraphs + callouts              |
| Stat-anchor      | Once or twice per document  | Oversized figure as page hero                          |
| Comparison       | When introducing trade-offs | Three-column compare table                             |
| Pull-quote       | Once per chapter, max       | Half-page editorial quote                              |

## Token snapshot

```css
--cream: #faf9f5;
--ink: #1a1a1a;
--ink-soft: #4a4a4a;
--rule: #d6d3c8;
--accent: #d97757; /* swap per document */
--accent-tint: #f0d5c7; /* mix 65% cream + 35% accent */

--font-serif: "Fraunces", "Tiempos Text", "Source Serif Pro", Georgia, serif;
--font-sans: "Inter Tight", "Inter", -apple-system, sans-serif;
```

## Cadence rule

Every 5–7 content pages need a visual reset: chapter divider, pull-quote page, or stat-anchor page. Founders skim — cadence keeps them in.

## Trigger → Do first

| Trigger                     | Do first                                                           |
| --------------------------- | ------------------------------------------------------------------ |
| User mentions a brand color | Verify WCAG AA contrast on cream; darken if it fails               |
| Document under 8 pages      | Suggest one-pager skill instead — Quire is for 10+ pages           |
| User wants slides           | Suggest a slides skill — Quire is for read-not-presented documents |
| User asks for "data viz"    | Use SVG inline; do not embed PNG screenshots from BI tools         |
| Document needs Chinese text | Switch to `playbook-zh.html`, use Source Han Serif as body         |

## Pre-flight checklist (run before delivery)

- [ ] Page count is even (covers + dividers prefer right-hand)
- [ ] Accent color ≤ 5 % per page, checked manually
- [ ] No widows / orphans (last paragraph of every page ≥ 2 lines)
- [ ] No more than 2 callouts per spread
- [ ] Every chapter has a divider, even short ones
- [ ] Print export tested at correct paper size (A4 or US-Letter)
- [ ] Fonts embedded in PDF (verify via `pdffonts output.pdf`)
