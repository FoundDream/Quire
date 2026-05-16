# Quire Design System

Quire's aesthetic compresses into one sentence: **cream canvas, single accent, serif carries hierarchy, cadence is everything.**

This is not a slide template or a UI framework. It is a constraint system for **multi-page bound documents** — the spiritual descendant of editorial print, adapted for AI-generated output.

---

## 1. Color

### Surface

```css
--cream: #faf9f5; /* Page background — primary canvas */
--cream-soft: #f5f4ed; /* Slightly warmer fallback */
--ivory: #fffefa; /* Lifted card / sidebar */
--rule: #d6d3c8; /* Primary divider line */
--rule-soft: #e5e3d8; /* Secondary divider line */
```

**Forbidden**: `#ffffff` pure white as page background. Any `#f3f4f6` / `#f8f9fa` cool-gray surface.

### Text

```css
--ink: #1a1a1a; /* Primary text — deep but not pure black */
--ink-soft: #3d3d3a; /* Secondary text, table headers */
--ink-muted: #6b6a64; /* Captions, metadata */
--ink-faint: #8c8a82; /* Page numbers, footnotes */
```

**All grays must have a yellow-brown undertone.** In `rgb()`, warm gray follows `R ≥ G > B` with small gaps (e.g. `rgb(107, 106, 100)`). Cool gray is `R = G = B` or `R < G < B` — forbidden.

### Accent (one per document, ≤ 5 % surface)

```css
--accent-clay: #d97757;
--accent-clay-tint: #f0d5c7;
--accent-sage: #629987;
--accent-sage-tint: #bcd1ca;
--accent-iris: #827dbd;
--accent-iris-tint: #cbcadb;
--accent-ink: #1b365d;
--accent-ink-tint: #e4ecf5;
--accent-rust: #a04b3a;
--accent-rust-tint: #e6c8be;
```

**Where the accent appears**:

- Chapter eyebrows (small uppercase labels)
- Pull-quote left rule
- Stat figures (large numbers)
- Table header bottom-border
- Link underline
- Tag pill backgrounds (use the `-tint` variant, solid hex only)

**Where the accent does NOT appear**:

- Body text (always `--ink`)
- Heading text (always `--ink`, accent goes on the eyebrow above)
- Page background of content pages (always cream)

**Tint variants** are 65 % cream + 35 % accent — only used for chapter divider page-fills.

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

**Why Fraunces**: it's a variable font with two unusual axes — `opsz` (optical size, 9–144) and `SOFT` (corner softness, 30–100). At display sizes set `opsz: 144, SOFT: 30` for crisp editorial titles; at body set `opsz: 14, SOFT: 50` for warm reading texture.

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

- Full-bleed cream, **or** full-bleed accent (founder-style splash).
- Display title at 36–48pt, weight 500, max 14ch line length.
- Eyebrow above title in sans-serif, accent color, +0.06em tracking.
- Subtitle below in serif italic-alternative (upright lighter weight if no italic).
- Page number absent on cover.

### Chapter divider

- Page-fill is the **lightened tint** of the document's accent (e.g. `#f0d5c7` for clay).
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

- Background: solid hex tint (e.g. `--accent-clay-tint`), never rgba.
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

---

## 6. The 10 invariants

1. Cream canvas `#faf9f5`, never pure white.
2. One accent color per document, ≤ 5 % surface area.
3. All grays warm-toned (yellow-brown undertone), no cool blue-grays.
4. One serif family carries hierarchy; sans only for UI chrome.
5. Two weights only: 400 / 500. No bold (600+), no italic body.
6. Line-height: titles 1.05–1.20, body 1.55–1.70.
7. Letter-spacing: titles tight (-0.02em+), eyebrows loose (+0.04em+), body 0.
8. Chapter dividers use lightened tints, not full-saturation fills.
9. No drop shadows, no gradients, no blur — depth via rule lines and tints.
10. Every callout has a label; unlabelled blockquotes drift into decoration.

Violating any of these has a real cost. If a document needs to break a rule, document why in a `# Style note` comment at the top of the HTML.
