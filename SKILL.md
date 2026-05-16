---
name: quire
description: 'Typeset multi-page playbooks, white papers, and editorial PDFs on a cream canvas with a single accent color and serif hierarchy. Triggers on "做 playbook / 白皮书 / 指南 / editorial PDF" or "make a playbook / white paper / long-form guide".'
---

# Quire

Constraint system for multi-page editorial PDFs. Four page archetypes: **cover · chapter divider · content · pull-quote**. Cream canvas, one accent color, serif hierarchy.

---

## Step 0 · Decide the document archetype

Quire targets long-form (10–80 page) documents structured as **cover → chapter dividers → content pages**. Use a different skill for:

- One-page resumes, single-page landing pages → use a one-pager skill
- Pure slides / keynotes → use a slides skill
- Short letters or single articles → markdown is fine

Confirm with the user when ambiguous. A 4-page document is a brochure, not a quire.

---

## Step 1 · Pick the accent color

Quire uses **one accent color per document**, applied to ≤ 5 % of total surface area (chapter eyebrows, pull-quote rules, stat figures, link underlines, table header borders).

Pre-tuned palette (all desaturated, paired with the cream canvas `#faf9f5`):

| Token           | Hex       | Mood                      |
| --------------- | --------- | ------------------------- |
| `--accent-clay` | `#d97757` | Warm, narrative (default) |
| `--accent-sage` | `#629987` | Calm, operations-focused  |
| `--accent-iris` | `#827dbd` | Strategic, future-facing  |
| `--accent-ink`  | `#1B365D` | Formal, financial         |
| `--accent-rust` | `#a04b3a` | Editorial, opinionated    |

If the user mentions a brand color, use it directly — but verify the hex value passes WCAG AA on cream (`#faf9f5`). If contrast fails, darken to the closest accessible variant before applying.

For chapter divider backgrounds, derive a **lightened tint** of the accent (mix 65 % cream + 35 % accent) — never use the accent at full saturation as a page-fill.

---

## Step 2 · Compose the page sequence

A standard Quire document follows this rhythm:

```
[1]   Cover                  ← full-bleed accent or cream + oversized title
[2]   Table of contents      ← cream, eyebrow + numbered list
[3]   Chapter 01 divider     ← lightened-accent tint, chapter number + title
[4–N] Chapter 01 content     ← cream, h1/h2/h3/p/callout/table/blockquote
[N+1] Chapter 02 divider
…
[end] Resources / colophon   ← cream, references and credits
```

**Rule of cadence**: every 5–7 content pages need one visual reset — a chapter divider, a full-page pull-quote, or a stat-block page.

---

## Step 3 · Fill the template

1. Open `assets/templates/playbook-en.html` (English) as the starting frame.
2. Replace the `{{PLACEHOLDER}}` tokens with real content. Do not add new sections that don't exist in the frame — Quire's rhythm is intentional.
3. For each chapter, use one of the four content-page archetypes from `references/components.md`:
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

| File                          | When to load                                                 |
| ----------------------------- | ------------------------------------------------------------ |
| `references/design.md`        | Full design system (color, type, spacing, the 10 invariants) |
| `references/components.md`    | Page archetypes and HTML snippets for each                   |
| `references/writing.md`       | Content brain — how to write prose readers finish, trust, remember |
| `references/anti-patterns.md` | Common ways AI-generated playbooks go wrong                  |
| `references/production.md`    | HTML → PDF export, font embedding, print pitfalls            |

Load only the file you need for the current task. Do not pre-load everything.

---

## The 10 invariants

These are the rules Quire will not break. Each has a real cost — think before overriding.

1. **Cream canvas `#faf9f5`**, never pure white.
2. **One accent color** per document, ≤ 5 % surface area.
3. **All grays are warm-toned** (R ≥ G > B). No cool blue-grays.
4. **One serif family** carries hierarchy (display + body). Sans-serif only for eyebrows, page numbers, table headers, and tags.
5. **Two weights only**: 400 regular, 500 medium. No 600+, no synthetic bold, no italic body text.
6. **Line-height**: titles 1.05–1.20, body 1.55–1.70.
7. **Letter-spacing**: display titles `-0.02em ~ -0.03em`; eyebrows and small caps `+0.04em ~ +0.08em`; body 0.
8. **Chapter dividers** use lightened accent tints, never full-saturation page fills.
9. **No drop shadows, no gradients, no blur effects.** Depth comes from rule lines and warm tints.
10. **Every callout has a label** (Exercise / Note / Think / Warning). Unlabelled blockquotes drift into decoration.
