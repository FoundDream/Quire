<div align="center">
  <h1>Quire</h1>
  <p><b>The playbook, bound.</b></p>
  <p>A constraint system for multi-page playbooks, white papers, and editorial PDFs.</p>
</div>

## Why

A _quire_ is the printer's term for a bundle of folded sheets stitched into a single signature — the smallest unit of a bound book.

## Structure

- **`SKILL.md`** — the agent's entry point: triggers, decision steps, page-sequence rules
- **`CHEATSHEET.md`** — one-page quick reference for the 10 invariants
- **`references/`** — full design spec, component library, writing voice, anti-patterns, production runbook
- **`assets/templates/`** — bilingual HTML templates (EN + ZH) ready to fill
- **`scripts/`** — build and lint utilities, font verification, packaging

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

## Inspired by

Structure and some design principles learned from [tw93/kami](https://github.com/tw93/kami).

## License

MIT.
