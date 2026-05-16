<div align="center">
  <h1>Quire</h1>
  <p><b>The playbook, bound.</b></p>
  <p>A constraint system for multi-page founder playbooks, white papers, and editorial PDFs.</p>
</div>

## Why

Founder playbooks have a problem: the content is usually thoughtful, but the typesetting collapses into either a generic Word document or an over-designed marketing brochure. The middle ground — _a document that reads like a book_ — gets skipped because it requires a real design system.

Quire fills that gap: one constraint language, four page archetypes, an accent palette of five pre-tuned colors, and an opinionated content rhythm that founders can actually ship without an in-house designer.

## What you get

- **`SKILL.md`** — the agent's entry point: triggers, decision steps, page-sequence rules
- **`CHEATSHEET.md`** — one-page quick reference for the 10 invariants
- **`references/`** — full design spec, component library, writing voice, anti-patterns, production runbook
- **`assets/templates/`** — bilingual HTML templates (EN + ZH) ready to fill
- **`assets/demos/`** — example output PDFs to show the user what to expect
- **`scripts/`** — build and lint utilities, font verification, packaging

## Page archetypes

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **Cover**            | Full-bleed accent or cream, oversized title, single subtitle |
| **TOC**              | Numbered list with leader dots, eyebrow header               |
| **Chapter divider**  | Lightened-accent tint, chapter number + title only           |
| **Standard content** | h1 + lead + h2/h3 + body + callouts                          |
| **Stat-anchor**      | Oversized figure as page hero, used 1–2x per doc             |
| **Comparison**       | Three-column compare table                                   |
| **Pull-quote**       | Half-page editorial quote                                    |

## Accent palette

```
clay   #d97757    warm, narrative (default)
sage   #629987    calm, operations-focused
iris   #827dbd    strategic, future-facing
ink    #1B365D    formal, financial
rust   #a04b3a    editorial, opinionated
```

One accent color per document, ≤ 5 % of total surface area. Chapter dividers use the lightened tint.

## Triggers

In any chat, Quire activates on:

- "做一份 playbook / 白皮书 / founder 指南"
- "build me a playbook / typeset a white paper / make this a founder's guide"
- "turn this content into an editorial PDF / chapter dividers"
- Mentions of multi-page editorial output ≥ 10 pages

## Lineage

A _quire_ is the printer's term for a bundle of folded sheets stitched into a single signature — the smallest unit of a bound book. Quire is built for the moment a founder's argument needs to feel like a book, not a slide deck.

## License

MIT.
