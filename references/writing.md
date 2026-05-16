# Quire · Writing — the content brain

Quire's design system handles "looks professional." This file handles "reads credibly."
Typography tells the reader *this is a serious document*; writing tells them
*this is worth your time, you can trust it, you'll remember it.*

For visual rules see `design.md`. For component HTML see `components.md`.

---

## The three reader goals

Professional readers — operators, founders, investors, technical leads — don't read
linearly. They scan, sample, and bail. Quire writing optimizes for three outcomes,
in order:

1. **They keep reading** — every page passes the "is this worth the next page?" test
2. **They trust the claims** — no single moment makes them doubt the rest
3. **They remember the point** — a week later, they can repeat the argument

If a sentence doesn't earn one of these three, it's filler. Cut.

---

## 1 · Make them keep reading

### Front-load the claim

The first sentence of a paragraph is the topic sentence. Skimmers who only read
sentence one should still extract the point.

> ✗ For many years, organizations have wrestled with how AI changes their
>   processes. The answer turns out to be that…
>
> ✓ AI changes internal processes by collapsing the gap between decision
>   and action.

### Concrete subjects, not abstractions

> ✗ It is critical that the right tools are used at the right time.
>
> ✓ Founders pick the wrong tool when they default to the one they know best.

### One claim per sentence

Two `and`s or a comma-spliced second clause = split it. Long sentences hide
weak claims; short sentences expose them.

### Short paragraphs

Three sentences average. Five maximum. One-sentence paragraphs allowed for
rhythm and emphasis — use sparingly.

### Specific beats vivid

"A 50-page wall of body text in Calibri on white" beats "a dense, lengthy
document." Specifics make scenes; abstractions make fog.

---

## 2 · Make them trust the claims

### Cite numbers, not adjectives

> ✗ A surprisingly large percentage of startups fail.
>
> ✓ 42 % of startups fail because they built something nobody wanted.
>   *(CB Insights, 2024 post-mortem analysis)*

### Name the gap when the source is missing

Vague claims with confident voice lose more credibility than honest gaps.

- "Anecdotally, in our portfolio…"
- "We don't have public data on this, but…"
- "Industry estimates vary widely; the upper bound is…"

Cutting the claim is also valid.

### Take a position; hedging is fine, mush is not

Hedged AI prose ("it depends," "in many cases," "may potentially") signals the
writer doesn't actually know. Operators trust writers who commit.

> ✗ Some experts believe that AI may potentially help certain founders to
>   perhaps accelerate validation in some cases.
>
> ✓ AI accelerates validation by an order of magnitude — but only for teams
>   that already know what to validate. For teams that don't, it accelerates
>   the wrong thing.

If you can't commit, name the trade-off explicitly. Stacking hedges is the worst
of both worlds: no commitment, no clarity.

### Falsifiable beats unfalsifiable

A claim that *could be wrong* carries information. A claim that can't possibly
be disputed carries none.

> ✗ Strong teams build strong products.
>
> ✓ Teams that ship a working prototype before customer discovery fail twice
>   as often as teams that interview first.

Even if the second claim is contestable, it's worth contesting. The first is
unfalsifiable filler.

### Acknowledge the counterargument

When you state a position, devote one sentence — not more — to the strongest
counter. Readers trust writers who admit nuance more than writers who pretend
it doesn't exist.

> Even within validation-first teams, builders who skip the interview phase
> sometimes ship faster — when the problem space is already saturated and
> the question is execution, not direction.

---

## 3 · Make them remember

### Name the pattern

Operators retain ideas that have labels. "The validation loop." "Sharpening the
hypothesis." A label gives the idea an address in memory.

If a chapter introduces no named pattern, the chapter has no anchor — readers
forget it within a day.

### Vivid contrast

Memory hooks on difference. Not "various tools for various stages" — instead,
"interviews for the question, prototypes for the answer."

### Concrete numbers beat round magnitudes

"5 %" beats "a small portion." "Three days" beats "more than a day." Specific
numbers stick; vague magnitudes evaporate.

### Lead with what readers *don't* already believe

If a point confirms the reader's prior, they file it as background and forget.
If it contradicts an assumption, they remember it.

> ✗ Validation is important.
>
> ✓ Validation usually feels like progress when it's actually stalling — and
>   most teams can't tell the difference until quarter end.

### Repeat the named pattern by its exact name

If you introduced "the validation loop" on page 3, call it that — not "the
process," not "the framework" — in every later reference. Synonym drift kills
the memory hook.

---

## The voice

Quire reads as **a thoughtful operator talking to other operators**: confident,
specific, willing to take a position, allergic to filler.

Reference voices:
- Stripe Press essays — long-form, opinionated, footnoted
- Stratechery — analytical, framework-driven
- The Economist — third-person, declarative, no hedging
- a16z guides — pattern-named, prescriptive

What the voice is *not*:
- LinkedIn thought-leader — over-emphatic, formulaic
- Marketing brochure — adjective-heavy, vague
- Academic paper — passive voice, hedge-heavy
- Tutorial — procedural, pedestrian

---

## The cut list

Editor-mode pass removes:

- **"In today's [adjective] world"** — every variation
- **"It is important to note that"** — say the thing
- **"Many [experts/companies] believe"** — name who, or cut
- **"Game-changer", "revolutionize", "unlock", "empower"** — marketing residue
- **"Best practices"** unless followed by exactly 3 named practices
- **Adjective stacks** — "innovative, scalable, seamless" → pick one or none
- **Rhetorical questions in body** — make the claim directly
- **Filler transitions** — "That said,", "With that in mind,", "It's worth noting,"
- **Stacked hedges** — "perhaps potentially in some cases may"
- **Confirmations of the obvious** — "Software is built by engineers"
- **Emoji** — Quire is bound, not chatted

When the user wrote it that way, surface the cut as a suggestion; don't silently
edit substance.

---

## Numbers, citations, units

- Numbers under 10: spell out ("three founders")
- Numbers 10+: numerals ("12 founders")
- Percentages: numeral + symbol, no space ("42%")
- Currency: full unit on first mention ("$50K ARR"), short form after
- Time ranges: "3+ days", not "3 or more days"
- Tabular-nums in tables and stat blocks

Inline citations beat footnotes for editorial PDFs:

> ✓ Per CB Insights' 2024 post-mortem analysis, 42 % of failures…
>
> ✗ 42 % of failures¹ … (footnote at page bottom)

If a footnote is unavoidable, use superscript numerals + a `.notes` block at
chapter end. Page-bottom footnotes break the cream rhythm.

When the source is missing, write a hedged magnitude ("low double digits, per
industry estimates") rather than fabricating a precise number.

---

## Credibility audit — run before delivery

- [ ] Every chapter opener leads with a claim that could be contested
- [ ] Every number cites a source or names the gap
- [ ] Every chapter introduces or reinforces a named pattern
- [ ] No paragraph buries its claim past the first sentence
- [ ] No "in today's world / it is important / game-changer" residue
- [ ] At least one paragraph per chapter acknowledges the counterargument
- [ ] Every pull-quote passes the "could a thoughtful reader disagree?" test
- [ ] Named patterns are repeated by their exact name, not paraphrased
