# Quire Design System

Quire's aesthetic compresses into one sentence: **cool canvas, sky-blue accent, serif carries hierarchy, the document feels composed.**

This is not a slide template or a UI framework. It is a constraint system for **editorial documents in print or screen-PDF form** — playbooks, white papers, resumes, single-page reports — the spiritual descendant of editorial print, adapted for AI-generated output.

---

## 1. Color

The entire system is **cold-toned and chromatically monochrome**: one accent, one canvas family, one gray scale. There is no secondary chromatic hue anywhere in the document.

### Surface

```css
--canvas:       #f6f8fb; /* Page background — cool white with hint of blue */
--canvas-soft:  #eef1f6; /* Lifted card / sidebar surface */
--rule:         #dce0e6; /* Primary divider line */
--rule-soft:    #e8ebf0; /* Secondary divider line */
```

**Forbidden**: `#ffffff` pure white (default-doc tell). Any warm-cream surface like `#faf9f5` (previous Quire heritage; now retired). Any saturated tinted background.

### Text

```css
--ink:        #16181d; /* Primary text — near-black, cool undertone */
--ink-soft:   #3d4148; /* Secondary text, table headers */
--ink-muted:  #6b6f78; /* Captions, metadata */
--ink-faint:  #8c919b; /* Page numbers, footnotes */
```

**All grays cool-toned.** In `rgb()`, every gray must follow `B ≥ G ≥ R` with the blue channel slightly higher (e.g. `rgb(107, 111, 120)`). Warm grays where `R > B` — forbidden. Pure neutral `R = G = B` — also forbidden; the system has temperature.

### Accent

```css
--accent:       #3a82c4; /* Clear-noon sky blue — single chromatic color */
--accent-tint:  #b8d6f0; /* 35 % accent + 65 % canvas */
--accent-deep:  #2a6299; /* Darker variant — links on tint, body emphasis */
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
- Saturation cap: the accent at `#3a82c4` is already at the cap. Do not invent more-saturated blues (`#0a66c2` is LinkedIn; `#0077FF` is consumer-tech; both off-limits).

---

## 2. Typography

### Stack

```css
/* Single serif handles display + body. */
--font-serif:
  "Fraunces", "Tiempos Text", "Source Serif Pro", "Iowan Old Style", Georgia,
  serif;

/* Sans only for UI chrome — eyebrows, page numbers, table headers, tags. */
--font-sans: "Inter Tight", "Inter", -apple-system, sans-serif;

/* Mono — code blocks only, with CJK fallback if document mixes Chinese. */
--font-mono: "JetBrains Mono", "SF Mono", Menlo, monospace;
```

**Why Fraunces**: it's a variable font with two unusual axes — `opsz` (optical size, 9–144) and `SOFT` (corner softness, 30–100). At display sizes set `opsz: 144, SOFT: 30` for crisp editorial titles; at body set `opsz: 14, SOFT: 50` for a slightly humanized reading texture.

If Fraunces unavailable, Tiempos Text → Source Serif Pro → Iowan Old Style → Georgia. Avoid stopping at Georgia — that's where "Word document feel" leaks in.

### Size scale (print, pt)

| Role    | Size | Weight | Line-height | Use                                |
| ------- | ---- | ------ | ----------- | ---------------------------------- |
| Display | 36   | 500    | 1.05        | Cover title, chapter divider title |
| H1      | 22   | 500    | 1.18        | Chapter / section open             |
| H2      | 16   | 500    | 1.25        | Subsection title                   |
| H3      | 13   | 500    | 1.30        | Inline section break               |
| Lead    | 11   | 400    | 1.55        | Chapter intro paragraph            |
| Body    | 10   | 400    | 1.65        | Reading body                       |
| Caption | 9    | 400    | 1.45        | Figure captions, table notes       |
| Label   | 9    | 500    | 1.30        | Eyebrows, tag pills, page corners  |
| Tiny    | 8.5  | 400    | 1.40        | Footers, metadata                  |

Screen px ≈ pt × 1.33 (10pt ≈ 13.3px). Minimum floor: web ≥ 12px, print ≥ 8.5pt.

### Weights

- **Body**: 400 only.
- **Headings & labels**: 500 only.
- **Forbidden**: 600, 700, 900. No synthetic bold. No italic body text. (`<em>` may render as upright + accent-color when needed.)

### Letter-spacing

| Context                | Value                             |
| ---------------------- | --------------------------------- |
| Display titles (24pt+) | `-0.022em ~ -0.028em`             |
| H1 / H2                | `-0.01em ~ -0.02em`               |
| Body                   | `0` (or `-0.003em` with Fraunces) |
| Eyebrows / small caps  | `+0.04em ~ +0.08em`               |
| Tag pills              | `+0.04em`                         |

The single biggest typographic mistake in AI-generated documents: **default Word-style letter-spacing on display titles**. Always tighten display titles below `-0.02em`.

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

## 4. Page archetypes (visual signals)

### Cover

- Full-bleed canvas, **or** full-bleed accent (used only on the main cover; never on chapter dividers).
- Display title at 36–48pt, weight 500, max 14ch line length.
- Eyebrow above title in sans-serif, accent color, +0.06em tracking.
- Subtitle below in serif italic-alternative (upright lighter weight if no italic).
- Page number absent on cover.

### Chapter divider

- Page-fill is `--accent-tint` (`#b8d6f0`), never the full-saturation `--accent`.
- Two text elements only: chapter number (eyebrow style) + chapter title (display size).
- No body text. No page number on dividers.
- Always positioned to start on a right-hand page (odd page number) in print binding.

### Standard content

- Cream canvas. Eyebrow at top showing chapter context (e.g. "Chapter 03 · Idea Stage").
- H1 with optional left-rule in accent color.
- Lead paragraph at 11pt, slightly muted (`--ink-soft`).
- Body paragraphs, lists, callouts, tables.
- Page number at bottom, sans-serif, `--ink-muted`.

### Stat-anchor

- Cream canvas. One oversized figure (50–80pt) as the page's visual anchor.
- Figure in accent color, weight 500, tabular-nums.
- Supporting label/sentence to the right or below in serif body size.
- Used max 2x per document — overuse turns it into an infographic.

### Comparison

- Three-column compare table (or two-column for binary choices).
- Header row uses sans-serif uppercase eyebrow style with accent border-bottom.
- Body cells in serif body size.
- Solid hex backgrounds only on cells, no rgba.

### Pull-quote

- Cream canvas, half page or more allocated to a single quotation.
- Serif at 18–22pt, weight 500, tight line-height (1.25).
- Left rule in accent color, 2pt thickness.
- Citation in sans-serif caption size below.

---

## 5. Components

### Callout

```html
<div class="callout">
  <span class="callout-label">Exercise</span>
  Body text follows directly after the label, not on a new line.
</div>
```

- Background: transparent, or `--ivory` for emphasis.
- Left border: 2pt solid accent color (`Exercise`, `Think`) or `--ink-muted` (`Note`).
- Label: sans-serif, uppercase, +0.06em tracking, accent color, 500 weight.
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

### Diagrams

Inline `<svg>` only — never embedded PNG / screenshots. Use accent + cool grays only; no second chromatic hue in chart series (secondary series use gray-scale, not a second color). (Not yet implemented in the current template.)

---

Working HTML for all page archetypes lives in `assets/templates/playbook.html` and `assets/output/quire-playbook.html`. Copy from there, do not redesign. The 10 invariants live in `SKILL.md`.
