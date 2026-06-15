# Ethan Hyun — Reference Sheet

**Role:** Protagonist · The Gifted Broken Protagonist  
**Sources:** Google Sheet tab **Ethan Hyun** · [`source-csv/Ethan-Hyun.csv`](./source-csv/Ethan-Hyun.csv) · [`characters/ethan-hyun.md`](../characters/ethan-hyun.md)

---

## Google Sheet Canon

| Field | Value |
|-------|-------|
| Age | 15 |
| Nationality | Korean-American |
| Height | 5'3" (160 cm) |
| Weight | 95 lbs (43.1 kg) |
| Division | Junior −45 kg |
| Belt | **3rd Dan** |
| Defining trait | The Prodigy Nobody Understands |
| Defining skills | Neverending Endurance · Berserker Trance |
| Favorite kicks | Outside-In Crescent · Counter Backleg Roundhouse |
| Loves | Sushi · Pineapple Fanta |

### Stats (sheet)

| Main | Grade | Secondary | Grade |
|------|-------|-----------|-------|
| Attack | B+ | Strength | B− |
| Defense | B | Endurance | A |
| Technique | A | Speed | A− |
| Mobility | A− | Reach | B |
| Physical | B+ | Tenacity | C · Charisma B− |

---

## Visual Lock — Do Not Drift

| Feature | Detail |
|---------|--------|
| Hair | **Dark blue shadow-perm** — soft volume, K-pop idol silhouette |
| Eyes | Brown, quiet intense |
| Build | **Small** — 5'3", light frame; shortest on Kwon's team |
| Signature gear | **Gold headphones** (neck/off-mat) · **white gear backpack** |
| Casual | **Oversized baggy hoodie** · **white tee hanging out** · **baggy wide pants** — K-pop streetwear, quiet vibe |
| Belt | **Silver-letter black belt** — only one at Kwon's (add lettering in post) |
| Dobok | Standard **white** · guards **under** dobok |
| Vibe | K-pop idol look × introverted stare — not smiling by default |

**Avoid:** taller than 5'3", black hair, no headphones in casual, red/blue generic belt, **wrong names (Jay Park, Kwon Euisik)**.

---

## AI Text Rule

**Never render names or stats in AI.** See [`CANON-LABELS.md`](./CANON-LABELS.md). Correct name: **Ethan Hyun** only.

Append to every prompt: `NO TEXT NO LETTERS NO NAME TAGS NO STAT BLOCKS NO HANGUL plain white background`

---

## Files to Generate

Save under `output/ethan-hyun/`:

| File | View | Outfit |
|------|------|--------|
| `casual-front.png` | Front full body | Street / dojang arrival |
| `casual-3q-left.png` | 3/4 left | Same |
| `casual-side.png` | Side profile | Same |
| `casual-back.png` | Back | Same — show backpack |
| `dobok-front.png` | Front | Kwon's white dobok — guards under |
| `dobok-3q-left.png` | 3/4 | Dobok |
| `gear-front.png` | Front | Electronic hogus + headgear |
| `expressions.png` | 3-face strip | Neutral · focused · pained smirk |

---

## Prompts — Casual (Off-Mat)

**Use for:** Arc 1 Ch 2–3 arrival, Ch 6–9 dialogue, team scenes.

### Casual — Front (Primary)
```
teen boy age 15 korean-american 5 foot 3 short light frame, dark blue shadow perm hair brown eyes,
quiet intense expression not smiling, gold headphones around neck, white taekwondo gear backpack,
oversized baggy dark navy hoodie unzipped open, plain white t-shirt hanging out visible below hoodie hem,
baggy black wide leg pants loose streetwear, white sneakers,
full body front turnaround sheet front side back views plain white background solo leveling manhwa lineart cel shading,
NO TEXT NO LETTERS NO NAME TAGS NO STAT BLOCKS NO HANGUL NO ENGLISH
```

### Casual — 3/4 Left
```
same teen boy ethan hyun dark blue shadow perm hair gold headphones white backpack,
3/4 view facing left, full body, character turnaround reference sheet, white background, manhwa
```

### Casual — Side
```
same teen boy 5'3 dark blue hair gold headphones white backpack side profile full body,
character model sheet, white background, manhwa webtoon
```

### Casual — Back
```
same teen boy from behind dark blue shadow perm hair white taekwondo gear backpack,
full body back view, character reference sheet, white background, manhwa
```

---

## Prompts — Dobok (Training)

**Locked design:** [`DOBOK-DESIGN.md`](./DOBOK-DESIGN.md). Guards **under** jacket/pants. Belt lettering added in post.

### Dobok — Front
```
teen boy 15 korean-american 5'3 dark blue shadow perm hair brown eyes,
standard white taekwondo dobok full coverage arm and leg guards hidden underneath dobok fabric,
plain black belt no readable embroidery, blank empty chest patch,
full body front turnaround front side back plain white background solo leveling manhwa,
NO TEXT NO LETTERS NO NAME TAGS NO STAT BLOCKS
```

### Dobok — 3/4
```
same ethan hyun white dobok plain black belt 3/4 view full body guards under dobok, character reference white background manhwa,
NO TEXT NO LETTERS
```

---

## Prompts — Tournament Gear

**Use for:** Arc 1 nightmare Ch 1, Arc 3 fights.

### Gear — Front
```
teen boy 5'3 dark blue shadow perm hair, white electronic taekwondo hogu chest guard,
arm guards leg guards headgear, premier school patch or neutral patch no text,
silver black belt, full body front guard stance, character reference sheet,
STYLE: TOURNAMENT manhwa
```

---

## Expression Mini-Sheet (Optional)

```
character expression sheet three panels same teen dark blue shadow perm hair,
neutral quiet face, focused competition eyes, painful smirk when hit,
bust portraits consistent design, white background, manhwa
```

---

## Master Reference Panel Tie-In

After generation, pick the best match to storyboard anchors:

- **Casual master:** Arc 1 panel **3.4**, **5.3**
- **Dobok master:** Arc 1 panel **4.2**, **4.4**

Use that PNG as img2img anchor for all Arc 1 Ethan panels.

**Generated:** `casual-front.png` v4 · `dobok-front.png` v4 · `gear-front.png` v2
