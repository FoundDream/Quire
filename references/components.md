# Quire Components

Page-level archetypes and reusable HTML snippets. Copy directly into a template; do not redesign.

For visual rules, see `design.md`. For prose credibility, see `writing.md`.

---

## Page archetypes

Each archetype is a `<section class="page ...">` block. Inside, the structure is fixed.

### 1. Cover

```html
<section class="page cover cover-main bg-clay">
  <p class="chapter-num">A Founder's Playbook · 2026</p>
  <h1 class="cover-title">Building an AI-Native Startup</h1>
  <p class="subtitle">The startup lifecycle, rebooted for the agentic era.</p>
  <span class="page-num"></span>
</section>
```

Variants:
- `bg-clay` / `bg-sage` / `bg-iris` / `bg-ink` / `bg-rust` — full-bleed accent
- (no `bg-*` class) — cream cover, accent only on eyebrow

Rules:
- Title max 14ch per line (use `<br>` for hard breaks if needed).
- Subtitle max 30ch.
- No page number on cover.

### 2. Table of contents

```html
<section class="page toc">
  <p class="chapter-tag">Contents</p>
  <h2>Inside this playbook</h2>
  <ol class="toc-list">
    <li><span class="num">01</span><span class="title">The startup lifecycle, rebooted</span><span class="page-ref">03</span></li>
    <li><span class="num">02</span><span class="title">What it means to be a founder</span><span class="page-ref">07</span></li>
  </ol>
</section>
```

- Use leader dots (CSS `::after { content: "·····" }`) between title and page reference.
- Numbers in accent color; titles in `--ink`; page refs in `--ink-muted`.

### 3. Chapter divider

```html
<section class="page cover bg-clay-tint">
  <p class="chapter-num">Chapter 03</p>
  <h1>Idea Stage</h1>
  <span class="page-num">08</span>
</section>
```

- Background: `bg-{accent}-tint` only — never the full-saturation accent.
- Two text elements: chapter eyebrow (sans, +0.05em tracking) and chapter title (display serif).
- Title at 60–78pt depending on length.

### 4. Standard content

```html
<section class="page content">
  <p class="chapter-tag">Chapter 03 · Idea Stage</p>
  <h2>Defining and pressure-testing the problem hypothesis</h2>

  <p class="lede">
    Lead paragraph in slightly larger size and muted color, sets up the section.
    <strong>Bold phrase for the operative claim</strong>, no italic.
  </p>

  <h3>Sub-heading</h3>
  <p>Body paragraph. Sentence-case. Active voice. Cite numbers, not adjectives.</p>

  <ul>
    <li>Bullet item, complete thought, full sentence.</li>
    <li>Second bullet, parallel grammar.</li>
  </ul>

  <span class="page-num">11</span>
</section>
```

### 5. Stat-anchor page

```html
<section class="page content content-stat">
  <p class="chapter-tag">Chapter 04 · MVP Stage</p>
  <p class="stat-eyebrow">A sobering number</p>
  <div class="stat-block">
    <span class="stat-figure">42%</span>
  </div>
  <p class="stat-supporting">
    of startups failed because they built something nobody wanted &mdash; and that was
    <em>before</em> agentic coding made shipping a prototype an afternoon's work.
  </p>
  <span class="page-num">17</span>
</section>
```

- One figure per page, never two.
- Figure size 80–140pt depending on width (single digit can go larger).
- Supporting paragraph max 32ch wide, positioned beside or below the figure.

### 6. Comparison page

```html
<section class="page content">
  <p class="chapter-tag">Chapter 03 · Idea Stage</p>
  <h2>Choosing the right surface</h2>
  <p class="lede">One-line setup for the comparison.</p>

  <table class="compare">
    <thead>
      <tr>
        <th style="width: 30%">If the task is…</th>
        <th style="width: 22%">Reach for</th>
        <th>Why</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>A quick brainstorm</td><td><strong>Chat</strong></td><td>Fast, no setup</td></tr>
      <tr><td>Research from your files</td><td><strong>Cowork</strong></td><td>Folder access, scheduled runs</td></tr>
      <tr><td>Shipping software</td><td><strong>Code</strong></td><td>Codebase access, git, dev envs</td></tr>
    </tbody>
  </table>

  <p class="caption">The three share the same engine; what changes is the workspace.</p>
  <span class="page-num">12</span>
</section>
```

- 3 columns max for printed page; collapse to 2 if cells get crowded.
- Header row in sans-serif uppercase eyebrow style.
- Body in serif.
- Caption below table sets context, never inside a cell.

### 7. Pull-quote page

```html
<section class="page content content-quote">
  <p class="chapter-tag">Chapter 02 · The founder's role</p>
  <blockquote>
    A working prototype is easy to mistake as concrete evidence that you're solving
    a real problem. It isn't. The conversations are.
    <span class="cite">— Founder's Playbook, Ch. 3</span>
  </blockquote>
  <span class="page-num">13</span>
</section>
```

- Quote at 18–22pt, weight 500, tight line-height (1.25).
- 2pt accent left rule, 14pt left padding.
- Citation in sans-serif caption size, separate line.
- Max one pull-quote page per chapter.

---

## Inline components

### Callout — Exercise / Note / Think / Warning

```html
<div class="callout">
  <span class="callout-label">Exercise</span>
  Body text immediately after the label, no line break.
</div>

<div class="callout note">
  <span class="callout-label">Note</span>
  Lower-stakes side commentary, smaller text, muted color.
</div>
```

| Variant | Border | Label color | Use |
|---|---|---|---|
| (default) | accent 2pt | accent | Exercise, Think — actionable |
| `.note` | `--ink-muted` 1pt | `--ink-muted` | Sidebar, caveat |
| `.warning` | `--accent-rust` 2pt | `--accent-rust` | Pre-mortem, gotcha |

### Tag pill

```html
<p>
  <span class="tag">CHAT</span>
  <span class="tag">COWORK</span>
  <span class="tag">CODE</span>
</p>
```

- Background: tint variant (`--accent-clay-tint`), solid hex, no rgba.
- Tracking: +0.04em.

### Inline highlight

```html
<p>The shift is <span class="hl">orchestrating agents, not writing code yourself.</span></p>
```

- `.hl` applies accent color + 500 weight to a phrase.
- Use 1–2x per page max. More than that = decoration.

### Inline quote (vs. block pull-quote)

```html
<p>The author calls this <em>"the orchestrator turn"</em> — and the framing matters.</p>
```

- `<em>` renders upright (no italic) with accent color.
- Use for terms of art, not emphasis.

---

## Diagrams (inline SVG only)

Quire does not embed PNG screenshots from BI tools. All diagrams are inline `<svg>` blocks using accent color + warm grays. Common types:

- **Process arrows** — horizontal flow with chevrons
- **Stage cards** — 3–5 cards in a row, lightened-tint backgrounds
- **Comparison matrices** — 2×2 grid with quadrant labels
- **Timelines** — horizontal axis with dot markers

Snippet for a 4-stage horizontal flow:

```html
<svg viewBox="0 0 800 100" class="diagram">
  <g font-family="Inter Tight" font-size="11" fill="var(--ink)">
    <rect x="10" y="20" width="180" height="60" fill="var(--accent-clay-tint)" rx="3"/>
    <text x="100" y="55" text-anchor="middle">Idea</text>
    <!-- repeat for MVP / Launch / Scale -->
  </g>
</svg>
```

Keep diagrams tonally consistent with the document — same accent, same warm grays, same typeface. No second design system inside Quire.

---

## What you should not build

- **Hero images** — Quire is editorial, not marketing brochure
- **Infographic-style multi-color charts** — one accent only
- **Sidebar boxes with shadows** — depth comes from rule lines
- **Decorative dingbats / emoji** — wordmarks and rule lines only
- **Background photos** — cream stays cream
