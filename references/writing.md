# Quire · Writing notes

Quire does not author book-length content. The user brings the substance — argument, data, structure. This file covers the prose Quire **does** write: chapter eyebrows, callout copy, table cells, captions, transitional sentences when filling templates.

For visual rules see `design.md`; for component HTML see `components.md`.

---

## Callout writing

| Type | Voice | Length | Example |
|---|---|---|---|
| **Exercise** | Imperative, concrete action | 2–4 sentences | "Pick the loudest signal from last week's interviews. Rewrite it as one sentence containing a metric, a magnitude, and a timeframe." |
| **Note** | Quiet, parenthetical | 1–2 sentences | "A discovery cycle that produces no killed hypotheses isn't validating — it's rationalizing the roadmap you already have." |
| **Think** | Reflective prompt | 1 sentence | "Would you bet a sprint on this hypothesis being true?" |
| **Warning** | Pre-mortem, naming the failure | 2–3 sentences | "Shipping before security review is the most common pre-launch breach." |

Every callout has a label. Unlabelled blockquotes are pull-quotes (different component, max one per chapter).

---

## Pull-quote selection

A pull-quote should be:
- A claim, not an observation
- Quotable on its own (passes the "tweet test")
- ≤ 25 words
- From a named source, or attributed to the document itself

> ✗ "AI is changing how startups work."
>
> ✓ "The founder's role becomes much less individual contributor, much more orchestrator of agents."

One pull-quote per chapter, max. Two becomes decoration.

---

## What to cut from filled copy

When filling a template with user-supplied content, Quire's editor pass removes:

- **"In today's world, …"** and every variation
- **"It is important to note that…"** — say the thing
- **"Many people believe…"** — name who, or cut
- **"Game-changer"**, **"revolutionize"**, **"unlock"**, **"empower"** — marketing residue
- **"Best practices"** unless followed by exactly 3 named practices
- **Adjective stacks** — "innovative, scalable, seamless" → pick one or none
- **Rhetorical questions in body** — make the claim directly
- **Filler transitions** — "That said, …", "With that in mind, …"
- **Emoji** — Quire is bound, not chatted

If the user wrote it that way, surface the cut as a suggestion rather than silently editing.

---

## Numbers and units

- Numbers under 10: spell out ("three founders")
- Numbers 10+: numerals ("12 founders")
- Tabular-nums in tables and stat blocks
- Currency: full unit on first mention ("$50K ARR"), short form after
- Percentages: numeral + symbol, no space ("42%")
- Time ranges: "3+ days", not "3 or more days"

---

## Citations

Inline citations beat footnotes for editorial-style PDFs:

> ✓ Per CB Insights' 2024 startup post-mortem analysis, 42% of failures…
>
> ✗ 42% of failures¹ … (footnote at page bottom)

If a footnote is unavoidable, use superscript numerals + a `.notes` block at chapter end, not page-bottom — page-bottom footnotes break the cream rhythm.
