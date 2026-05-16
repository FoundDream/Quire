# Quire · Anti-Patterns

Common ways AI-generated playbooks go wrong. Each entry has a bad example, the diagnosis, and the fix.

Use alongside `writing.md` (content) and `design.md` (visual).

---

## Visual anti-patterns

### 1. The Word document leak

**Symptom**: cream canvas with Times New Roman / Calibri / Arial body, default Word margins, no eyebrows, no rule lines.

**Why it happens**: AI fell back to system fonts when Fraunces wasn't loaded, or skipped CSS variable declarations.

**Fix**: always include the full Fraunces + Inter Tight web-font import at the top of the HTML. Verify with `pdffonts output.pdf` after export — Times New Roman in the embedded font list = failed.

---

### 2. Two-color brand sprawl

**Symptom**: cover uses orange, callouts use blue, table headers use green, "because variety".

**Why it happens**: AI tried to mimic infographic templates seen during training.

**Fix**: pick one accent from the palette, use only that accent + its tint variant across the entire document. The 5 % surface-area cap forces this naturally.

---

### 3. Decorative blockquotes

**Symptom**: every other page has a `<blockquote>` with no label, no left rule, no author — just italicized loose text.

**Why it happens**: AI used `<blockquote>` as a "make this paragraph look fancy" tool.

**Fix**: blockquotes are **pull-quotes only**, max one per chapter, with mandatory left rule + citation. For sidebar commentary use `.callout.note` with a label. For emphasis use `<strong>` or `.hl`.

---

### 4. Emoji and dingbats

**Symptom**: 🚀 in cover title, ✅ in callouts, 💡 next to "Think:" labels.

**Why it happens**: AI picked up consumer-product blog conventions.

**Fix**: Quire is bound, not chatted. No emoji. No dingbats. Labels do the work.

---

### 5. RGBA tag backgrounds

**Symptom**: tag pills with `background: rgba(217, 119, 87, 0.15)` look fine on screen but render as **double rectangles** in PDF.

**Why it happens**: WeasyPrint and similar engines composite alpha layers per glyph cluster, producing visible seams.

**Fix**: always use solid hex tints. `rgba(217,119,87,0.15)` over cream = `#f0d5c7`. Compute the solid equivalent and store it as a token.

---

### 6. Page numbers on dividers and covers

**Symptom**: cover page shows "01" in the bottom corner.

**Why it happens**: CSS `@page` counter applied uniformly.

**Fix**: use `@page:first` to suppress on cover. Add `.page.cover .page-num { display: none }` for chapter dividers. First numbered page is the TOC or Chapter 01 first content page.

---

## Content anti-patterns

### 7. Empty thought-leader opener

**Symptom**:
> "In today's rapidly evolving AI landscape, founders face unprecedented challenges. This playbook will help you navigate them."

**Why it happens**: AI started in LinkedIn-essay mode.

**Fix**: open with a concrete claim that **could be wrong**. "Founders who skip validation will ship faster than ever — and fail faster." If the opening sentence couldn't possibly be disputed, it's adding zero information.

---

### 8. The adjective stack

**Symptom**:
> "Our innovative, scalable, AI-native, founder-friendly approach unlocks unprecedented value."

**Fix**: pick one adjective, or none. The stack is marketing residue. "AI-native" alone is fine; the rest is noise.

---

### 9. Hedge soup

**Symptom**: "Some experts believe that, in many cases, AI may potentially help certain founders to perhaps accelerate…"

**Fix**: name the expert, name the case, name the founder type. If you can't, the claim doesn't survive an editor — cut it.

---

### 10. Rhetorical question carpets

**Symptom**: every section begins with "But what does this really mean?" / "So how do you actually do this?" / "Where does this leave us?"

**Fix**: replace each rhetorical question with the answer it was avoiding. Rhetorical questions in body are stalling tactics.

---

### 11. The "best practices" without practices

**Symptom**: "Following best practices for AI-native development is essential."

**Fix**: either name the 3 practices ("(1) write specs first, (2) version your prompts, (3) review every commit") or cut the sentence. "Best practices" with no list is filler.

---

### 12. Tables that should be paragraphs

**Symptom**: a 2-column "Pros / Cons" table with one bullet per side, taking half a page.

**Fix**: if a comparison has fewer than 4 rows or fewer than 3 columns, write it as prose. Tables are for ≥ 4 row × ≥ 3 column data, or columns with parallel-keyed structure.

---

### 13. Numbers without sources

**Symptom**: "73% of founders report higher productivity with AI tools."

**Fix**: name the source inline ("per Stripe's 2024 founder survey,"). If no source exists, change to anecdote ("in our experience working with 50+ early-stage teams,") or cut.

---

### 14. Procedural list cosplay

**Symptom**: "Step 1. Open Claude. Step 2. Type your question. Step 3. Read the answer."

**Fix**: Quire is for **frameworks and arguments**, not tutorials. If the content is procedural, suggest a tutorial / how-to format instead. Quire prose names patterns and trade-offs, not key sequences.

---

## Production anti-patterns

### 15. Forgetting font embedding

**Symptom**: PDF looks fine on the author's Mac, looks broken on a colleague's Windows machine — Fraunces fell back to Times.

**Fix**: when exporting via headless Chrome, fonts are auto-embedded. When exporting via WeasyPrint, you must `@font-face` declare each font with a local `src: url(...)` pointing to a .woff2 in `assets/fonts/`. Verify with `pdffonts output.pdf` — every font should show "(embedded)".

---

### 16. Page count parity ignored

**Symptom**: a 35-page playbook ends with chapter content on a left page, blank back, then a colophon.

**Fix**: Quire prefers covers + chapter dividers on right-hand (odd) pages in print. If a chapter ends on a left page, insert a brief "intentionally blank" right page or move a pull-quote to fill. Page count should be even.

---

### 17. Mixing print pt and screen px

**Symptom**: H1 declared as `font-size: 22px` but margins as `2cm` — at print scale the H1 looks tiny relative to the page.

**Fix**: pick one unit system per template. Print templates: pt for type, mm for margins. Screen-only templates: px / rem throughout. Mixing units breaks the grid at zoom levels.

---

### 18. Asymmetric margins on the wrong side

**Symptom**: left margin tighter than right — fine on screen, but in print this looks unbalanced when the binding is on the left.

**Fix**: for spiral-bound or perfect-bound output, the **gutter side** (binding) needs the larger margin. For Quire's typical "stapled / saddle-stitched" output, the right side is the gutter when reading; left margin tighter is correct. Always confirm with the user how the document will be bound.

---

## Common false alarms (these are not anti-patterns)

- **One color across many pages** — that's the rule, not a problem
- **Lots of whitespace** — Quire is editorial; whitespace is the design
- **Short chapters (2–3 pages)** — fine, as long as cadence is preserved
- **No images** — Anthropic's playbook has none, neither should Quire by default
