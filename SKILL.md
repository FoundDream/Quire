---
name: quire
description: 'Typeset editorial documents on a cool canvas with a single sky-blue accent and serif hierarchy. First format is multi-page playbooks; the same system also handles resumes, white papers, and single-page A4 reports. Triggers on "做 playbook / 白皮书 / 简历 / 报告 / editorial PDF" or "make a playbook / white paper / resume / single-page report".'
---

# Quire

A cold-toned, chromatically monochrome design system for editorial documents. Single accent (sky blue `#3a82c4`), single serif carries hierarchy, no second color anywhere. Output formats: playbook (default), resume, white paper, single-page report — each a "format profile" of the same underlying system.

---

## Step 0 · Decide the document archetype

Quire targets long-form (10–80 page) documents structured as **cover → chapter dividers → content pages**. Use a different skill for:

- One-page resumes, single-page landing pages → use a one-pager skill
- Pure slides / keynotes → use a slides skill
- Short letters or single articles → markdown is fine

Confirm with the user when ambiguous. A 4-page document is a brochure, not a quire.

---

## Step 1 · The palette is locked

Quire has **one accent color, system-wide**: sky blue `#3a82c4`. There is no palette to pick from. There is no second chromatic hue allowed anywhere in the document.

| Token            | Hex       | Use                                       |
| ---------------- | --------- | ----------------------------------------- |
| `--canvas`       | `#f6f8fb` | Page background (cool white)              |
| `--ink`          | `#16181d` | Primary text                              |
| `--accent`       | `#3a82c4` | Eyebrows, stat figures, table rules, tags |
| `--accent-tint`  | `#b8d6f0` | Chapter divider page-fill, tag bg         |
| `--accent-deep`  | `#2a6299` | Body links, emphasis on tint backgrounds  |

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

**Rule of cadence**: every 5–7 content pages need one visual reset — a chapter divider, a full-page pull-quote, or a stat-block page.

---

## Step 3 · Fill the template

1. Open `assets/templates/playbook.html` (working frame) or `assets/output/quire-playbook.html` (12-page reference with all archetypes) as the starting point.
2. Replace the content with real material. Do not add new sections that don't exist in the frame — Quire's rhythm is intentional.
3. For each chapter, pick one of the four content-page archetypes (spec in `references/design.md` §4):
   - **Standard** — h1 + lead + h2/h3 + paragraphs
   - **Stat-anchor** — oversized figure block as the page hero
   - **Comparison** — three-column compare table + commentary
   - **Pull-quote** — half-page editorial quote from a source

---

## Step 4 · Verify before delivery

Run the production check before handing off the PDF:

1. **Accent color audit** — measure: highlight all elements using `--accent` on every page; if any single page has accent on > 15 % of its surface, that page is overusing it.
2. **No widows / orphans** — last paragraph of every page must have ≥ 2 lines.
3. **Callout density** — no more than two callouts (Exercise / Note / Think) per spread. Three or more breaks rhythm.

For full export instructions, see `references/production.md`.

---

## Reference docs

| File                          | When to load                                                       |
| ----------------------------- | ------------------------------------------------------------------ |
| `references/design.md`        | Full design system (color, type, spacing, archetypes, components)  |
| `references/writing.md`       | Content brain — how to write prose readers finish, trust, remember |
| `references/anti-patterns.md` | Common ways AI-generated playbooks go wrong                        |
| `references/production.md`    | HTML → PDF export, font embedding, print pitfalls                  |

Load only the file you need for the current task. Do not pre-load everything.

---

## The 10 invariants

These are the rules Quire will not break. Each has a real cost — think before overriding.

1. **Cool canvas `#f6f8fb`**, never pure white. Never a warm cream.
2. **Sky blue `#3a82c4` is the only chromatic color** in the document. No second hue — no orange engagement, no green success, no red warning.
3. **All grays cool-toned** (`B ≥ G ≥ R`). No warm yellow-brown grays. No pure-neutral `R = G = B` either.
4. **One serif family** carries hierarchy. Sans only for UI chrome (eyebrows, page numbers, table headers, tags).
5. **Two weights only**: 400 regular, 500 medium. No 600+, no synthetic bold, no italic body.
6. **Typography mechanics**: titles tight (-0.02em to -0.03em), eyebrows loose (+0.04em to +0.08em), body 0; line-heights 1.05–1.20 for titles, 1.55–1.70 for body.
7. **Chapter dividers use the `--accent-tint`**, never the full-saturation accent.
8. **No drop shadows, no gradients, no blur.** `border-radius` ≤ 3pt; strokes ≤ 2px. Depth comes from rule lines and tints, not weight.
9. **No personal-brand chrome** — no avatar circles, no signature boxes, no badges, no italic quote cards. Quire is editorial, not a profile page.
10. **Every callout has a label** (Exercise / Note / Think / Warning). Unlabelled blockquotes drift into decoration.
