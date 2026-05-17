# Quire · Anti-Patterns

How AI-generated playbooks visibly fail. Each entry: a symptom you can see, and the fix. Entries are numbered **1–16** in document order (Visual 1–4 → Diagrams 5–8 → Content 9–16).

For prose-level moves see `writing.md`. For build/export failures see `production.md`. Diagram catalog and shared rules: `diagrams.md`.

---

## Visual

| # | Name | Symptom | Fix |
| --- | --- | --- | --- |
| 1 | Word document leak | Cool canvas but body in Times / Calibri / Arial; no eyebrows, no rule lines. | Verify `assets/styles/quire-type.css` loaded and its Fraunces + Inter Tight import resolved. `pdffonts output.pdf` lists embedded fonts; a system serif in the list = fallback fired. |
| 2 | Two-color brand sprawl | Cover orange, callouts blue, table headers green — "because variety." | One accent per document. Anything additional must be a tint of the same accent. The 5% surface cap enforces this naturally. |
| 3 | Decorative blockquotes | Italicized loose paragraphs in `<blockquote>` with no label, no rule, no citation. | `<blockquote>` is the pull-quote component only (one per chapter, left rule + citation). Sidebar commentary → `.callout.note`; emphasis → `<strong>` or `.hl`. |
| 4 | Page numbers on covers and dividers | Cover page reads "01" in the corner. | Suppress with `@page:first` for the cover; `.page.cover .page-num { display: none }` for chapter dividers. First numbered page is the TOC. |

---

## Diagrams

Entries below are symptoms when `diagrams.md` rules are skipped.

| # | Name | Symptom | Fix |
| --- | --- | --- | --- |
| 5 | Second hue for a second series | Line chart: blue line for Product A, orange for Product B. Or each bar category gets its own color. | Small multiples (one panel per series, identical axes; see `diagrams.md` §1). If they won't fit: line style (solid vs dashed), `--accent` for the focal series, gray for the rest. Never a second chromatic hue — breaks SKILL.md invariant #2. |
| 6 | Donut / pie chart | 4–6 segment donut filling a third of the page, each segment a different tint. | Replace with a horizontal bar chart (`diagrams.md` §4.1). Bars are more accurate, encode rank directly, and survive the one-accent constraint. |
| 7 | Free-floating legend | Corner box: `■ Series 1   ■ Series 2   ■ Series 3`. Eye ping-pongs between legend and data. | Label data directly. End-of-line labels matching line color; bar value labels at bar ends. See `diagrams.md` §4.2. |
| 8 | Chart-library default styling leak | Drop shadows, 8pt rounded corners, Helvetica axis labels, rgba grays, watermark. Chart looks Mermaid- or Chart.js-shaped. | Hand-write inline SVG per `diagrams.md` §4. Never paste exported PNG or library-default SVG. Those defaults violate strokes, radii, color, and typography at once. |

---

## Content

The cut list lives in `writing.md`. This table adds visible symptoms and examples.

| # | Name | Symptom | Fix |
| --- | --- | --- | --- |
| 9 | Empty thought-leader opener | "In today's rapidly evolving AI landscape, founders face unprecedented challenges." | Open with a falsifiable claim: "Founders who skip validation will ship faster — and fail faster." A first sentence nobody could dispute carries zero information. |
| 10 | Adjective stack | "Our innovative, scalable, AI-native, founder-friendly approach unlocks unprecedented value." | Pick one adjective, or none. |
| 11 | Hedge soup | "Some experts believe that, in many cases, AI may potentially help certain founders to perhaps accelerate…" | Name the expert, the case, and the founder type. If you can't, cut the claim. |
| 12 | Rhetorical question carpets | Every section opens with "But what does this really mean?" / "So how do you actually do this?" | Replace each rhetorical question with the answer it was avoiding. |
| 13 | "Best practices" without practices | "Following best practices for AI-native development is essential." | Name three specific practices, or cut. |
| 14 | Tables that should be paragraphs | 2-column "Pros / Cons" with one bullet per side, half a page. | Write as prose. Tables earn space at ≥ 4 rows × ≥ 3 columns, or with parallel-keyed structure. |
| 15 | Numbers without sources | "73% of founders report higher productivity with AI tools." (No citation.) | Cite inline ("per Stripe's 2024 founder survey"); hedge ("anecdotally, in our portfolio"); or cut. |
| 16 | Procedural list cosplay | "Step 1. Open Claude. Step 2. Type your question. Step 3. Read the answer." | Quire is for frameworks and arguments, not tutorials. Procedural content → how-to format. Name patterns and trade-offs, not key sequences. |

---

## Common false alarms

These are not problems:

| Pattern | Why it's OK |
| --- | --- |
| One color across many pages | That's the rule |
| Lots of whitespace | Quire is editorial; whitespace is the design |
| Short chapters (2–3 pages) | Fine — Quire doesn't mandate chapter length |
| No images | Editorial playbooks rarely need them |
