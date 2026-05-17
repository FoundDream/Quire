# Quire · Diagrams

Eight inline-SVG archetypes that survive Quire's monochrome constraint. Copy the SVG block, swap data, ship.

This file covers **what to draw, how to draw it, and when not to**. For broader visual rules (color, type, page chrome) see `design.md`. For diagram-specific anti-patterns see `anti-patterns.md` #5–8.

---

## 0 · When NOT to draw a diagram

Editorial documents under-draw, not over-draw. Before adding any visual:

- **2 numbers to compare** → write a sentence: "Adoption rose from 35 % to 92 % over four quarters."
- **1 data point** → use a `.stat` block, not a chart.
- **A textual list** → use `<ul class="list">` or `<ol class="list-num">`.
- **A process of ≤ 3 steps** → use `<ol class="list-num">`, not a flow diagram.
- **Decorative reinforcement** → if the diagram would only restate what the prose already said, cut it.

**When in doubt, ask the user**: *"Is a diagram needed here, or would a sentence do?"* Quire's bias is toward the sentence.

---

## 1 · Multivariate data → small multiples

Quire allows **one chromatic accent**. Color cannot encode a second variable. The system-level answer is **small multiples**: render N small copies of the same chart side by side, one per category, instead of one chart with N colored series.

```html
<div class="small-multiples">
  <figure class="fig fig-half"><!-- SVG: Series A --></figure>
  <figure class="fig fig-half"><!-- SVG: Series B --></figure>
  <figure class="fig fig-half"><!-- SVG: Series C --></figure>
  <figure class="fig fig-half"><!-- SVG: Series D --></figure>
</div>
```

```css
.small-multiples {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18pt;
}
.small-multiples .fig figcaption { font-size: 9pt; }
```

Rules for small multiples:

- All panels share **identical axes, scales, and ranges**. Different y-maxes per panel defeats the comparison.
- The accent encodes "this one's data"; gray ghost-lines may show all-panels-overlay context.
- Title each panel with the category only — the shared caption explains what the grid means.

Anything that resists small multiples (e.g. > 6 categories, non-aligned ranges) probably wants a table, not a chart.

---

## 2 · Shared visual rules

These apply to every archetype below. Don't restate them inside individual examples.

### Color

| Element                          | Color                                    |
| -------------------------------- | ---------------------------------------- |
| Primary series / focal element   | `var(--accent)`                          |
| Secondary series (when unavoidable) | `var(--ink-soft)`, `var(--ink-muted)`, `var(--ink-faint)` — pick by hierarchy |
| Axis baseline                    | `var(--rule)` at 1px                     |
| Tick marks, callout lines        | `var(--ink-faint)` at 1px                |
| Gridlines (if used at all)       | `var(--rule-soft)` at 0.5px, dashed `2 4` |
| Text labels                      | `var(--ink-soft)` (primary), `var(--ink-muted)` (secondary) |

**No second hue, ever.** If a second series must be distinguished and small multiples won't work, use line style (solid vs dashed) plus a gray.

### Strokes

```
hairline rule (axis, faint connectors)  1px
data line / primary stroke              1.5px
quote-style emphasis bar                2px  ← never thicker
```

### Labels

- **Direct labeling** on the data, never a legend box. If a line needs identification, put the label at the end of the line in the same color as the line.
- All numerals: `font-feature-settings: 'tnum'` for tabular alignment.
- Axis labels: sans `var(--font-sans)` 9pt, `var(--ink-muted)`, no decoration.
- Series titles inside SVGs: serif `var(--font-serif)` 11–12pt, `var(--ink)`.
- Eyebrow-style category labels (e.g. node-type "SERVICE"): sans 9pt, `letter-spacing: 1px` (~ +0.06em), accent or `--ink-muted`.

### Caption

Every diagram lives inside `<figure class="fig">` with a `<figcaption>`. Caption is the **takeaway**, not a description (see `writing.md` §caption). Format: `<span class="fig-num">Figure 03</span> Takeaway sentence.`

### Implementation

- **Inline SVG only.** Never `<img src="chart.png">`, never embedded raster, never D3 / Chart.js / Mermaid output (their default styling will leak — see `anti-patterns.md` #8).
- SVG inherits CSS variables from the page — author with `var(--accent)` etc., not hex literals.
- `role="img"` and `<title>` for accessibility.

---

## 3 · Standard sizes

Two `viewBox` ratios cover every archetype below. A third inline form (`.spark`) is the sparkline exception.

| Class       | viewBox       | When                                                |
| ----------- | ------------- | --------------------------------------------------- |
| `.fig-half` | `0 0 360 240` | Side-by-side in spread; small multiples; system / quadrant diagrams |
| `.fig-full` | `0 0 720 280` | Full content-width band: horizontal bar, line, timeline, dot-range |
| `.spark`    | varies; inline | Sparkline inside body text, sized in `em`           |

Add to your template's stylesheet:

```css
.fig { margin: 18pt 0; }
.fig-half svg, .fig-full svg { width: 100%; height: auto; display: block; }
.fig figcaption {
  margin-top: 8pt;
  font: 400 9pt/1.45 var(--font-serif);
  color: var(--ink-muted);
}
.fig figcaption .fig-num {
  display: inline-block;
  margin-right: 6pt;
  font-family: var(--font-sans);
  font-size: 9pt;
  color: var(--accent);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.spark {
  display: inline-block;
  vertical-align: -0.15em;
  width: 4.5em;
  height: 1em;
}
```

## 4 · The eight archetypes

Ordered by use frequency. Pick the one that fits the data; do not invent a ninth.

### 4.1 Horizontal bar

The single most useful chart in editorial work. Replaces 90 % of misused pie / donut charts. One series, ranked, with direct value labels.

```html
<figure class="fig fig-full">
  <svg viewBox="0 0 720 280" role="img" aria-labelledby="hbar-t">
    <title id="hbar-t">Adoption rate by segment</title>
    <!-- row labels -->
    <g font-family="var(--font-sans)" font-size="10" fill="var(--ink-soft)"
       text-anchor="end">
      <text x="100" y="40">Enterprise</text>
      <text x="100" y="92">Mid-market</text>
      <text x="100" y="144">Startup</text>
      <text x="100" y="196">Solo</text>
      <text x="100" y="248">Education</text>
    </g>
    <!-- bars -->
    <g fill="var(--accent)">
      <rect x="116" y="26" width="470" height="20"/>
      <rect x="116" y="78" width="362" height="20"/>
      <rect x="116" y="130" width="278" height="20"/>
      <rect x="116" y="182" width="174" height="20"/>
      <rect x="116" y="234" width="92"  height="20"/>
    </g>
    <!-- value labels -->
    <g font-family="var(--font-sans)" font-size="10" fill="var(--ink-muted)"
       font-feature-settings="'tnum'">
      <text x="594" y="40">94%</text>
      <text x="486" y="92">72%</text>
      <text x="402" y="144">56%</text>
      <text x="298" y="196">35%</text>
      <text x="216" y="248">18%</text>
    </g>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 01</span>
    Enterprise adoption is 5× the long-tail — top three segments carry the curve.
  </figcaption>
</figure>
```

**Variant — focal bar**: highlight one row in `--accent`, leave the others in `--ink-faint`. Use when the point is "this one stands out", not "rank order".

### 4.2 Annotated line

Time series with one or two annotations marking the moment that matters. Annotation is the point — an unannotated line is just decoration.

```html
<figure class="fig fig-full">
  <svg viewBox="0 0 720 280" role="img" aria-labelledby="line-t">
    <title id="line-t">Quarterly NDR with platform-shift annotation</title>
    <line x1="50" y1="230" x2="690" y2="230"
          stroke="var(--rule)" stroke-width="1"/>
    <g font-family="var(--font-sans)" font-size="9" fill="var(--ink-muted)"
       text-anchor="middle">
      <text x="80"  y="252">Q1·22</text>
      <text x="180" y="252">Q1·23</text>
      <text x="280" y="252">Q1·24</text>
      <text x="380" y="252">Q1·25</text>
      <text x="480" y="252">Q1·26</text>
      <text x="580" y="252">Q1·27</text>
    </g>
    <polyline fill="none" stroke="var(--accent)" stroke-width="1.5"
              points="80,200 130,190 180,180 230,178 280,150 330,128
                     380,115 430,105 480,98 530,92 580,80 630,72"/>
    <!-- annotation -->
    <circle cx="280" cy="150" r="3" fill="var(--accent)"/>
    <line x1="280" y1="146" x2="280" y2="86"
          stroke="var(--ink-faint)" stroke-width="1" stroke-dasharray="2 3"/>
    <text x="290" y="80" font-family="var(--font-sans)" font-size="9"
          fill="var(--ink-soft)">Platform v2 · Apr 2024</text>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 02</span>
    NDR inflected after the v2 launch — the slope before and after differ by 3×.
  </figcaption>
</figure>
```

### 4.3 System / node-link diagram

Boxes and arrows. Used for architecture, request flow, ownership. One focal node in accent; the rest in gray.

```html
<figure class="fig fig-half">
  <svg viewBox="0 0 360 240" role="img" aria-labelledby="sys-t">
    <title id="sys-t">Request flow</title>
    <defs>
      <marker id="arr" viewBox="0 0 8 8" refX="6" refY="4"
              markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0 1 L6 4 L0 7" fill="none"
              stroke="var(--ink-faint)" stroke-width="1"/>
      </marker>
    </defs>
    <!-- nodes -->
    <g font-family="var(--font-sans)" font-size="9" text-anchor="middle"
       letter-spacing="1">
      <rect x="20" y="100" width="80" height="50"
            fill="none" stroke="var(--ink-faint)" stroke-width="1"/>
      <text x="60" y="124" fill="var(--ink-muted)">CLIENT</text>
      <text x="60" y="142" font-family="var(--font-serif)" font-size="11"
            letter-spacing="0" fill="var(--ink-soft)">Browser</text>

      <rect x="140" y="100" width="80" height="50"
            fill="none" stroke="var(--accent)" stroke-width="1.5"/>
      <text x="180" y="124" fill="var(--accent)">SERVICE</text>
      <text x="180" y="142" font-family="var(--font-serif)" font-size="11"
            letter-spacing="0" fill="var(--ink)">API gateway</text>

      <rect x="260" y="100" width="80" height="50"
            fill="none" stroke="var(--ink-faint)" stroke-width="1"/>
      <text x="300" y="124" fill="var(--ink-muted)">DATA</text>
      <text x="300" y="142" font-family="var(--font-serif)" font-size="11"
            letter-spacing="0" fill="var(--ink-soft)">Postgres</text>
    </g>
    <!-- edges -->
    <g stroke="var(--ink-faint)" stroke-width="1" fill="none">
      <path d="M100 125 L140 125" marker-end="url(#arr)"/>
      <path d="M220 125 L260 125" marker-end="url(#arr)"/>
    </g>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 03</span>
    The API gateway is the single piece of code that owns auth — every request transits here.
  </figcaption>
</figure>
```

Keep nodes to ≤ 7. Beyond that, redesign as a table or a series of smaller diagrams.

### 4.4 Sparkline

Inline trend indicator. Appears in body text or table cells, not in its own figure block. Sized in `em` so it scales with surrounding type.

```html
<p>
  Revenue trended up
  <svg class="spark" viewBox="0 0 60 14" aria-hidden="true">
    <path d="M2 11 L12 9 L22 10 L32 7 L42 8 L52 3"
          fill="none" stroke="var(--accent)" stroke-width="1.5"/>
    <circle cx="52" cy="3" r="1.5" fill="var(--accent)"/>
  </svg>
  through six quarters, with the last quarter the strongest.
</p>
```

Sparklines have no axes, no labels, no caption. If you need any of those, use an annotated line (§4.2) instead.

### 4.5 Process flow

Linear sequence of steps with arrows. Use only for ≥ 4 steps; ≤ 3 is a numbered list (see §0).

```html
<figure class="fig fig-full">
  <svg viewBox="0 0 720 280" role="img" aria-labelledby="proc-t">
    <title id="proc-t">Validation pipeline</title>
    <defs>
      <marker id="arr-p" viewBox="0 0 8 8" refX="6" refY="4"
              markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0 1 L6 4 L0 7" fill="none"
              stroke="var(--ink-faint)" stroke-width="1"/>
      </marker>
    </defs>
    <g text-anchor="middle">
      <!-- boxes -->
      <g stroke="var(--ink-faint)" stroke-width="1" fill="none">
        <rect x="20"  y="100" width="140" height="80"/>
        <rect x="200" y="100" width="140" height="80"/>
        <rect x="380" y="100" width="140" height="80"/>
        <rect x="560" y="100" width="140" height="80"/>
      </g>
      <!-- step numbers -->
      <g fill="var(--accent)" font-family="var(--font-sans)" font-size="9"
         letter-spacing="1">
        <text x="90"  y="125">01</text>
        <text x="270" y="125">02</text>
        <text x="450" y="125">03</text>
        <text x="630" y="125">04</text>
      </g>
      <!-- step titles -->
      <g fill="var(--ink)" font-family="var(--font-serif)" font-size="12">
        <text x="90"  y="148">Signal</text>
        <text x="270" y="148">Hypothesis</text>
        <text x="450" y="148">Test</text>
        <text x="630" y="148">Decide</text>
      </g>
      <!-- step subtitles -->
      <g fill="var(--ink-muted)" font-family="var(--font-sans)" font-size="9">
        <text x="90"  y="166">Observation</text>
        <text x="270" y="166">Prediction</text>
        <text x="450" y="166">Measurement</text>
        <text x="630" y="166">Commit or kill</text>
      </g>
    </g>
    <g stroke="var(--ink-faint)" stroke-width="1" fill="none">
      <path d="M160 140 L200 140" marker-end="url(#arr-p)"/>
      <path d="M340 140 L380 140" marker-end="url(#arr-p)"/>
      <path d="M520 140 L560 140" marker-end="url(#arr-p)"/>
    </g>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 05</span>
    Four steps, one decision at the end. Everything before step 04 is reversible.
  </figcaption>
</figure>
```

### 4.6 Dot / range plot

Shows distributions: median (dot) plus an inter-quartile or min-max range (line). Replaces stacked bars and the "error bars on bar chart" anti-pattern.

```html
<figure class="fig fig-full">
  <svg viewBox="0 0 720 280" role="img" aria-labelledby="dot-t">
    <title id="dot-t">P25–P75 latency range with median, by quarter</title>
    <g font-family="var(--font-sans)" font-size="10" fill="var(--ink-soft)"
       text-anchor="end">
      <text x="100" y="58">Q1</text>
      <text x="100" y="116">Q2</text>
      <text x="100" y="174">Q3</text>
      <text x="100" y="232">Q4</text>
    </g>
    <!-- range bars -->
    <g stroke="var(--ink-faint)" stroke-width="2" stroke-linecap="round">
      <line x1="200" y1="58"  x2="420" y2="58"/>
      <line x1="240" y1="116" x2="490" y2="116"/>
      <line x1="280" y1="174" x2="560" y2="174"/>
      <line x1="310" y1="232" x2="610" y2="232"/>
    </g>
    <!-- median dots -->
    <g fill="var(--accent)">
      <circle cx="320" cy="58"  r="4"/>
      <circle cx="380" cy="116" r="4"/>
      <circle cx="430" cy="174" r="4"/>
      <circle cx="470" cy="232" r="4"/>
    </g>
    <!-- x-axis baseline -->
    <line x1="116" y1="262" x2="700" y2="262"
          stroke="var(--rule)" stroke-width="1"/>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 06</span>
    Median latency climbs each quarter, but the spread climbs faster — the slow tail is the problem.
  </figcaption>
</figure>
```

### 4.7 2×2 quadrant

Editorial concept tool. Two axes, four labeled regions, optional focal quadrant in accent.

```html
<figure class="fig fig-half">
  <svg viewBox="0 0 360 240" role="img" aria-labelledby="q-t">
    <title id="q-t">Effort × Impact</title>
    <rect x="40" y="40" width="300" height="160"
          fill="none" stroke="var(--rule)" stroke-width="1"/>
    <g stroke="var(--ink-faint)" stroke-width="0.5">
      <line x1="190" y1="40"  x2="190" y2="200"/>
      <line x1="40"  y1="120" x2="340" y2="120"/>
    </g>
    <!-- axes -->
    <g font-family="var(--font-sans)" font-size="9" fill="var(--ink-muted)"
       letter-spacing="1">
      <text x="190" y="222" text-anchor="middle">EFFORT →</text>
      <text x="22"  y="120" text-anchor="middle"
            transform="rotate(-90 22 120)">IMPACT →</text>
    </g>
    <!-- quadrant labels -->
    <g font-family="var(--font-serif)" font-size="12" text-anchor="middle">
      <text x="115" y="82" fill="var(--accent)">Quick wins</text>
      <text x="265" y="82" fill="var(--ink-soft)">Big bets</text>
      <text x="115" y="168" fill="var(--ink-muted)">Fill-in</text>
      <text x="265" y="168" fill="var(--ink-muted)">Thankless</text>
    </g>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 07</span>
    Quick wins this quarter; big bets next. The two lower quadrants stay on the kill list.
  </figcaption>
</figure>
```

The accent goes on the focal quadrant — the one the document is recommending. If no quadrant is focal, use `--ink-soft` for all four; the diagram becomes a frame, not a recommendation.

### 4.8 Timeline

Horizontal axis with event markers. Labels alternate above / below to avoid collision.

```html
<figure class="fig fig-full">
  <svg viewBox="0 0 720 280" role="img" aria-labelledby="tl-t">
    <title id="tl-t">Funding timeline</title>
    <line x1="40" y1="160" x2="690" y2="160"
          stroke="var(--rule)" stroke-width="1"/>
    <!-- year ticks -->
    <g stroke="var(--ink-faint)" stroke-width="1">
      <line x1="80"  y1="156" x2="80"  y2="164"/>
      <line x1="240" y1="156" x2="240" y2="164"/>
      <line x1="400" y1="156" x2="400" y2="164"/>
      <line x1="560" y1="156" x2="560" y2="164"/>
    </g>
    <g font-family="var(--font-sans)" font-size="9" fill="var(--ink-muted)"
       text-anchor="middle">
      <text x="80"  y="184">2023</text>
      <text x="240" y="184">2024</text>
      <text x="400" y="184">2025</text>
      <text x="560" y="184">2026</text>
    </g>
    <!-- event dots -->
    <g fill="var(--accent)">
      <circle cx="130" cy="160" r="4"/>
      <circle cx="320" cy="160" r="4"/>
      <circle cx="500" cy="160" r="4"/>
      <circle cx="640" cy="160" r="4"/>
    </g>
    <!-- connectors -->
    <g stroke="var(--ink-faint)" stroke-width="1" stroke-dasharray="2 3">
      <line x1="130" y1="156" x2="130" y2="102"/>
      <line x1="320" y1="164" x2="320" y2="218"/>
      <line x1="500" y1="156" x2="500" y2="102"/>
      <line x1="640" y1="164" x2="640" y2="218"/>
    </g>
    <!-- labels -->
    <g font-family="var(--font-sans)" font-size="10" fill="var(--ink-soft)"
       text-anchor="middle">
      <text x="130" y="94">Seed · $2M</text>
      <text x="320" y="232">Series A · $12M</text>
      <text x="500" y="94">Series B · $40M</text>
      <text x="640" y="232">IPO</text>
    </g>
  </svg>
  <figcaption>
    <span class="fig-num">Figure 08</span>
    Three rounds in 18 months, then a 14-month gap to IPO — the inflection is the gap, not the rounds.
  </figcaption>
</figure>
```

---

## 5 · Quick reference

| Need                              | Use                          |
| --------------------------------- | ---------------------------- |
| Ranked comparison, one series     | Horizontal bar (§4.1)        |
| Time series with key moment       | Annotated line (§4.2)        |
| Architecture, request flow        | System diagram (§4.3)        |
| Trend indicator inside prose      | Sparkline (§4.4)             |
| Sequence of ≥ 4 steps             | Process flow (§4.5)          |
| Distribution: median + range      | Dot / range plot (§4.6)      |
| Editorial concept frame           | 2×2 quadrant (§4.7)          |
| Events on a date axis             | Timeline (§4.8)              |
| > 1 categorical series            | Small multiples (§1)         |
| Donut / pie / stacked / 3D / etc. | Forbidden — see `anti-patterns.md` #5–8 |
