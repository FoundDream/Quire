# Quire Design System

Quire's aesthetic compresses into one sentence: **cool canvas, sky-blue accent, serif carries hierarchy, the document feels composed.**

This is not a slide template or a UI framework. It is a constraint system for **editorial screen-PDF documents** — playbooks, white papers, single-page reports — the spiritual descendant of editorial typography, adapted for AI-generated output.

---

## 1. Color

The entire system is **cold-toned and chromatically monochrome**: one accent, one canvas family, one gray scale. There is no secondary chromatic hue anywhere in the document.

### Surface

```css
--canvas:       #f7fbff; /* Page background — cool white with hint of blue */
--canvas-soft:  #edf3fa; /* Lifted card / sidebar surface */
--rule:         #d3e0ed; /* Primary divider line */
--rule-soft:    #e2ebf3; /* Secondary divider line */
```

**Forbidden**: `#ffffff` pure white (default-doc tell). Any warm-cream surface like `#faf9f5` (previous Quire heritage; now retired). Any saturated tinted background.

### Text

```css
--ink:        #131b2a; /* Primary text — near-black, cool undertone */
--ink-soft:   #38465a; /* Secondary text, table headers */
--ink-muted:  #647184; /* Captions, metadata */
--ink-faint:  #94a3b8; /* Page numbers, footnotes */
```

**All grays cool-toned.** In `rgb()`, every gray must follow `B ≥ G ≥ R` with the blue channel meaningfully higher (e.g. `rgb(100, 113, 132)` for `--ink-muted`). Warm grays where `R > B` — forbidden. Pure neutral `R = G = B` — also forbidden; the system has temperature.

### Accent

```css
--accent:       #1cb2f5; /* Clear-noon sky blue — single chromatic color */
--accent-tint:  #c8ebfa; /* 35 % accent + 65 % canvas */
--accent-deep:  #0d8ace; /* Darker variant — links on tint, body emphasis */
```

**There is no second accent.** Anything that needs to be "different" uses gray-scale weight differentiation, not a second color.

**Where the accent appears**:

- Chapter eyebrows (small uppercase labels)
- Pull-quote left rule
- Stat figures (large numbers)
- Table header bottom-border
- Link underline (use `--accent-deep` for body links to pass WCAG AA)
- Tag pill backgrounds (use `--accent-tint`, solid hex only)
- Chapter divider page-fills (use `--accent-tint`, never the full `--accent`)

**Where the accent does NOT appear**:

- Body text (always `--ink`)
- Heading text (always `--ink`; accent goes on the eyebrow above)
- Page background of content pages (always `--canvas`)
- Any chart series that isn't the "primary" one (use grays for secondary series)

### The anti-LinkedIn guard

This palette deliberately rejects the LinkedIn aesthetic — saturated corporate blue + orange highlights + bold thought-leader typography. Concrete bans:

- No second chromatic hue, ever. No orange engagement color, no green for "success," no red for "warning."
- No personal-brand chrome — no avatar circles, no signature boxes, no badges, no certified-icon decorations.
- No accent on `border-radius` larger than 3pt — pill-shaped buttons read as profile UI.
- Saturation cap: the accent at `#1cb2f5` is already at the cap. Do not invent more-saturated blues (`#0a66c2` is LinkedIn; `#0077FF` is consumer-tech; both off-limits).

---

## 2. Typography

### Source

The canonical implementation lives in `assets/styles/quire-type.css`. Templates
and showcase pages must link that file instead of copying font stacks inline.

### Roles

```css
--type-editorial: Fraunces stack;   /* titles, body, quotes, stat figures */
--type-interface: Inter Tight stack; /* eyebrows, table heads, tags, buttons */
--type-code: JetBrains Mono stack;   /* code, version strings, page chrome */
```

Legacy aliases (`--font-serif`, `--font-sans`, `--font-mono`) are kept for
existing templates, but new work should think in roles: editorial, interface,
code.

**Why Fraunces**: it's a variable font with two unusual axes — `opsz` (optical size, 9–144) and `SOFT` (corner softness, 30–100). At display sizes set `opsz: 144, SOFT: 30` for crisp editorial titles; at body set `opsz: 14, SOFT: 50` for a slightly humanized reading texture.

If Fraunces unavailable, Tiempos Text → Source Serif Pro → Iowan Old Style → Georgia. Avoid stopping at Georgia — that's where "Word document feel" leaks in.

For Chinese documents, the same roles receive Chinese font pairing via
`:lang(zh)`: editorial adds Noto/Source Han serif; interface adds
Noto/Source Han sans.

### Type levels (pt)

| Level    | Size | Weight | Line-height | Use                                |
| -------- | ---- | ------ | ----------- | ---------------------------------- |
| Display  | 36   | 500    | 1.05        | Cover title, chapter divider title |
| Title    | 22   | 500    | 1.18        | Chapter / section open             |
| Subtitle | 16   | 500    | 1.25        | Subsection title                   |
| Body     | 10   | 400    | 1.65        | Reading body                       |
| Caption  | 9    | 400    | 1.45        | Figure captions, table notes       |
| Label    | 9    | 500    | 1.30        | Eyebrows, tag pills, page corners  |
| Tiny     | 8.5  | 400    | 1.40        | Footers, metadata                  |

Screen px ≈ pt × 1.33 (10pt ≈ 13.3px). Minimum floor: 8.5pt (≈ 11.3px).

### Weights

- **Body**: 400 only.
- **Headings & labels**: 500 only.
- **Forbidden**: 600, 700, 900. No synthetic bold. No italic body text. (`<em>` may render as upright + accent-color when needed.)

---

## 3. Spacing

Base unit: **4pt** (4px on screen).

| Tier | Value | Use                               |
| ---- | ----- | --------------------------------- |
| xs   | 3pt   | Inline adjacent elements          |
| sm   | 5pt   | Tag padding, dense layout         |
| md   | 10pt  | Component interior padding        |
| lg   | 18pt  | Between paragraphs / inside cards |
| xl   | 28pt  | Below H1 / H2 titles              |
| 2xl  | 50pt  | Between major sections            |
| 3xl  | 90pt  | Cover title to subtitle gap       |

### Page margins

| Document                     | Top    | Right  | Bottom | Left   |
| ---------------------------- | ------ | ------ | ------ | ------ |
| Standard A4 portrait         | 22mm   | 24mm   | 24mm   | 22mm   |
| Letter portrait              | 0.85in | 0.95in | 0.95in | 0.85in |
| Landscape (founder playbook) | 18mm   | 22mm   | 22mm   | 18mm   |

Asymmetric horizontal margins (left tighter than right) leave breathing room on the right edge — used for marginalia, callouts, page numbers.

---

## 4. Strokes & radii

Three line weights cover every divider, table head, and quote bar. Radii stay flat.

### Stroke weights

```css
--stroke-rule:    1px;   /* table rows, section dividers, card border */
--stroke-accent:  1.5px; /* under table heads, emphasis rule */
--stroke-quote:   2px;   /* callout left bar, pull-quote bar */
```

**Forbidden**: weights heavier than 2px. Thick borders read as boxed brochure UI, not editorial. Use whitespace and rule lines for separation, not heavier strokes.

### Border radius

```css
--r-none: 0;     /* default: cards, callouts, pages */
--r-sm:   2pt;   /* tag pills, inline labels */
--r-md:   3pt;   /* small contained components — the maximum allowed */
```

**Forbidden**: any radius greater than 3pt. Pill-shaped buttons and rounded cards read as profile-page UI; Quire is editorial typography, not app chrome.

---

## 5. Page archetypes (visual signals)

### Cover

- Full-bleed canvas, **or** full-bleed accent (used only on the main cover; never on chapter dividers).
- Display title at 36–48pt, weight 500, max 14ch line length.
- Eyebrow above title in sans-serif, accent color.
- Subtitle below in serif italic-alternative (upright lighter weight if no italic).
- Page number absent on cover.

### Chapter divider

- Page-fill is `--accent-tint` (`#c8ebfa`), never the full-saturation `--accent`.
- Two text elements only: chapter number (eyebrow style) + chapter title (display size).
- No body text. No page number on dividers.

### Standard content

- Canvas. Eyebrow at top showing chapter context (e.g. "Chapter 03 · Idea Stage").
- H1 with optional left-rule in accent color.
- Lead paragraph at 11pt, slightly muted (`--ink-soft`).
- Body paragraphs, lists, callouts, tables.
- Page number at bottom, sans-serif, `--ink-muted`.

### Stat-anchor

- Canvas. One oversized figure (50–80pt) as the page's visual anchor.
- Figure in accent color, weight 500, tabular-nums.
- Supporting label/sentence to the right or below in serif body size.
- Used max 2x per document — overuse turns it into an infographic.

### Comparison

- Three-column compare table (or two-column for binary choices).
- Header row uses sans-serif uppercase eyebrow style with accent border-bottom.
- Body cells in serif body size.
- Solid hex backgrounds only on cells, no rgba.

### Pull-quote

- Canvas, half page or more allocated to a single quotation.
- Serif at 18–22pt, weight 500, tight line-height (1.25).
- Left rule in accent color, 2pt thickness.
- Citation in sans-serif caption size below.

---

## 6. Page chrome

Running header and page number are the only marks outside the content area. Tiny, cool-toned, mono — present enough to orient, quiet enough to disappear.

### Running header

- Position: 12pt above the top edge.
- Style: `mono 8pt`, `--ink-faint`.
- Content: document name (left) · current chapter title (right).
- Landscape may compress to chapter title only when the document name is long.

### Page number

- Position: 12pt below the bottom edge, right corner.
- Style: `mono 9pt`, `--ink-faint`, `tabular-nums`.
- Suppressed on cover and chapter dividers.

### Margin rule (optional)

A 1px `--ink-faint` hairline between header and body. Use only on documents over 40 pages — long-form work benefits from a stronger visual anchor; shorter docs do not.

### Chrome by archetype

| Archetype        | Header | Page # | Notes                                     |
| ---------------- | :----: | :----: | ----------------------------------------- |
| Cover            |   —    |   —    | Title is the whole page; nothing competes |
| TOC              |   ●    |   ●    | First navigable page; full chrome         |
| Chapter divider  |   —    |   —    | Visual reset; chrome breaks the pause     |
| Standard content |   ●    |   ●    | Default; both marks present               |
| Stat-anchor      |   —    |   ●    | Drop header so figure dominates           |
| Comparison       |   ●    |   ●    | Standard chrome                           |
| Pull-quote       |   —    |   ●    | Quote needs air                           |
| Colophon         |   ●    |   ●    | Final page; full chrome closes the doc    |

---

## 7. Components

### Callout

```html
<div class="callout">
  <span class="callout-label">Exercise</span>
  Body text follows directly after the label, not on a new line.
</div>
```

- Background: transparent, or `--ivory` for emphasis.
- Left border: 2pt solid accent color (`Exercise`, `Think`) or `--ink-muted` (`Note`).
- Label: sans-serif, uppercase, accent color, 500 weight.
- Max 2 callouts per spread (two-page view).

### Table

```html
<table class="compare">
  <thead>
    <tr>
      <th>Header</th>
      …
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell</td>
      …
    </tr>
  </tbody>
</table>
```

- Headers: sans-serif uppercase eyebrow, accent color, 1pt accent border-bottom.
- Body cells: serif body size, 0.5pt rule-color border-bottom (last row borderless).
- No vertical column borders.
- Tabular-nums for any column containing numbers.

### Tag pill

```html
<span class="tag">CHAT</span>
```

- Background: `--accent-tint` (solid hex, never rgba).
- Text: sans-serif, accent color (darkened to ensure WCAG AA on tint).
- Padding: 2pt vertical, 7pt horizontal.
- Border-radius: 2pt (subtle — never pill-shaped unless the document is consumer-facing).

### Stat block

```html
<div class="stat">
  <span class="stat-figure">42%</span>
  <p class="stat-label">of startups failed because…</p>
</div>
```

- Figure: 56pt or larger, accent color, weight 500, tabular-nums, line-height 1.
- Label: 10pt body, `--ink-soft`, max 24 em width.
- Top + bottom rule in `--rule`, vertical padding 14pt.

### Inline highlight (`.hl`)

`<span class="hl">phrase</span>` → accent color + 500 weight. Max 1–2 per page; more becomes decoration.

### Term-of-art `<em>`

`<em>` renders **upright** (no italic), accent color. Use for terms of art, not emphasis.

### List

Three list variants, all serif-bodied. Use lists in body paragraphs; lists inside callouts double-structure.

**Unordered** — em-dash bullet in accent color:

```html
<ul class="list">
  <li><strong>Signal</strong> — observation from interviews, tickets, or telemetry.</li>
  <li><strong>Hypothesis</strong> — a prediction with metric, magnitude, timeframe.</li>
</ul>
```

**Ordered** — `01` `02` `03` numerals in mono accent:

```html
<ol class="list-num">
  <li>State the signal in one sentence.</li>
  <li>Rewrite it as a hypothesis.</li>
</ol>
```

**Definition** — term in accent, body in serif:

```html
<dl class="list-def">
  <dt>Signal</dt>
  <dd>An observation; not yet a claim.</dd>
</dl>
```

### Diagrams

Inline `<svg>` only — never embedded PNG / screenshots. Use accent + cool grays only; no second chromatic hue in chart series (secondary series use gray-scale, not a second color). For the eight chart and diagram archetypes (horizontal bar, annotated line, system diagram, sparkline, process flow, dot/range, 2×2 quadrant, timeline) plus the small-multiples rule for multivariate data, see `diagrams.md`.

---

Working HTML for all page archetypes lives in `assets/templates/playbook.html` and `assets/output/quire-playbook.html`. Copy from there, do not redesign.
