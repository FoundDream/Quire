---
name: quire
description: 'Typeset editorial documents on cool canvas with a single sky-blue accent and serif hierarchy. First format is multi-page playbooks; the same system also handles white papers, single-page A4 reports, long-form landing pages, and HTML slide decks. Triggers on "做 playbook / 白皮书 / 报告 / landing page / 幻灯片 / editorial PDF" or "make a playbook / white paper / single-page report / landing page / slides".'
---

# Quire

A cold-toned, chromatically monochrome design system for editorial documents. Single accent (sky blue `#1cb2f5`), single serif carries hierarchy, no second color anywhere. Output formats: playbook (default), white paper, single-page report, landing page, slide deck — each a "format profile" of the same underlying system.

---

## Step 0 · Decide the document archetype

Quire targets long-form (10–80 page) documents structured as **cover → chapter dividers → content pages**, plus a few shorter format profiles (single-page, landing-page, slides) that share the same design system. Use a different skill for:

- Short letters or single articles → markdown is fine
- Decks heavier than 60 slides, or anything requiring animations / builds → use a dedicated slides tool

Confirm with the user when ambiguous. A 4-page document is a brochure, not a quire.

---

## Step 1 · The palette is locked

Quire has **one accent color, system-wide**: sky blue `#1cb2f5`. There is no palette to pick from. There is no second chromatic hue allowed anywhere in the document.

| Token            | Hex       | Use                                       |
| ---------------- | --------- | ----------------------------------------- |
| `--canvas`       | `#f7fbff` | Page background (cool white)              |
| `--ink`          | `#131b2a` | Primary text                              |
| `--accent`       | `#1cb2f5` | Eyebrows, stat figures, table rules, tags |
| `--accent-tint`  | `#c8ebfa` | Chapter divider page-fill, tag bg         |
| `--accent-deep`  | `#0d8ace` | Body links, emphasis on tint backgrounds  |

If the user requests a brand color, ask explicitly whether they want to override the system or stay on-brand-for-Quire. Quire's identity *is* this blue. Swapping it produces a different system.

For chapter divider backgrounds, use `--accent-tint`. **Never use `--accent` at full saturation as a page-fill** — that's marketing splash, not editorial.

---

## Step 2 · Compose the page sequence

A standard Quire document follows this rhythm:

```
[1]   Cover                  ← full-bleed accent or canvas + oversized title
[2]   Table of contents      ← canvas, eyebrow + numbered list
[3]   Chapter 01 divider     ← accent-tint fill, chapter number + title
[4–N] Chapter 01 content     ← canvas, h1/h2/h3/p/callout/table/blockquote
[N+1] Chapter 02 divider
…
[end] Resources / colophon   ← canvas, references and credits
```

**Clickable TOC**: each TOC row must be an `<a href="#sec-NN">` (not a `<span>`), and the section it points to must carry the matching `id`. Headless Chrome preserves these as internal GoTo links in the PDF. Inherit color and remove the underline so the row looks identical to a span. Reference patterns: `assets/output/quire-playbook.html` (`#ch-01` style) and `assets/output/quire-white-paper.html` (`#sec-01` style).

**Diagrams**: when data or process warrants visual support, use the eight inline-SVG archetypes in `references/diagrams.md`. Default bias is to *not* draw — see §0.

---

## Step 3 · Pick your starting point

Quire supports two working modes. Decide first, then proceed.

### Mode A · Template-constrained (default)

Use when your document fits one of the existing format profiles. Lowest variance, fastest path.

Pick a template:

| Profile      | Format                          | Template                             | Use for                                                                                  |
| ------------ | ------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------- |
| Playbook     | 10–80 pp, 11×8.5in landscape    | `assets/templates/playbook.html`     | Long-form editorial. `assets/output/quire-playbook.html` is an 11-page reference.         |
| White paper  | 8–30 pp, A4 portrait            | `assets/templates/white-paper.html`  | Research-style documents. `assets/output/quire-white-paper.html` is a 10-page reference. |
| Single-page  | 1 pp, A4 portrait               | `assets/templates/single-page.html`  | Briefs, posters, executive summaries. Capped at one A4 sheet.                            |
| Landing page | Continuous, A4 width, paginates | `assets/templates/landing-page.html` | Long-form scroll for web reading; no chapter dividers.                       |
| Slides       | 16:9, 1280×720, on-screen deck  | `assets/templates/slides.html`       | Talks and walk-throughs; one idea per slide, no body paragraphs.                         |

Then:

1. Replace the content with real material. Do not add new sections that don't exist in the frame — Quire's rhythm is intentional.
2. For multi-page profiles (playbook, white-paper), pick one of the content-page archetypes per chapter (spec in `references/design.md` §5):
   - **Standard** — h1 + lead + h2/h3 + paragraphs
   - **Stat-anchor** — oversized figure block as the page hero
   - **Comparison** — three-column compare table + commentary
   - **Pull-quote** — half-page editorial quote from a source

   Single-page and landing-page profiles skip archetypes — they're one continuous composition.

### Mode B · System-constrained (free-form)

Use when no template fits — manifestos, posters, scrolly case studies, invitations, custom page sizes, anything off the shelf. Higher variance, but still Quire as long as the design system (`references/design.md` §1–§4) is respected.

1. Start from a blank HTML. Load `references/design.md` in full — it is the system's source of truth (tokens, typography, spacing, strokes, components).
2. Link `assets/styles/quire-type.css` for typography, then inherit the local `:root` color / spacing / stroke tokens verbatim. Do not re-derive colors or pick new fonts — that produces a different system, not a Quire variant.
3. Decide page size, rhythm, and chrome from scratch, but stay inside the design system's hard rules. If a requirement forces you to break one, surface it to the user before proceeding — don't quietly bend the system.

Templates are one productization of Quire. Mode B is Quire without the productization.

---

## Step 4 · Verify before delivery

Run the production check before handing off the PDF:

1. **Accent color audit** — measure: highlight all elements using `--accent` on every page; if any single page has accent on > 15 % of its surface, that page is overusing it.
2. **No widows / orphans** — last paragraph of every page must have ≥ 2 lines.
3. **Callout density** — no more than two callouts (Exercise / Note / Think) per spread. Three or more breaks rhythm.
4. **Diagram audit** — every chart uses `--accent` + cool grays only, no second hue. Direct labeling, no legend. Captions are takeaways, not descriptions.

For full export instructions, see `references/production.md`.

---

## Reference docs

| File                          | When to load                                                       |
| ----------------------------- | ------------------------------------------------------------------ |
| `references/design.md`        | Full design system (color, type, spacing, archetypes, components)  |
| `references/writing.md`       | Content brain — how to write prose readers finish, trust, remember |
| `references/diagrams.md`      | Inline-SVG chart and diagram archetypes (8) + small-multiples rule |
| `references/anti-patterns.md` | Common ways AI-generated playbooks go wrong                        |
| `references/production.md`    | HTML → PDF export, font embedding, rendering pitfalls              |

Load only the file you need for the current task. Do not pre-load everything.
