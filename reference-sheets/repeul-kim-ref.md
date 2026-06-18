# Repeul Kim — Reference Sheet

**Role:** Background only · Ttong Kim's wife · **never speaks**  
**Sources:** [`characters/repeul-kim.md`](../characters/repeul-kim.md)

## AI Text Rule

Append: `NO TEXT NO LETTERS NO NAME TAGS NO STAT SHEET NO QUOTES NO SPEECH BUBBLE` — label **Repeul Kim** in post only. See [`CANON-LABELS.md`](./CANON-LABELS.md).

---

| Field | Value |
|-------|-------|
| Name | Repeul Kim |
| Sex | **Female** — **wife of Ttong Kim** |
| Age | 37 |
| Height | 5'5" |
| Build | Pretty overweight — soft round, not athletic |
| Hair | Brown, curly, medium-to-long |
| Outfit | **Always casual** — ugly clashing multicolor fashion only |
| Dialogue | **Never** — background extra only |

---

## Visual Lock — Do Not Drift

| Feature | Detail |
|---------|--------|
| Sex | **Adult woman / female only** — Ttong Kim's **wife** |
| Hair | **Brown curls** — medium/long, messy volume |
| Build | **Heavyset woman** — average height, wide hips, soft feminine round figure |
| Clothes | **Maximum ugly** — neon + floral + plaid + stripes **clashing**; mismatched shoes; tacky accessories |
| Expression | **Ugly + mean** — sour scowl, judgmental narrowed eyes, tight lips; **mouth closed**, no speaking pose |
| Role | **Background** — slightly soft focus OK in panel refs; not hero lighting |

**Avoid:** **male body, man, masculine face, beard**, thin model body, stylish outfit, **kind smile, warm friendly face, pretty influencer look**, dobok, hogu, center-stage pose, open mouth mid-speech, **any text in image**.

---

## Files to Generate

Save under `output/repeul-kim/`:

| File | View | Outfit |
|------|------|--------|
| `casual-front.png` | Front turnaround | Primary ugly multicolor casual |
| `casual-3q.png` | 3/4 | Same outfit family (new clash combo OK) |

---

## Prompts — Casual (Primary)

### Casual — Front
```
ADULT WOMAN FEMALE ONLY wife character NOT male NOT man,
korean-american woman age 37 feminine soft round overweight female body wide hips soft arms 5 foot 5 average height,
medium long brown curly hair messy curls past shoulders tacky claw clip,
intentionally UGLY hideous clashing multicolor women's casual outfit neon pink green yellow floral print plaid leopard stripes layered cardigan,
mismatched sneakers gaudy plastic jewelry worst taste maximal chaos fashion,
MEAN ugly aesthetic sour resting bitch face judgmental scowl narrowed eyes tight thin lips unkind dismissive NOT smiling,
full body front turnaround sheet front side back profile views plain white background,
solo leveling manhwa lineart cel shading,
NO TEXT NO LETTERS NO NUMBERS NO NAME TAGS NO STAT BLOCKS NO LOGO TEXT NO QUOTES NO SPEECH BUBBLE
```

**Negative (append):** `male, man, masculine, beard, muscular man, boy, kind smile, warm expression, pretty, elegant fashion`

### Casual — 3/4 (Panel Background)
```
same overweight brown curly hair woman ugly clashing multicolor casual outfit mean scowl judgmental face,
slightly out of focus background extra standing at edge of frame arms crossed or hands on hips,
character reference 3/4 view plain white background manhwa,
NO TEXT NO LETTERS NO NAME TAGS NO SPEECH BUBBLE
```

---

## Panel Use

- Attach **`casual-front.png`** when Ttong Kim appears at Prime tournaments, VIP payments, parent meetings.
- Keep her **peripheral** — img2img at low weight or describe as background blur.
- **Never** generate dialogue for this character.

---

## Master Reference Panel Tie-In

- **Intro card:** Arc 1 panel **1.13a-R** (after Ttong **1.13a-T**, before KO bounty **1.13b**)
- **Background:** Arc 1 panels **1.4**, **1.8**, **1.9**, **1.13b**, **1.14** — optional `+ Repeul Kim background`

**Generated v2:** `output/repeul-kim/casual-front.png` — adult woman, ugly multicolor casual, **mean scowl**
