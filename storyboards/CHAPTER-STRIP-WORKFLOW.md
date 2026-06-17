# Chapter Strip / Page Workflow

**Single source of truth:** `storyboards/arc-01-panel-storyboard.md` + **`data/manhwa-pages-arc01-ch01.json`** (page prompts & refs).

**Cursor skill:** `.cursor/skills/manhwa-page-gen/SKILL.md` — read when generating art in Cursor.

## Generate in Cursor

1. `python scripts/generate_manhwa_page.py --arc 1 --chapter 1 --page page2 --dry-run` — print prompt + refs
2. Agent uses **GenerateImage** with those refs (method A in skill)
3. Or API: `python scripts/generate_manhwa_page.py --arc 1 --chapter 1 --page page2 --quality high` (needs `OPENAI_API_KEY`)
4. `python scripts/build_chapter_strip_reader.py --arc 1 --chapter 1`

## Two generation modes

| Mode | When | Source |
|------|------|--------|
| **Manhwa page** | Continuity pass · fewer files | Storyboard **PAGE 1 / 2 / 3** layout tables + outfit lock |
| **Panel-by-panel** | Final reader · swap one beat | `### Panel N.M` blocks in storyboard |

Dialogue always lives in the **HTML reader** — not burned into art.

## Dynamic layout rules

- **3 panel rows max** per page (1536×1024). Splits/insets inside a row are OK.
- **Not** equal-height panel grids — specify splash / split / inset rows (Solo Leveling style).
- Thin gutters · outer margin · **no readable text** in image.
- Attach ref sheet matching **outfit phase** (casual → dobok → gear).

## Reader

- Panel view: `arcs/new-beginnings/chapter-01.html`
- Optional strip view: drop page PNG in `gallery/strips/arc-01/` and run `python scripts/build_chapter_strip_reader.py --arc 1 --chapter 1`

Rebuild after storyboard changes:

```bash
python scripts/generate_panels.py --arc 1 --chapter 1 --manifest-only
python scripts/build_arc_reader.py 1
```
