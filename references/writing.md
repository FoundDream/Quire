# Quire · Writing

Prose credibility for playbooks and white papers (10–80 pages). Visual rules: `design.md`. HTML: `assets/templates/`. Failure modes: `anti-patterns.md`.

---

## Reader goals

Operators scan, sample, bail. Every sentence must earn one of:

1. **Keep reading** — worth the next page
2. **Trust** — nothing triggers doubt
3. **Remember** — they can repeat the argument a week later

Otherwise cut.

---

## Core principles

- **Data over adjectives** — survives "how much?" No number → don't write it.
- **Judgment over execution** — why you chose, what you predicted right; not what you shipped.
- **Distinctive phrasing** — your words, not earnings-call vocabulary.
- **Honest boundaries** — no inflated scope; no fake precision; credit collaborators.
- **Sources before phrasing** — verify facts before "latest", versions, or market stats. User material > official docs > filings > credible media. Conflicts → ask, don't pick.
- **Materials serve recognition** — logo / product or UI proof / accent color confirmed; mark gaps, don't substitute unrelated imagery. Figure redraws → _Schematic redrawn_; primary evidence → original + attribution.
- **Term half-life (~8–10 pages)** — define on first use; re-annotate briefly when term returns after the window; don't re-annotate inside the window.
- **CJK English density** — ≤ 1 unannotated English term per sentence; action glosses over concept labels (_rollout_ → 跑一遍生成).

---

## Playbook shape

**Arc**: cover → TOC → exec summary (≤ 1 page, 3–5 takeaways) → chapters → colophon.

**Per chapter**: claim paragraph (2–3 sentences, passes "so what?") → claim / evidence / conclusion. Inline source cues on external facts: `(Gartner, 2025)`, `per the 10-K`.

**Density**: ~1 heading + 2–4 paragraphs + ≤ 1 figure per content page; merge chapters under 40 % page fill; bottom whitespace = draft defect. ≥ 1 data point per paragraph when possible. Headlines + H1s alone should tell the story.

**Rhythm**: after > 5 lines of dense prose, break with callout, pull-quote, or figure (max 2 callouts per spread).

---

## Keep reading

- First sentence = the claim. Concrete subject, not abstraction.
- One claim per sentence; ~3 sentences per paragraph, 5 max.
- Specific beats vivid ("50-page Calibri wall" not "dense document").
- No opening ceremony — open falsifiable (`anti-patterns.md` #9).

---

## Trust

- Numbers with source inline, or name the gap ("anecdotally…", "we don't have public data…"). Cutting is valid.
- Magnitude beats false precision (`~$10M`, not `$9,876,543`).
- Commit or name the trade-off — no hedge stacks (`anti-patterns.md` #11).
- Claims should be falsifiable; one sentence for the strongest counter.
- **Owned** vs **contributed** vs **coordinated** — don't inflate.

> ✗ Strong teams build strong products.  
> ✓ Teams that ship before customer discovery fail 2× as often as teams that interview first.

---

## Remember

- Each chapter needs a **named pattern** ("the validation loop") — repeat the exact name, unify spellings of terms used 3+ times.
- Contrast sticks: "interviews for the question, prototypes for the answer."
- Prefer measured numbers and before/after (`800ms → 120ms`). Lead with what contradicts priors.

---

## Figures, emphasis, numbers

**Figure copy** (tighter than body): no slogan/bait (白搭, 一图看懂, 爆款); prefer paradigm over product names that age; caption = why it matters (tradeoff, boundary, insight) — not title restate or flow narration.

**Emphasis**: ≤ 2 `span.hl` per line; numbers or distinctive phrases only — never adjectives; color only, no extra bold (`design.md`).

**Format**: `5,000+`, `42%`, `→`, `2026.04` in tight layouts; CJK uses `「」`, half-width digits in metrics, space around Latin product names.

**Units**: spell out numbers under 10 in prose; inline citations over footnotes (else superscript + `.notes` at chapter end). Tabular-nums in stat blocks.

---

## Voice and cuts

**Voice**: thoughtful operator to operators — confident, specific, positioned. Not LinkedIn, brochure, hedge-mush, or procedural tutorial (`anti-patterns.md` #16).

**Cut on edit**: today's-world openers; "important to note"; unnamed "experts"; unlock/empower/leverage/pioneer; CN 拥抱/赋能/本质是/不仅而且; EN em-dash piles / "worth noting"; best practices without 3 named practices; adjective stacks; rhetorical questions; filler transitions; obvious confirmations; emoji. Surface cuts to the user — don't silently rewrite their substance.

Full symptom/fix pairs: `anti-patterns.md` #9–16.
