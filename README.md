<div align="center">
  <h1>Quire</h1>
  <p><b>One sky-blue, five formats, no second color.</b></p>
  <p>A cold-toned, chromatically monochrome design system for editorial documents.</p>
</div>

## What it is

Quire is a constraint system for editorial documents — playbooks, white papers, single-page reports — that share one design language and produce typeset PDFs. Cool canvas, single sky-blue accent, serif carries hierarchy, no second color anywhere.

## Format profiles

| Profile      | Pages       | Format                      |
| ------------ | ----------- | --------------------------- |
| Playbook     | 10–80       | 11×8.5in landscape          |
| White paper  | 8–30        | A4 portrait                 |
| Single-page  | 1           | A4 portrait, fixed          |
| Landing page | continuous  | A4 width, flows + paginates |
| Slides       | 5–60        | 16:9 HTML deck, 1280×720    |

## Palette

```
canvas       #f6f8fb     cool white, never pure white
ink          #16181d     primary text, cool-toned near-black
accent       #3a82c4     sky blue — the only chromatic color
accent-tint  #b8d6f0     chapter divider fill, tag background
accent-deep  #2a6299     body links, AA-passing accent text
```

The accent is locked. There is no palette to pick from, and no second chromatic hue allowed.

## Structure

- **`SKILL.md`** — agent entry point: triggers, decision steps, 10 invariants
- **`CHEATSHEET.md`** — one-page quick reference
- **`references/`** — full spec (design / writing / anti-patterns / production)
- **`assets/styles/`** — shared system CSS (typography source of truth)
- **`assets/templates/`** — fillable HTML templates
- **`assets/output/`** — rendered demos (the self-introducing playbook lives here)
- **`scripts/`** — build (`build.sh`), linter (`check.py`)

## Triggers

- "做一份 playbook / 白皮书 / 报告"
- "build me a playbook / typeset a white paper / single-page report"
- "turn this content into an editorial PDF"

## What it deliberately is not

Quire is the opposite of:

- **LinkedIn** — no saturated corporate blue, no orange highlights, no personal-brand chrome
- **Default Word doc** — no pure white, no Calibri, no cool blue-gray defaults
- **Marketing brochure** — no multi-color charts, no gradients, no infographic decoration
- **Profile / dashboard UI** — no avatar circles, no badges, no card shadows, no pill buttons

## Inspired by, departed from

The repository structure was originally learned from [tw93/kami](https://github.com/tw93/kami). The current palette, single-accent rule, and anti-LinkedIn stance are Quire's own.

## License

MIT.
