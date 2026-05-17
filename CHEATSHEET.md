# Quire · Cheatsheet

One-page quick reference. Scan before filling a template. Full spec in `references/design.md`.

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
--canvas:       #f7fbff;   /* page background */
--canvas-soft:  #edf3fa;   /* lifted surface */
--ink:          #131b2a;   /* primary text */
--ink-soft:     #38465a;   /* secondary text */
--ink-muted:    #647184;   /* captions */
--rule:         #d3e0ed;   /* divider line */

--accent:       #1cb2f5;   /* sky blue — the only chromatic color */
--accent-tint:  #c8ebfa;   /* chapter divider fill, tag bg */
--accent-deep:  #0d8ace;   /* body links, AA-passing accent text */

--stroke-rule:   1px;      /* dividers, table rows, card border */
--stroke-accent: 1.5px;    /* under table heads */
--stroke-quote:  2px;      /* callout / pull-quote left bar */

--r-none:        0;        /* default; cards, callouts, pages */
--r-sm:          2pt;      /* tag pills */
--r-md:          3pt;      /* small components, max allowed */

/* Typography source: assets/styles/quire-type.css */
--type-editorial: "Fraunces", "Tiempos Text", "Source Serif Pro", "Iowan Old Style", Georgia, serif;
--type-interface: "Inter Tight", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
--type-code:      "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;

--type-axis-display: "opsz" 144, "SOFT" 30;
--type-axis-text:    "opsz" 14, "SOFT" 50;
```

## Format profiles

Quire is one design language, multiple output forms. Each profile inherits the palette and typography; only physical constraints and rhythm differ.

| Profile        | Pages   | Page size                   |
| -------------- | ------- | --------------------------- |
| Playbook       | 10–80   | 11×8.5in landscape          |
| White paper    | 8–30    | A4 portrait                 |
| Single-page    | 1       | A4 portrait                 |
| Landing page   | cont.   | A4 width, flows + paginates |
| Slides         | 5–60    | 16:9 HTML deck, 1280×720    |

## Anti-LinkedIn guard

Quire reads as editorial, not as a profile page. Concrete bans:

- No second chromatic hue (no orange, no green-for-success, no red-for-warning)
- No `border-radius` > 3pt
- No avatar circles, badges, signature boxes, certified-icon decorations
- No saturated corporate blue (`#0a66c2`, `#0077FF` are off-limits)
- No font weights above 500
