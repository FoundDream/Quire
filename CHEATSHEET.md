# Quire · Cheatsheet

One-page quick reference. Scan before filling a template. Full spec in `references/design.md`.

## The 10 invariants

| Category | Rule                                               | Detail                                                  |
| -------- | -------------------------------------------------- | ------------------------------------------------------- |
| Color    | Cool canvas `#f6f8fb`                              | Never pure white, never a warm cream                    |
| Color    | Sky blue `#3a82c4` is the only chromatic color     | No second hue                                           |
| Color    | All grays cool-toned (`B ≥ G ≥ R`)                 | No warm yellow-brown grays                              |
| Color    | Chapter dividers use `--accent-tint`               | Never full-saturation fills                             |
| Type     | One serif family carries hierarchy                 | Sans-serif only for UI chrome                           |
| Type     | Two weights only: 400 / 500                        | No bold (600+), no italic body                          |
| Type     | Titles tight (-0.02em+), eyebrows loose (+0.04em+) | Line-height 1.05–1.20 / 1.55–1.70                       |
| Form     | No shadows, gradients, or blur                     | `border-radius` ≤ 3pt; strokes ≤ 2px                    |
| Form     | No personal-brand chrome                           | No avatars, badges, signature boxes, italic quote cards |
| Form     | Every callout has a label                          | Unlabelled blockquotes drift into decoration            |

## Page archetypes

| Type             | When to use                 | Visual signal                                          |
| ---------------- | --------------------------- | ------------------------------------------------------ |
| Cover            | Page 1 only                 | Full-bleed accent or canvas + oversized title          |
| TOC              | Page 2                      | Eyebrow + numbered list with leader dots               |
| Chapter divider  | Start of each chapter       | `--accent-tint` fill, chapter number + title, no body  |
| Standard content | Most pages                  | h1 + lead + h2/h3 + paragraphs + callouts              |
| Stat-anchor      | Once or twice per document  | Oversized figure as page hero                          |
| Comparison       | When introducing trade-offs | Three-column compare table                             |
| Pull-quote       | Once per chapter, max       | Half-page editorial quote                              |

## Token snapshot

```css
--canvas:       #f6f8fb;   /* page background */
--canvas-soft:  #eef1f6;   /* lifted surface */
--ink:          #16181d;   /* primary text */
--ink-soft:     #3d4148;   /* secondary text */
--ink-muted:    #6b6f78;   /* captions */
--rule:         #dce0e6;   /* divider line */

--accent:       #3a82c4;   /* sky blue — the only chromatic color */
--accent-tint:  #b8d6f0;   /* chapter divider fill, tag bg */
--accent-deep:  #2a6299;   /* body links, AA-passing accent text */

--stroke-rule:   1px;      /* dividers, table rows, card border */
--stroke-accent: 1.5px;    /* under table heads */
--stroke-quote:  2px;      /* callout / pull-quote left bar */

--r-none:        0;        /* default; cards, callouts, pages */
--r-sm:          2pt;      /* tag pills */
--r-md:          3pt;      /* small components, max allowed */

--font-serif:   "Fraunces", "Tiempos Text", "Source Serif Pro", Georgia, serif;
--font-sans:    "Inter Tight", "Inter", -apple-system, sans-serif;
```

## Format profiles

Quire is one design language, multiple output forms. Each profile inherits the palette and typography; only physical constraints and rhythm differ.

| Profile        | Pages   | Page size                  | Cadence rule              |
| -------------- | ------- | -------------------------- | ------------------------- |
| Playbook       | 10–80   | 11×8.5in landscape         | Reset every 5–7 pages     |
| White paper    | 8–30    | A4 portrait                | Reset every 5–7 pages     |
| Resume         | 1–2     | A4 / Letter portrait       | No cadence; one rhythm    |
| Single-page    | 1       | A4 portrait                | No cadence                |

## Anti-LinkedIn guard

Quire reads as editorial, not as a profile page. Concrete bans:

- No second chromatic hue (no orange, no green-for-success, no red-for-warning)
- No `border-radius` > 3pt
- No avatar circles, badges, signature boxes, certified-icon decorations
- No saturated corporate blue (`#0a66c2`, `#0077FF` are off-limits)
- No font weights above 500
