# Character Reference Sheets

Turnaround model sheets for **consistent AI panel generation** (img2img / IP-Adapter / character LoRA).

**Primary source:** [Google Sheets — Character Card](https://docs.google.com/spreadsheets/d/18DGBDJphipA9le931yoLtFqWFlLESeIMyyiIGv10-MU/edit?usp=sharing) (one tab per fighter).

**Import-ready CSVs (cleaned):** [`google-sheets-import/`](./google-sheets-import/) — regenerate with `python scripts/export_google_sheets.py`.

**Legacy CSV snapshots:** [`source-csv/`](./source-csv/) — old exports; prefer `google-sheets-import/` after sync.

**Extended profiles:** [`../characters/`](../characters/README.md) — story beats, MV/Ttong Kim details added after the sheet.

---

## Generation Order

| Batch | Character | Sheet tab | Ref file |
|-------|-----------|-----------|----------|
| **P0** | Ethan Hyun | Ethan Hyun | [ethan-hyun-ref.md](./ethan-hyun-ref.md) |
| **P0** | Master Viet (**Viet Na**) | *(no dedicated tab — use profile)* | [master-viet-ref.md](./master-viet-ref.md) · casual front/side/back |
| **P0** | Ttong Kim | *(no dedicated tab — use profile)* | [ttong-kim-ref.md](./ttong-kim-ref.md) |
| **P0** | Repeul Kim | *(background — use profile)* | [repeul-kim-ref.md](./repeul-kim-ref.md) |
| **P1** | TJ Lim | TJ Lim | [tj-lim-ref.md](./tj-lim-ref.md) |
| **P1** | Kieryn Lim | Kieryn Lim | [kieryn-lim-ref.md](./kieryn-lim-ref.md) |
| **P1** | Logan Hyun | Logan Hyun | [logan-hyun-ref.md](./logan-hyun-ref.md) |
| **P2** | Kian Sang | Kian Sang | [kian-sang-ref.md](./kian-sang-ref.md) |
| **P2** | Ariana Yang | Ariana Yang | [ariana-yang-ref.md](./ariana-yang-ref.md) |
| **P2** | Yuna Park | *(no tab — use profile)* | [yuna-park-ref.md](./yuna-park-ref.md) ✓ |

**P0 complete** — see [`P0-MANIFEST.md`](./P0-MANIFEST.md) for panel attach guide.

### P0 generation status ✅

| Character | Required views | Status |
|-----------|----------------|--------|
| **Ethan Hyun** | casual · dobok · gear | ✅ All PNGs in `output/ethan-hyun/` |
| **Master Viet** | vest · dobok · polo | ✅ All PNGs in `output/master-viet/` |
| **Ttong Kim** | shorts · jaw-profile · dobok · suit | ✅ All PNGs in `output/ttong-kim/` |
| **Repeul Kim** | casual · casual-3q | ✅ All PNGs in `output/repeul-kim/` |

### P1 generation status ✅

| Character | Views | Status |
|-----------|-------|--------|
| **TJ Lim** | casual · dobok · gear | ✅ |
| **Kieryn Lim** | casual · dobok · gear | ✅ |
| **Logan Hyun** | casual · dobok · gear | ✅ |

### P2 generation status ✅

| Character | Views | Status |
|-----------|-------|--------|
| **Kian Sang** | casual · dobok · gear | ✅ |
| **Ariana Yang** | casual · dobok · gear | ✅ |
| **Yuna Park** | poomsae · casual · college-casual-ring | ✅ |

---

## Workflow

1. Open the character's **ref markdown** file.
2. Generate **Outfit A (casual)** — all four views — pick the best **front** as master ref.
3. Generate **Outfit B (dobok)** — front + 3/4 minimum.
4. Save PNGs to `reference-sheets/output/<character-id>/` using the filenames in each ref file.
5. Panel generation: attach **front dobok** for fight scenes, **casual front** for dojang arrival scenes.
6. **Never** ask AI to render name text on ref sheets — label files by filename only. Use [`CANON-LABELS.md`](./CANON-LABELS.md) for post-production text.

---

## Every Prompt — Append

**Global style** (from [STORYBOARD-GUIDE.md](../storyboards/STORYBOARD-GUIDE.md)):

```
manhwa webtoon, clean lineart, cel shading, korean sports manhwa, solo leveling character aesthetic,
sharp focus, character reference sheet, neutral pose, plain white background
```

**Global negative:**

```
photorealistic, 3d render, western comic, extra limbs, deformed hands, blurry, watermark, text, logo,
speech bubble, low quality, chibi, multiple characters, cropped head, cropped feet
```

**Palette (when not white bg):**

- Kwon's scenes: append `STYLE: KWONS`
- Prime flashbacks: append `STYLE: PRIME`

---

## Output Folder Layout

```
reference-sheets/
├── CANON-LABELS.md      ← correct names for post-production
├── output/
│   ├── ethan-hyun/      ← casual · dobok · gear
│   ├── master-viet/     ← vest · dobok · polo (tournament)
│   ├── ttong-kim/       ← shorts · jaw-profile · dobok · suit
│   ├── repeul-kim/       ← casual · casual-3q (background)
│   ├── tj-lim/          ← casual · dobok · gear
│   ├── kieryn-lim/      ← casual · dobok · gear
│   ├── logan-hyun/      ← casual · dobok · gear
│   ├── kian-sang/       ← casual · dobok · gear
│   ├── ariana-yang/     ← casual · dobok · gear
│   ├── yuna-park/       ← poomsae · casual · college-casual-ring
│   ├── derek-cole/      ← dobok
│   ├── maya-ortiz/      ← dobok
│   ├── lee-ji-woo/      ← dobok
│   ├── kim-min-ho/      ← dobok
│   ├── han-do-won/      ← dobok
│   └── park-sung-min/   ← dobok
```

---

## Sheet vs Story — Known Differences

| Field | Google Sheet | Story canon (use for art) |
|-------|--------------|---------------------------|
| Kian nationality | Indian-American | **Half Korean, half Indian** — Korean-American |
| Kieryn surname tab | Kieryn Lim | **Lim** (confirmed) |
| Master Viet | No tab | **Viet Na**, called Master Viet — chubby, vest, small eyes |
| Ttong Kim | No tab | Stocky, square jaw, tight shorts / suit |
| Repeul Kim | No tab | Overweight woman, brown curls, ugly multicolor casual, **mean scowl** — **silent background** |
| Yuna Park | No tab | Poomsae dobok, casual, **college-casual-ring** (Arc 8 epilogue) — see [yuna-park-ref.md](./yuna-park-ref.md) |

When sheet and profile conflict, **profile wins** unless you update the sheet.

**Dobok designs:** See [`DOBOK-DESIGN.md`](./DOBOK-DESIGN.md) — per-character colors, guard layering, belt lettering, and back patches. **Logan:** standard white dobok, plain black belt.

---

## Link Back

After refs exist, update [STORYBOARD-GUIDE.md](../storyboards/STORYBOARD-GUIDE.md) recurring fragments if a design locks in differently than prompts suggest.
