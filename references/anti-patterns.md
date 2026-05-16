# Quire · Anti-Patterns

How AI-generated playbooks visibly fail. Each entry: a symptom you can see, and the fix.

For prose-level moves see `writing.md`. For build/export failures see `production.md`.

---

## Visual

### 1. The Word document leak

**Symptom** — cool canvas but body in Times / Calibri / Arial; no eyebrows, no rule lines.

**Fix** — verify the Fraunces + Inter Tight web-font import loaded. `pdffonts output.pdf` lists embedded fonts; a system serif in the list = fallback fired.

### 2. Two-color brand sprawl

**Symptom** — cover orange, callouts blue, table headers green, "because variety."

**Fix** — one accent per document. Anything additional must be a tint of the same accent. The 5 % surface cap enforces this naturally.

### 3. Decorative blockquotes

**Symptom** — italicized loose paragraphs in `<blockquote>` with no label, no rule, no citation.

**Fix** — `<blockquote>` is the pull-quote component only (one per chapter, left rule + citation). For sidebar commentary use `.callout.note`; for emphasis use `<strong>` or `.hl`.

### 4. Page numbers on covers and dividers

**Symptom** — cover page reads "01" in the corner.

**Fix** — suppress with `@page:first` for the cover; `.page.cover .page-num { display: none }` for chapter dividers. First numbered page is the TOC.

---

## Diagrams

The diagram catalog and shared rules live in `diagrams.md`. The entries below are the symptoms that show up when those rules are skipped.

### 13. Second hue to encode a second series

**Symptom** — a line chart with a blue line for Product A and an orange line for Product B; or a bar chart where each category gets its own color.

**Fix** — small multiples (one panel per series, identical axes; see `diagrams.md` §1). If small multiples won't fit, use line style (solid vs dashed) with `--accent` for the focal series and a gray for the rest. Never introduce a second chromatic hue — that breaks SKILL.md invariant #2.

### 14. Donut / pie chart

**Symptom** — a 4–6 segment donut filling a third of the page, each segment in a different tinted color.

**Fix** — replace with a horizontal bar chart (see `diagrams.md` §4.1). Bars are more accurate (angle / area judgments are unreliable), they encode rank directly, and they survive the one-accent constraint without inventing extra hues.

### 15. Free-floating legend

**Symptom** — a small framed box in the corner: `■ Series 1   ■ Series 2   ■ Series 3`. Reader's eye ping-pongs between legend and data to decode.

**Fix** — label the data directly. End-of-line labels in the same color as the line; bar value labels at the end of each bar. See the annotated-line example in `diagrams.md` §4.2.

### 16. Chart-library default styling leak

**Symptom** — drop shadows behind bars, 8pt rounded corners on nodes, Helvetica in axis labels, rgba grays, a watermark in the bottom-right. The chart looks Mermaid- or Chart.js- shaped.

**Fix** — hand-write inline SVG using the archetypes in `diagrams.md` §4. Never paste exported PNG or library-default SVG into a Quire document. The styling defaults of those libraries violate strokes, radii, color, and typography rules simultaneously.

---

## Content

The cut list lives in `writing.md`. The entries below add the visible symptom and a concrete example for the patterns it names.

### 5. Empty thought-leader opener

**Symptom** — "In today's rapidly evolving AI landscape, founders face unprecedented challenges."

**Fix** — open with a falsifiable claim. "Founders who skip validation will ship faster — and fail faster." A first sentence nobody could possibly dispute carries zero information.

### 6. The adjective stack

**Symptom** — "Our innovative, scalable, AI-native, founder-friendly approach unlocks unprecedented value."

**Fix** — pick one adjective, or none.

### 7. Hedge soup

**Symptom** — "Some experts believe that, in many cases, AI may potentially help certain founders to perhaps accelerate…"

**Fix** — name the expert, the case, and the founder type. If you can't, the claim doesn't survive the editor — cut it.

### 8. Rhetorical question carpets

**Symptom** — every section opens with "But what does this really mean?" / "So how do you actually do this?"

**Fix** — replace each rhetorical question with the answer it was avoiding.

### 9. "Best practices" without practices

**Symptom** — "Following best practices for AI-native development is essential."

**Fix** — name three specific practices, or cut.

### 10. Tables that should be paragraphs

**Symptom** — a 2-column "Pros / Cons" table with one bullet per side filling half a page.

**Fix** — write it as prose. Tables earn their space at ≥ 4 rows × ≥ 3 columns, or with parallel-keyed structure.

### 11. Numbers without sources

**Symptom** — "73 % of founders report higher productivity with AI tools." (No citation.)

**Fix** — cite inline ("per Stripe's 2024 founder survey,"); or hedge explicitly ("anecdotally, in our portfolio,"); or cut.

### 12. Procedural list cosplay

**Symptom** — "Step 1. Open Claude. Step 2. Type your question. Step 3. Read the answer."

**Fix** — Quire is for frameworks and arguments, not tutorials. If content is procedural, redirect to a how-to format. Quire names patterns and trade-offs, not key sequences.

---

## Common false alarms

These are not problems:

- **One color across many pages** — that's the rule
- **Lots of whitespace** — Quire is editorial; whitespace is the design
- **Short chapters (2–3 pages)** — fine, as long as cadence is preserved
- **No images** — editorial playbooks rarely need them
