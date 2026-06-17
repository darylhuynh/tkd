# Arc 1 — Panel Storyboard (Chapters 1–10)

**New Beginnings** · Premier trauma → Kwon's sanctuary → team reveal.

Append [Global Style from STORYBOARD-GUIDE](./STORYBOARD-GUIDE.md) to all prompts unless a panel specifies `STYLE: PREMIER` or `STYLE: KWONS`.

**Reference sheets:** [reference-sheets/](../reference-sheets/README.md) — attach Ethan, MV, Ttong Kim refs for Ch 1–10 batch gen.

**Premier flash (extended):** [flash-premier-knockout-bounty.md](../scripts/flash-premier-knockout-bounty.md) § Scene 1 → **1.37** · § Scene 2 → **1.38–1.42** bridge.

---

## How to Use

1. Generate panels in order (`1.1` → `10.40`).
2. Append **Global Style** to every prompt unless a panel says `STYLE: PREMIER` or `STYLE: KWONS`.
3. For dialogue, add text in your editor after generation — most AI tools render text poorly.
4. **Character continuity:** Always use **canon names + locked outfit** in prompts (never generic "instructor" / "teen boy"). See **Chapter 1 — Outfit Lock** below and [STORYBOARD-GUIDE § Continuity](./STORYBOARD-GUIDE.md#panel-prompt-continuity).
5. **Aspect ratio:** vertical panels `2:3` or `9:16` for webtoon scroll.
6. **Montage / flash clarity:** [STORYBOARD-CLARITY-GUIDE.md](./STORYBOARD-CLARITY-GUIDE.md) — label **FLASH** vs **PRESENT** (see Ch 1 **1.27–1.31**).

---

## Global Style (append to all prompts)

```
manhwa webtoon, vertical comic panel, clean lineart, cel shading, korean sports manhwa,
solo leveling aesthetic, cinematic lighting, sharp focus, detailed background
```

## Global Negative Prompt

```
photorealistic, 3d render, western comic style, extra limbs, deformed hands, fused fingers,
blurry, watermark, logo, text overlay, speech bubble, low quality, chibi unless specified
```

## Recurring Characters — Prompt Fragments

| Character | Fragment |
|-----------|----------|
| **Ethan Hyun** | teen boy 15, korean-american, 5'3", dark blue shadow perm hair, brown eyes, quiet intense expression |
| **Ethan (gear)** | + **full olympic kyorugi kit:** white WT dobok · **blue electronic hogu** · **blue helmet** · white forearm/shin/foot guards · black belt **silver 태권도 embroidery** |
| **Other athletes (tournament)** | Mixed **red OR blue** hogu + helmet · **male and female** teens · varied heights/builds (tall/short/stocky/lean) — never homogeneous crowd |
| **Ethan (casual)** | + gold headphones · white backpack · **oversized black hoodie** · white undershirt · **black cargo pants** · white sneakers |
| **Ethan (dobok)** | + standard white dobok, guards under, silver-letter black belt *(post)* |
| **Master Viet** | **Viet Na** — chubby 5'8", kind small eyes, kwon vest or white dobok black neck stripes |
| **Ttong Kim** | **5'8" slightly stocky**, obvious underbite teeth showing, tight shorts or suit or white dobok black neck stripes, cold predatory grin, gold watch |
| **Grandmother** | elderly korean woman, hospital gown, kind tired eyes, thin hands |
| **Repeul Kim** | **ADULT WOMAN female**, **5'5" pretty overweight**, **brown curly** medium-long hair, **ugly clashing multicolor casual**, **mean sour scowl** — **Ttong Kim's wife**, **background only, never speaking**, edge of frame |
| **Team (Ch 10)** | TJ teal headband · Kieryn teal purple bob · Logan bowl cut · Kian silver hair · Ariana red streak bob |

## Palette Keys

| Location | STYLE tag |
|----------|-----------|
| Premier / nightmare / hospital threat | `STYLE: PREMIER` — desaturated, blue-grey, harsh fluorescent |
| Kwon's dojang | `STYLE: KWONS` — warm amber, golden hour through windows, wood floors |

---

# Chapter 1 — Nightmare

## Chapter 1 — Outfit Lock *(copy into every Ch 1 prompt)*

| Phase | Panels | Ethan look |
|-------|--------|------------|
| **Casual arrival** | 1.1–1.5 | Oversized **black hoodie** · white undershirt · **black cargo pants** · white sneakers · **gold headphones** · **white backpack** · **no dobok / no hogu** |
| **Dobok change** | 1.6–1.7 | **1.6** shirtless black short tights → white dobok pants · **1.7** dobok top over head abs visible · belt off-page |
| **Dobok warmup** | 1.8 | White **WT dobok** · black belt silver **태권도** · **NO hogu / NO helmet / NO guards** — stretching only |
| **First full kit** | 1.9–1.14 | Gear donning on PAGE 2 · mirror **1.14** |
| **Full kit (present)** | 1.15–1.46 | Same tournament kit as above — **SAME face/hair/kit** every panel |
| **Flash enrollment** | 1.28 | Young Ethan ~5 · shadow parent · Ttong + Repeul counting money |
| **Flash scrimmage** | 1.31 | White dobok · black belt · **no headgear** · Premier dojang kick montage |
| **Flash sidelines** | 1.32 | Ttong displeased watching · arms crossed · Repeul chips · dojang |
| **Bedroom** | 1.47–1.48 | Grey sleep tee · messy dark blue hair · gold headphones on nightstand · **NO dobok** |

| Character | Locked look |
|-----------|-------------|
| **Ttong Kim** | 38 · 5'8" stocky · underbite · **Premier polo + tight black shorts + gold watch** |
| **Repeul Kim** | 37 · 5'5" · brown curly hair · **ugly multicolor casual** · scowl · silent edge of frame |
| **Ring opponent** | Taller older Premier teen · **same blue-hogu kit as Ethan** |

**Visual arc:** casual kid → dobok → athlete → neglected all day → KO → wake.

**Manhwa pages (for multi-panel generation):**
- **PAGE 1a/1b — Arrival & change:** 1.1–1.7
- **PAGE 2 — Neglect & warmup:** 1.7b–1.8
- **PAGE 3 — Preparation:** 1.9–1.16 *(skipped in strip reader)*
- **PAGE 4 — Isolation:** 1.17–1.26
- **PAGE 5a–5c — Favoritism & called:** 1.27–1.33
- **PAGE 6 — Cards & hook:** 1.35–1.37 · 1.41–1.43
- **PAGE 7 — KO aftermath:** 1.44–1.45
- **PAGE 8 — Wake:** 1.46–1.48

**Rule:** Ref sheets — `casual-front.png` (1.1–1.5, van) · `dobok-front.png` (1.6–1.8) · `gear-front.png` (1.9+).

---

## Chapter 1 — Manhwa page layouts *(optional batch gen)*

Use when generating **one PNG per page** (not one PNG per panel). Dialogue stays in HTML reader — **no text in art**.

### PAGE 1a — Arrival (panels 1.1–1.3)
**3 rows** · arena → van → crowd walk.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~35% | 1.1 **busy arena exterior** · crowds walking to entrance |
| R2 | Wide ~35% | 1.2 van · teammates in **doboks** · Ethan **casual walking toward stadium** |
| R3 | Wide ~30% | 1.3 Ethan + crowd **walking TOWARD stadium** |

**Refs:** `ethan-hyun/casual-front.png` · style anchor PAGE 2

### PAGE 1b — Change (panels 1.4, 1.6–1.7)
**3 rows** · locker → dobok pants → dobok top · **no belt panel**.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~25% | 1.4 hallway · sign **MALE LOCKER** |
| R2 | Wide ~40% | 1.6 **dobok pants** · shirtless · black short tights |
| R3 | Wide ~35% | 1.7 **dobok top** over head · **no belt** |

**Refs:** `ethan-hyun/casual-front.png` · `ethan-hyun/dobok-front.png`

### PAGE 2 — Neglect & warmup (panels 1.7b–1.8)
**3 panel rows** · quad-split warmup = one row.

| Panel | Shape | Beats |
|-------|-------|-------|
| P1 | Wide ~40% | **1.7b-a** Ethan **paddle at side** · **looks at Ttong** · Ttong **faces away** · talks masters/parents |
| P2 | Wide ~40% **CUT** | **1.7b-b** Ethan **exasperated sigh** walks away · Ttong looks · **Repeul whispers** |
| P3 | Quad-split ~20% | 1.8 warmup montage · dobok only |

**Refs:** `ethan-hyun/dobok-front.png` · `ttong-kim/suit-front.png` · `repeul-kim/casual-front.png`

### PAGE 3 — Preparation (panels 1.9–1.16) · *skipped in strip reader*
**3 rows** when generated — gear-up montage + neglect contrast.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Thin wide ~20% | 1.9 hogu on \| 1.10 forearm guards |
| R2 | Tall center ~50% | 1.14 **mirror** full kit reveal |
| R3 | Wide asymmetric ~30% | 1.15 **Ttong** coaching favored kid · **Repeul** chips \| 1.16 Ethan alone |

### PAGE 4 — Isolation & wait (panels 1.17–1.26) · *live — legacy 4-row; regen as 3-row optional*
**4 rows** (legacy) · hours after PAGE 2 · clock **~7 PM**.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~30% | Bleachers · Ethan **full kit** slumped alone · snack wrapper · **clock ~7 PM** |
| R2 | Wide ~25% | 1.21 crowd waiting · **Ttong** + parents · **Repeul** edge |
| R3 | Medium ~25% | 1.22 Ethan isolated · empty seats · clock ~7 PM |
| R4 | Medium ~20% | 1.26 stiff leg · pins & needles · clock ~7 PM |

### PAGE 5a — Bleachers & contract (panels 1.27–1.28) · **NEXT TO GENERATE**
**3 rows** · present watch → enrollment flash → reaction.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~40% | **1.27 PRESENT** Ethan on bleachers watching Ttong hands-on warmup with **young female student** — touchy spotting |
| R2 | FLASH inset ~35% | **1.28** shadow parent · VIP brochure · **Ethan ~5** joyous · Repeul counting money |
| R3 | Medium ~25% | **1.27** Ethan close-up unsettled · helmet on bench |

**Refs:** `ethan-hyun/gear-front.png` · `ttong-kim/casual-front.png` · `repeul-kim/casual-front.png`

### PAGE 5b — Called & walk past (panels 1.29–1.30) · **NEXT TO GENERATE**
**3 rows** · PA call → stand → pass Ttong without acknowledgment.

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~35% | **1.29** referee/PA · *Hyun, Ethan — Ring 4* · Ethan looks up |
| R2 | Medium ~35% | **1.29** Ethan picks up helmet · stiff legs |
| R3 | Wide ~30% | **1.30** Ethan walks past Ttong + female student · Ttong ignores him |

**Refs:** `ethan-hyun/gear-front.png` · `ttong-kim/casual-front.png` · style anchor PAGE 5a

### PAGE 5c — Dojang montage & ring start (panels 1.31–1.33)

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Tri-cut ~40% | **1.31 FLASH** head kick \| roundhouse \| push kick down |
| R2 | Wide ~30% | **1.32 FLASH dojang** Ttong arms crossed displeased watching · Repeul chips · Ethan looks back |
| R3 | Wide ~30% | **1.33 PRESENT** Ethan helmet on in ring · ref hand raised · taller **red hogu** opponent |

**Refs:** `dobok-front` · `gear-front` · `ttong-kim` · `repeul-kim` · style anchor PAGE 5b

### PAGE 6 — Cards, bounty & the hook (panels 1.35–1.37, 1.41–1.43) · **NEXT TO GENERATE**

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | **33\|33\|33 ~35%** | **Fighter cards** with portrait + **Age · Ht · Wt · Rank** (match pitch site): **Ttong** \| **Repeul** \| **Ethan** |
| R2 | Wide ~30% | **1.37** Knockout bounty — Ttong holds **1,000 won** · eyes Ethan · *too soft* · Repeul edge |
| R3 | Wide ~35% tri-beat | **1.41–1.43** OTS Ethan POV · Ttong yelling *attack don't be soft* · hesitant vs **looming** red hogu · steps forward · **hook kick (heel)** · **mouthguard flies out** close-up |

**Card stat lock (ROW 1 only — readable text allowed on cards):**

| Card | Age | Ht | Wt | Rank |
|------|-----|----|----|------|
| **Ttong Kim** | 38 | 5'8" | 198 lbs | 2nd Dan |
| **Repeul Kim** | 37 | 5'5" | 230 lbs | Premier (staff) |
| **Ethan Hyun** | 15 | 5'3" | 95 lbs | 3rd Dan · −45kg |

**Refs:** `ttong-kim` · `repeul-kim` · `ethan-hyun/gear-front` · style anchor PAGE 5c

### PAGE 7 — Score, silence & black (panels 1.44–1.45) · **LIVE**

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Wide ~30% | **1.44a** Scoreboard **RED 6 · BLUE 0** (labels only) · Ethan falling · mouthguard + helmet airborne |
| R2 | Wide ~40% **4-panel strip** | **1.44b** Ethan **face down** → Ttong unconcerned → one-hand wave → walks away |
| R3 | Full ~30% | **1.45** Fade to black **from face-down Ethan** on mat · not bedroom |

**ROW 2 layout (40 / 20 / 20 / 20):**

| Frame | Size | Beat |
|-------|------|------|
| **1** | **40%** | Ethan **face down** prone on mat · silent horror · desaturated |
| **2** | **20%** | Ttong **unconcerned** · indifferent · not disappointed |
| **3** | **20%** | Ttong **one hand** dismissive wave |
| **4** | **20%** | Ttong **walking away** · back turned |

**Refs:** `ethan-hyun/gear-front` · `ttong-kim/casual-front` · style anchor PAGE 6

### PAGE 8 — Wake (panels 1.46–1.48) · *planned*

| Row | Shape | Beats |
|-----|-------|-------|
| R1 | Tall ~40% | **1.46** Smash cut — bolts upright in bed · gasping |
| R2 | Medium ~30% | **1.47** Ceiling stare · headphones on nightstand · block hand trembling |
| R3 | Medium ~30% | **1.48** Grey sleep tee · breath slowing · dawn birds |

---

### Panel 1.1 — Title Card — Venue
**Scene:** **Indoor sports arena building** — modern enclosed tournament facility (glass/concrete facade). **Busy tournament morning** — families, athletes, parents walking toward entrance with gear bags. **NOT** empty, **NOT** dark night, **NOT** gloomy silence.

**Prompt:**
```
INDOOR sports arena tournament building exterior modern glass concrete facade dawn overcast bright alive BUSY morning crowds families athletes parents teens walking toward entrance carrying gear bags tournament banners parking lot activity energetic arrival NOT empty NOT dark night NOT gloomy NO Ethan focus wide cinematic establishing shot STYLE PREMIER
```

---
### Panel 1.2 — Premier Van
**Scene:** Premier team van. **At most 4–5 people total** including Ethan. Teammates **already in white doboks** with **colored rank belts** (white/yellow/green/blue/red — **not black**). Mixed male/female, bland generic extras. One or two stepping out staggered; one or two already waiting on pavement. **Ethan Hyun** exits **last** — **only one in casual clothes** (black hoodie).

**Prompt:**
```
dawn parking lot black Premier passenger van ONE SINGLE sliding side door ONLY open all other doors closed NO front doors NO rear doors NO three doors AT MOST four teammates plus Ethan generic bland teens FULL white WT dobok white top AND white pants NO shorts NO dobok shorts COLORED belts yellow green blue red NOT black mixed male female staggered exit Ethan Hyun ONLY casual black hoodie gold headphones stepping out LAST wide shot STYLE PREMIER
```

---
### Panel 1.3 — Crowd Walk Toward Stadium
**Scene:** Ethan walking **with** Premier teammates **inside the arriving crowd**, all moving **toward** the stadium entrance. Arena visible **ahead**. **NOT** walking away from the venue.

**Prompt:**
```
rear or three-quarter tracking shot Ethan Hyun teen black hoodie cargo pants gold headphones white backpack walking WITH Premier teammates INSIDE busy tournament crowd moving TOWARD indoor arena glass entrance building visible AHEAD in background same direction as arriving families NOT walking away from stadium NOT leaving venue NOT back turned exiting parking lot STYLE PREMIER
```

---
### Panel 1.4 — Male Locker Door
**Scene:** Venue hallway. Ethan approaches locker room door. Sign reads **MALE LOCKER** (English block letters). **No dobok pictogram.**

**Prompt:**
```
tournament venue interior hallway Ethan Hyun teen black hoodie cargo pants headphones backpack approaching plain locker room door door sign reads MALE LOCKER in simple English block letters ONLY sign text on door NO dobok icon NO martial arts uniform pictogram medium shot STYLE PREMIER
```

---
### Panel 1.5 — Hallway — Too Early
**Scene:** Venue hallway. **Ethan still casual** — carrying gear bag. Wall clock **7:00 AM**. Other athletes in kit pass him.
**Dialogue:** Kid A: "Why are we here so early?"

**Prompt:**
```
tournament venue interior wall clock 7 AM Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression oversized black hoodie white undershirt black cargo pants white sneakers gold headphones white backpack NO dobok NO white pants NO hogu carrying white gear backpack walking hallway diverse mixed gender male female athletes varied heights builds in MIXED red and blue electronic hogu helmets passing him harsh fluorescent tired expressions wide hallway STYLE PREMIER
```

---
### Panel 1.6 — Dobok Pants
**Scene:** Changing area. Ethan **shirtless** — wearing **black short compression tights only** (no shirt). **Pulling on white dobok pants.** No dobok top yet. **No hogu.**

**Prompt:**
```
changing area locker room Ethan Hyun teen boy 15 korean-american lean athletic dark blue Korean shadow perm hair SHIRTLESS wearing black short compression athletic tights only NO shirt NO dobok top pulling ON white WT dobok pants mid-change harsh fluorescent tournament STYLE PREMIER
```

---
### Panel 1.7 — Dobok Top Over Head
**Scene:** Changing area. White dobok pants already on. Ethan **shirtless** — **pulling white dobok top over his head**, arms raised, **lean abs visible**. **No belt tying shown.** **No hogu.**

**Prompt:**
```
changing area locker room Ethan Hyun teen boy 15 korean-american lean athletic abs visible dark blue Korean shadow perm hair white dobok pants already on SHIRTLESS pulling white WT dobok top OVER head arms raised mid-change NO belt tying NO hogu NO chest protector harsh fluorescent STYLE PREMIER
```

---
### Panel 1.7b — Paddles Ignored (two-panel cut)

**Panel A — Waiting with paddle, ignored**
**Scene:** Inside stadium on mats. Ethan **waits** with kicking paddle **held naturally at his side** — relaxed grip, **not extended toward anyone**. He **looks at Ttong Kim** (patient, hopeful). Ttong **faces away from Ethan** — body and gaze toward **other masters and parents**, mid-conversation, **never making eye contact with Ethan**. Repeul **not** whispering yet.

**Prompt:**
```
INSIDE indoor stadium blue red competition mats Ethan Hyun teen white WT dobok black belt silver 태권도 NO hogu at distance standing waiting holding ONE kicking paddle naturally at his side relaxed arm down NOT extending paddle NOT raising paddle toward coach LOOKING at Ttong Kim patient hopeful expression eyes on coach Ttong Kim stocky underbite black polo shorts body turned AWAY from Ethan face and eyes toward group of OLDER master coaches glasses polo shirt tie AND tournament parents adults mid-conversation animated hand gestures Ttong NOT looking at Ethan zero eye contact with Ethan completely ignoring Ethan wide shot spatial distance STYLE PREMIER
```

**Panel B — Cut: exasperated sigh, walks away**
**Scene:** **Cut panel.** Ethan **walking away** alone with paddle — **exasperated sigh** (frustrated exhale, defeated). **Ttong looks back at Ethan.** **Repeul whispers** in Ttong’s ear.

**Prompt:**
```
CUT panel INSIDE stadium mats Ethan Hyun walking away alone carrying kicking paddle EXASPERATED SIGH frustrated exhale eyes half-closed or looking up defeated slumped shoulders giving up Ttong Kim looking over shoulder AT Ethan watching him leave Repeul Kim overweight brown curls ugly multicolor casual whispering into Ttong Kim ear mean scowl ONLY Repeul whispers wide cinematic STYLE PREMIER
```

---
### Panel 1.8 — Warmup Montage (Dobok Only)
**Scene:** **Quad-split panel** — four warmup beats, **dobok only** (no gear). Sparse background; optional few athletes stretching in distance.

| Segment | Beat |
|---------|------|
| A | Side **splits** on mat |
| B | **Toe touches** / forward fold |
| C | **Leg stretch** foot against wall |
| D | **Roundhouse kick** |

**Prompt:**
```
quad-split panel four segments warmup montage Ethan Hyun teen boy 15 korean-american white WT dobok black belt silver 태권도 NO hogu NO helmet NO guards segment 1 side splits on mat segment 2 standing toe touches forward fold segment 3 leg stretch foot against wall segment 4 roundhouse kick mid-kick sparse warmup area few distant athletes stretching in background NOT crowded fluorescent gym STYLE PREMIER
```

---
### Panel 1.9 — Chest Protector
**Scene:** Blue electronic **hogu** going on over dobok.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression putting on blue electronic chest hogu over white WT dobok black belt silver embroidery changing area close-up hands STYLE PREMIER
```

---
### Panel 1.10 — Forearm Guards
**Scene:** White **forearm guards** strapped on.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression strapping white forearm guards white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit preparation sequence close-up STYLE PREMIER
```

---
### Panel 1.11 — Shin Guards
**Scene:** White **shin guards** secured.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression securing white shin guards sitting bench white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit preparation detail STYLE PREMIER
```

---
### Panel 1.12 — Foot Sensors
**Scene:** White **foot protectors** / sensors on.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression fitting white foot protectors sensors white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit preparation close-up feet hands STYLE PREMIER
```

---
### Panel 1.13 — Helmet Clipped
**Scene:** Blue **helmet** clipped / face shield down.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression clipping blue helmet face shield white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit preparation profile close-up STYLE PREMIER
```

---
### Panel 1.14 — Mirror — Full Reveal
**Scene:** Mirror shot. **First full competition reveal** — complete blue-hogu kit. Reserved expression.

**Prompt:**
```
mirror reflection Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit full competition reveal first time complete kit sharp eyes reserved expression changing room mirror shot STYLE PREMIER
```

---
### Panel 1.15 — Warmup Floor — Ttong Coaches (Not Ethan)
**Scene:** Warmup area. **Ttong Kim** coaching a **favored student** with pads — animated, attentive. **Repeul Kim** in background eating chips, multicolor casual, scowl, silent. **Not Ethan.**

**Prompt:**
```
warmup area wide shot Ttong Kim adult man 38 slightly stocky 5 foot 8 square face obvious underbite teeth showing predatory grin Premier polo shirt tight black shorts gold watch holding kicking pad coaching favored teen athlete in blue hogu animated attentive Repeul Kim adult woman 37 pretty overweight brown curly hair ugly multicolor casual clothes mean scowl background edge eating potato chips from bag silent mouth closed diverse male female athletes red blue hogus STYLE PREMIER
```

---
### Panel 1.16 — Ethan Alone — No Warmup
**Scene:** Same floor. **Ethan Hyun alone.** No coach. No advice. No warmup. Something is wrong.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards white shin guards white foot protectors Premier patch full Olympic kyorugi kit standing alone empty warmup mat no coach no instructor nearby other athletes coached in far background isolated neglectful atmosphere wide shot STYLE PREMIER
```

---
### Panel 1.17 — Gear Check Line
**Scene:** ** Wristband table. Official scanning athletes. **Ethan Hyun** waiting in line in **full kit**, adjusting forearm guard strap.
**Dialogue:** ** *(none)*

**Prompt:**
```
tournament gear check wristband table official scanning athletes queue Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt waiting adjusting forearm guard strap fluorescent hallway, STYLE: PREMIER
```

---
### Panel 1.18 — Empty Warmup Floor
**Scene:** ** **Ethan Hyun** passes open mats — no instructor. Kids sitting on floor in hogus, scrolling phones.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt walking past empty warmup mats no coach teens sitting on gym floor in kyorugi gear on phones neglectful atmosphere wide shot, STYLE: PREMIER
```

---
### Panel 1.19 — Bracket Shock
**Scene:** ** Ethan (15, small, dark blue hair) stares at bracket board. His division circled: **−45kg — Ring 4 — 3:12 PM**.
**Dialogue:** ** Ethan (internal): *Seven hours.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, teen boy dark blue shadow perm hair staring at tournament bracket board, finger on paper bracket,
shocked quiet expression, taekwondo uniform with school patch, crowded gymnasium background,
close-up on face and bracket, STYLE: PREMIER
```

---
### Panel 1.20 — Walking to Bleachers
**Scene:** ** POV climbing metal bleacher steps in **hogu**. Crowd noise above. **Ethan Hyun's** guarded knees in frame.
**Dialogue:** ** *(none)*

**Prompt:**
```
POV climbing metal bleacher steps Olympic blue electronic hogu forearm shin guards in frame tournament gymnasium crowd above Ethan Hyun teen 15 dark blue shadow perm hair full Olympic kyorugi kit white dobok Premier patch perspective immersive shot, STYLE: PREMIER
```

---
### Panel 1.21 — No Warmup
**Scene:** ** Wide shot — 20+ Premier kids in gear. Instructor at far end talking to parents with coffee. **Repeul Kim** in ugly multicolor casual at edge of parent cluster — silent. No one on mats.
**Dialogue:** ** *(none)*

**Prompt:**
```
wide shot metal bleachers in gymnasium, young taekwondo fighters sitting in full protective gear
waiting, coach ignoring them talking to parents with coffee cups, overweight woman ugly multicolor clothes mean scowl background silent,
no training mats in use, neglectful atmosphere, STYLE: PREMIER
```

---
### Panel 1.22 — Bleacher Isolation
**Scene:** ** Ethan alone on bleachers. Empty seats on both sides. Legs in hogu, mouthguard case open.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, lonely teen boy in taekwondo chest guard sitting alone on metal bleachers, empty seats around him,
slumped posture, mouthguard on bench beside him, isolated composition, grey desaturated palette,
STYLE: PREMIER
```

---
### Panel 1.23 — Time Passes (Montage Cell 1)
**Scene:** ** Phone screen overlay: **10:23 AM**. Ethan same seat, vending machine snack wrapper nearby.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, same teen on bleachers time skip montage panel, phone screen showing 10 AM, crumpled snack wrapper,
legs still in gear, bored exhausted expression, STYLE: PREMIER
```

---
### Panel 1.24 — Vending Run
**Scene:** ** **Ethan Hyun** walking concourse in **full kit**. Returns to bleachers with snack wrapper, still alone.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt walking tournament concourse vending machines returning to bleachers crumpled snack wrapper in hand empty corridor afternoon, STYLE: PREMIER
```

---
### Panel 1.25 — Time Passes (Montage Cell 2)
**Scene:** ** Clock **1:47 PM**. Other kids on phones. Ethan staring at ring — still not his turn.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, gymnasium bleachers afternoon, wall clock 1 PM, teen athletes scrolling phones in taekwondo gear,
one small dark blue hair boy staring forward at distant competition ring, STYLE: PREMIER
```

---
### Panel 1.26 — Legs Asleep
**Scene:** ** **Ethan Hyun** on bleachers shaking leg — pins and needles. Grimace. Clock still hours from his match.
**Dialogue:** ** Ethan (internal): *Come on.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt sitting on bleachers shaking stiff leg pins and needles grimacing afternoon wall clock background bored exhausted, STYLE: PREMIER
```

---
### Panel 1.27 — Bleachers Watch [PRESENT — tournament venue]
**Scene:** **Ethan Hyun** in full kit on bleachers waiting. Across the floor, **Ttong Kim** personally warms up a **young female teen student** — hands-on spotting, adjusting stance, hands on shoulders/hips longer than necessary. Reads **touchy and uncomfortable**; implies nefarious favoritism. Ethan watches, unsettled. Blue helmet on bench beside him.
**Timeline:** ** **PRESENT** — nightmare tournament day, after long wait (PAGE 4).
**Dialogue:** ** *(none — visual only)*

**Prompt:**
```
Ethan Hyun teen 15 full competition kit blue hogu blue helmet off on bleacher bench sitting alone watching across gymnasium,
distant Ttong Kim instructor hands-on warming up young female teen athlete spotting stretch hands on shoulders hips too long uncomfortable favoritism,
Ethan unsettled tight expression empty seats beside him tournament fluorescents, STYLE: PREMIER
```

---
### Panel 1.28 — The Contract [FLASH — enrollment day]
**Scene:** Small bordered desaturated inset. Premier front desk. **Faceless dark shadow parent** (no features) extends **VIP brochure** to **Ttong Kim**. **Repeul Kim** in background **counting money**. **Young Ethan ~5 years old** at frame edge beside shadow parent — **joyous grin**, excited to join. Not the favored stranger kid — this is **Ethan's own enrollment memory**.
**Timeline:** ** **FLASH** — years earlier, Premier enrollment (not tournament).
**Dialogue:** ** Ttong Kim (to shadow parent): "We'll take good care of **him**." *(him = young Ethan)*

**Prompt:**
```
flashback inset border desaturated Premier taekwondo front desk enrollment,
faceless dark shadow parent silhouette no facial features handing VIP brochure to Ttong Kim sleazy smile,
Repeul Kim background counting cash money stack,
young boy Ethan age 5 small child dark hair joyous excited grin beside shadow parent ready to join taekwondo,
STYLE: PREMIER flashback sleazy contract
```

---
### Panel 1.29 — Called to Ring [PRESENT — tournament venue]
**Scene:** Referee or PA at competition floor. Arena wide enough to show bleachers. **"Hyun, Ethan — Ring 4."** Ethan on bleachers looks up — finally his match. Legs stiff from waiting.
**Timeline:** ** **PRESENT** — same day, afternoon.
**SFX:** ** PA / referee: *"Hyun, Ethan — Ring 4."*

**Prompt:**
```
tournament gymnasium referee or PA announcement wide shot competition rings,
Ethan Hyun teen full kit on bleachers looking up alert stiff legs afternoon harsh fluorescents,
Ring 4 staging visible background, STYLE: PREMIER
```

---
### Panel 1.30 — Walk Past [PRESENT — tournament floor]
**Scene:** Ethan picks up **blue helmet** from bench, stands, walks toward ring. Passes **Ttong Kim** still focused on the **young female student** — Ttong does **not** look at Ethan, no goodbye, no corner advice. Ethan walks alone toward sparring ring.
**Timeline:** ** **PRESENT** — immediately after 1.29.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen full competition kit carrying blue helmet walking past Ttong Kim instructor,
Ttong still hands-on with young female student ignoring Ethan completely,
Ethan alone walking toward distant competition ring tournament floor tracking shot neglect,
STYLE: PREMIER
```

---
### Panel 1.31 — Dojang Montage [FLASH — training cuts]
**Scene:** Intercut flash montage at Premier dojang — teen **Ethan** in white dobok/black belt during sparring: **(a)** clean **head kick** landing, **(b)** **roundhouse to body**, **(c)** **cut kick / push kick** sending opponent to floor. Fast kinetic cuts — he was skilled.
**Timeline:** ** **FLASH** — weeks/months before tournament, dojang scrimmage.
**Dialogue:** ** Ethan (internal, optional): *Won every scrimmage last month.*

**Prompt:**
```
FLASH montage tri-cut Premier dojang sparring teen Ethan dark blue hair white dobok black belt,
panel A clean head kick landing on teammate,
panel B roundhouse kick to body,
panel C cut kick push kick opponent falling to mat,
dynamic action sharp linework, STYLE: PREMIER flashback
```

---
### Panel 1.32 — Displeased Coach [FLASH — dojang]
**Scene:** Premier **dojang** (not tournament). **Ttong Kim** standing sidelines, **arms crossed**, **watching** sparring with **displeased unsatisfied** expression — not happy with Ethan. **Repeul Kim** behind/near him **eating potato chips**. Teen **Ethan** in dobok **looks back** over shoulder and **notices** Ttong's displeased look.
**Timeline:** ** **FLASH** — same period as 1.31 dojang scrimmage.
**Dialogue:** ** *(none)*

**Prompt:**
```
FLASH Premier dojang Ttong Kim standing arms crossed watching sparring displeased unsatisfied scowl frown judging,
Repeul Kim behind eating potato chips bag multicolor casual mean scowl,
teen Ethan white dobok black belt looking back over shoulder noticing coach unhappy expression dojang mirrors trophies,
desaturated flashback NOT tournament, STYLE: PREMIER
```

---
### Panel 1.33 — Ring Start [PRESENT — competition ring]
**Scene:** **Blue center / red border** ring mat. **Ethan** in **blue hogu** putting **helmet on** in ring. **Opponent** in **red hogu** opposite — **noticeably taller/bigger** than Ethan by a few inches. **Referee** (black pants, white shirt, red tie) **hand raised** about to start match.
**Timeline:** ** **PRESENT** — nightmare tournament, first moment in ring before fight.
**Dialogue:** ** *(none)*

**Prompt:**
```
tournament ring blue center mat red border Ethan Hyun teen small 5 foot 3 blue hogu fastening blue helmet on,
taller bigger teen opponent red hogu facing opposite standoff few inches taller larger build,
referee black pants white dress shirt red tie hand raised starting match,
crowd arena background, STYLE: PREMIER
```

---
### Panel 1.34 — Staging Line *(may skip in strip reader)*
**Scene:** ** Officials checking gear. **Ethan Hyun** in queue — chest sensor tap, headgear check.
**Dialogue:** ** Official: "Next."

**Prompt:**
```
tournament staging line officials checking electronic hogu blue helmet Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt waiting in queue tense expression gear inspection, STYLE: PREMIER
```

---
### Panel 1.35 — [CARD] Ttong Kim Intro ★
**Scene:** Fighter profile card — portrait + **stat block** (match GitHub roster): **Age 38 · Ht 5'8" · Wt 198 lbs · 2nd Dan · Premier**. Red accent bar. Underbite, predatory grin, polo/shorts.
**Note:** **Readable stat text allowed on fighter cards only.**

**Prompt:**
```
manhwa fighter profile card Ttong Kim portrait stocky underbite predatory grin black polo shorts,
stat block readable Age 38 Height 5'8 Weight 198 lbs Rank 2nd Dan Premier,
red accent bar STYLE CARD STYLE PREMIER
```

---
### Panel 1.36 — [CARD] Repeul Kim Intro ★
**Scene:** Fighter card — **Age 37 · Ht 5'5" · Wt 230 lbs · Premier (staff)**. Multicolor casual, mean scowl. **Never speaks.**

**Prompt:**
```
manhwa fighter profile card Repeul Kim brown curls multicolor floral ugly casual mean scowl,
stat block Age 37 Height 5'5 Weight 230 lbs Premier staff,
red-grey accent bar STYLE CARD STYLE PREMIER
```

---
### Panel 1.36b — [CARD] Ethan Hyun Intro ★
**Scene:** Fighter card — **Age 15 · Ht 5'3" · Wt 95 lbs · 3rd Dan · Junior −45kg · Premier** (nightmare roster). Gear-front portrait.

**Prompt:**
```
manhwa fighter profile card Ethan Hyun teen 15 dark blue hair full kit blue hogu Premier patch,
stat block Age 15 Height 5'3 Weight 95 lbs Rank 3rd Dan Division Junior -45kg,
blue accent bar STYLE CARD STYLE PREMIER
```

---
### Panel 1.37 — Knockout Bounty [REAL #28] ★
**Scene:** Ttong holds **1,000 won**. Eyes Ethan — *too soft.* Repeul blurred edge, scowl, silent.
**Dialogue:** ** Ttong: "One thousand won if you knock them out… Too soft."
**Script:** [flash-premier-knockout-bounty.md](../scripts/flash-premier-knockout-bounty.md)

**Prompt:**
```
Ttong Kim holding 1000 won coin bill pointing at teen Ethan black belt too soft unsettling,
Repeul Kim multicolor casual scowl blurred edge silent,
STYLE: PREMIER
```

---
### Panel 1.38 — Ninety Seconds *(skipped — in ring from 5c)*
**Scene:** ** Instructor appears — first time all day close to Ethan. Looks at watch. Points at ring.
**Dialogue:** ** Instructor: **"Go fight."**

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, cold taekwondo instructor pointing toward competition ring, dismissive expression,
teen athlete in white dobok full olympic kyorugi gear blue electronic hogu blue helmet forearm shin foot guards listening,
instructor checking wristwatch, no warmth,
dramatic low angle, STYLE: PREMIER
```

---
### Panel 1.39 — Walk to Ring
**Scene:** ** **Ethan Hyun** in corridor toward competition floor. Referee whistle distant. Legs still stiff.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt walking corridor toward competition floor distant referee whistle stiff gait overhead arena lights dramatic depth, STYLE: PREMIER
```

---
### Panel 1.40 — Ring Threshold
**Scene:** ** **Ethan Hyun** stepping over boundary tape onto competition mat. Opponent warming up ahead.
**Dialogue:** ** *(none)*

**Prompt:**
```
close-up feet stepping over competition ring boundary tape onto mat Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, full Olympic kyorugi kit white dobok blue electronic hogu blue helmet forearm shin foot guards Premier school patch black belt entering ring opponent warming up background low angle threshold moment, STYLE: PREMIER
```

---
### Panel 1.41 — Hesitant Step [PRESENT — ring] *(PAGE 6 R3 part A)*
**Scene:** **Over-shoulder Ethan POV.** Looming **red hogu** opponent. **Ttong yelling** at corner — *attack, attack, don't be soft.* Ethan **hesitant**.
**Dialogue:** ** Ttong (O.S.): "Attack! Attack! Don't be soft!"

**Prompt:**
```
over shoulder POV Ethan blue hogu facing looming taller red hogu opponent,
Ttong Kim at corner yelling aggressive pointing attack,
hesitant frozen stance blue center red border mat, STYLE: PREMIER
```

---
### Panel 1.42 — Abandoned Corner *(skipped — replaced by 1.41 POV)*
**Scene:** ** Over-shoulder from ring — instructor already walking toward another kid in premium gear.
**Dialogue:** ** *(none)*

**Prompt:**
```
over shoulder view from competition ring,
abandoned fighter in foreground white dobok full olympic kyorugi gear blue electronic hogu blue helmet forearm shin guards,
coach walking away toward another student in full competition kit,
emotional gut punch composition, STYLE: PREMIER
```

---
### Panel 1.43 — Hook Kick & Mouthguard [PRESENT] *(PAGE 6 R3 part B)*
**Scene:** Ethan **steps forward** — opponent **hook kick (huryeo chagi)** facing Ethan, head peeking over shoulder, **heel** strikes blue helmet. **Close-up**: **mouthguard flies out**. Sensor flash.
**SFX:** ** *THWACK* · +3**

**Prompt:**
```
spinning hook kick impact Ethan blue helmet sensor flash,
extreme close-up mouthguard flying out of mouth,
Ethan stepping into kick taller red hogu opponent, STYLE: PREMIER action
```

---
### Panel 1.44 — Score & Silence [PRESENT] *(PAGE 7)*
**Scene:** **R1 (1.44a):** Scoreboard **RED 6 · BLUE 0** (labels only). Ethan falling backward · mouthguard + helmet airborne. **R2 (1.44b):** Four-panel strip — Ethan **face down** → Ttong unconcerned → one-hand wave → walks away.
**Dialogue:** ** *(silence)*

**Prompt:**
```
ROW1 scoreboard 6-0 Ethan falling backward head kick,
ROW2 five-frame montage 50-25-25 layout:
FRAME A 50% left Ethan knocked down on blue red mat silent horror crowd mouths no sound,
FRAME B 25% Ttong disappointed arms crossed,
FRAME C 25% Ttong dismissive hand wave shooing,
FRAME D 25% Ethan still on floor alone,
FRAME E 25% Ttong walking away back turned leaving,
muted desaturated STYLE: PREMIER
```

---
### Panel 1.45 — Fade to Black *(PAGE 7 R3)*
**Scene:** After KO — traumatic fade **from face-down Ethan on mat** dissolving into black. Not bedroom yet.
**Dialogue:** ** *(silence)*

**Prompt:**
```
traumatic fade to black Ethan Hyun falling after head kick silhouette disappearing soundless horror muted desaturated vignette closing NOT bedroom yet, STYLE: PREMIER
```

---
### Panel 1.46 — Smash Cut Wake
**Scene:** ** Ethan bolts upright in bed. Sweat on temples. Mouth open — silent scream.
**SFX:** ** *GASP*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, teen boy jolting awake in bed sweating, gasping, dark blue hair messy, dawn light through curtains,
horror wake up moment, bedroom interior, dramatic upward angle, STYLE: PREMIER fading to neutral
```

---
### Panel 1.47 — Aftermath
**Scene:** ** Ethan staring at ceiling. Gold headphones on nightstand. Hand raised — block position — trembling.
**Dialogue:** ** Ethan (internal): *It wasn't just the kick.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression, teen lying in bed staring at ceiling, hand raised in taekwondo block pose trembling,
gold headphones on nightstand, soft morning light, quiet emotional aftermath, close-up,
```

---
### Panel 1.48 — Slow Breath
**Scene:** ** **Ethan Hyun** in bed — hands on chest. Breath slowing. Dawn birds outside. Grey sleep tee. Calming after gasp.
**Dialogue:** ** *(none)*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok lying in bed hands on chest slow breathing calming dawn birds outside window soft grey morning light emotional recovery beat, STYLE: neutral
```

---

# Chapter 2 — Arrival at Kwon's

### Panel 2.1 — Morning Crosswalk
**Scene:** **Ethan Hyun** at crosswalk. White gear backpack. Light traffic. Kwon's direction ahead.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants waiting at suburban crosswalk morning light headphones around neck quiet determination, STYLE: KWONS
```

---
### Panel 2.2 — New Day
**Scene:** Ethan walks street with white gear backpack. Headphones on. Kwon's sign visible ahead.
**Dialogue:** *(none)*

**Prompt:**
```
teen boy walking suburban street wearing gold headphones white gear backpack,
taekwondo academy sign visible ahead, overcast morning clearing to soft light,
STYLE: KWONS beginning
```

---
### Panel 2.3 — Slowing Near Sign
**Scene:** Ethan slows as Kwon's Taekwondo sign comes into view. Steps shorten.

**Prompt:**
```
teen boy slowing walk Kwon's taekwondo academy sign coming into view street level Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants, STYLE: KWONS
```

---
### Panel 2.4 — Through the Window
**Scene:** Ethan peeks through dojang glass. Inside: MV holds focus mitts — one student throwing roundhouses. MV adjusts foot angle mid-drill.
**Dialogue:** MV (muffled): "Turn the hip more — yes, like that."

**Prompt:**
```
view through dojang window, korean taekwondo master holding focus mitts coaching one student,
individual attention, footwork correction, warm interior golden light, observer silhouette outside,
STYLE: KWONS
```

---
### Panel 2.5 — Reading Sign Exterior
**Scene:** Close on sign — clean logo, hours, no Premier branding. Ethan reads from sidewalk.
**Dialogue:** Ethan (internal): *Different name. Different air.*

**Prompt:**
```
Kwon's taekwondo academy exterior sign close-up clean logo warm wood trim no premier branding observer silhouette below, STYLE: KWONS
```

---
### Panel 2.6 — Contrast Split
**Scene:** Split panel. LEFT: Premier — crowded mat, instructor's back, kids waiting. RIGHT: Kwon's — two people, eye contact.
**Dialogue:** *(none)*

**Prompt:**
```
split screen comic panel left cold crowded taekwondo school instructor back turned,
right warm small class one coach facing one student eye contact, visual contrast,
STYLE: PREMIER left STYLE: KWONS right
```

---
### Panel 2.7 — Stepping Back From Window
**Scene:** Ethan steps back from dojang glass after peeking — breath visible. Decision pause.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants stepping back from dojang window hands in hoodie pocket hesitant exhale warm interior glow reflection, STYLE: KWONS
```

---
### Panel 2.8 — Hand on Door
**Scene:** Ethan at entrance. Hand on door handle. Headphones around neck now. Hesitation.
**Dialogue:** Ethan (internal): *What if it's the same?*

**Prompt:**
```
close-up teen hand on dojang door handle hesitating, white taekwondo backpack strap visible,
warm light leaking through door gap, emotional threshold moment, STYLE: KWONS
```

---
### Panel 2.9 — Second Door Approach
**Scene:** Ethan approaches entrance again — headphones now around neck. Hand rises to handle.

**Prompt:**
```
teen approaching dojang door second time Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants hand reaching door handle threshold moment warm light leak, STYLE: KWONS
```

---
### Panel 2.10 — Door Opens
**Scene:** Ethan steps in. MV and student look over — not hostile, curious. Clean mats. Quiet.
**Dialogue:** *(none)*

**Prompt:**
```
teen entering taekwondo dojang doorway, warm wooden floors clean mats, coach and student pausing to look,
welcoming quiet atmosphere, backlit entrance silhouette, STYLE: KWONS
```

---
### Panel 2.11 — Foyer Entry Walk
**Scene:** Ethan walks through small foyer — shoe racks, bulletin board, quiet.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking small dojang foyer shoe racks bulletin board clean quiet atmosphere, STYLE: KWONS
```

---
### Panel 2.12 — Premier Ghost
**Scene:** Ethan pauses inside entrance. **FLASH inset** — crowded Premier mat, instructor's back. Snaps back to quiet Kwon's.
**Dialogue:** Ethan (internal): *Same sport. Different air.*

**Prompt:**
```
teen fighter just inside dojang doorway small flashback inset crowded cold school instructor back turned,
present warm empty reception area contrast, dissociation beat, STYLE: KWONS with PREMIER inset
```

---
### Panel 2.13 — Hallway to Shoe Rack
**Scene:** Short hallway. Ethan spots shoe cubbies. Pauses at Premier-habit speed.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants short hallway approaching shoe cubby wall pausing old habit tension, STYLE: KWONS
```

---
### Panel 2.14 — Shoes Off
**Scene:** Close-up — Ethan removes sneakers, lines them beside others. Kwon's shoe rack — worn but neat.
**Dialogue:** *(none — ritual beat)*

**Prompt:**
```
close-up teen removing sneakers placing on wooden shoe rack taekwondo dojang entrance,
other student shoes lined neatly, respectful detail panel, STYLE: KWONS
```

---
### Panel 2.15 — Walking to Wall Spot
**Scene:** Ethan walks to open wall space — not on mat yet. Bag down. Observing.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants setting white gear backpack against wall watching class from edge not on mat yet, STYLE: KWONS
```

---
### Panel 2.16 — Observation — MV Counts
**Scene:** Wide — MV counts reps aloud for one student on mitts. No yelling. Steady rhythm.
**Dialogue:** MV: "Four… five… turn the hip on six."

**Prompt:**
```
taekwondo master counting reps calmly holding focus mitts one student kicking,
empty space on mat not overcrowded, patient coaching wide shot, STYLE: KWONS
```

---
### Panel 2.17 — Glance at Restroom Door
**Scene:** Ethan glances at changing room door — dobok inside bag. Not ready yet.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants glance at changing room door gear bag at feet hesitation quiet dojang background, STYLE: KWONS
```

---
### Panel 2.18 — Student Thanks
**Scene:** Student bows, wipes sweat — genuine smile at MV. MV nods once — not performative.
**Dialogue:** Student: "Thank you, Master."

**Prompt:**
```
teen student bowing to taekwondo master after drill genuine grateful smile,
master modest nod not theatrical, warm mentor moment, STYLE: KWONS
```

---
### Panel 2.19 — Shifting Weight at Cubbies
**Scene:** Ethan shifts weight at cubbies — MV drilling in background blur.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants shifting weight near shoe cubbies Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes coaching blurred background warm floor light, STYLE: KWONS
```

---
### Panel 2.20 — Ethan Watches From Wall
**Scene:** Ethan stands by gear cubbies — hasn't changed yet. Arms crossed. Studying the room.
**Dialogue:** *(none)*

**Prompt:**
```
short teen boy with white gear backpack standing against dojang wall arms crossed observing,
other students training background soft focus, guarded watcher composition, STYLE: KWONS
```

---
### Panel 2.21 — Following MV Gesture
**Scene:** MV subtle gesture — *you can sit there*. Ethan nods micro, moves.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes subtle welcoming gesture toward wall spot Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants small nod moving to sit respectful distance, STYLE: KWONS
```

---
### Panel 2.22 — Trophy Shelf Honest
**Scene:** Ethan glances at modest trophy shelf — local medals, faded ribbon. No fake gold wall.
**Dialogue:** Ethan (internal): *No brochure lies.*

**Prompt:**
```
modest taekwondo dojang trophy shelf few real medals honest worn ribbon,
teen glancing sideways at shelf detail shot, STYLE: KWONS
```

---
### Panel 2.23 — Sunset Light Shift
**Scene:** Golden hour light crawls across mat. Class time passing. Ethan still watching.

**Prompt:**
```
dojang wooden floor sunset light band moving across mat time passage warm amber student training silhouette, STYLE: KWONS
```

---
### Panel 2.24 — Window Light
**Scene:** Golden hour through high windows. Dust motes. Ethan exhales — shoulders drop one inch.
**Dialogue:** *(none — beat)*

**Prompt:**
```
golden afternoon light through dojang windows dust particles floating,
teen silhouette relaxing shoulders slightly emotional release, STYLE: KWONS
```

---
### Panel 2.25 — Student File Past
**Scene:** Student files past Ethan — polite nod. Ethan nods back — first social beat.

**Prompt:**
```
dojang student walking past Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants polite nod exchange warm corridor light found-family seed, STYLE: KWONS
```

---
### Panel 2.26 — Other Student Notices
**Scene:** A cadet student (background extra) whispers to friend — points subtly at Ethan's backpack.
**Dialogue:** Cadet: "New guy brought competition gear."

**Prompt:**
```
two background taekwondo students whispering glancing at newcomer with gear backpack,
new student unaware foreground, natural dojang gossip, STYLE: KWONS
```

---
### Panel 2.27 — Class Ends — Ethan Stands
**Scene:** Students bow out. Ethan stands when class ends — unsure if he should.

**Prompt:**
```
students bowing out end of class Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants standing uncertain whether to join warm dojang, STYLE: KWONS
```

---
### Panel 2.28 — MV Finishes Drill
**Scene:** MV dismisses student with pat on shoulder. Turns — sees Ethan properly for first time inside.
**Dialogue:** MV: "You can put your bag down. You're not in the way."

**Prompt:**
```
taekwondo master finishing lesson turning to notice visitor teen with backpack,
kind open expression not suspicious, STYLE: KWONS
```

---
### Panel 2.29 — Exit Walk Stops
**Scene:** Ethan walks toward exit — stops mid-step. Hand on bag strap.
**Dialogue:** Ethan (internal): *…*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking toward dojang exit stopping mid-step hand on backpack strap threshold indecision, STYLE: KWONS
```

---
### Panel 2.30 — Bag Down
**Scene:** Ethan sets white gear backpack on bench — slow, deliberate. Sits beside it without changing.
**Dialogue:** Ethan: "I'm… just looking today."

**Prompt:**
```
teen placing white taekwondo gear backpack on bench sitting beside it hesitant,
dojo interior quiet, first honest words, STYLE: KWONS
```

---
### Panel 2.31 — Looking Back at Mat
**Scene:** Ethan looks back at empty mat — MV rolling shoulders. Quiet.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants looking back at empty training mat Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes rolling shoulders end of day quiet emotional beat, STYLE: KWONS
```

---
### Panel 2.32 — MV Doesn't Push
**Scene:** MV pulls chair — sits across from Ethan. Not looming. Same eye level again.
**Dialogue:** MV: "Looking is allowed here."

**Prompt:**
```
master sitting on chair same height as seated teen equal conversation posture,
no pressure body language, STYLE: KWONS
```

---
### Panel 2.33 — MV Rolling Mat
**Scene:** MV rolls mat in background. Ethan still at door. Unspoken permission to stay.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes rolling up training mat background Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants silhouette at doorway golden hour light, STYLE: KWONS
```

---
### Panel 2.34 — Street Sound Memory
**Scene:** Through open door — distant car horn. Ethan's fingers twitch. **FLASH** — tournament PA echo *"Ring 4."*
**Dialogue:** *(SFX only)*

**Prompt:**
```
teen fingers twitching on bench open dojang door background street sound trigger,
small traumatic flash inset tournament PA speaker, STYLE: KWONS with PREMIER flash
```

---
### Panel 2.35 — Street Outside Golden Hour
**Scene:** Kwon's exterior — golden hour. Ethan exits small in frame.

**Prompt:**
```
Kwon's taekwondo academy exterior golden hour street warm light small teen exiting doorway peaceful suburban, STYLE: KWONS
```

---
### Panel 2.36 — MV Waits
**Scene:** MV doesn't ask what happened. Offers water bottle — unopened — slides it across bench.
**Dialogue:** MV: "When you're ready."

**Prompt:**
```
master sliding sealed water bottle across bench to quiet teen patient waiting,
simple kindness gesture close-up hands, STYLE: KWONS
```

---
### Panel 2.37 — Sidewalk Pause
**Scene:** Ethan pauses on sidewalk. Looks back at dojang window glow.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants pausing on sidewalk looking back at glowing dojang window evening peaceful expression, STYLE: KWONS
```

---
### Panel 2.38 — Ethan Accepts Water
**Scene:** Ethan takes bottle. Doesn't drink yet. Holds it like an anchor.
**Dialogue:** Ethan (internal): *One student. One voice.*

**Prompt:**
```
teen holding unopened water bottle both hands sitting on bench emotional anchor object,
soft side lighting face downcast, STYLE: KWONS
```

---
### Panel 2.39 — Phone Buzz — Deep Breath
**Scene:** Phone buzzes — Ethan ignores. Deep breath. Hint of next day.
**Dialogue:** Ethan (internal): *Tomorrow.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants phone buzzing in pocket ignored deep breath evening street soft sky tomorrow hint, STYLE: KWONS
```

---
### Panel 2.40 — Stay Until Close
**Scene:** Wide — class ends. Students bow out. Ethan still on bench. MV rolls mats nearby — doesn't rush him.
**Dialogue:** MV (off): "Lock-up's at nine. Take your time."

**Prompt:**
```
wide shot emptying dojang students bowing out teen still on bench master rolling mats background,
patient sanctuary atmosphere golden light, STYLE: KWONS
```

---

# Chapter 3 — Meeting MV

### Panel 3.1 — Silver Belt Close
**Scene:** Close on **Ethan Hyun's** silver-letter black belt — before MV approaches.

**Prompt:**
```
close-up silver-letter black belt on white dobok waist Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt hands at sides dojang floor, STYLE: KWONS
```

---
### Panel 3.2 — Silver Belt
**Scene:** Close-up — Ethan's silver-letter black belt. Other students whisper.
**Dialogue:** Student: "Is that real?"

**Prompt:**
```
close-up unusual silver letter embroidery on black taekwondo belt, other students whispering background,
dojo interior, detail shot, STYLE: KWONS
```

---
### Panel 3.3 — MV Crossing Mat
**Scene:** Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes crosses mat toward Ethan — unhurried. Other students quiet.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes walking across wooden mat toward teen student other students quiet watching warm light, STYLE: KWONS
```

---
### Panel 3.4 — MV Approaches
**Scene:** MV walks over — open posture, eye level with Ethan (Ethan short — MV slightly crouches).
**Dialogue:** MV: "You can watch as long as you want. Or you can join."

**Prompt:**
```
kind korean taekwondo master approaching short teen at equal eye level respectful posture,
open hands non-threatening, warm dojang background, STYLE: KWONS
```

---
### Panel 3.5 — Mirroring Bow Distance
**Scene:** Ethan mirrors bow distance — formal. MV matches. Respect established.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt and Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes bowing at respectful distance formal introduction mirror symmetry, STYLE: KWONS
```

---
### Panel 3.6 — No Sales Pitch
**Scene:** MV gestures to sign — *Kwon's Taekwondo Academy*. No trophy wall of lies. Simple, honest space.
**Dialogue:** MV: "No pressure. What's your name?"

**Prompt:**
```
simple honest taekwondo dojang interior modest trophy shelf, master gesturing welcome,
teen with dark blue hair quiet guarded expression, STYLE: KWONS
```

---
### Panel 3.7 — Changing Room Door
**Scene:** Ethan at changing room door — hand on frame. Dobok inside now.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants hand on changing room door frame white dobok visible inside decision moment, STYLE: KWONS
```

---
### Panel 3.8 — Ethan Speaks
**Scene:** Ethan removes headphones fully for first time. Small voice.
**Dialogue:** Ethan: "...Ethan."

**Prompt:**
```
teen boy removing gold headphones, vulnerable quiet expression saying his name,
close-up face, soft lighting, character introduction moment, STYLE: KWONS
```

---
### Panel 3.9 — Dobok Tie Hands
**Scene:** Close — Ethan's hands tying dobok belt. Silver letters visible.

**Prompt:**
```
close-up hands tying white dobok belt silver lettering Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt changing room mirror edge, STYLE: KWONS
```

---
### Panel 3.10 — Belt Question
**Scene:** Two students in background — one nudges other — staring at silver letters on Ethan's belt (still in bag, partially visible).
**Dialogue:** Student B: "Silver letters… you don't see that here."

**Prompt:**
```
background taekwondo students whispering pointing at unusual black belt silver embroidery in bag,
curious not hostile, STYLE: KWONS
```

---
### Panel 3.11 — Return to Main Mat
**Scene:** Ethan walks back to main mat — dobok on. MV nods once.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking back to main training mat Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes single approving nod warm dojang, STYLE: KWONS
```

---
### Panel 3.12 — MV Introduces Self
**Scene:** MV offers hand — Western shake, then switches to bow when Ethan bows first.
**Dialogue:** MV: "Viet Na. Most people say Master Viet. Either's fine."

**Prompt:**
```
taekwondo master introducing himself respectful bow handshake hybrid,
teen returning bow awkward polite, STYLE: KWONS
```

---
### Panel 3.13 — First Step on Mat
**Scene:** Close-up — Ethan's bare foot on wood. First official step on Kwon's mat.

**Prompt:**
```
close-up bare foot stepping onto polished wooden dojang mat first step Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt symbolic beat, STYLE: KWONS
```

---
### Panel 3.14 — Looking or Training
**Scene:** MV crosses arms — not aggressive. Direct question.
**Dialogue:** MV: "You looking or training?"

**Prompt:**
```
master direct question arms crossed relaxed teen considering answer pause panel,
dojo background quiet tension, STYLE: KWONS
```

---
### Panel 3.15 — Class Circle Wide
**Scene:** Wide — class in loose circle. Ethan at assigned edge. MV center.

**Prompt:**
```
wide shot dojang class loose circle formation Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes center Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt at edge attentive warm light, STYLE: KWONS
```

---
### Panel 3.16 — Long Beat
**Scene:** Beat panel — Ethan's eyes on mat lines. Jaw working. Silence stretches.
**Dialogue:** *(none — 3-second beat)*

**Prompt:**
```
minimal beat panel teen staring at dojang floor mat lines internal decision,
empty negative space emotional silence, STYLE: KWONS
```

---
### Panel 3.17 — MV Pointing Lane
**Scene:** MV points to training lane. Ethan watches direction.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes pointing to marked training lane Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt watching attentive coaching gesture, STYLE: KWONS
```

---
### Panel 3.18 — Training
**Scene:** Ethan stands — small nod.
**Dialogue:** Ethan: "…Training."

**Prompt:**
```
teen standing with quiet determined nod choosing to train,
character decision moment medium shot, STYLE: KWONS
```

---
### Panel 3.19 — Walking to Lane
**Scene:** Ethan walks to assigned lane. Shoulders lower — slightly less guarded.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to assigned training lane shoulders relaxing slightly warm floor, STYLE: KWONS
```

---
### Panel 3.20 — Changing Room
**Scene:** Ethan in corner — pulls dobok from bag. Hands pause on silver-letter belt.
**Dialogue:** Ethan (internal): *Last thing they couldn't take.*

**Prompt:**
```
teen changing into white taekwondo dobok holding silver letter black belt reverently,
private corner of dojang emotional detail, STYLE: KWONS
```

---
### Panel 3.21 — Feet on Tape Marks
**Scene:** Ethan's feet on floor tape marks. Stance setup.

**Prompt:**
```
close-up feet on dojang floor tape marks fighting stance setup Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt precise foot placement, STYLE: KWONS
```

---
### Panel 3.22 — First Bow In
**Scene:** Ethan steps onto mat — bows to room. Other students pause — return bow.
**Dialogue:** *(none — ritual)*

**Prompt:**
```
teen bowing entering taekwondo mat other students pausing to return bow respect,
formal dojang etiquette wide shot, STYLE: KWONS
```

---
### Panel 3.23 — Student Passing Nod
**Scene:** Another student passes — small nod. Ethan returns it.

**Prompt:**
```
dojang student passing nod Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt returning nod brief friendly exchange background class, STYLE: KWONS
```

---
### Panel 3.24 — MV Watches Footwork
**Scene:** MV asks for casual stance — Ethan shifts weight — professional habit from old school.
**Dialogue:** MV: "Show me how you stand before anyone tells you to."

**Prompt:**
```
master observing teen fighter natural fighting stance evaluation,
instructional medium two-shot, STYLE: KWONS
```

---
### Panel 3.25 — MV Demo Kick — Ethan Watches
**Scene:** MV demonstrates kick — clean chamber. Ethan watches eyes tracking.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes demonstrating roundhouse kick clean chamber Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt watching intently tracking movement teaching moment, STYLE: KWONS
```

---
### Panel 3.26 — Quiet Class
**Scene:** Observation — no one filming for social. No parents coaching from bleachers. Just training.
**Dialogue:** Ethan (internal): *No audience.*

**Prompt:**
```
taekwondo class training without parents filming without chaos focused practice,
teen noticing difference observational panel, STYLE: KWONS
```

---
### Panel 3.27 — Slow Chamber Copy
**Scene:** Ethan copies chamber — deliberately slow. MV observes without interrupting.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt copying kick chamber slowly deliberate form Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes observing patient coaching distance, STYLE: KWONS
```

---
### Panel 3.28 — Silver Belt Close-Up
**Scene:** Detail — silver letters catch window light. MV's eyes flick to belt — doesn't comment yet.
**Dialogue:** MV: "That's a serious belt."

**Prompt:**
```
close-up silver embroidered letters on black taekwondo belt catching light,
master's eyes in soft focus background measuring not judging, STYLE: KWONS
```

---
### Panel 3.29 — Sweat Towel Beat
**Scene:** Ethan wipes sweat with towel. First real exertion at Kwon's.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt wiping sweat with small towel first training exertion tired satisfied micro-expression, STYLE: KWONS
```

---
### Panel 3.30 — No Sales Pitch (Sign)
**Scene:** MV walks Ethan past wall — simple rates sheet. No "VIP package." No merch table.
**Dialogue:** MV: "We don't sell dreams. We train bodies."

**Prompt:**
```
simple honest taekwondo school tuition notice board no flashy marketing,
master gesturing matter-of-fact teen listening, STYLE: KWONS
```

---
### Panel 3.31 — Water Fountain Walk
**Scene:** Ethan walks to water fountain — hallway quiet. Breath steady.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to hallway water fountain short break steady breathing dojang corridor, STYLE: KWONS
```

---
### Panel 3.32 — Ethan Almost Smiles
**Scene:** Corner of Ethan's mouth — almost — doesn't complete. MV pretends not to notice.
**Dialogue:** *(none)*

**Prompt:**
```
subtle almost-smile on guarded teen face master looking away giving privacy,
micro-expression character beat, STYLE: KWONS
```

---
### Panel 3.33 — Bench Rest
**Scene:** Ethan on bench rest — water bottle. Watching class through doorway.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt sitting bench rest water bottle watching class through doorway warm light, STYLE: KWONS
```

---
### Panel 3.34 — Other Students Resume
**Scene:** Class returns to drills — but side glances — curiosity not hostility.
**Dialogue:** Cadet (whisper): "He moves like a black belt."

**Prompt:**
```
taekwondo students resuming drills stealing glances at skilled newcomer,
natural peer observation, STYLE: KWONS
```

---
### Panel 3.35 — MV Approaching Again
**Scene:** MV approaches again — crouches to Ethan's eye level.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes approaching crouching to teen eye level kind expression Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt listening respectful, STYLE: KWONS
```

---
### Panel 3.36 — MV Assigns Space
**Scene:** MV points open mat lane — not back corner exile.
**Dialogue:** MV: "You can work here. Same air as everyone else."

**Prompt:**
```
master pointing to open space on main dojang mat welcoming not segregating,
teen carrying belt to assigned spot, STYLE: KWONS
```

---
### Panel 3.37 — Evening Long Shadows
**Scene:** Evening — longer shadows on mat. Class winding down.

**Prompt:**
```
dojang wooden floor long evening shadows class winding down warm amber window light time passage, STYLE: KWONS
```

---
### Panel 3.38 — First Instruction
**Scene:** MV holds paddle low — testing reaction speed, not showmanship.
**Dialogue:** MV: "When I say hold, you hold. When I say go, you go. Clear?"

**Prompt:**
```
master holding focus paddle low ready position teen nodding understanding,
clear boundary setting mentor moment, STYLE: KWONS
```

---
### Panel 3.39 — Last Bow Out Walk
**Scene:** Ethan bows out with class — walks to changing room. Lighter step.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt bowing out with class walking toward changing room lighter step end of session, STYLE: KWONS
```

---
### Panel 3.40 — Ethan Nods
**Scene:** Ethan nods once — sharp. First crack of trust.
**Dialogue:** Ethan: "Clear."

**Prompt:**
```
teen sharp single nod focused eyes first trust beat,
close-up face golden light, STYLE: KWONS
```

---

# Chapter 4 — Training

### Panel 4.1 — Glove Wrap Hands
**Scene:** Close — Ethan wrapping hands for pad work. Focused.

**Prompt:**
```
close-up wrapping hands for pad work tape Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt focused expression preparation beat, STYLE: KWONS
```

---
### Panel 4.2 — Pad Work Begins [TEACH]
**Scene:** MV holds shield. Ethan in dobok — roundhouse kick chamber.
**Dialogue:** MV: "Roundhouse — dollyo chagi. Turn the hip, snap the leg. Show me."

**Prompt:**
```
taekwondo training teen chambering roundhouse kick labeled hip rotation,
master holding kicking shield instructional sports manga, STYLE: KWONS TEACH
```

---
### Panel 4.3 — Walking to Pad Lane
**Scene:** Ethan walks to pad lane — MV already turning with mitts.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to pad training lane Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes turning with focus mitts ready coaching setup, STYLE: KWONS
```

---
### Panel 4.4 — Roundhouse [TEACH]
**Scene:** Clean roundhouse impact. MV nods. Inset: strike zone on hogu highlighted.
**SFX:** *SMACK*
**Dialogue:** MV: "Two points to the body in a match — if the sensor agrees."

**Prompt:**
```
action taekwondo roundhouse kick hitting chest hogu target zone highlight,
instructional inset, master bracing shield, STYLE: KWONS TEACH
```

---
### Panel 4.5 — MV Holding Pads Approach
**Scene:** MV holds pads at perfect height. Ethan squares shoulders.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes holding focus mitts at proper height Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt squaring shoulders ready stance coaching intimacy, STYLE: KWONS
```

---
### Panel 4.6 — Back Kick [TEACH]
**Scene:** Ethan back kick — looking over shoulder. Textbook form.
**Dialogue:** MV: "Back kick — dwi chagi. Don't chase. Let them run into it."

**Prompt:**
```
teen executing taekwondo back kick looking over shoulder foot path diagram space,
instructional side view, STYLE: KWONS TEACH
```

---
### Panel 4.7 — Reset Walk Between Combos
**Scene:** Reset between combos — Ethan walks two steps back. Breath control.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt stepping back between combo resets controlled breathing Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes waiting patient pads down, STYLE: KWONS
```

---
### Panel 4.8 — Cut Kick [TEACH]
**Scene:** Cut kick to paddle — low line attack.
**Dialogue:** MV: "Cut kick — oreo chagi. Low line. Disrupt their balance before you score."

**Prompt:**
```
taekwondo cut kick low line striking focus paddle, leg chamber diagram inset,
instructional sports manga, STYLE: KWONS TEACH
```

---
### Panel 4.9 — Shield Pickup
**Scene:** Ethan picks up kicking shield — weight familiar from Premier, context different.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt picking up large kicking shield familiar weight new peaceful dojang context, STYLE: KWONS
```

---
### Panel 4.10 — Perfect Form
**Scene:** MV stops drill. Studies Ethan. Long pause.
**Dialogue:** MV: "Your form is perfect. Why would you leave a school that taught you this?"

**Prompt:**
```
taekwondo master studying teen fighter with serious impressed expression,
teen sweating breathing hard, quiet tension, medium two-shot, STYLE: KWONS
```

---
### Panel 4.11 — Rotation Wait Turn
**Scene:** Class rotation — Ethan waits turn against wall. Watching senior.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt waiting against wall during class rotation watching senior student train attentive, STYLE: KWONS
```

---
### Panel 4.12 — No Answer
**Scene:** Ethan looks away. Jaw tight.
**Dialogue:** Ethan: "..."

**Prompt:**
```
teen athlete looking away unable to answer, jaw clenched, master waiting patiently background,
emotional silence panel, STYLE: KWONS
```

---
### Panel 4.13 — Watching Senior Kick
**Scene:** Senior student kicks — clean snap. Ethan files movement.

**Prompt:**
```
senior student clean snapping kick demo Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt watching from sideline studying form, STYLE: KWONS
```

---
### Panel 4.14 — They Didn't Have Me
**Scene:** Ethan finally — quiet but clear — eyes still averted.
**Dialogue:** Ethan: "They didn't have me."

**Prompt:**
```
teen speaking difficult truth looking away master listening still not pushing,
emotional honesty panel medium shot, STYLE: KWONS
```

---
### Panel 4.15 — Back to Pads Focus
**Scene:** Back to pads — Ethan's eyes narrow. Focus returns.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt returning to focus mitts intense eyes narrow ready stance Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes holding pads, STYLE: KWONS
```

---
### Panel 4.16 — MV Adjusts Shield
**Scene:** MV resets drill — doesn't dwell. Professional pivot back to work.
**Dialogue:** MV: "Then show me what you kept."

**Prompt:**
```
master resetting kicking shield professional calm after emotional beat,
back to training transition, STYLE: KWONS
```

---
### Panel 4.17 — Mat Scuff Detail
**Scene:** Close — mat scuff from pivot. Evidence of real work.

**Prompt:**
```
close-up wooden dojang mat scuff mark from pivot foot training wear detail authentic practice, STYLE: KWONS
```

---
### Panel 4.18 — Chamber Speed [TEACH]
**Scene:** MV calls speed — Ethan chambers roundhouse faster — still clean.
**Dialogue:** MV: "Speed without form is just noise."

**Prompt:**
```
teen chambering fast roundhouse kick master observing hip alignment,
instructional speed vs form panel, STYLE: KWONS TEACH
```

---
### Panel 4.19 — MV Nod Continue
**Scene:** MV nods — *continue*. Ethan chambers again.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes nodding continue gesture Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt chambering kick again coaching rhythm trust building, STYLE: KWONS
```

---
### Panel 4.20 — Combo Flow
**Scene:** Roundhouse → cut kick chain on paddle. Fluid. Other students stop to watch.
**Dialogue:** *(SFX)* *smack-smack*

**Prompt:**
```
dynamic taekwondo combo roundhouse into cut kick on focus mitts,
background students pausing to watch impressed, STYLE: KWONS
```

---
### Panel 4.21 — Electronic Hogu Door Peek
**Scene:** Ethan peeks into electronic hogu room — sensors on wall.
**Dialogue:** MV (O.S.): "Sport mind stays with you."

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt peeking into electronic hogu training room sensors on wall curious respectful, STYLE: KWONS
```

---
### Panel 4.22 — Breathing Control
**Scene:** Ethan finishes — controlled breathing — not gasping. MV notes it.
**Dialogue:** MV (internal caption): *Conditioning held.*

**Prompt:**
```
teen fighter controlled breathing after combo sweat on brow steady,
master noting endurance detail observation panel, STYLE: KWONS
```

---
### Panel 4.23 — Walking to Sensor Zone
**Scene:** Ethan walks to sensor zone — one practice kick. Light registers.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to electronic scoring sensor zone practice kick light registering sport training, STYLE: KWONS
```

---
### Panel 4.24 — Back Kick Distance [TEACH]
**Scene:** MV steps in — Ethan back kick — perfect distance — MV doesn't flinch.
**Dialogue:** MV: "You don't flinch when they crowd you."

**Prompt:**
```
precise taekwondo back kick stopping inches from master chest perfect distance control,
instructional trust drill, STYLE: KWONS TEACH
```

---
### Panel 4.25 — Return to Main Mat
**Scene:** Ethan returns to main mat — MV already resetting shields.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking back to main mat Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes resetting kicking shields background routine coaching, STYLE: KWONS
```

---
### Panel 4.26 — Class Resumes Watching
**Scene:** Wide — whole class at water break — watching Ethan from sidelines. Not jealous — measuring.
**Dialogue:** Student: "Where'd he come from?"

**Prompt:**
```
taekwondo class on water break watching talented newcomer train sideline whispers,
peer assessment wide shot, STYLE: KWONS
```

---
### Panel 4.27 — Cool Down Perimeter Walk
**Scene:** Cool down — Ethan walks mat perimeter. Slow steps.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt cool down walking dojang mat perimeter slow steps relaxed shoulders, STYLE: KWONS
```

---
### Panel 4.28 — MV Correction Micro
**Scene:** MV taps Ethan's rear foot — tiny angle fix. Ethan adjusts instantly.
**Dialogue:** MV: "There. Don't lose that."

**Prompt:**
```
master correcting teen foot angle tiny adjustment instant compliance,
detail instructional panel feet and mat, STYLE: KWONS TEACH
```

---
### Panel 4.29 — Bow to MV Close
**Scene:** Close — Ethan bows to MV. MV returns deeper bow.

**Prompt:**
```
close-up mutual bow Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt and Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes respectful deep formal gratitude moment, STYLE: KWONS
```

---
### Panel 4.30 — Electronic Hogu Mention [TEACH]
**Scene:** MV holds chest hogu — points at sensor zone.
**Dialogue:** MV: "Olympic rules — chest sensor, head sensor. Power in the right zone beats flashy everywhere."

**Prompt:**
```
master holding electronic chest hogu explaining sensor zone diagram inset,
olympic taekwondo education panel, STYLE: KWONS TEACH
```

---
### Panel 4.31 — Gear Bag Zip
**Scene:** Ethan zips gear bag — satisfied tired. Locker number visible.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants zipping white gear backpack satisfied tired expression locker area end of training, STYLE: KWONS
```

---
### Panel 4.32 — Ethan Nods — Sport Mind
**Scene:** Ethan touches hogu — familiar — tournament muscle memory.
**Dialogue:** Ethan: "I know the zones."

**Prompt:**
```
teen touching electronic hogu chest sensor familiar tournament gear,
confident quiet knowledge, STYLE: KWONS
```

---
### Panel 4.33 — Exit Mat Backward Bow
**Scene:** Ethan exits mat with backward bow tradition — MV watches approving.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt exiting mat backward bow tradition Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes watching approving small smile warm light, STYLE: KWONS
```

---
### Panel 4.34 — Sweat On Mat
**Scene:** Close — sweat drop on mat. Ethan's first real work at Kwon's.
**Dialogue:** *(none — symbolic)*

**Prompt:**
```
close-up sweat drop on taekwondo mat after training symbolic first real work,
detail shot warm lighting, STYLE: KWONS
```

---
### Panel 4.35 — Water Bottle Break
**Scene:** Water bottle break — Ethan drinks. MV resets shields in background.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt water bottle break drinking Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes resetting kicking shields background end of pad session, STYLE: KWONS
```

---
### Panel 4.36 — Other Students Bow Out
**Scene:** Class ends — students bow to MV — Ethan follows half a beat late — copies form.
**Dialogue:** All: "Thank you, Master."

**Prompt:**
```
taekwondo class bowing out teen newcomer copying bow half beat late learning ritual,
group etiquette wide shot, STYLE: KWONS
```

---
### Panel 4.37 — MV Resetting Shields
**Scene:** MV stacks shields against wall — class winding down.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes stacking kicking shields against wall class winding down Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt toweling off background, STYLE: KWONS
```

---
### Panel 4.38 — MV Quiet Praise
**Scene:** MV to Ethan alone — low voice — not for show.
**Dialogue:** MV: "Better than most black belts I see walk in."

**Prompt:**
```
master quiet private praise to teen after class not performative,
intimate mentor moment two-shot, STYLE: KWONS
```

---
### Panel 4.39 — Hallway Bow Exit
**Scene:** Ethan bows toward mat from hallway door — last look.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants bowing toward training mat from hallway doorway last look respectful habit forming, STYLE: KWONS
```

---
### Panel 4.40 — Ethan Doesn't Know What To Do
**Scene:** Ethan opens mouth — closes it — bows instead. MV accepts bow.
**Dialogue:** *(none)*

**Prompt:**
```
teen awkward grateful bow instead of words master accepting bow warm,
character beat silence, STYLE: KWONS
```

---

# Chapter 5 — The Goal

### Panel 5.1 — MV Question Silence Wide
**Scene:** Wide — MV's question hangs. Ethan silent center frame.

**Prompt:**
```
wide shot dojang Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes asking question Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt silent center frame heavy emotional stillness, STYLE: KWONS
```

---
### Panel 5.2 — The Question
**Scene:** MV pours water for Ethan. Sitting on mats after drill.
**Dialogue:** MV: "What do you want?"

**Prompt:**
```
taekwondo master handing water bottle to teen sitting on dojang mats, post-training,
calm mentoring moment, golden afternoon light, STYLE: KWONS
```

---
### Panel 5.3 — Staring at Floor Tiles
**Scene:** Ethan staring at floor tiles — jaw tight.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt staring down at wooden floor tiles jaw tight internal conflict close angle, STYLE: KWONS
```

---
### Panel 5.4 — Silence
**Scene:** Ethan stares at water bottle. Reflection in cap.
**Dialogue:** *(none — beat panel)*

**Prompt:**
```
close-up teen staring at water bottle cap reflection, internal struggle, beat panel minimal action,
STYLE: KWONS
```

---
### Panel 5.5 — Korea U20 Poster Glance
**Scene:** Ethan glances at Korea U20 poster on wall — dream object.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt glancing at Korea U20 taekwondo poster on dojang wall dream aspiration detail, STYLE: KWONS
```

---
### Panel 5.6 — Korea U20
**Scene:** Ethan looks up — first fierce expression.
**Dialogue:** Ethan: "Korea U20 National Team."

**Prompt:**
```
teen boy looking up with fierce determined eyes, first sign of ambition,
dramatic low angle face close-up, dark blue hair, STYLE: KWONS
```

---
### Panel 5.7 — Window City View
**Scene:** Ethan at window — city view. MV small in reflection.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt at dojang window city view reflection Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes small behind thoughtful wide shot, STYLE: KWONS
```

---
### Panel 5.8 — The Ask
**Scene:** Ethan stands, bows slightly awkward.
**Dialogue:** Ethan: "I want to join Kwon's Taekwondo Academy."

**Prompt:**
```
teen standing bowing slightly awkward to taekwondo master, determination and vulnerability,
dojo background, respectful request moment, STYLE: KWONS
```

---
### Panel 5.9 — Fist Unclench
**Scene:** Close — Ethan's fist unclenches at window sill.

**Prompt:**
```
close-up fist unclenching on window sill Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt emotional release decision forming, STYLE: KWONS
```

---
### Panel 5.10 — MV Response
**Scene:** MV doesn't smile big — doesn't dismiss. Considers.
**Dialogue:** MV: "That's not a small dream. We can talk about it."

**Prompt:**
```
taekwondo master thoughtful expression arms crossed not dismissive not overjoyed,
measured response, teen waiting, STYLE: KWONS
```

---
### Panel 5.11 — Enrollment Desk Walk
**Scene:** Ethan walks to simple enrollment desk — papers ready.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to simple front desk enrollment papers ready small dojang office, STYLE: KWONS
```

---
### Panel 5.12 — Not A Small Dream
**Scene:** MV repeats — slower — letting words land.
**Dialogue:** MV: "That's not a small dream."

**Prompt:**
```
master repeating serious statement teen absorbing weight of words,
mentor gravity panel, STYLE: KWONS
```

---
### Panel 5.13 — Pen Hover
**Scene:** Pen hovers over signature line — tremor stills.
**Dialogue:** Ethan (internal): *Not small.*

**Prompt:**
```
close-up pen hovering over enrollment signature line hand steadying Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt decisive moment, STYLE: KWONS
```

---
### Panel 5.14 — Ethan Knows
**Scene:** Ethan — fierce again — doesn't back down from scale of goal.
**Dialogue:** Ethan: "I know."

**Prompt:**
```
teen fierce determined expression not backing down from big dream,
low angle face close-up, STYLE: KWONS
```

---
### Panel 5.15 — Signature Close-Up
**Scene:** Signature close-up — Ethan Hyun. Ink wet.

**Prompt:**
```
close-up signing enrollment form signature Ethan Hyun wet ink simple paper warm desk light, STYLE: KWONS
```

---
### Panel 5.16 — Small Dreams Die
**Scene:** MV wipes mouth with towel — matter-of-fact coaching wisdom.
**Dialogue:** MV: "Small dreams don't survive hard weeks."

**Prompt:**
```
master with towel around neck coaching wisdom matter-of-fact expression,
teen listening intently sitting on mat, STYLE: KWONS
```

---
### Panel 5.17 — Copy Paper Fold
**Scene:** MV folds copy paper — hands Ethan his. Matter-of-fact kindness.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes folding enrollment copy handing to Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt matter-of-fact kindness simple ritual, STYLE: KWONS
```

---
### Panel 5.18 — Formal Distance Narrows
**Scene:** MV sits beside Ethan — not above — same mat level.
**Dialogue:** MV: "What do you want from taekwondo — not what you think I want to hear."

**Prompt:**
```
master sitting beside teen on mat equal level honest question,
trust building composition, STYLE: KWONS
```

---
### Panel 5.19 — Locker Number 14
**Scene:** Locker number **14** — Ethan reads tag.

**Prompt:**
```
locker number 14 tag close-up Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants reading assigned locker belonging beat, STYLE: KWONS
```

---
### Panel 5.20 — Ethan Almost Lies Small
**Scene:** Ethan's mouth opens — "to get better" — stops himself.
**Dialogue:** Ethan (internal): *Don't shrink it.*

**Prompt:**
```
teen internal struggle almost saying small safe answer catching himself,
close-up face hesitation, STYLE: KWONS
```

---
### Panel 5.21 — Empty Locker Open
**Scene:** Ethan opens empty locker — echo inside metal.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants opening empty gym locker echo inside metal new beginning space, STYLE: KWONS
```

---
### Panel 5.22 — Room Still
**Scene:** Wide — empty dojang — two figures on mat — clock ticks.
**Dialogue:** *(none — beat)*

**Prompt:**
```
wide empty dojang two figures on mat silence clock on wall,
decision atmosphere beat panel, STYLE: KWONS
```

---
### Panel 5.23 — Placing Silver Belt Inside
**Scene:** Ethan places silver-letter belt inside locker — deliberate.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants placing silver-letter black belt inside locker deliberate careful ritual belonging, STYLE: KWONS
```

---
### Panel 5.24 — Korea U20 (Repeat Weight)
**Scene:** Same line — but now MV hears the weight. Ethan doesn't look away this time.
**Dialogue:** Ethan: "Korea U20 National Team."

**Prompt:**
```
teen stating ambitious goal eye contact with master not looking away,
dramatic character moment, STYLE: KWONS
```

---
### Panel 5.25 — Hallway Exit Night
**Scene:** Hallway exit — night. Ethan walks toward door light.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking dojang hallway toward exit door night interior warm hope, STYLE: KWONS
```

---
### Panel 5.26 — MV Doesn't Laugh
**Scene:** MV's reaction — no ridicule — slight eyebrow raise — respect.
**Dialogue:** *(none)*

**Prompt:**
```
master reaction no laughter slight eyebrow raise respect not mockery,
reaction panel face close-up, STYLE: KWONS
```

---
### Panel 5.27 — Streetlight Walk Home
**Scene:** Streetlight walk — slower pace. Looking up.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking home under streetlights slower pace looking up quiet hope night, STYLE: KWONS
```

---
### Panel 5.28 — Can I Train Here
**Scene:** Ethan bows from seated position — awkward but sincere.
**Dialogue:** Ethan: "Can I… train here?"

**Prompt:**
```
teen bowing from seated position awkward sincere request,
vulnerable formal ask, STYLE: KWONS
```

---
### Panel 5.29 — Apartment Door Unlock
**Scene:** Apartment door unlock — same keys, new chapter feeling.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants unlocking apartment door keys in hand new chapter quiet hope expression, STYLE: KWONS
```

---
### Panel 5.30 — No Promise
**Scene:** MV stands — offers hand to help Ethan up.
**Dialogue:** MV: "We'll see if you mean it."

**Prompt:**
```
master offering hand to help teen up no empty promise serious deal,
handshake help-up panel, STYLE: KWONS
```

---
### Panel 5.31 — Kitchen Water Glass
**Scene:** Kitchen — Ethan drinks water. Apartment still. Calmer than before.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants drinking water glass kitchen apartment still calm evening domestic peace, STYLE: KWONS
```

---
### Panel 5.32 — Ethan Takes Hand
**Scene:** Ethan accepts hand up — first physical trust.
**Dialogue:** *(none)*

**Prompt:**
```
teen accepting master's hand being helped up first physical trust gesture,
hands close-up warm light, STYLE: KWONS
```

---
### Panel 5.33 — Bed Stare Calmer
**Scene:** Ethan on bed staring at ceiling — calmer than Ch 1 nightmare aftermath.
**Dialogue:** Ethan (internal): *I said it out loud.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok lying on bed staring ceiling calmer expression soft night light contrast chapter 1 trauma, STYLE: KWONS soft
```

---
### Panel 5.34 — Enrollment Paper Simple
**Scene:** Front desk — one-page form. No VIP upsell. Ethan reads — plain language.
**Dialogue:** MV: "Month to month. Leave if we fail you."

**Prompt:**
```
simple one page taekwondo enrollment form no upsell teen reading relieved,
honest business practice panel, STYLE: KWONS
```

---
### Panel 5.35 — Locker Door Close
**Scene:** Locker door closes on silver belt — click. Belonging sealed.

**Prompt:**
```
close-up locker door closing on silver-letter black belt inside click sound belonging sealed, STYLE: KWONS
```

---
### Panel 5.36 — Ethan Signs
**Scene:** Ethan signs — hand steady. MV witnesses — no hard sell smile.
**Dialogue:** *(SFX)* *pen scratch*

**Prompt:**
```
teen signing enrollment form steady hand master witnessing no pressure smile,
commitment moment detail, STYLE: KWONS
```

---
### Panel 5.37 — Apartment Light Off
**Scene:** Ethan flips apartment light off — hallway dark. Day done.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants flipping apartment light switch off hallway going dark end of enrollment day, STYLE: KWONS soft
```

---
### Panel 5.38 — Gear Locker
**Scene:** MV assigns cubby number. Ethan places white backpack inside.
**Dialogue:** MV: "Same spot every day. This is yours."

**Prompt:**
```
master assigning gear locker cubby teen placing white backpack inside belonging moment,
dojo cubby row, STYLE: KWONS
```

---
### Panel 5.39 — Dawn Without Alarm
**Scene:** Dawn without alarm — Ethan wakes naturally. No gasp.

**Prompt:**
```
dawn waking naturally no alarm Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok calm eyes opening new routine hope, STYLE: KWONS soft
```

---
### Panel 5.40 — Night Exit Hope
**Scene:** Ethan leaves — night air — looks back through window — MV rolling last mat. Golden interior.
**Dialogue:** Ethan (internal): *Maybe.*

**Prompt:**
```
teen leaving dojang at night looking back through window master rolling mats inside golden light,
hopeful ending shot street exterior, STYLE: KWONS
```

---

# Chapter 6 — Why Leave

### Panel 6.1 — MV Direct Question Close
**Scene:** Close — MV's direct question. Kind eyes, no flinch.

**Prompt:**
```
close-up Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes direct kind question expression patient eyes no judgment coaching intimacy, STYLE: KWONS
```

---
### Panel 6.2 — Direct Question
**Scene:** MV and Ethan walking mats edge. Other students packing up.
**Dialogue:** MV: "Why did you leave your old school?"

**Prompt:**
```
master and teen walking along edge of dojang mats, quiet after hours, direct conversation,
STYLE: KWONS
```

---
### Panel 6.3 — Jaw Working
**Scene:** Ethan's jaw working — words stuck.

**Prompt:**
```
close-up Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt jaw clenching working words stuck internal struggle, STYLE: KWONS
```

---
### Panel 6.4 — Deflection
**Scene:** Ethan puts headphones back on one ear.
**Dialogue:** Ethan: "It wasn't home anymore."

**Prompt:**
```
teen putting gold headphones on one ear deflecting, guarded body language,
master listening without pushing, STYLE: KWONS
```

---
### Panel 6.5 — Mat Edge Walk Slow
**Scene:** Ethan walks mat edge slowly — fingers trail wall.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking slowly along dojang mat edge fingers trailing wall heavy steps, STYLE: KWONS
```

---
### Panel 6.6 — Flash Sting (Money)
**Scene:** Quick flash — Premier instructor's cold face. Hands exchanging cash. Red tint.
**Dialogue:** *(distorted)* "...with us or..."

**Prompt:**
```
traumatic flashback inset cold angry taekwondo instructor face, hands exchanging money,
red desaturated overlay, sharp fragment panel, STYLE: PREMIER
```

---
### Panel 6.7 — Flash Trigger Doorway
**Scene:** Doorway triggers flash — Premier logo ghost. Ethan flinches micro.

**Prompt:**
```
doorway frame triggering memory Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt micro flinch Premier logo ghost overlay desaturated flash edge, STYLE: PREMIER flash inset
```

---
### Panel 6.8 — MV Backs Off
**Scene:** MV nods — accepts answer for now.
**Dialogue:** MV: "When you're ready to tell me the rest, I'll listen."

**Prompt:**
```
kind taekwondo master nodding accepting answer, respectful distance, teen relieved but tense,
STYLE: KWONS
```

---
### Panel 6.9 — Present Feet on Wood
**Scene:** Present anchor — Ethan's feet on Kwon's wood. Solid.

**Prompt:**
```
close-up feet planted on warm wooden dojang floor present anchor Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt grounding beat, STYLE: KWONS
```

---
### Panel 6.10 — Walking Mats Edge
**Scene:** Ethan and MV walk perimeter — shoes off — evening class cleaning up.
**Dialogue:** MV: "Premier still has your friends on their roster."

**Prompt:**
```
master and teen walking dojang mat edge evening cleanup conversation,
casual serious talk wide shot, STYLE: KWONS
```

---
### Panel 6.11 — Cleaning Bucket Walk
**Scene:** Ethan carries cleaning bucket — MV hands him rag. Shared work.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt carrying cleaning bucket Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes handing rag shared dojang maintenance quiet bonding, STYLE: KWONS
```

---
### Panel 6.12 — Ethan Stiffens
**Scene:** Ethan flinches at school name — headphones hand moves to pocket.
**Dialogue:** Ethan: "They're not my friends if they stay."

**Prompt:**
```
teen flinching at mention of old school hand moving to headphones pocket,
defensive reaction close-up, STYLE: KWONS
```

---
### Panel 6.13 — Mop Stroke
**Scene:** Mop stroke across mat — rhythmic. Conversation optional.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt mopping wooden dojang mat rhythmic stroke Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes nearby quiet companionship, STYLE: KWONS
```

---
### Panel 6.14 — MV Corrects Gently
**Scene:** MV — calm — doesn't argue.
**Dialogue:** MV: "Some of them followed you out. Give them time."

**Prompt:**
```
master gentle correction calm expression teen stubborn profile,
mentor patience panel, STYLE: KWONS
```

---
### Panel 6.15 — Window Premier Logo Memory
**Scene:** Window reflection — Premier logo memory overlay. Ethan blinks it away.

**Prompt:**
```
dojang window reflection Premier logo memory overlay Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt blinking away returning to present, STYLE: PREMIER flash inset
```

---
### Panel 6.16 — Flash VIP [FLASH]
**Scene:** **FLASH** — paying kid gear adjustment — Ethan on bleachers same memory frame.
**Dialogue:** Instructor (flash): "Investment pays off."

**Prompt:**
```
flashback inset favored student gear adjustment instructor praising,
bleachers lonely teen same memory frame, STYLE: PREMIER flash
```

---
### Panel 6.17 — Phone Face Down Table
**Scene:** Phone face-down on table — Premier spam incoming.

**Prompt:**
```
smartphone face-down on table Premier spam notifications vibrating ignored boundary setting, STYLE: KWONS
```

---
### Panel 6.18 — Present — Jaw Clench
**Scene:** **PRESENT** — Ethan's jaw — knuckles white on belt.
**Dialogue:** *(none)*

**Prompt:**
```
present teen jaw clenched white knuckles on black belt emotional trigger,
close-up detail STYLE: KWONS
```

---
### Panel 6.19 — Spam Texts Blur
**Scene:** Spam texts blur on screen edge before Ethan flips phone over.

**Prompt:**
```
smartphone screen edge blurred Premier spam group texts Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants flipping phone face-down refusal, STYLE: PREMIER soft
```

---
### Panel 6.20 — Direct Question Again
**Scene:** MV stops walking — direct eye contact.
**Dialogue:** MV: "Did someone hurt you?"

**Prompt:**
```
master stopping direct eye contact serious care question,
teen caught off guard, STYLE: KWONS
```

---
### Panel 6.21 — Apartment Quiet Wide
**Scene:** Apartment wide — quiet. Ethan small on couch. City hum.

**Prompt:**
```
wide shot small apartment quiet Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants on couch city hum evening solitude not lonely, STYLE: KWONS soft
```

---
### Panel 6.22 — Ethan Opens Mouth
**Scene:** Ethan starts to speak — stops — shame and anger mix.
**Dialogue:** Ethan: "They…"

**Prompt:**
```
teen trying to speak stopping mid word shame anger mixed expression,
vulnerable beat panel, STYLE: KWONS
```

---
### Panel 6.23 — Mirror Belt Ritual
**Scene:** Mirror — Ethan ties belt. Same silver letters. Different home.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt tying belt before mirror silver letters same belt different home ritual calm, STYLE: KWONS
```

---
### Panel 6.24 — Flash Cash [FLASH]
**Scene:** **FLASH sting** — hands exchanging cash — Ttong cold grin — red overlay.
**Dialogue:** Ttong (distorted): "…with us or…"

**Prompt:**
```
traumatic flash hands exchanging money cold instructor grin red overlay fragment,
STYLE: PREMIER flash sting
```

---
### Panel 6.25 — Sleep Dark Room
**Scene:** Dark room — Ethan asleep. No nightmare sweat.

**Prompt:**
```
dark bedroom sleeping peacefully Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok no sweat no nightmare soft blanket calm, STYLE: KWONS soft
```

---
### Panel 6.26 — It Wasn't Home
**Scene:** **PRESENT** — Ethan blurts — then regrets volume.
**Dialogue:** Ethan: "It wasn't home anymore."

**Prompt:**
```
teen blurting emotional truth then immediately guarded,
master listening still, STYLE: KWONS
```

---
### Panel 6.27 — Dawn Without Gasp
**Scene:** Dawn light — Ethan wakes without gasp. Contrast Ch 1.

**Prompt:**
```
dawn light waking gently Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok no gasp no jolt calm eyes opening contrast chapter 1 nightmare, STYLE: KWONS soft
```

---
### Panel 6.28 — MV Accepts
**Scene:** MV nods — doesn't pry further today.
**Dialogue:** MV: "Home isn't a building. You'll know when you're in one."

**Prompt:**
```
master nodding wise quiet response teen processing,
mentor wisdom two-shot, STYLE: KWONS
```

---
### Panel 6.29 — Morning Street Routine
**Scene:** Morning street — Ethan walks to Kwon's. Routine forming.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants morning walk to dojang routine forming familiar street peaceful determination, STYLE: KWONS
```

---
### Panel 6.30 — Cleaning Together
**Scene:** Ethan picks up water bottle someone left — MV notices — doesn't comment.
**Dialogue:** *(none — character action)*

**Prompt:**
```
teen picking up forgotten water bottle helping clean dojang unprompted,
master noticing approving without words, STYLE: KWONS
```

---
### Panel 6.31 — Dojang Key Jingle
**Scene:** Close — keys jingle. Ethan opens door — early.

**Prompt:**
```
close-up keys in hand opening dojang door early morning Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants responsible routine, STYLE: KWONS dawn
```

---
### Panel 6.32 — Night Street
**Scene:** Ethan walks home — streetlights — phone dark in pocket.
**Dialogue:** Ethan (internal): *Not yet.*

**Prompt:**
```
teen walking home night streetlights hands in hoodie pocket phone dark,
contemplative solitude, STYLE: KWONS night
```

---
### Panel 6.33 — Lights Flip On
**Scene:** Lights flip on — empty mat glow. Ethan exhales.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants flipping on dojang lights empty mat glowing exhale ownership feeling, STYLE: KWONS dawn
```

---
### Panel 6.34 — Premier Text Spam
**Scene:** Phone lights up — spam — *"Come back for black belt test special."* Ethan deletes without opening.
**Dialogue:** (text) **"Limited slots — VIP only."**

**Prompt:**
```
smartphone spam text VIP taekwondo marketing teen deleting without reading,
disgust micro-expression, STYLE: PREMIER cold on phone glow
```

---
### Panel 6.35 — Mat Straighten
**Scene:** Ethan straightens mat corner — small care task.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt straightening training mat corner small care task quiet pride, STYLE: KWONS
```

---
### Panel 6.36 — Apartment Quiet
**Scene:** Ethan's room — gear bag by door — medal drawer closed — doesn't open it.
**Dialogue:** *(none)*

**Prompt:**
```
teen bedroom gear bag by door closed medal drawer not opening past trauma,
quiet domestic panel, STYLE: KWONS soft night
```

---
### Panel 6.37 — Window Rain Start
**Scene:** Window — rain starts. Ethan watches without flinching.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt watching rain begin on dojang window calm expression no trauma flinch, STYLE: KWONS
```

---
### Panel 6.38 — Mirror — Belt On
**Scene:** Ethan ties silver belt in mirror — practice — not for show.
**Dialogue:** Ethan (internal): *Still mine.*

**Prompt:**
```
teen tying black belt with silver letters in bedroom mirror private ritual,
identity affirmation close-up mirror, STYLE: KWONS soft
```

---
### Panel 6.39 — MV Arrives Nod
**Scene:** MV arrives — nods at Ethan's work. No lecture.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes arriving nodding at straightened mat Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt slight proud nod exchange morning, STYLE: KWONS
```

---
### Panel 6.40 — Sleep — No Nightmare
**Scene:** Ethan in bed — headphones on — eyes close — no smash cut this time.
**Dialogue:** *(none — relief beat)*

**Prompt:**
```
teen falling asleep with headphones calm breathing no nightmare transition,
soft peaceful panel contrast chapter 1, STYLE: KWONS soft
```

---

# Chapter 7 — Flashbacks

### Panel 7.1 — Young Ethan Doorway Flash
**Scene:** **FLASH** — young Ethan in Premier doorway — excited. Smaller frame.

**Prompt:**
```
FLASH young Ethan Hyun excited smaller frame Premier dojang doorway enrollment day bright hopeful, STYLE: PREMIER flashback
```

---
### Panel 7.2 — Opening Day (Warm)
**Scene:** Flashback — small empty Premier dojang. Younger Ethan (white belt) bows. Instructor smiles genuinely.
**Dialogue:** Instructor: "Welcome to the family."

**Prompt:**
```
flashback small new taekwondo dojang, young white belt boy bowing, warm smiling instructor,
hopeful beginning, soft warm memory filter, STYLE: PREMIER lighter
```

---
### Panel 7.3 — Present Flinch
**Scene:** **PRESENT** — Ethan flinches at same door memory. MV steady beside.

**Prompt:**
```
PRESENT Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt micro flinch at doorway memory Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes steady beside grounding present, STYLE: KWONS
```

---
### Panel 7.4 — Growth
**Scene:** Time montage — more students enroll. More trophies. Instructor's smile smaller each panel.
**Dialogue:** *(none)*

**Prompt:**
```
montage three panels taekwondo school growing more students more trophies,
instructor smile fading each panel, time passage, STYLE: PREMIER cooling
```

---
### Panel 7.5 — MV Breathing Demo
**Scene:** MV demonstrates breathing — hand on own chest. Slow.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes demonstrating slow breathing hand on chest coaching calm Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt watching, STYLE: KWONS
```

---
### Panel 7.6 — Favoritism Montage
**Scene:** Paying kid gets new gear. Ethan in old gear. Instructor praises paying kid's mediocre kick.
**Dialogue:** Instructor: "Excellent! See — investment pays off."

**Prompt:**
```
taekwondo instructor praising student with expensive gear, another talented teen in worn gear ignored corner,
favoritism visual, STYLE: PREMIER
```

---
### Panel 7.7 — Ethan Copying Inhale
**Scene:** Ethan copies inhale — eyes closed. Shoulders drop.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt copying breathing inhale eyes closed shoulders dropping release exercise, STYLE: KWONS
```

---
### Panel 7.8 — Sidelined
**Scene:** Ethan wins drill — instructor looks at clipboard, calls paying kid for "advanced work."
**Dialogue:** Instructor: "Ethan — sit. Marcus — come here."

**Prompt:**
```
teen winning sparring drill but coach pointing to bench telling him to sit,
less skilled wealthy student called forward instead, injustice panel, STYLE: PREMIER
```

---
### Panel 7.9 — One-Step Slide Foot
**Scene:** One-step drill — Ethan slides foot. Present focus.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt one-step sparring drill sliding foot precise present focus Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes guiding, STYLE: KWONS
```

---
### Panel 7.10 — Present Anchor
**Scene:** Snap back — Ethan on Kwon's mats alone after hours. Same drill stance. MV's voice off-panel.
**Dialogue:** MV (off): "Ethan? You okay?"

**Prompt:**
```
present day teen frozen in fighting stance on dojang mats alone, dissociating,
warm dojang, concerned coach voice off panel, STYLE: KWONS
```

---
### Panel 7.11 — Partner Shadow Imaginary
**Scene:** Ethan practices against imaginary partner — shadow on mat.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt practicing footwork shadow partner on wooden mat focused solitary drill, STYLE: KWONS
```

---
### Panel 7.12 — MV Enters Frame
**Scene:** MV steps into Ethan's eyeline — doesn't touch — waits.
**Dialogue:** MV: "Flashback or footwork?"

**Prompt:**
```
master stepping into view careful not to startle dissociating teen,
gentle check-in, STYLE: KWONS
```

---
### Panel 7.13 — Flash Trophy Shelf Premier
**Scene:** **FLASH** — Premier trophy shelf — young Ethan reflected in glass.

**Prompt:**
```
FLASH Premier dojang trophy shelf young Ethan Hyun reflection in glass early pride before neglect, STYLE: PREMIER flashback
```

---
### Panel 7.14 — Ethan Returns
**Scene:** Ethan blinks — exhales — embarrassed.
**Dialogue:** Ethan: "Footwork."

**Prompt:**
```
teen returning to present embarrassed exhale master half-smile not calling lie,
recovery moment, STYLE: KWONS
```

---
### Panel 7.15 — Present Fist Unclench Mat
**Scene:** **PRESENT** — fist unclenches on mat. Ghost fading.

**Prompt:**
```
PRESENT Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt fist unclenching on mat ghost memory fading warm light winning, STYLE: KWONS
```

---
### Panel 7.16 — Opening Day Detail [FLASH]
**Scene:** **FLASH** — empty Premier — fresh mats — Ttong younger — genuine smile.
**Dialogue:** Ttong (younger): "Small school. Big heart."

**Prompt:**
```
flashback brand new small taekwondo dojang empty fresh mats younger instructor genuine smile,
hopeful memory filter, STYLE: PREMIER lighter
```

---
### Panel 7.17 — Window Ledge Walk
**Scene:** Ethan walks to window ledge — city traffic below.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt walking to dojang window ledge city traffic below contemplative wide shot, STYLE: KWONS
```

---
### Panel 7.18 — Young Ethan Excited [FLASH]
**Scene:** **FLASH** — white belt Ethan — first uniform — parents proud off-panel.
**Dialogue:** Ethan (V.O.): *I believed him.*

**Prompt:**
```
flashback young white belt boy first taekwondo uniform excited parents blurred proud,
childhood hope, STYLE: PREMIER lighter
```

---
### Panel 7.19 — City Traffic Below
**Scene:** POV — traffic below. Scale. Ethan's small reflection.

**Prompt:**
```
POV city traffic below dojang window small teen reflection in glass contemplative scale shot, STYLE: KWONS
```

---
### Panel 7.20 — Enrollment Line [FLASH]
**Scene:** **FLASH montage cell** — enrollment line grows — brochures multiply — **Repeul Kim** silent with stack.
**Dialogue:** *(none)*

**Prompt:**
```
flashback montage enrollment line growing VIP brochures multiplying silent woman background,
commercialization creeping in, STYLE: PREMIER cooling
```

---
### Panel 7.21 — MV Hand on Shoulder
**Scene:** MV hand on shoulder — brief. Ethan doesn't shrug off.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes hand on shoulder brief supportive gesture Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt accepting not shrugging off, STYLE: KWONS
```

---
### Panel 7.22 — First Trophy [FLASH]
**Scene:** **FLASH** — Ethan wins local medal — Ttong hugs paying kid instead in background.
**Dialogue:** Ethan (V.O.): *I won. He photographed someone else.*

**Prompt:**
```
flashback teen winning medal instructor hugging different student in background for photo,
betrayal seed memory, STYLE: PREMIER
```

---
### Panel 7.23 — Ethan Minimal Nod
**Scene:** Ethan minimal nod — gratitude without words.

**Prompt:**
```
close-up Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt minimal nod quiet gratitude no words emotional beat, STYLE: KWONS
```

---
### Panel 7.24 — Scrimmage King [FLASH]
**Scene:** **FLASH** — Ethan dominates scrimmage — coach claps for paying kid's bad kick.
**Dialogue:** Instructor: "Excellent form, Marcus!"

**Prompt:**
```
flashback sparring teen dominating coach applauding weaker wealthy student instead,
injustice montage cell, STYLE: PREMIER
```

---
### Panel 7.25 — Bow Together
**Scene:** Ethan and MV bow together — matched depth.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt and Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes bowing together matched depth mutual respect flashback session close, STYLE: KWONS
```

---
### Panel 7.26 — Demo Team Pick [FLASH]
**Scene:** **FLASH** — clipboard — Ethan's name crossed out — paying kid circled.
**Dialogue:** Instructor: "Ethan — sit. Marcus — demo team."

**Prompt:**
```
flashback clipboard names crossed out favored student circled demo team selection,
explicit sideline panel, STYLE: PREMIER
```

---
### Panel 7.27 — Ghost Flash Fade
**Scene:** Premier ghost flash fades — trophy shelf dissolves to Kwon's wood.

**Prompt:**
```
Premier trophy flash dissolving into warm Kwon's wooden floor ghost memory fading transition, STYLE: PREMIER to KWONS
```

---
### Panel 7.28 — Gear Gap [FLASH]
**Scene:** **FLASH split** — new electronic hogus on paying kid — Ethan's worn straps.
**Dialogue:** Ethan (V.O.): *Same patch. Different price tag.*

**Prompt:**
```
flashback split panel expensive new taekwondo gear vs worn gear same school patch,
economic favoritism visual, STYLE: PREMIER
```

---
### Panel 7.29 — Present Color Warmer
**Scene:** Present frame warms — amber returns. Ethan exhales.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt present frame warming amber light returning exhale relief after flashback, STYLE: KWONS
```

---
### Panel 7.30 — Ttong Smile Thin [FLASH]
**Scene:** **FLASH** — Ttong portrait — smile doesn't reach eyes — underbite grin.
**Dialogue:** Ttong: "We're a family."

**Prompt:**
```
flashback instructor portrait smile not reaching eyes predatory undertone,
unsettling promo photo aesthetic, STYLE: PREMIER
```

---
### Panel 7.31 — Class Joins Wide
**Scene:** Wide — class resumes. Ethan in line. Not sidelined.

**Prompt:**
```
wide shot class training line Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt included not sidelined warm dojang community, STYLE: KWONS
```

---
### Panel 7.32 — Present — Ethan Fists
**Scene:** **PRESENT** — Ethan on Kwon's mat — fists unclench when MV speaks.
**Dialogue:** MV: "Breathe. Then move."

**Prompt:**
```
present teen unclenching fists on mat master coaching breathing,
grounding exercise, STYLE: KWONS
```

---
### Panel 7.33 — Partner Bow Exchange
**Scene:** Partner bow exchange — Ethan included.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt bowing with training partner included exchange respectful class rhythm, STYLE: KWONS
```

---
### Panel 7.34 — One Step Drill
**Scene:** MV runs simple one-step — Ethan flows — muscle memory from pain.
**Dialogue:** *(SFX)* *tap — step — kick*

**Prompt:**
```
master running one step self defense drill teen flowing through movements,
therapeutic movement panel, STYLE: KWONS
```

---
### Panel 7.35 — MV Counts Combo
**Scene:** MV counts combo — Ethan keeps pace.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes counting combination Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt keeping pace focused training flow, STYLE: KWONS
```

---
### Panel 7.36 — Kind When Empty [V.O.]
**Scene:** Ethan kicks — **FLASH overlay faint** — empty Premier opening day ghosted on present mat.
**Dialogue:** Ethan (V.O.): *He was kind when the room was empty.*

**Prompt:**
```
present kick with faint ghost overlay flash empty dojang opening day double exposure,
poetic memory blend, STYLE: KWONS with PREMIER ghost
```

---
### Panel 7.37 — Sunset Bow Out
**Scene:** Sunset bow out — Ethan last to rise. Slower, not excluded.

**Prompt:**
```
sunset class bow out Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt last to rise slower not excluded warm light, STYLE: KWONS
```

---
### Panel 7.38 — MV Sees Ghost Too
**Scene:** MV watches Ethan — sees something behind eyes — doesn't name it.
**Dialogue:** MV (internal): *That school left marks.*

**Prompt:**
```
master watching teen train recognizing trauma behind eyes compassionate observation,
mentor POV panel, STYLE: KWONS
```

---
### Panel 7.39 — Street Peace After Flash
**Scene:** Street outside — Ethan walks peaceful. Flash session digested.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking evening street peaceful expression after heavy flashback session, STYLE: KWONS
```

---
### Panel 7.40 — Bow Out — Present Wins
**Scene:** Ethan bows — present tense — chooses Kwon's air.
**Dialogue:** Ethan (internal): *Room's not empty anymore.*

**Prompt:**
```
teen bowing on kwons mat present tense choosing forward golden light,
arc closure beat chapter 7, STYLE: KWONS
```

---

# Chapter 8 — Hospital

### Panel 8.1 — Hospital Elevator Numbers
**Scene:** Elevator numbers climb — Ethan watches floor indicator.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants watching hospital elevator floor numbers climb tense quiet fluorescent, STYLE: PREMIER soft
```

---
### Panel 8.2 — Hospital Hall
**Scene:** Ethan in casual clothes — headphones, hoodie. Hospital corridor. Fluorescent buzz.
**Dialogue:** *(none)*

**Prompt:**
```
teen boy walking hospital corridor hoodie gold headphones around neck,
quiet somber atmosphere, fluorescent lighting, STYLE: PREMIER soft
```

---
### Panel 8.3 — Hall Walk to Room
**Scene:** Ethan walks hall to room — shoes quiet on linoleum.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants walking hospital corridor toward room quiet linoleum long hallway soft dread, STYLE: PREMIER soft
```

---
### Panel 8.4 — Grandmother
**Scene:** Ethan enters room. Grandmother in bed — frail but smiles when she sees him.
**Dialogue:** Grandmother: "My champion."

**Prompt:**
```
elderly korean grandmother in hospital bed smiling weakly at visiting teen grandson,
tender emotional reunion, soft window light, hospital room, STYLE: PREMIER soft
```

---
### Panel 8.5 — Hand Sanitizer Stop
**Scene:** Hand sanitizer dispenser — Ethan pauses, pumps twice.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants pausing at hospital hand sanitizer dispenser pumping twice ritual delay, STYLE: PREMIER soft
```

---
### Panel 8.6 — Hand Hold
**Scene:** Ethan holds her hand — too gently, like she's glass.
**Dialogue:** Ethan: "I found a new school."

**Prompt:**
```
close-up teen holding elderly woman's thin hand gently, emotional restraint,
hospital bedsheets, intimate detail shot, STYLE: PREMIER soft
```

---
### Panel 8.7 — Door Half Open
**Scene:** Room door half open — warm light inside. Ethan hesitates.

**Prompt:**
```
hospital room door half open warm light inside Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants hesitating threshold emotional, STYLE: PREMIER soft
```

---
### Panel 8.8 — Phone Buzz
**Scene:** Phone on side table vibrates — stack of notifications. Ethan's face tightens.
**SFX:** *buzz buzz buzz*

**Prompt:**
```
smartphone vibrating many notification badges, teen's tense face in background blur,
ominous mood shift, hospital room, STYLE: PREMIER
```

---
### Panel 8.9 — Chair Scrape Sit
**Scene:** Chair scrape — Ethan sits bedside. Small in room.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants pulling chair scraping sitting bedside small figure hospital room gentle, STYLE: PREMIER soft
```

---
### Panel 8.10 — Threatening Messages
**Scene:** Phone screen — texts from unknown numbers. *"Stop talking about my school."* *"You're making this worse."*
**Dialogue:** (text) **"I know where you train now."**

**Prompt:**
```
close-up smartphone screen threatening text messages, dark ominous lighting on phone glow,
teen hands gripping phone, no faces, STYLE: PREMIER
```

---
### Panel 8.11 — Bedside Table Flowers
**Scene:** Bedside table — flowers, water cup. Domestic detail in clinical space.

**Prompt:**
```
hospital bedside table flowers water cup domestic detail clinical room soft focus background, STYLE: PREMIER soft
```

---
### Panel 8.12 — Silence Phone
**Scene:** Ethan silences phone. Puts in pocket. Returns to holding grandmother's hand. Forces small smile.
**Dialogue:** Ethan: "It's nothing."

**Prompt:**
```
teen silencing phone putting in pocket, returning to hold grandmother hand forced small smile,
protective grandson moment, hospital room, STYLE: PREMIER soft
```

---
### Panel 8.13 — Window Rain Streak
**Scene:** Window — rain streak. Ethan's reflection layered on glass.

**Prompt:**
```
hospital window rain streaks Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants reflection layered on glass melancholy wide, STYLE: PREMIER soft
```

---
### Panel 8.14 — Halmeoni Notices
**Scene:** Grandmother's thin hand squeezes his — she saw the phone.
**Dialogue:** Grandmother: "Bad men on the phone?"

**Prompt:**
```
elderly grandmother squeezing teen hand asking gentle question tired kind eyes,
hospital bed intimate two-shot, STYLE: PREMIER soft
```

---
### Panel 8.15 — Phone Buzz Pocket
**Scene:** Phone buzzes in pocket — Ethan stiffens. Doesn't look yet.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants phone buzzing in pocket stiffening not looking yet hospital bedside tension, STYLE: PREMIER soft
```

---
### Panel 8.16 — Ethan Deflects Korean
**Scene:** Ethan answers in Korean — soft — protective lie.
**Dialogue:** Ethan: "Nothing. Rest."

**Prompt:**
```
teen speaking korean softly to grandmother protective deflection,
cultural intimate dialogue panel, STYLE: PREMIER soft
```

---
### Panel 8.17 — Voicemail Waveform
**Scene:** Phone screen — voicemail waveform. Ttong Kim name visible.

**Prompt:**
```
smartphone voicemail waveform playing threatening message screen glow Ethan hand tense hospital, STYLE: PREMIER
```

---
### Panel 8.18 — You Came
**Scene:** Grandmother pats his hand — winces less when smiling at him.
**Dialogue:** Grandmother: "You came. That's enough for today."

**Prompt:**
```
grandmother patting grandson hand weak smile enough for today emotional,
tender hospital beat, STYLE: PREMIER soft
```

---
### Panel 8.19 — Delete Confirm Thumb
**Scene:** Delete confirm — thumb hovers, then taps.
**Dialogue:** Ethan (internal): *Not today.*

**Prompt:**
```
close-up thumb hovering delete voicemail confirm button Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants decisive tap hospital, STYLE: PREMIER soft
```

---
### Panel 8.20 — Window Rain
**Scene:** Rain on hospital window — Ethan watches — reflection overlays his face.
**Dialogue:** *(none)*

**Prompt:**
```
rain on hospital window teen face reflected in glass contemplative,
melancholy atmosphere panel, STYLE: PREMIER soft
```

---
### Panel 8.21 — Nurse Shadow Pass
**Scene:** Nurse shadow passes doorway — Ethan glances, returns to grandmother.

**Prompt:**
```
nurse shadow passing hospital doorway Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants glancing back to grandmother bedside, STYLE: PREMIER soft
```

---
### Panel 8.22 — Voicemail Play [REAL #15]
**Scene:** Ethan steps into hall — alone — plays voicemail — hand over mouth.
**Dialogue:** Ttong (V.O.): "Stop talking about my school. Stop making kids leave."

**Prompt:**
```
teen alone hospital hallway playing voicemail hand over mouth shaken,
threatening audio visual, STYLE: PREMIER harsh
```

---
### Panel 8.23 — Hallway Bench Alone
**Scene:** Hallway bench — Ethan sits alone after room visit. Head down.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants sitting alone hospital hallway bench head down exhausted grief quiet, STYLE: PREMIER soft
```

---
### Panel 8.24 — Delete Voicemail
**Scene:** Ethan deletes message — block number — hands tremble.
**Dialogue:** *(none)*

**Prompt:**
```
teen deleting voicemail blocking number trembling hands phone screen,
fear and anger panel, STYLE: PREMIER harsh
```

---
### Panel 8.25 — Bus Stop Wait
**Scene:** Bus stop — Ethan waits. Rain on hood.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants waiting at bus stop rain on hoodie hood evening city melancholy, STYLE: PREMIER soft to KWONS
```

---
### Panel 8.26 — Nurse Passes
**Scene:** Nurse walks by — Ethan straightens — hides phone — trained to look fine.
**Dialogue:** Nurse: "Visiting hours end at eight."

**Prompt:**
```
hospital nurse walking past teen straightening hiding phone performing okay,
masking trauma public space, STYLE: PREMIER soft
```

---
### Panel 8.27 — Rain on Hood
**Scene:** Close — raindrops on hood fabric. Breath fog.

**Prompt:**
```
close-up raindrops on hoodie fabric breath fog Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants cold evening detail shot, STYLE: PREMIER soft
```

---
### Panel 8.28 — Return To Room
**Scene:** Ethan returns — smile ready — sits back down.
**Dialogue:** Ethan: "New school has good mats."

**Prompt:**
```
teen returning to hospital room forced gentle smile sitting by grandmother,
protective grandson returning, STYLE: PREMIER soft
```

---
### Panel 8.29 — Kwon's Text Glow
**Scene:** Phone glow — text from MV at Kwon's. Warm notification tone.

**Prompt:**
```
smartphone screen glow kind text message from Master Viet warm notification Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants rain background, STYLE: KWONS soft
```

---
### Panel 8.30 — Photo In Purse
**Scene:** Grandmother shows worn photo — young Ethan white belt — creased edges.
**Dialogue:** Grandmother: "Before the big school."

**Prompt:**
```
elderly woman showing creased photo young grandson white belt in hospital bed,
nostalgic tender detail, STYLE: PREMIER soft
```

---
### Panel 8.31 — Reply Thumb Hover
**Scene:** Reply thumb hovers — small smile trying.

**Prompt:**
```
close-up thumb hovering over reply send button Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants small smile forming rain bus stop, STYLE: KWONS soft
```

---
### Panel 8.32 — Ethan Can't Look
**Scene:** Ethan looks at photo — too long — pain — looks away.
**Dialogue:** Ethan: "That was a long time ago."

**Prompt:**
```
teen looking at childhood photo then looking away pain restrained,
emotional avoidance close-up, STYLE: PREMIER soft
```

---
### Panel 8.33 — Send Small Smile Lost
**Scene:** Send — smile fades to tired. Message sent.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants sending text small smile fading to tired relief message sent bus stop rain, STYLE: KWONS soft
```

---
### Panel 8.34 — Bus Ride Home
**Scene:** Ethan on night bus — forehead on window — city lights streak.
**Dialogue:** Ethan (internal): *I won't bring this to her room again.*

**Prompt:**
```
teen on night bus forehead against window city lights streak exhausted,
transit solitude panel, STYLE: PREMIER soft night
```

---
### Panel 8.35 — Bus Arrival Lights
**Scene:** Bus arrival lights — Ethan boards. Chapter exhale.

**Prompt:**
```
city bus arrival lights Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants boarding rain evening transition exhale, STYLE: PREMIER soft to KWONS
```

---
### Panel 8.36 — Kwon's Text From MV
**Scene:** Phone — new message — MV — *"Door's open tomorrow. Early class if you want."*
**Dialogue:** (text) MV: **"No pressure."**

**Prompt:**
```
smartphone text from taekwondo master kind message door open tomorrow,
warm notification glow on tired teen face bus, STYLE: KWONS soft on phone
```

---
### Panel 8.37 — Apartment Window Night
**Scene:** Apartment window night — Ethan home. City lights bokeh.

**Prompt:**
```
apartment window night Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants silhouette city lights bokeh exhausted safe home, STYLE: KWONS soft
```

---
### Panel 8.38 — Small Reply
**Scene:** Ethan types — deletes — types — sends one word.
**Dialogue:** (text) Ethan: **"Early."**

**Prompt:**
```
teen typing short reply on phone careful minimal emotional text,
close-up thumbs screen, STYLE: KWONS soft
```

---
### Panel 8.39 — Hospital Exit Wide Dawn
**Scene:** Wide — hospital exterior dawn breaking. Small figure leaving.
**Dialogue:** *(none — transition)*

**Prompt:**
```
wide shot hospital exterior dawn breaking small teen figure leaving transition hope hard week continues, STYLE: PREMIER soft to KWONS dawn
```

---
### Panel 8.40 — Hospital Exit Wide
**Scene:** Wide — hospital exterior — Ethan small in frame — dawn breaking.
**Dialogue:** *(none — transition)*

**Prompt:**
```
wide shot hospital exterior dawn breaking small teen figure leaving,
transition hope hard week continues, STYLE: PREMIER soft to KWONS dawn
```

---

# Chapter 9 — Can They Come

### Panel 9.1 — MV Answer Gentle
**Scene:** MV answers gently — open hands. Ethan listens.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes answering gently open hands kind expression Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt listening hopeful, STYLE: KWONS
```

---
### Panel 9.2 — The Ask
**Scene:** Ethan and MV after class. Ethan unusually nervous — fidgeting with belt.
**Dialogue:** Ethan: "Some friends... they left Premier too. Can they join?"

**Prompt:**
```
nervous teen fidgeting with black belt asking question, taekwondo master listening after class,
empty dojang, hopeful anxiety, STYLE: KWONS
```

---
### Panel 9.3 — Phone Unlock
**Scene:** Ethan unlocks phone — contact list scroll begins.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt unlocking smartphone beginning contact scroll nervous hope, STYLE: KWONS
```

---
### Panel 9.4 — MV Answer
**Scene:** MV — simple nod.
**Dialogue:** MV: "Everyone deserves a home."

**Prompt:**
```
taekwondo master simple kind nod, warm expression, short powerful dialogue moment,
teen visible relief, STYLE: KWONS
```

---
### Panel 9.5 — Premier Names Scroll
**Scene:** Contact list — Premier names scroll. Old team.

**Prompt:**
```
smartphone contact list scrolling Premier taekwondo team names old connections emotional weight, STYLE: PREMIER soft
```

---
### Panel 9.6 — The Text
**Scene:** Ethan on phone — group chat. Typing. Names visible: **TJ · Kieryn · Logan · Kian · Ariana**
**Dialogue:** (text) Ethan: *"Found a place. Kwon's. He said yes."*

**Prompt:**
```
close-up smartphone group chat typing message, contact names visible,
teen thumbs typing, golden hour through window on hands, STYLE: KWONS
```

---
### Panel 9.7 — Group Chat Icon
**Scene:** Group chat icon — cursor/thumb hovers. MV nods background.

**Prompt:**
```
smartphone group chat icon hover Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes nodding background Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt nervous invitation moment, STYLE: KWONS
```

---
### Panel 9.8 — Replies Flood
**Scene:** Phone notifications — question marks, fire emojis, "OMW", "FINALLY"
**Dialogue:** (text) Kieryn: *"Took you long enough."*

**Prompt:**
```
smartphone screen flooding with reply notifications excited messages,
comic relief energy, warm lighting, STYLE: KWONS
```

---
### Panel 9.9 — Typing Bubble
**Scene:** Typing bubble — message draft to team.
**Dialogue:** Ethan (typing): "Practice at Kwon's Saturday…"

**Prompt:**
```
smartphone typing message bubble draft invitation Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt focused screen glow, STYLE: KWONS
```

---
### Panel 9.10 — TJ First Reply
**Scene:** Text thread — **TJ** — *"Send address. We're not staying at Premier another week."*
**Dialogue:** (text) TJ: **"Is the mat actually soft or Kieryn will complain."**

**Prompt:**
```
smartphone group chat TJ message confident tone address request,
text UI panel comic energy, STYLE: KWONS
```

---
### Panel 9.11 — Send Arrow Tap
**Scene:** Send arrow tap — message gone. Ethan holds breath.

**Prompt:**
```
close-up send arrow tap smartphone message sent Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt holding breath anticipation, STYLE: KWONS
```

---
### Panel 9.12 — Kieryn Sarcasm
**Scene:** Kieryn typing bubble — long — sends anyway.
**Dialogue:** (text) Kieryn: **"Took you long enough, prodigy."**

**Prompt:**
```
smartphone chat kieryn sarcastic reply typing bubble energy,
character voice through text, STYLE: KWONS
```

---
### Panel 9.13 — Waiting Clock Wall
**Scene:** Wall clock — waiting. Phone face up — no replies yet.

**Prompt:**
```
dojang wall clock waiting Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt phone face up no replies yet anxious patience, STYLE: KWONS
```

---
### Panel 9.14 — Logan Sticker Flood
**Scene:** Logan sends food stickers — ramen — spaghetti — question marks.
**Dialogue:** (text) Logan: **"Is there food near there??"**

**Prompt:**
```
smartphone chat logan food emoji stickers flood comic relief,
character personality text only, STYLE: KWONS
```

---
### Panel 9.15 — MV Preparing Mats Early
**Scene:** MV preparing mats early — alone. Dawn light.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes preparing training mats early morning alone dawn light through windows dedication, STYLE: KWONS dawn
```

---
### Panel 9.16 — Kian Short
**Scene:** Kian — one line — no emoji.
**Dialogue:** (text) Kian: **"I owe you a rematch. Send pin."**

**Prompt:**
```
smartphone chat kian short blunt message rematch energy,
minimal text panel, STYLE: KWONS
```

---
### Panel 9.17 — Ethan Early Street Walk
**Scene:** Ethan early walk on street — same route, lighter step.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants early morning street walk to dojang lighter step anticipation, STYLE: KWONS dawn
```

---
### Panel 9.18 — Ariana Read Receipt
**Scene:** Ariana — typing… — stops — **Read 9:42 PM** — no reply yet.
**Dialogue:** *(none — mystery beat)*

**Prompt:**
```
smartphone chat ariana read receipt no reply typing stopped mystery,
quiet character tease, STYLE: KWONS
```

---
### Panel 9.19 — Key Turn Door
**Scene:** Key turn — dojang door. Ethan first inside.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants turning key opening dojang door early arrival first inside dawn, STYLE: KWONS dawn
```

---
### Panel 9.20 — Ethan Stares At Screen
**Scene:** Ethan on dojang steps after class — screen glow — almost smiles.
**Dialogue:** Ethan (internal): *I didn't ask them to follow me. I asked if they could breathe.*

**Prompt:**
```
teen sitting on dojang steps phone glow face almost smiling internal relief,
golden evening, STYLE: KWONS
```

---
### Panel 9.21 — Lights Flip On
**Scene:** Lights flip on — empty mat. Team day approaching.

**Prompt:**
```
dojang lights flipping on empty training mat team day approaching wide dawn shot, STYLE: KWONS dawn
```

---
### Panel 9.22 — MV Over Shoulder
**Scene:** MV locks door — sees Ethan on steps — doesn't ask who texts.
**Dialogue:** MV: "Friends?"

**Prompt:**
```
master locking dojang door seeing teen on steps simple question,
warm evening two-shot, STYLE: KWONS
```

---
### Panel 9.23 — Mat Layout Straighten
**Scene:** Ethan straightens mat layout — parallel lines.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt straightening mat layout parallel lines responsible preparation team day, STYLE: KWONS dawn
```

---
### Panel 9.24 — Ethan Nods
**Scene:** Ethan nods — doesn't hide phone for once.
**Dialogue:** Ethan: "Maybe."

**Prompt:**
```
teen nodding not hiding phone hopeful maybe answer,
trust micro-moment, STYLE: KWONS
```

---
### Panel 9.25 — Text Reply Vibration
**Scene:** Phone vibrates — reply incoming. Ethan's eyes widen micro.

**Prompt:**
```
smartphone vibration reply notification Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt eyes widening micro hope team response, STYLE: KWONS
```

---
### Panel 9.26 — Everyone Deserves Home (Repeat Weight)
**Scene:** MV repeats earlier line — now Ethan hears full meaning.
**Dialogue:** MV: "Everyone deserves a home. Even the loud ones."

**Prompt:**
```
master repeating kind policy line teen listening full meaning landing,
mentor wisdom evening light, STYLE: KWONS
```

---
### Panel 9.27 — Ariana Typing Finally
**Scene:** Screen — Ariana typing indicator finally appears.

**Prompt:**
```
smartphone screen Ariana typing indicator finally appearing group chat hope beat, STYLE: KWONS
```

---
### Panel 9.28 — Schedule Check
**Scene:** Ethan pulls up class schedule — screenshots — sends to group.
**Dialogue:** (text) Ethan: **"Saturday 10 AM. Don't be late."**

**Prompt:**
```
teen screenshotting class schedule sending group chat taking charge,
leadership seed panel, STYLE: KWONS
```

---
### Panel 9.29 — Ethan Small Exhale
**Scene:** Ethan small exhale — shoulders drop. Not alone.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt small exhale shoulders dropping relief not alone anymore emotional beat, STYLE: KWONS
```

---
### Panel 9.30 — Premier Group Chat Muted
**Scene:** Ethan mutes old Premier team chat — 99+ notifications — doesn't open.
**Dialogue:** (text preview) **"Where did Hyun go?"**

**Prompt:**
```
smartphone muting old premier group chat notification badge ignored,
breaking away panel, STYLE: PREMIER cold on KWONS present
```

---
### Panel 9.31 — Replies Flood Montage
**Scene:** Montage hint — multiple reply bubbles stacking.

**Prompt:**
```
smartphone montage multiple reply bubbles stacking team responses warming screen glow, STYLE: KWONS
```

---
### Panel 9.32 — Ariana Finally Replies
**Scene:** Ariana — one word — lands heavy.
**Dialogue:** (text) Ariana: **"Okay."**

**Prompt:**
```
smartphone single word reply ariana okay minimal emotional weight,
quiet character text beat, STYLE: KWONS
```

---
### Panel 9.33 — MV Over Shoulder Check
**Scene:** MV over shoulder — checks Ethan's face. Small proud nod.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes over shoulder checking Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt face small proud nod mentor approval, STYLE: KWONS
```

---
### Panel 9.34 — Night Before — Ethan Prepares
**Scene:** Ethan lays out extra guest waivers MV left on desk — neat stack.
**Dialogue:** Ethan (internal): *Six chairs. One room.*

**Prompt:**
```
teen preparing guest enrollment forms on dojang desk night before arrivals,
anticipation detail shot, STYLE: KWONS night
```

---
### Panel 9.35 — Evening Gear Prep
**Scene:** Evening — Ethan lays out extra guest gear. Anticipation.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt laying out extra guest training gear evening anticipation team visit prep, STYLE: KWONS
```

---
### Panel 9.36 — MV Early Light
**Scene:** MV alone — opens dojang early — turns on lights — extra mats out.
**Dialogue:** MV (internal): *Big day.*

**Prompt:**
```
master opening dojang early morning turning on lights extra mats prepared,
mentor preparation wide shot, STYLE: KWONS dawn
```

---
### Panel 9.37 — Night Before Window
**Scene:** Night before — Ethan at window. Street quiet.
**Dialogue:** Ethan (internal): *They might come.*

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, gold headphones white gear backpack oversized navy hoodie white tee baggy pants at apartment window night before team day quiet street reflective hope, STYLE: KWONS soft
```

---
### Panel 9.38 — Ethan Early Arrival
**Scene:** Ethan already waiting outside — bag packed — headphones off.
**Dialogue:** Ethan: "I couldn't sleep."

**Prompt:**
```
teen waiting outside dojang early morning bag packed no headphones nervous excited,
dawn arrival, STYLE: KWONS
```

---
### Panel 9.39 — Dawn Team Day Hint Wide
**Scene:** Dawn wide — dojang exterior. Team day hint. Caption space.

**Prompt:**
```
wide shot Kwon's dojang exterior dawn team day approaching hopeful golden light caption space, STYLE: KWONS dawn
```

---
### Panel 9.40 — Door Unlock
**Scene:** MV unlocks — first inside — Ethan follows — empty mat like promise.
**Dialogue:** MV: "Let's get the room ready."

**Prompt:**
```
master unlocking dojang door teen following inside empty mat morning light ready,
chapter transition to team arrival, STYLE: KWONS dawn
```

---

# Chapter 10 — Welcome

### Panel 10.1 — Parking Lot Arrivals Montage
**Scene:** Parking lot — multiple arrivals montage walk. Saturday morning.

**Prompt:**
```
suburban dojang parking lot Saturday morning multiple arrivals montage teens approaching warm light, STYLE: KWONS HAIKYUU
```

---
### Panel 10.2 — Arrivals Begin
**Scene:** Dojang door — multiple figures arriving. Silhouettes with distinct hair colors.
**Dialogue:** *(none)*

**Prompt:**
```
taekwondo dojang entrance multiple teen silhouettes arriving different colored hair shapes,
hero team arrival composition backlit, STYLE: KWONS
```

---
### Panel 10.3 — TJ Door Open Grin
**Scene:** **TJ Lim** — door open grin. Teal headband. Energy spike.

**Prompt:**
```
TJ Lim teen boy teal headband cheerful grin opening dojang door energetic entrance, STYLE: KWONS HAIKYUU
```

---
### Panel 10.4 — TJ Lim
**Scene:** TJ enters — teal hair, headband, muscular, confident grin. Carries himself like he owns the room.
**Dialogue:** TJ: "So this is the famous Kwon's."

**Prompt:**
```
teen boy 15 teal hair headband muscular build confident grin entering dojang,
taekwondo gear bag, champion presence, character reveal, STYLE: KWONS
```

---
### Panel 10.5 — Kieryn Mat Toe Test
**Scene:** **Kieryn Lim** tests mat with toe — teal-purple bob. Critical eye.

**Prompt:**
```
Kieryn Lim teen girl teal purple bob hair testing wooden mat with toe critical expression, STYLE: KWONS HAIKYUU
```

---
### Panel 10.6 — Kieryn Lim
**Scene:** Kieryn — teal/purple hair, asymmetrical bob, arms crossed, smirk.
**Dialogue:** Kieryn: "Smaller than I expected."

**Prompt:**
```
tall teen girl 13 teal hair purple streaks asymmetrical bob arms crossed smirk,
sassy entrance, taekwondo dobok, character reveal, STYLE: KWONS
```

---
### Panel 10.7 — Logan Snack Bag
**Scene:** **Logan Hyun** — snack bag already open. Bowl cut bounce.

**Prompt:**
```
Logan Hyun teen boy bowl cut hair snack bag open cheerful hungry expression dojang entrance, STYLE: KWONS HAIKYUU
```

---
### Panel 10.8 — Logan Hyun
**Scene:** Logan — bowl cut, big eyes, waves at everyone including strangers.
**Dialogue:** Logan: "Hi! Hi! Is there food nearby?"

**Prompt:**
```
cheerful teen boy 13 dark blue bowl cut big eyes waving enthusiastically oversized backpack,
friendly energy character reveal, STYLE: KWONS
```

---
### Panel 10.9 — Kian Shadow Box Air
**Scene:** **Kian Sang** shadow boxes air — silver hair catch light.

**Prompt:**
```
Kian Sang teen boy silver white hair shadow boxing air confident entrance athletic, STYLE: KWONS HAIKYUU
```

---
### Panel 10.10 — Kian Sang
**Scene:** Kian — white/silver hair, lean, hands in pockets, challenging glance at Ethan.
**Dialogue:** Kian: "...You got here first. Doesn't mean you're ahead."

**Prompt:**
```
teen boy 15 white silver hair low taper fade dark brown skin lean athletic,
hands in pockets challenging smirk looking at another fighter, character reveal, STYLE: KWONS
```

---
### Panel 10.11 — Ariana Last Through Door
**Scene:** **Ariana Yang** last through door — red streak bob. Scanning room.

**Prompt:**
```
Ariana Yang teen girl red streak bob hair last through dojang door scanning room guarded expression, STYLE: KWONS HAIKYUU
```

---
### Panel 10.12 — Ethan & Kian Eye Lock
**Scene:** Ethan and Kian — brief stare. Not hatred — spark.
**Dialogue:** *(none)*

**Prompt:**
```
two teen taekwondo fighters eye contact moment, dark blue hair vs white silver hair,
friendly rivalry spark not hatred, medium shot, STYLE: KWONS
```

---
### Panel 10.13 — Ethan Introducing MV
**Scene:** **Ethan Hyun** introduces **MV** to arriving team — small gesture.

**Prompt:**
```
Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt introducing Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes to arriving Premier teens team bridge gesture warm dojang, STYLE: KWONS HAIKYUU
```

---
### Panel 10.14 — Ariana Yang
**Scene:** Ariana enters last — quiet, black/red hair, extra bandages on arms visible. Finds corner, starts stretching without a word.
**Dialogue:** *(none)*

**Prompt:**
```
quiet teen girl 15 black hair red streaks chin bob blunt bangs dark brown skin,
extra arm bandages stretching alone in corner silently, stoic character reveal, STYLE: KWONS
```

---
### Panel 10.15 — Team Shoe Line
**Scene:** Team shoe line — chaotic polite. Multiple pairs at cubbies.

**Prompt:**
```
teen taekwondo team shoes lined at cubby wall chaotic polite arrivals Saturday morning, STYLE: KWONS HAIKYUU
```

---
### Panel 10.16 — MV Addresses All
**Scene:** MV stands before full group — Ethan, TJ, Kieryn, Logan, Kian, Ariana. Seven on mat.
**Dialogue:** MV: "Kwon's isn't a business. It's a team. If you work, I work."

**Prompt:**
```
taekwondo master addressing group of six diverse teen students on dojang mats,
team assembly wide shot, mentor speech moment, STYLE: KWONS
```

---
### Panel 10.17 — Stretch Row Formation
**Scene:** Stretch row formation — uneven spacing. MV corrects one arm.

**Prompt:**
```
team stretch row formation uneven spacing Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes correcting one arm warm dojang group, STYLE: KWONS HAIKYUU
```

---
### Panel 10.18 — Ethan Looks Around
**Scene:** Ethan's POV — faces of new family. Headphones in pocket.
**Dialogue:** Ethan (internal): *Home.*

**Prompt:**
```
POV looking at group of teammates smiling talking on taekwondo mats,
warm golden dojang light, emotional found family moment, STYLE: KWONS
```

---
### Panel 10.19 — MV Center Circle
**Scene:** MV center circle — team around. Ethan opposite MV.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes center of team circle seven teens around Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt opposite mentor group formation, STYLE: KWONS HAIKYUU
```

---
### Panel 10.20 — Final Wide
**Scene:** Epic wide — all seven on mat, MV center-back. Golden hour through windows. Team formation.
**Caption:** *Welcome to Kwon's.*
**Dialogue:** *(none — title card energy)*

**Prompt:**
```
epic wide shot seven taekwondo fighters and master on dojang mats team formation,
golden hour light through windows, found family anime poster composition,
emotional finale, caption space at bottom, STYLE: KWONS
```

---
### Panel 10.21 — Group Bow Low
**Scene:** Group bow low — synchronized enough. Found-family chemistry.

**Prompt:**
```
seven teen taekwondo students group bow low synchronized enough found family chemistry, STYLE: KWONS HAIKYUU
```

---
### Panel 10.22 — Team Stretch Circle
**Scene:** MV leads stretch circle — seven students — Ethan not in corner — in ring.
**Dialogue:** MV: "Same rules for everyone."

**Prompt:**
```
taekwondo team stretch circle seven students master leading ethan included in ring,
team chemistry haikyuu warmth, STYLE: KWONS
```

---
### Panel 10.23 — TJ Joke Whisper
**Scene:** TJ whispers joke — Kieryn eye roll incoming.

**Prompt:**
```
TJ Lim whispering joke to teammate Kieryn Lim eye roll incoming comic beat team dynamic, STYLE: KWONS HAIKYUU
```

---
### Panel 10.24 — TJ Windows Line
**Scene:** TJ grins at Ethan — callback Ch 2.
**Dialogue:** TJ: "You picked a place with windows. Good call."

**Prompt:**
```
confident teen teal headband grinning at ethan team banter dojang,
character voice panel HAIKYUU warmth, STYLE: KWONS
```

---
### Panel 10.25 — Kieryn Eye Roll
**Scene:** Kieryn eye roll — tries not to smile.

**Prompt:**
```
Kieryn Lim eye roll trying not to smile sibling dynamic team stretch background, STYLE: KWONS HAIKYUU
```

---
### Panel 10.26 — Kieryn Mat Test
**Scene:** Kieryn presses mat with foot — dramatic — actually fine.
**Dialogue:** Kieryn: "If the mats are soft, I'm still leaving."

**Prompt:**
```
sarcastic teen girl testing dojang mat with foot dramatic expression,
comic team intro, STYLE: KWONS
```

---
### Panel 10.27 — Logan Stretch Wrong
**Scene:** Logan stretches wrong — MV gentle correction.

**Prompt:**
```
Logan Hyun stretching incorrectly Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes gentle correction hand on shoulder comic team moment, STYLE: KWONS HAIKYUU
```

---
### Panel 10.28 — Logan Food Question
**Scene:** Logan — bowl cut — backpack overflowing — raises hand like school.
**Dialogue:** Logan: "Is there food later? Important question."

**Prompt:**
```
cheerful small teen bowl cut raising hand asking about food oversized backpack,
comic relief character intro, STYLE: KWONS
```

---
### Panel 10.29 — Kian Ethan Stare
**Scene:** **Kian** and **Ethan** stare — rematch energy. Respect.

**Prompt:**
```
Kian Sang and Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt eye lock rematch energy mutual respect team circle, STYLE: KWONS HAIKYUU
```

---
### Panel 10.30 — Kian Rematch
**Scene:** Kian — silver hair — hands in pockets — locks eyes with Ethan.
**Dialogue:** Kian: "You owe me a rematch from Premier."

**Prompt:**
```
silver hair teen challenging smirk hands in pockets facing ethan rivalry spark,
character intro tension friendly, STYLE: KWONS
```

---
### Panel 10.31 — Ariana Corner Stretch
**Scene:** Ariana corner stretch — alone in crowd. Ethan notices.

**Prompt:**
```
Ariana Yang stretching alone in corner guarded Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt noticing team wide shot, STYLE: KWONS HAIKYUU
```

---
### Panel 10.32 — Ariana Silent Stretch
**Scene:** Ariana — red streak bob — stretching alone — doesn't look up — bandages on ankle.
**Dialogue:** *(none)*

**Prompt:**
```
quiet teen girl red hair streak stretching alone extra ankle bandages not looking up,
introverted character intro, STYLE: KWONS
```

---
### Panel 10.33 — MV Team Speech Wide
**Scene:** MV team speech wide — hands open. Everyone listening.

**Prompt:**
```
Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes team speech wide shot hands open everyone listening Saturday welcome energy, STYLE: KWONS HAIKYUU
```

---
### Panel 10.34 — MV Team Speech
**Scene:** MV center — team semicircle — Ethan off-center not hiding.
**Dialogue:** MV: "We train hard. We don't tear each other down. You brought family — don't waste it."

**Prompt:**
```
master addressing semicircle team speech ethan visible among peers not spotlight,
mentor team speech wide, STYLE: KWONS
```

---
### Panel 10.35 — Team First Unified Bow
**Scene:** Team first unified bow — Ethan slightly late. Logan stifles laugh.

**Prompt:**
```
team first unified bow Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt slightly late Logan Hyun stifling laugh group sync, STYLE: KWONS HAIKYUU
```

---
### Panel 10.36 — Curiosity Not Pity
**Scene:** Team glances at Ethan — curiosity — TJ nudges Kieryn — no pity faces.
**Dialogue:** Kieryn (whisper): "So *that's* the prodigy."

**Prompt:**
```
team glancing at ethan curious not pitying whispered comment,
group reaction panel, STYLE: KWONS
```

---
### Panel 10.37 — Curiosity Not Pity Beat
**Scene:** Faces — curiosity not pity. Ethan reads it.

**Prompt:**
```
team teen faces curious not pitying Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes, standard white dobok guards under silver-letter black belt reading expressions found family seed, STYLE: KWONS HAIKYUU
```

---
### Panel 10.38 — First Group Bow
**Scene:** MV calls bow — seven sync — Ethan one beat late — laughs quietly with Logan.
**Dialogue:** All: "Thank you, Master!"

**Prompt:**
```
seven students bowing together ethan slightly late logan stifling laugh team sync,
found family chemistry, STYLE: KWONS HAIKYUU
```

---
### Panel 10.39 — Caption Wide Hero
**Scene:** Wide hero — team on mat. Caption space. Arc 1 crescendo.

**Prompt:**
```
wide hero shot full team on dojang mat caption space arc finale crescendo warm golden light, STYLE: KWONS HAIKYUU
```

---
### Panel 10.40 — Caption Card
**Scene:** Black hold — white text — same energy as 1.1 title card inverted.
**Caption:** *Welcome to Kwon's.*
**Dialogue:** *(none — end arc 1)*

**Prompt:**
```
title card black background white caption space welcome to kwons text added in post,
arc finale card minimal, STYLE: KWONS
```

---

---

## Arc 1 Panel Count Summary

| Chapter | Panels | Range |
|---------|--------|-------|
| 1 — Nightmare | 40 | 1.1–1.40 |
| 2 — Arrival | 40 | 2.1–2.40 |
| 3 — Meeting MV | 40 | 3.1–3.40 |
| 4 — Training | 40 | 4.1–4.40 |
| 5 — The Goal | 40 | 5.1–5.40 |
| 6 — Why Leave | 40 | 6.1–6.40 |
| 7 — Flashbacks | 40 | 7.1–7.40 |
| 8 — Hospital | 40 | 8.1–8.40 |
| 9 — Can They Come | 40 | 9.1–9.40 |
| 10 — Welcome | 40 | 10.1–10.40 |
| **Total** | **400** | |

---

## Next Steps

- **Character reference sheets:** [reference-sheets/](../reference-sheets/README.md) — start with **Ethan** (Google Sheet tab + P0 prompts).
- **Arc 2+ expansion:** Match ~40 panels/chapter when expanding other arcs — see [STORYBOARD-GUIDE.md](./STORYBOARD-GUIDE.md).
- **Batch generation tip:** Generate Ethan reference sheet first (panels 3.4, 4.2, 5.3) and use as image-to-image reference for consistency.
