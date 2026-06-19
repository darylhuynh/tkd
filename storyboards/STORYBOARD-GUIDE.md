# Taekwondo Legends — Storyboard Guide

Master reference for all panel-by-panel AI prompts across the series.

**Clarity & flow:** [STORYBOARD-CLARITY-GUIDE.md](./STORYBOARD-CLARITY-GUIDE.md) · **Story review (Arcs 1–8):** [STORY-FLOW-REVIEW.md](./STORY-FLOW-REVIEW.md)

---

## File Index

| Arc | Chapters | File | Panels |
|-----|----------|------|--------|
| 1 — New Beginnings | 1–10 | [arc-01-panel-storyboard.md](./arc-01-panel-storyboard.md) | 408 |
| 2 — The Team | 11–20 | [arc-02-panel-storyboard.md](./arc-02-panel-storyboard.md) | 200 |
| 3 — First Tournament | 21–35 | [arc-03-panel-storyboard.md](./arc-03-panel-storyboard.md) | 300 |
| 4 — The Shadow School | 36–50 | [arc-04-panel-storyboard.md](./arc-04-panel-storyboard.md) | 300 |
| 5 — The Road to Korea | 51–70 | [arc-05-panel-storyboard.md](./arc-05-panel-storyboard.md) | 400 |
| 6 — Korea Regionals | 71–90 | [arc-06-panel-storyboard.md](./arc-06-panel-storyboard.md) | 400 |
| 7 — Legends | 91–110 | [arc-07-panel-storyboard.md](./arc-07-panel-storyboard.md) | 400 |
| 8 — Closure | 111–120 | [arc-08-panel-storyboard.md](./arc-08-panel-storyboard.md) | 200 |
| **Total** | **120** | | **2,403** |

---

## Prime Flashbacks & Short Threads

Extended dialogue lives in `scripts/` — storyboards below are the **panel attach map**. Always **`STYLE: PRIME`** inside flash; explicit return to present palette.

### Prime flash scripts

| Script | REAL # | Storyboard slots |
|--------|--------|------------------|
| [flash-prime-knockout-bounty.md](../scripts/flash-prime-knockout-bounty.md) | #28 | Arc 1 **1.37** · Arc 2 **15.2b** · Arc 3 **22.4** (MV contrast) · Arc 4 **39.2** · **40.2** (optional inset) |
| [flash-prime-board-break.md](../scripts/flash-prime-board-break.md) | #24, #9, #10 | Arc 3 **§28.1–28.8** · Arc 4 **§36.0–36.2** · Ch 35 eval callback |
| [flash-prime-girl-favoritism.md](../scripts/flash-prime-girl-favoritism.md) | #9, #25–27 | Arc 4 **§37.2–37.6** · Ch 42–43 callbacks |

**Rule:** Flash triggered by **present stimulus** — never orphan flash chapters. Full integration checklist: [scripts/README.md](../scripts/README.md).

### Shorts & threads

| Script | Thread | Storyboard slots |
|--------|--------|------------------|
| [short-yuna-pineapple-fanta.md](../scripts/short-yuna-pineapple-fanta.md) | Ethan's drink · Yuna observes → gifts Ch 108 | Arc 3 **§34.4–34.10** · Arc 5 **§63.3–63.4** · Arc 6 **§77.7** · Arc 7 **§108.2–108.4** |

---

## How to Use

1. Append **Global Style** to every prompt.
2. Use **Global Negative** in your tool's negative field.
3. Tag `[HAIKYUU]` panels = team chemistry priority — extra care on expressions and group framing.
4. Tag `[TEACH]` panels = sport education — rules/kicks for new readers. See [OLYMPIC-TKD-EDUCATION.md](../OLYMPIC-TKD-EDUCATION.md).
5. Tag `[ACTION]` panels = expanded fight choreography — **10–14 panels per major match**. See [ACTION-CHOREOGRAPHY.md](./ACTION-CHOREOGRAPHY.md).
6. Tag `[CARD]` panels = fighter stat card(s) before match or intro — see [CHARACTER-CARDS.md](./CHARACTER-CARDS.md).
7. Add dialogue in post-production — AI text is unreliable.
8. **Aspect ratio:** `2:3` or `9:16` vertical webtoon panels.
9. **Manhwa page batch gen (optional):** multi-panel pages live in the storyboard chapter header — e.g. Arc 1 Ch 1 **PAGE 1–3** in [arc-01-panel-storyboard.md](./arc-01-panel-storyboard.md). Single source of truth; no separate strip prompt files.

---

## Global Style

```
manhwa webtoon, vertical comic panel, clean lineart, cel shading, korean sports manhwa,
solo leveling character aesthetic, haikyuu style team warmth and expressive faces,
cinematic lighting, sharp focus
```

## Global Negative

```
photorealistic, 3d render, western comic, extra limbs, deformed hands, blurry,
watermark, speech bubble text, low quality, chibi unless specified
```

---

## Palette Keys

| Tag | Use |
|-----|-----|
| `STYLE: PRIME` | Desaturated blue-grey, harsh fluorescent, neglect |
| `STYLE: KWONS` | **Kwon's Taekwondo Academy** — warm amber dojang, golden hour, wood floors |
| `STYLE: TOURNAMENT` | Bright venue, electronic scoreboards, crowd energy |
| `STYLE: KOREA` | Modern Korean dojang, national flags, clean architecture |
| `STYLE: HAIKYUU` | Warm group lighting, exaggerated friendly expressions, sweat sparkle |
| `STYLE: CARD` | Fighter profile / VS stat card — empty text boxes for post-production |

---

## Panel Prompt Continuity

**Problem:** Generic words (*instructor*, *teen boy*, *coach*) make each panel look like a different cast.

**Fix — every prompt must include:**

1. **Canon name** — `Ethan Hyun`, `Ttong Kim`, `Master Viet` (not "instructor").
2. **Locked outfit for the scene** — e.g. Ch 1 tournament = Ethan **full Olympic kyorugi kit**; Ttong **Prime polo + tight black shorts + gold watch**; bedroom = Ethan **grey sleep tee, no dobok**.
3. **Same hair/build tags** every time — Ethan's **dark blue shadow perm**, Ttong's **underbite**, Yeo Woo's **brown curls + multicolor casual**.
4. **Reference sheet attach** when batch-generating — see [P0-MANIFEST](../reference-sheets/P0-MANIFEST.md).

**Chapter outfit locks:** Arc 1 Ch 1 table in [arc-01-panel-storyboard.md](./arc-01-panel-storyboard.md#chapter-1--outfit-lock-copy-into-every-ch-1-prompt).

**Regenerate rule:** If you change outfit wording mid-chapter, **delete** old PNGs for that chapter and re-run from panel 1 of the scene block.

---

## Character Prompt Fragments

See [Arc 1 storyboard](./arc-01-panel-storyboard.md) for Ethan, MV, Ttong Kim, Yeo Woo Kim, Grandmother.

**Reference sheets (turnarounds):** [reference-sheets/](../reference-sheets/README.md) · [P0-MANIFEST](../reference-sheets/P0-MANIFEST.md) — **P0–P2 complete**; attach refs per manifest when batch panel gen.

| Character | Fragment |
|-----------|----------|
| **TJ Lim** | teen 15, teal hair headband, muscular 5'11", confident grin |
| **Logan Hyun** | teen 13, dark blue bowl cut, big eyes, oversized backpack, cheerful |
| **Kieryn Lim** | teen girl 13, teal purple streak hair, asymmetrical bob, sharp smirk |
| **Kian Sang** | teen 15, **half korean half indian**, white silver hair, dark brown skin, lean, intense |
| **Ariana Yang** | teen girl 15, black red streak bob, bandages on arms, stoic |
| **Yuna Park** (poomsae) | teen girl 15–17, long black ponytail · poomsae dobok · epilogue: SNU casual + friendship ring |
| **Yeo Woo Kim** (background) | overweight 5'5" woman, brown curls, ugly multicolor casual, **mean scowl** — **never speaks** · beside Ttong at Prime |

---

## Haikyuu Moment Types (used in series)

| Type | Example Arcs |
|------|--------------|
| **Ramen / team meal** | 2, 4, 6, 8 |
| **Rules lecture chaos** | 2 |
| **Synchronized drill fail → laugh** | 2, 5 |
| **Post-loss bench huddle** | 3, 7 |
| **Corner cheer wall** | 3, 6, 7 |
| **Captain anchor speech** | 3, 5, 7 |
| **Rival push in practice** | 2, 5, 7 |
| **Group conditioning / sprints** | 5 |
| **Food breaks argument** | 4, 7, 8 |
| **Silent support (sit beside)** | 3, 8 |
| **Team pose before match** | 6, 7 |

Panels tagged `[HAIKYUU]` in arc files match these beats.

---

## Sport Education `[TEACH]`

Periodic Olympic scoring and kick tutorials for readers new to taekwondo. Full schedule: **[OLYMPIC-TKD-EDUCATION.md](../OLYMPIC-TKD-EDUCATION.md)**.

| Type | Example |
|------|---------|
| Whiteboard rules lecture | Arc 2 Ch 12 |
| Pad drill kick names | Arc 1 Ch 4, Arc 2 Ch 16 |
| Gear / electronic scoring | Arc 3 Ch 21 |
| Pre-fight technique tip | Arc 3 Ch 24, Arc 5 Ch 59 |
| Live scoreboard callout | Arc 3, 6, 7 match panels |
| Slow-mo kick diagram | Arc 3 Ch 29, Arc 7 **Ch 98** |
| Poomsae vs sparring | Arc 5 Ch 63 |

**AI add-on for `[TEACH]` panels:**
```
instructional sports manga panel, clear technique form, strike zone highlight space
```

---

## Action Choreography `[ACTION]`

Olympic kyorugi fight sequences — modern WT style, research-backed combos, 12-panel templates.

Full guide: **[ACTION-CHOREOGRAPHY.md](./ACTION-CHOREOGRAPHY.md)**

| Type | Example |
|------|---------|
| Cut kick → spinning counter | Arc 7 **Ch 98** |
| Cut trap → turning head +5 | Arc 3 Ch 33 |
| Endurance round activity | Arc 6 Ch 77 |
| Berserker anti-pattern | Arc 5 Ch 59 |

**AI add-on for `[ACTION]` panels:**
```
dynamic olympic taekwondo kyorugi, white dobok full olympic kyorugi gear electronic chest hogu headgear forearm guards shin foot guards,
motion blur kicking leg, impact frame speed lines, sports manga action NOT wire fu
```

---

## Character Cards `[CARD]`

Pre-fight and introduction stat blocks — name, age, height, weight, division, dan.

Full roster + opponents: **[CHARACTER-CARDS.md](./CHARACTER-CARDS.md)**

| Type | When |
|------|------|
| Single intro | First Kwon's appearance, walk to ring |
| Dual VS | Before P0 fights (Ch 25, **98**, 77, 118) |
| Team montage | Arc 3 Ch 21 equipment day |

**Panel ID:** `XX.0` or `XX.C1` — always **before** `XX.1` guard bounce.

---

## Panel ID Format

`Chapter.Panel` — e.g. **14.3** = Chapter 14, Panel 3.

---

## Kyorugi Sparring Gear (required)

When teens are **about to spar**, **walking to the ring**, or in **live match / round / `[ACTION]`** panels — they wear **white dobok + full competition kit**, not dobok alone:

| Piece | Prompt term |
|-------|-------------|
| Chest | electronic chest guard (hogu) |
| Head | headgear with face shield |
| Arms | forearm guards |
| Legs | shin guards + foot guards |

**Standard fragment** — append to every spar/match/fight prompt:

```
white dobok, full olympic kyorugi gear, electronic chest hogu, headgear, forearm guards, shin foot guards
```

**Use for:** tournament rings, inter-school spar, mock bouts, training spar with scoring, U20/Korea/collegiate matches, walk-to-ring sendoffs.

**Skip for:** poomsae-only, pad/shield drills, footwork without contact, rules lecture, dobok-only bow circle, flashback Prime *(unless already in-ring with gear)*.

---

## Modification Notes

These are **draft baselines**. Adjust panel count, dialogue, and prompts as you generate and see what works. Expand thin chapters by splitting montages into extra panels.
