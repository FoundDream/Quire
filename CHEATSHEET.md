# Quire · Cheatsheet

One-page quick reference. Scan before filling a template. Full spec in `references/design.md`.

## The 10 invariants

1. Cool canvas `#f6f8fb`, never pure white, never a warm cream
2. Sky blue `#3a82c4` is the only chromatic color — no second hue
3. All grays cool-toned (`B ≥ G ≥ R`), no warm yellow-brown grays
4. One serif family carries hierarchy; sans-serif only for UI chrome
5. Two weights only: 400 / 500. No bold (600+), no italic body
6. Typography mechanics: titles tight (-0.02em+), eyebrows loose (+0.04em+), body 0; line-height 1.05–1.20 / 1.55–1.70
7. Chapter dividers use `--accent-tint`, never full-saturation fills
8. No shadows, no gradients, no blur. `border-radius` ≤ 3pt
9. No personal-brand chrome — no avatars, badges, signature boxes, italic quote cards
10. Every callout has a label; unlabelled blockquotes drift into decoration

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
