# Character Cards — Fighter Intro & Pre-Match

**Haikyuu / Blue Lock style** stat cards before fights and on **first major introduction**.

Append **Global Style** from [STORYBOARD-GUIDE.md](./STORYBOARD-GUIDE.md). Add dialogue text in post — leave **blank stat boxes** in AI gen if text fails.

---

## Card Layout

```
┌─────────────────────────────────────┐
│  [COLOR BAR — blue=Ethan side]      │
│  ┌──────┐  ETHAN HYUN               │
│  │ portrait │  Age · Height · Weight │
│  │  slot    │  Division · Dan rank   │
│  └──────┘  School: Kwon's Academy   │
│  STYLE: manhwa fighter profile card │
└─────────────────────────────────────┘
```

**Pre-fight dual card panel:** Left fighter (blue) | VS divider | Right fighter (red) — vertical webtoon stack also works (top/bottom).

**Fields (always show):**

| Field | Example |
|-------|---------|
| **Name** | ETHAN HYUN |
| **Age** | 15 |
| **Height** | 5'3" / 160 cm |
| **Weight** | 95 lbs / 43 kg |
| **Division** | Junior −45 kg |
| **Level** | 3rd Dan |
| **School** | Kwon's Taekwondo Academy |

**Optional:** Flag (🇺🇸/🇰🇷), win-loss record, signature skill (*Neverending Endurance*).

---

## When to Use `[CARD]`

| Trigger | Format | Example |
|---------|--------|---------|
| **First major appearance** | Single card | Arc 1 Ch 3 — Ethan at Kwon's |
| **Prime staff intro** | Single ×2 (stacked) | Arc 1 **1.13a-T** Ttong → **1.13a-R** Yeo Woo (Yeo Woo **never speaks** after) |
| **Before P0/P1 fight** | Dual VS card | Ch 25, **98**, 77, 118 |
| **Before team member fight** | Single card on walk to ring | Ch 32 TJ, Ch 33 Kieryn |
| **Poomsae intro** | Single — discipline line | Yuna Arc 3 Ch 34 |
| **Skip card** | Dialogue scenes, flashbacks, hospital | Arc 5 Ch 58 |

Tag in storyboard: `[CARD]` · Panel ID `XX.0` or `XX.C1` / `XX.C2`.

---

## Kwon's Roster — Canon Stats (Series Start · Age 15)

*Adjust age in Arc 8: Ethan/team **16–17**; Kieryn/Logan **14–15**.*

| Name | Age | Height | Weight | Division | Dan | School |
|------|-----|--------|--------|----------|-----|--------|
| **Ethan Hyun** | 15 → 17† | 5'3" (160 cm) | 95 lb (43 kg) | Junior −45 kg → Collegiate −58 kg† | **3rd Dan** | Kwon's |
| **TJ Lim** | 15 | 5'11" (180 cm) | 150 lb (68 kg) | Junior −68 kg | 3rd Dan | Kwon's |
| **Kieryn Lim** | 13 → 15† | 5'8" (173 cm) | 108 lb (49 kg) | Cadet −49 kg | 2nd Dan | Kwon's |
| **Kian Sang** | 15 | 5'10" (178 cm) | 108 lb (49 kg) | Junior −49 kg | 2nd Dan | Kwon's |
| **Ariana Yang** | 15 | 4'11" (150 cm) | 92 lb (42 kg) | Junior −42 kg | 2nd Dan | Kwon's |
| **Logan Hyun** | 13 → 15† | 4'10" (147 cm) | 84 lb (38 kg) | Cadet −41 kg | 2nd Dan | Kwon's |
| **Yuna Park** | 15 → 17† | 5'6" (168 cm) | 115 lb (52 kg) | Poomsae (Senior) | 2nd Dan | Independent / poomsae circuit |

†Arc 8 epilogue — use updated row in [Epilogue cards](#epilogue-cards-ch-118).

---

## Key Opponents — Pre-Match Cards

| Name | Arc/Ch | Age | Height | Weight | Division | Dan | School | Notes |
|------|--------|-----|--------|--------|----------|-----|--------|-------|
| **Derek Cole** | 3 · Ch 25 | 16 | 5'10" (178 cm) | 128 lb (58 kg) | Open −54 kg | 2nd Dan | Apex TKD | Taller — spinning hook specialist |
| **Maya Ortiz** | 3 · Ch 33 | 14 | 5'9" (175 cm) | 112 lb (51 kg) | Cadet −49 kg | 2nd Dan | Valley Martial Arts | Kieryn's bracket |
| **Kim Min-ho** | 7 · **Ch 98** | 17 | 5'11" (180 cm) | 132 lb (60 kg) | U20 −58 kg | 3rd Dan | Korea National TC | Left shoulder tell before spin |
| **Han Do-won** | 7 · **Ch 99** | 17 | 6'0" (183 cm) | 158 lb (72 kg) | U20 −68 kg | 3rd Dan | Korea National TC | TJ finals ace — pressure volume |
| **Lee Ji-woo** | 6 · Ch 77 | 16 | 5'6" (168 cm) | 99 lb (45 kg) | Junior −45 kg | 3rd Dan | Busan Youth Team | Korea regional — endurance test |
| **Park Sung-min** | 8 · Ch 118 | 21 | 5'10" (178 cm) | 145 lb (66 kg) | Collegiate −68 kg | 4th Dan | Yonsei Univ. | Collegiate final opponent |

---

## Epilogue Cards (Ch 118)

| Name | Age | Height | Weight | Division | Dan |
|------|-----|--------|--------|----------|-----|
| **Ethan Hyun** | 17 | 5'5" (165 cm) | 110 lb (50 kg) | Collegiate −58 kg | 3rd Dan |
| **Park Sung-min** | 21 | 5'10" (178 cm) | 145 lb (66 kg) | Collegiate −68 kg | 4th Dan |

*Weight bump = growth + proper cut for collegiate class — not a power-up.*

---

## Card Schedule by Chapter

| Ch | Panel | Who | Type |
|----|-------|-----|------|
| 1 | 1.13a-T | Ttong Kim | Prime intro ★ |
| 1 | 1.13a-R | Yeo Woo Kim | Background intro ★ (no dan) |
| 1 | 3.4 | Ethan | Intro (optional — nightmare first) |
| 3 | 3.4 | Ethan | First Kwon's intro ★ |
| 21 | 21.0 | Full team | Team roster montage (6 cards) |
| 25 | 25.0 | Ethan vs Derek Cole | Dual VS ★ |
| 32 | 32.0 | TJ Lim | Single pre-match |
| 33 | 33.0 | Kieryn vs Maya Ortiz | Dual VS ★ |
| 33 | 33.1b | Logan Hyun | Single (underdog) |
| 59 | 59.2.0 | Ethan vs Kian | Sparring dual |
| 77 | 77.0 | Ethan vs Lee Ji-woo | Dual VS ★ |
| **98** | 98.1 | Ethan vs Kim Min-ho | Dual VS ★ |
| **99** | 99.0 | TJ vs Han Do-won | Dual VS ★ |
| 118 | 118.0 | Ethan vs Park Sung-min | Dual VS ★ |

---

## AI Prompt — Single Card

```
manhwa webtoon fighter profile card vertical panel, solo leveling aesthetic,
teen korean-american male taekwondo athlete portrait left side,
stat block empty boxes right side for name age height weight division dan rank,
blue accent bar kwon taekwondo academy logo space, clean graphic design,
cel shading, no readable text, space for typography overlay, STYLE: CARD
```

## AI Prompt — Dual VS Card

```
manhwa webtoon dual fighter VS profile card vertical panel,
two taekwondo athletes portraits top and bottom divided by VS emblem,
blue fighter red fighter color coding, empty stat boxes for both sides,
olympic taekwondo tournament pre-match graphic, cel shading,
no readable text, space for name age height weight dan overlay, STYLE: CARD TOURNAMENT
```

## Global Negative (cards)

```
misspelled text, gibberish letters, photorealistic, 3d render, extra faces, chibi
```

---

## Background / Non-Fighting Intros

Use **single card** with Role instead of Division/Dan when the character does not compete.

| Name | Age | Height | Weight | Role | School |
|------|-----|--------|--------|------|--------|
| **Ttong Kim** | 38 | 5'8" (173 cm) | 198 lb (90 kg) | 2nd Dan instructor | Prime |
| **Yeo Woo Kim** | 37 | 5'5" (165 cm) | 265 lb (120 kg) | Background (spouse) | Prime |

**Yeo Woo Kim:** Post-production only — **no dialogue bubbles ever.**

---

## Post-Production Text (copy-paste)

### Ethan Hyun — Ch 25
```
ETHAN HYUN · Age 15 · 5'3" · 95 lbs
Junior −45 kg · 3rd Dan · Kwon's Taekwondo Academy
```

### Derek Cole — Ch 25
```
DEREK COLE · Age 16 · 5'10" · 128 lbs
Open −54 kg · 2nd Dan · Apex TKD
```

### Kieryn Lim — Ch 33
```
KIERYN LIM · Age 13 · 5'8" · 108 lbs
Cadet −49 kg · 2nd Dan · Kwon's Taekwondo Academy
```

### Kim Min-ho — Ch 98
```
KIM MIN-HO · Age 17 · 5'11" · 132 lbs
U20 −58 kg · 3rd Dan · Korea National Training Center
```

### Han Do-won — Ch 99
```
HAN DO-WON · Age 17 · 6'0" · 158 lbs
U20 −68 kg · 3rd Dan · Korea National Training Center
```

### Park Sung-min — Ch 118
```
PARK SUNG-MIN · Age 21 · 5'10" · 145 lbs
Collegiate −68 kg · 4th Dan · Yonsei University
```

### Ttong Kim — Ch 1 (1.13a-T)
```
TTONG KIM · Age 38 · 5'8" · 198 lbs
2nd Dan · Prime Taekwondo Sports Dynasty
```

### Yeo Woo Kim — Ch 1 (1.13a-R)
```
YEO WOO KIM · Age 37 · 5'5" · 265 lbs
Prime (background)
```

---

## Links

- Character profiles: [characters/](../characters/)
- Fight panels: [ACTION-CHOREOGRAPHY.md](./ACTION-CHOREOGRAPHY.md)
- Storyboard tag: `[CARD]` in [STORYBOARD-GUIDE.md](./STORYBOARD-GUIDE.md)
