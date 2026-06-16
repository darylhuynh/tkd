# Arc 1 — Panel Storyboard (Chapters 1–10)

**New Beginnings** · Premier trauma → Kwon's sanctuary → team reveal.

Append [Global Style from STORYBOARD-GUIDE](./STORYBOARD-GUIDE.md) to all prompts unless a panel specifies `STYLE: PREMIER` or `STYLE: KWONS`.

**Reference sheets:** [reference-sheets/](../reference-sheets/README.md) — attach Ethan, MV, Ttong Kim refs for Ch 1–10 batch gen.

**Premier flash (extended):** [flash-premier-knockout-bounty.md](../scripts/flash-premier-knockout-bounty.md) § Scene 1 → **1.13b** · § Scene 2 → **1.14–1.16** bridge.

---

## How to Use

1. Generate panels in order (`1.1` → `10.20`).
2. Append **Global Style** to every prompt unless a panel says `STYLE: PREMIER` or `STYLE: KWONS`.
3. For dialogue, add text in your editor after generation — most AI tools render text poorly.
4. **Aspect ratio:** vertical panels `2:3` or `9:16` for webtoon scroll.
5. **Montage / flash clarity:** [STORYBOARD-CLARITY-GUIDE.md](./STORYBOARD-CLARITY-GUIDE.md) — label **FLASH** vs **PRESENT** on every quick cut (see Ch 1 panels **1.8–1.12**).

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
| **Ethan (gear)** | + **full olympic kyorugi kit:** white dobok, electronic chest hogu, headgear (face shield), forearm guards, shin/foot guards |
| **Ethan (casual)** | + gold headphones, white backpack, oversized navy hoodie, white tee hanging out, baggy pants |
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

---

### Panel 1.1 — Title Card
**Scene:** Black screen fading to tournament venue exterior. Banner: *Premier Taekwondo Sports Dynasty — Regional Open*.
**SFX:** *(none — silence)*

**Prompt:**
```
empty martial arts tournament venue exterior at dawn, large banner with taekwondo logos,
overcast sky, desaturated colors, establishing shot, wide angle, moody atmosphere,
STYLE: PREMIER
```

---

### Panel 1.2 — Too Early
**Scene:** Clock on venue wall reads **7:04 AM**. Kids in full electronic hogus walking in.
**Dialogue:** Kid A: "Why are we here so early?"

**Prompt:**
```
tournament venue interior wall clock showing 7 AM, young taekwondo athletes in white hogus
walking with gear bags, harsh fluorescent lighting, tired expressions, wide hallway,
STYLE: PREMIER
```

---

### Panel 1.3 — Bracket Shock
**Scene:** Ethan (15, small, dark blue hair) stares at bracket board. His division circled: **−45kg — Ring 4 — 3:12 PM**.
**Dialogue:** Ethan (internal): *Seven hours.*

**Prompt:**
```
teen boy dark blue shadow perm hair staring at tournament bracket board, finger on paper bracket,
shocked quiet expression, taekwondo uniform with school patch, crowded gymnasium background,
close-up on face and bracket, STYLE: PREMIER
```

---

### Panel 1.4 — No Warmup
**Scene:** Wide shot — 20+ Premier kids in gear. Instructor at far end talking to parents with coffee. **Repeul Kim** in ugly multicolor casual at edge of parent cluster — silent. No one on mats.
**Dialogue:** *(none)*

**Prompt:**
```
wide shot metal bleachers in gymnasium, young taekwondo fighters sitting in full protective gear
waiting, coach ignoring them talking to parents with coffee cups, overweight woman ugly multicolor clothes mean scowl background silent,
no training mats in use, neglectful atmosphere, STYLE: PREMIER
```

---

### Panel 1.5 — Bleacher Isolation
**Scene:** Ethan alone on bleachers. Empty seats on both sides. Legs in hogu, mouthguard case open.
**Dialogue:** *(none)*

**Prompt:**
```
lonely teen boy in taekwondo chest guard sitting alone on metal bleachers, empty seats around him,
slumped posture, mouthguard on bench beside him, isolated composition, grey desaturated palette,
STYLE: PREMIER
```

---

### Panel 1.6 — Time Passes (Montage Cell 1)
**Scene:** Phone screen overlay: **10:23 AM**. Ethan same seat, vending machine snack wrapper nearby.
**Prompt:**
```
same teen on bleachers time skip montage panel, phone screen showing 10 AM, crumpled snack wrapper,
legs still in gear, bored exhausted expression, STYLE: PREMIER
```

---

### Panel 1.7 — Time Passes (Montage Cell 2)
**Scene:** Clock **1:47 PM**. Other kids on phones. Ethan staring at ring — still not his turn.
**Prompt:**
```
gymnasium bleachers afternoon, wall clock 1 PM, teen athletes scrolling phones in taekwondo gear,
one small dark blue hair boy staring forward at distant competition ring, STYLE: PREMIER
```

---

### Panel 1.8 — VIP Flash Insert [FLASH — dojang enrollment]
**Timeline:** **FLASH** — Premier front desk / enrollment day (not tournament venue). **ANCHOR returns in 1.9.**
**Scene:** Parent hands check to **Ttong Kim**. VIP brochure. **Repeul Kim** behind him with brochure stack — silent. **Favored kid** (not Ethan) visible at edge of frame.
**Dialogue:** Ttong Kim (to VIP parent): "We'll take good care of **him**." *(him = paying kid in frame)*

**Prompt:**
```
flashback inset border taekwondo school front desk check payment VIP brochure,
favored student partial figure edge of frame NOT protagonist, overweight woman ugly clothes silent behind instructor,
sleazy enrollment atmosphere, STYLE: PREMIER flashback
```

---

### Panel 1.9 — Favoritism [PRESENT — tournament venue]
**Timeline:** **PRESENT** — same nightmare tournament day as bleachers montage. Ttong coaches a **different** paying kid.
**Scene:** Ttong kneels — adjusts **another kid's** headgear — laughing. Parents proud.
**Dialogue:** Ttong Kim: "Remember — feint left, kick right."

**Prompt:**
```
taekwondo instructor kneeling adjusting favored student headgear tournament venue,
wealthy parents watching proudly personal coaching, warm light on favored student NOT small dark blue hair boy,
STYLE: PREMIER
```

---

### Panel 1.10 — Ethan's View [PRESENT — bleachers ANCHOR]
**Timeline:** **PRESENT** — Ethan's bleacher seat. Same day; clock between 1:47 PM and 2:47 PM.
**Scene:** POV from Ethan's bleachers — Ttong small in distance — backs turned to Ethan.
**Dialogue:** Ethan (internal): *Same dobok. Same patch.*

**Prompt:**
```
POV from bleachers looking across gymnasium at distant coach helping another student,
blurred foreground lonely knees in hogu gear empty seats beside him, emotional isolation,
STYLE: PREMIER
```

---

### Panel 1.11 — Wrong Stretch [PRESENT — bleachers]
**Timeline:** **PRESENT** — still on bleachers. Shows neglect stacking: stranger "helps" while **his** coach ignores him.
**Scene:** Random parent yanks Ethan's arm into bad stretch. Ethan winces. Ttong doesn't look.
**Dialogue:** Parent (O.S.): "Loosen up, kid."

**Prompt:**
```
well-meaning stranger parent stretching teen athlete arm awkwardly on bleachers,
teen wincing coach far background turned away not watching neglect,
STYLE: PREMIER
```

---

### Panel 1.12 — Skill vs Silence [FLASH inset + PRESENT split]
**Timeline:** **Top — FLASH — dojang scrimmage, weeks earlier.** **Bottom — PRESENT — bleachers 2:47 PM.**
**Scene:** Flash — Ethan lands clean head kick on teammate — smirks. Present — phone **2:47 PM** — alone on same bleacher seat.
**Dialogue:** Ethan (internal): *Won every scrimmage last month.*

**Prompt:**
```
split panel top FLASH inset dojang scrimmage teen landing head kick smirking weeks ago,
bottom PRESENT same teen alone bleachers phone 2 47 PM contrast best fighter still ignored,
STYLE: PREMIER
```

---

### Panel 1.13 — Finally Called
**Scene:** Staging area. Official calls name. Ethan stands — legs stiff, grabs belt wrong.
**SFX:** PA: *"Hyun, Ethan — Ring 4."*

**Prompt:**
```
teen taekwondo fighter standing stiffly from bleachers, legs asleep expression,
competition staging area, referee in background, afternoon harsh light, STYLE: PREMIER
```

---

### Panel 1.13a-T — [CARD] Ttong Kim Intro ★
**Scene:** Fighter-style profile card — **Ttong Kim** before he speaks at staging. Empty stat boxes for post.
**Post text:** `TTONG KIM · Age 38 · 5'8" · 198 lbs · 2nd Dan · Premier Taekwondo Sports Dynasty`
**Prompt:**
```
manhwa webtoon fighter profile card vertical panel, korean taekwondo instructor antagonist portrait,
square face obvious underbite teeth visible predatory grin tight black shorts polo,
stat block empty boxes right side red accent bar premier school logo space,
cel shading no readable text STYLE CARD STYLE PREMIER
```

---

### Panel 1.13a-R — [CARD] Repeul Kim Intro ★
**Scene:** Profile card immediately after Ttong's — **Repeul Kim**. Role line only (no dan/division). Empty boxes for post.
**Post text:** `REPEUL KIM · Age 37 · 5'5" · 230 lbs · Premier (background)`
**Note:** **No dialogue ever** — intro is the only time her name appears on a card.
**Prompt:**
```
manhwa webtoon profile card vertical panel, overweight korean-american woman brown curly hair,
intentionally ugly clashing multicolor casual outfit neon floral plaid mean sour scowl judgmental face NOT smiling closed mouth not speaking, stat block empty boxes,
red-grey premier accent bar cel shading no readable text STYLE CARD STYLE PREMIER
```

---

### Panel 1.13b — Knockout Bounty [REAL #28] ★
**Scene:** Before ring — Ttong Kim holds **1,000 won** — **black belts knock out opponents, don't play nice** — **eyes Ethan** — *too soft, too nice for black belt*.
**Dialogue:** Ttong Kim: **"One thousand won if you knock them out. Black belt doesn't mean nice — it means you finish them."** · *(to Ethan)* **"Too soft."**
**Script:** [flash-premier-knockout-bounty.md](../scripts/flash-premier-knockout-bounty.md)
**Prompt:** `taekwondo coach holding 1000 won coin pointing at small black belt teen too nice speech unsettling, overweight woman ugly multicolor clothes mean scowl blurred background edge of frame not speaking, STYLE: PREMIER`

---

### Panel 1.14 — Ninety Seconds
**Scene:** Instructor appears — first time all day close to Ethan. Looks at watch. Points at ring.
**Dialogue:** Instructor: **"Go fight."**

**Prompt:**
```
cold taekwondo instructor pointing toward competition ring, dismissive expression,
teen athlete in white dobok full olympic kyorugi gear chest hogu headgear forearm shin foot guards listening,
instructor checking wristwatch, no warmth,
dramatic low angle, STYLE: PREMIER
```

---

### Panel 1.15 — Cold Entry
**Scene:** Ethan steps into ring. Stiff footwork. No sweat on brow. Opponent already bouncing.
**Dialogue:** *(none)*

**Prompt:**
```
teen entering taekwondo competition ring with stiff awkward movement,
white dobok full olympic kyorugi gear electronic chest hogu headgear forearm guards shin foot guards,
opponent in same full kit warming up bouncing in fighting stance, referee center, STYLE: PREMIER
```

---

### Panel 1.16 — Abandoned Corner
**Scene:** Over-shoulder from ring — instructor already walking toward another kid in premium gear.
**Dialogue:** *(none)*

**Prompt:**
```
over shoulder view from competition ring,
abandoned fighter in foreground white dobok full olympic kyorugi gear chest hogu headgear forearm shin guards,
coach walking away toward another student in full competition kit,
emotional gut punch composition, STYLE: PREMIER
```

---

### Panel 1.17 — The Spinning Hook
**Scene:** Opponent (taller, older) mid-spin — hook kick connecting with head sensor.
**SFX:** *THWACK* · electronic scoreboard flash **+3**

**Prompt:**
```
dynamic action shot taekwondo spinning hook kick impact on headgear,
both fighters white dobok full olympic kyorugi gear chest hogu headgear forearm shin foot guards,
motion blur on kicking leg, electronic score sensor flash, dramatic speed lines, impact frame, STYLE: PREMIER
```

---

### Panel 1.18 — Sound Dies
**Scene:** Ethan falling. Crowd mouths moving — no sound. Instructor in BG, arms crossed, disappointed.
**Dialogue:** *(silence)*

**Prompt:**
```
teen taekwondo fighter falling after head kick impact,
white dobok full olympic kyorugi gear chest hogu headgear forearm shin foot guards,
silent horror moment, muted desaturated colors,
disappointed coach arms crossed background, crowd blurred, soundless atmosphere visual,
STYLE: PREMIER
```

---

### Panel 1.19 — Smash Cut Wake
**Scene:** Ethan bolts upright in bed. Sweat on temples. Mouth open — silent scream.
**SFX:** *GASP*

**Prompt:**
```
teen boy jolting awake in bed sweating, gasping, dark blue hair messy, dawn light through curtains,
horror wake up moment, bedroom interior, dramatic upward angle, STYLE: PREMIER fading to neutral
```

---

### Panel 1.20 — Aftermath
**Scene:** Ethan staring at ceiling. Gold headphones on nightstand. Hand raised — block position — trembling.
**Dialogue:** Ethan (internal): *It wasn't just the kick.*

**Prompt:**
```
teen lying in bed staring at ceiling, hand raised in taekwondo block pose trembling,
gold headphones on nightstand, soft morning light, quiet emotional aftermath, close-up,
```

---

# Chapter 2 — Arrival at Kwon's

---

### Panel 2.1 — New Day
**Scene:** Ethan walks street with white gear backpack. Headphones on. Kwon's sign visible ahead.
**Dialogue:** *(none)*

**Prompt:**
```
teen boy walking suburban street wearing gold headphones white gear backpack,
taekwondo academy sign visible ahead, overcast morning clearing to soft light,
STYLE: KWONS beginning
```

---

### Panel 2.2 — Through the Window
**Scene:** Ethan peeks through dojang glass. Inside: MV holds focus mitts — one student throwing roundhouses. MV adjusts foot angle mid-drill.
**Dialogue:** MV (muffled): "Turn the hip more — yes, like that."

**Prompt:**
```
view through dojang window, korean taekwondo master holding focus mitts coaching one student,
individual attention, footwork correction, warm interior golden light, observer silhouette outside,
STYLE: KWONS
```

---

### Panel 2.3 — Contrast Split
**Scene:** Split panel. LEFT: Premier — crowded mat, instructor's back, kids waiting. RIGHT: Kwon's — two people, eye contact.
**Dialogue:** *(none)*

**Prompt:**
```
split screen comic panel left cold crowded taekwondo school instructor back turned,
right warm small class one coach facing one student eye contact, visual contrast,
STYLE: PREMIER left STYLE: KWONS right
```

---

### Panel 2.4 — Hand on Door
**Scene:** Ethan at entrance. Hand on door handle. Headphones around neck now. Hesitation.
**Dialogue:** Ethan (internal): *What if it's the same?*

**Prompt:**
```
close-up teen hand on dojang door handle hesitating, white taekwondo backpack strap visible,
warm light leaking through door gap, emotional threshold moment, STYLE: KWONS
```

---

### Panel 2.5 — Door Opens
**Scene:** Ethan steps in. MV and student look over — not hostile, curious. Clean mats. Quiet.
**Dialogue:** *(none)*

**Prompt:**
```
teen entering taekwondo dojang doorway, warm wooden floors clean mats, coach and student pausing to look,
welcoming quiet atmosphere, backlit entrance silhouette, STYLE: KWONS
```

---

### Panel 2.6 — Premier Ghost
**Scene:** Ethan pauses inside entrance. **FLASH inset** — crowded Premier mat, instructor's back. Snaps back to quiet Kwon's.
**Dialogue:** Ethan (internal): *Same sport. Different air.*

**Prompt:**
```
teen fighter just inside dojang doorway small flashback inset crowded cold school instructor back turned,
present warm empty reception area contrast, dissociation beat, STYLE: KWONS with PREMIER inset
```

---

### Panel 2.7 — Shoes Off
**Scene:** Close-up — Ethan removes sneakers, lines them beside others. Kwon's shoe rack — worn but neat.
**Dialogue:** *(none — ritual beat)*

**Prompt:**
```
close-up teen removing sneakers placing on wooden shoe rack taekwondo dojang entrance,
other student shoes lined neatly, respectful detail panel, STYLE: KWONS
```

---

### Panel 2.8 — Observation — MV Counts
**Scene:** Wide — MV counts reps aloud for one student on mitts. No yelling. Steady rhythm.
**Dialogue:** MV: "Four… five… turn the hip on six."

**Prompt:**
```
taekwondo master counting reps calmly holding focus mitts one student kicking,
empty space on mat not overcrowded, patient coaching wide shot, STYLE: KWONS
```

---

### Panel 2.9 — Student Thanks
**Scene:** Student bows, wipes sweat — genuine smile at MV. MV nods once — not performative.
**Dialogue:** Student: "Thank you, Master."

**Prompt:**
```
teen student bowing to taekwondo master after drill genuine grateful smile,
master modest nod not theatrical, warm mentor moment, STYLE: KWONS
```

---

### Panel 2.10 — Ethan Watches From Wall
**Scene:** Ethan stands by gear cubbies — hasn't changed yet. Arms crossed. Studying the room.
**Dialogue:** *(none)*

**Prompt:**
```
short teen boy with white gear backpack standing against dojang wall arms crossed observing,
other students training background soft focus, guarded watcher composition, STYLE: KWONS
```

---

### Panel 2.11 — Trophy Shelf Honest
**Scene:** Ethan glances at modest trophy shelf — local medals, faded ribbon. No fake gold wall.
**Dialogue:** Ethan (internal): *No brochure lies.*

**Prompt:**
```
modest taekwondo dojang trophy shelf few real medals honest worn ribbon,
teen glancing sideways at shelf detail shot, STYLE: KWONS
```

---

### Panel 2.12 — Window Light
**Scene:** Golden hour through high windows. Dust motes. Ethan exhales — shoulders drop one inch.
**Dialogue:** *(none — beat)*

**Prompt:**
```
golden afternoon light through dojang windows dust particles floating,
teen silhouette relaxing shoulders slightly emotional release, STYLE: KWONS
```

---

### Panel 2.13 — Other Student Notices
**Scene:** A cadet student (background extra) whispers to friend — points subtly at Ethan's backpack.
**Dialogue:** Cadet: "New guy brought competition gear."

**Prompt:**
```
two background taekwondo students whispering glancing at newcomer with gear backpack,
new student unaware foreground, natural dojang gossip, STYLE: KWONS
```

---

### Panel 2.14 — MV Finishes Drill
**Scene:** MV dismisses student with pat on shoulder. Turns — sees Ethan properly for first time inside.
**Dialogue:** MV: "You can put your bag down. You're not in the way."

**Prompt:**
```
taekwondo master finishing lesson turning to notice visitor teen with backpack,
kind open expression not suspicious, STYLE: KWONS
```

---

### Panel 2.15 — Bag Down
**Scene:** Ethan sets white gear backpack on bench — slow, deliberate. Sits beside it without changing.
**Dialogue:** Ethan: "I'm… just looking today."

**Prompt:**
```
teen placing white taekwondo gear backpack on bench sitting beside it hesitant,
dojo interior quiet, first honest words, STYLE: KWONS
```

---

### Panel 2.16 — MV Doesn't Push
**Scene:** MV pulls chair — sits across from Ethan. Not looming. Same eye level again.
**Dialogue:** MV: "Looking is allowed here."

**Prompt:**
```
master sitting on chair same height as seated teen equal conversation posture,
no pressure body language, STYLE: KWONS
```

---

### Panel 2.17 — Street Sound Memory
**Scene:** Through open door — distant car horn. Ethan's fingers twitch. **FLASH** — tournament PA echo *"Ring 4."*
**Dialogue:** *(SFX only)*

**Prompt:**
```
teen fingers twitching on bench open dojang door background street sound trigger,
small traumatic flash inset tournament PA speaker, STYLE: KWONS with PREMIER flash
```

---

### Panel 2.18 — MV Waits
**Scene:** MV doesn't ask what happened. Offers water bottle — unopened — slides it across bench.
**Dialogue:** MV: "When you're ready."

**Prompt:**
```
master sliding sealed water bottle across bench to quiet teen patient waiting,
simple kindness gesture close-up hands, STYLE: KWONS
```

---

### Panel 2.19 — Ethan Accepts Water
**Scene:** Ethan takes bottle. Doesn't drink yet. Holds it like an anchor.
**Dialogue:** Ethan (internal): *One student. One voice.*

**Prompt:**
```
teen holding unopened water bottle both hands sitting on bench emotional anchor object,
soft side lighting face downcast, STYLE: KWONS
```

---

### Panel 2.20 — Stay Until Close
**Scene:** Wide — class ends. Students bow out. Ethan still on bench. MV rolls mats nearby — doesn't rush him.
**Dialogue:** MV (off): "Lock-up's at nine. Take your time."

**Prompt:**
```
wide shot emptying dojang students bowing out teen still on bench master rolling mats background,
patient sanctuary atmosphere golden light, STYLE: KWONS
```

---

# Chapter 3 — Meeting Master Viet

---

### Panel 3.1 — Silver Belt
**Scene:** Close-up — Ethan's silver-letter black belt. Other students whisper.
**Dialogue:** Student: "Is that real?"

**Prompt:**
```
close-up unusual silver letter embroidery on black taekwondo belt, other students whispering background,
dojo interior, detail shot, STYLE: KWONS
```

---

### Panel 3.2 — MV Approaches
**Scene:** MV walks over — open posture, eye level with Ethan (Ethan short — MV slightly crouches).
**Dialogue:** MV: "You can watch as long as you want. Or you can join."

**Prompt:**
```
kind korean taekwondo master approaching short teen at equal eye level respectful posture,
open hands non-threatening, warm dojang background, STYLE: KWONS
```

---

### Panel 3.3 — No Sales Pitch
**Scene:** MV gestures to sign — *Kwon's Taekwondo Academy*. No trophy wall of lies. Simple, honest space.
**Dialogue:** MV: "No pressure. What's your name?"

**Prompt:**
```
simple honest taekwondo dojang interior modest trophy shelf, master gesturing welcome,
teen with dark blue hair quiet guarded expression, STYLE: KWONS
```

---

### Panel 3.4 — Ethan Speaks
**Scene:** Ethan removes headphones fully for first time. Small voice.
**Dialogue:** Ethan: "...Ethan."

**Prompt:**
```
teen boy removing gold headphones, vulnerable quiet expression saying his name,
close-up face, soft lighting, character introduction moment, STYLE: KWONS
```

---

### Panel 3.5 — Belt Question
**Scene:** Two students in background — one nudges other — staring at silver letters on Ethan's belt (still in bag, partially visible).
**Dialogue:** Student B: "Silver letters… you don't see that here."

**Prompt:**
```
background taekwondo students whispering pointing at unusual black belt silver embroidery in bag,
curious not hostile, STYLE: KWONS
```

---

### Panel 3.6 — MV Introduces Self
**Scene:** MV offers hand — Western shake, then switches to bow when Ethan bows first.
**Dialogue:** MV: "Viet Na. Most people say Master Viet. Either's fine."

**Prompt:**
```
taekwondo master introducing himself respectful bow handshake hybrid,
teen returning bow awkward polite, STYLE: KWONS
```

---

### Panel 3.7 — Looking or Training
**Scene:** MV crosses arms — not aggressive. Direct question.
**Dialogue:** MV: "You looking or training?"

**Prompt:**
```
master direct question arms crossed relaxed teen considering answer pause panel,
dojo background quiet tension, STYLE: KWONS
```

---

### Panel 3.8 — Long Beat
**Scene:** Beat panel — Ethan's eyes on mat lines. Jaw working. Silence stretches.
**Dialogue:** *(none — 3-second beat)*

**Prompt:**
```
minimal beat panel teen staring at dojang floor mat lines internal decision,
empty negative space emotional silence, STYLE: KWONS
```

---

### Panel 3.9 — Training
**Scene:** Ethan stands — small nod.
**Dialogue:** Ethan: "…Training."

**Prompt:**
```
teen standing with quiet determined nod choosing to train,
character decision moment medium shot, STYLE: KWONS
```

---

### Panel 3.10 — Changing Room
**Scene:** Ethan in corner — pulls dobok from bag. Hands pause on silver-letter belt.
**Dialogue:** Ethan (internal): *Last thing they couldn't take.*

**Prompt:**
```
teen changing into white taekwondo dobok holding silver letter black belt reverently,
private corner of dojang emotional detail, STYLE: KWONS
```

---

### Panel 3.11 — First Bow In
**Scene:** Ethan steps onto mat — bows to room. Other students pause — return bow.
**Dialogue:** *(none — ritual)*

**Prompt:**
```
teen bowing entering taekwondo mat other students pausing to return bow respect,
formal dojang etiquette wide shot, STYLE: KWONS
```

---

### Panel 3.12 — MV Watches Footwork
**Scene:** MV asks for casual stance — Ethan shifts weight — professional habit from old school.
**Dialogue:** MV: "Show me how you stand before anyone tells you to."

**Prompt:**
```
master observing teen fighter natural fighting stance evaluation,
instructional medium two-shot, STYLE: KWONS
```

---

### Panel 3.13 — Quiet Class
**Scene:** Observation — no one filming for social. No parents coaching from bleachers. Just training.
**Dialogue:** Ethan (internal): *No audience.*

**Prompt:**
```
taekwondo class training without parents filming without chaos focused practice,
teen noticing difference observational panel, STYLE: KWONS
```

---

### Panel 3.14 — Silver Belt Close-Up
**Scene:** Detail — silver letters catch window light. MV's eyes flick to belt — doesn't comment yet.
**Dialogue:** MV: "That's a serious belt."

**Prompt:**
```
close-up silver embroidered letters on black taekwondo belt catching light,
master's eyes in soft focus background measuring not judging, STYLE: KWONS
```

---

### Panel 3.15 — No Sales Pitch (Sign)
**Scene:** MV walks Ethan past wall — simple rates sheet. No "VIP package." No merch table.
**Dialogue:** MV: "We don't sell dreams. We train bodies."

**Prompt:**
```
simple honest taekwondo school tuition notice board no flashy marketing,
master gesturing matter-of-fact teen listening, STYLE: KWONS
```

---

### Panel 3.16 — Ethan Almost Smiles
**Scene:** Corner of Ethan's mouth — almost — doesn't complete. MV pretends not to notice.
**Dialogue:** *(none)*

**Prompt:**
```
subtle almost-smile on guarded teen face master looking away giving privacy,
micro-expression character beat, STYLE: KWONS
```

---

### Panel 3.17 — Other Students Resume
**Scene:** Class returns to drills — but side glances — curiosity not hostility.
**Dialogue:** Cadet (whisper): "He moves like a black belt."

**Prompt:**
```
taekwondo students resuming drills stealing glances at skilled newcomer,
natural peer observation, STYLE: KWONS
```

---

### Panel 3.18 — MV Assigns Space
**Scene:** MV points open mat lane — not back corner exile.
**Dialogue:** MV: "You can work here. Same air as everyone else."

**Prompt:**
```
master pointing to open space on main dojang mat welcoming not segregating,
teen carrying belt to assigned spot, STYLE: KWONS
```

---

### Panel 3.19 — First Instruction
**Scene:** MV holds paddle low — testing reaction speed, not showmanship.
**Dialogue:** MV: "When I say hold, you hold. When I say go, you go. Clear?"

**Prompt:**
```
master holding focus paddle low ready position teen nodding understanding,
clear boundary setting mentor moment, STYLE: KWONS
```

---

### Panel 3.20 — Ethan Nods
**Scene:** Ethan nods once — sharp. First crack of trust.
**Dialogue:** Ethan: "Clear."

**Prompt:**
```
teen sharp single nod focused eyes first trust beat,
close-up face golden light, STYLE: KWONS
```

---

# Chapter 4 — Training Demonstration

---

### Panel 4.1 — Pad Work Begins [TEACH]
**Scene:** MV holds shield. Ethan in dobok — roundhouse kick chamber.
**Dialogue:** MV: "Roundhouse — dollyo chagi. Turn the hip, snap the leg. Show me."

**Prompt:**
```
taekwondo training teen chambering roundhouse kick labeled hip rotation,
master holding kicking shield instructional sports manga, STYLE: KWONS TEACH
```

---

### Panel 4.2 — Roundhouse [TEACH]
**Scene:** Clean roundhouse impact. MV nods. Inset: strike zone on hogu highlighted.
**SFX:** *SMACK*
**Dialogue:** MV: "Two points to the body in a match — if the sensor agrees."

**Prompt:**
```
action taekwondo roundhouse kick hitting chest hogu target zone highlight,
instructional inset, master bracing shield, STYLE: KWONS TEACH
```

---

### Panel 4.3 — Back Kick [TEACH]
**Scene:** Ethan back kick — looking over shoulder. Textbook form.
**Dialogue:** MV: "Back kick — dwi chagi. Don't chase. Let them run into it."

**Prompt:**
```
teen executing taekwondo back kick looking over shoulder foot path diagram space,
instructional side view, STYLE: KWONS TEACH
```

---

### Panel 4.4 — Cut Kick [TEACH]
**Scene:** Cut kick to paddle — low line attack.
**Dialogue:** MV: "Cut kick — oreo chagi. Low line. Disrupt their balance before you score."

**Prompt:**
```
taekwondo cut kick low line striking focus paddle, leg chamber diagram inset,
instructional sports manga, STYLE: KWONS TEACH
```

---

### Panel 4.5 — Perfect Form
**Scene:** MV stops drill. Studies Ethan. Long pause.
**Dialogue:** MV: "Your form is perfect. Why would you leave a school that taught you this?"

**Prompt:**
```
taekwondo master studying teen fighter with serious impressed expression,
teen sweating breathing hard, quiet tension, medium two-shot, STYLE: KWONS
```

---

### Panel 4.6 — No Answer
**Scene:** Ethan looks away. Jaw tight.
**Dialogue:** Ethan: "..."

**Prompt:**
```
teen athlete looking away unable to answer, jaw clenched, master waiting patiently background,
emotional silence panel, STYLE: KWONS
```

---

### Panel 4.7 — They Didn't Have Me
**Scene:** Ethan finally — quiet but clear — eyes still averted.
**Dialogue:** Ethan: "They didn't have me."

**Prompt:**
```
teen speaking difficult truth looking away master listening still not pushing,
emotional honesty panel medium shot, STYLE: KWONS
```

---

### Panel 4.8 — MV Adjusts Shield
**Scene:** MV resets drill — doesn't dwell. Professional pivot back to work.
**Dialogue:** MV: "Then show me what you kept."

**Prompt:**
```
master resetting kicking shield professional calm after emotional beat,
back to training transition, STYLE: KWONS
```

---

### Panel 4.9 — Chamber Speed [TEACH]
**Scene:** MV calls speed — Ethan chambers roundhouse faster — still clean.
**Dialogue:** MV: "Speed without form is just noise."

**Prompt:**
```
teen chambering fast roundhouse kick master observing hip alignment,
instructional speed vs form panel, STYLE: KWONS TEACH
```

---

### Panel 4.10 — Combo Flow
**Scene:** Roundhouse → cut kick chain on paddle. Fluid. Other students stop to watch.
**Dialogue:** *(SFX)* *smack-smack*

**Prompt:**
```
dynamic taekwondo combo roundhouse into cut kick on focus mitts,
background students pausing to watch impressed, STYLE: KWONS
```

---

### Panel 4.11 — Breathing Control
**Scene:** Ethan finishes — controlled breathing — not gasping. MV notes it.
**Dialogue:** MV (internal caption): *Conditioning held.*

**Prompt:**
```
teen fighter controlled breathing after combo sweat on brow steady,
master noting endurance detail observation panel, STYLE: KWONS
```

---

### Panel 4.12 — Back Kick Distance [TEACH]
**Scene:** MV steps in — Ethan back kick — perfect distance — MV doesn't flinch.
**Dialogue:** MV: "You don't flinch when they crowd you."

**Prompt:**
```
precise taekwondo back kick stopping inches from master chest perfect distance control,
instructional trust drill, STYLE: KWONS TEACH
```

---

### Panel 4.13 — Class Resumes Watching
**Scene:** Wide — whole class at water break — watching Ethan from sidelines. Not jealous — measuring.
**Dialogue:** Student: "Where'd he come from?"

**Prompt:**
```
taekwondo class on water break watching talented newcomer train sideline whispers,
peer assessment wide shot, STYLE: KWONS
```

---

### Panel 4.14 — MV Correction Micro
**Scene:** MV taps Ethan's rear foot — tiny angle fix. Ethan adjusts instantly.
**Dialogue:** MV: "There. Don't lose that."

**Prompt:**
```
master correcting teen foot angle tiny adjustment instant compliance,
detail instructional panel feet and mat, STYLE: KWONS TEACH
```

---

### Panel 4.15 — Electronic Hogu Mention [TEACH]
**Scene:** MV holds chest hogu — points at sensor zone.
**Dialogue:** MV: "Olympic rules — chest sensor, head sensor. Power in the right zone beats flashy everywhere."

**Prompt:**
```
master holding electronic chest hogu explaining sensor zone diagram inset,
olympic taekwondo education panel, STYLE: KWONS TEACH
```

---

### Panel 4.16 — Ethan Nods — Sport Mind
**Scene:** Ethan touches hogu — familiar — tournament muscle memory.
**Dialogue:** Ethan: "I know the zones."

**Prompt:**
```
teen touching electronic hogu chest sensor familiar tournament gear,
confident quiet knowledge, STYLE: KWONS
```

---

### Panel 4.17 — Sweat On Mat
**Scene:** Close — sweat drop on mat. Ethan's first real work at Kwon's.
**Dialogue:** *(none — symbolic)*

**Prompt:**
```
close-up sweat drop on taekwondo mat after training symbolic first real work,
detail shot warm lighting, STYLE: KWONS
```

---

### Panel 4.18 — Other Students Bow Out
**Scene:** Class ends — students bow to MV — Ethan follows half a beat late — copies form.
**Dialogue:** All: "Thank you, Master."

**Prompt:**
```
taekwondo class bowing out teen newcomer copying bow half beat late learning ritual,
group etiquette wide shot, STYLE: KWONS
```

---

### Panel 4.19 — MV Quiet Praise
**Scene:** MV to Ethan alone — low voice — not for show.
**Dialogue:** MV: "Better than most black belts I see walk in."

**Prompt:**
```
master quiet private praise to teen after class not performative,
intimate mentor moment two-shot, STYLE: KWONS
```

---

### Panel 4.20 — Ethan Doesn't Know What To Do
**Scene:** Ethan opens mouth — closes it — bows instead. MV accepts bow.
**Dialogue:** *(none)*

**Prompt:**
```
teen awkward grateful bow instead of words master accepting bow warm,
character beat silence, STYLE: KWONS
```

---

# Chapter 5 — The Goal

---

### Panel 5.1 — The Question
**Scene:** MV pours water for Ethan. Sitting on mats after drill.
**Dialogue:** MV: "What do you want?"

**Prompt:**
```
taekwondo master handing water bottle to teen sitting on dojang mats, post-training,
calm mentoring moment, golden afternoon light, STYLE: KWONS
```

---

### Panel 5.2 — Silence
**Scene:** Ethan stares at water bottle. Reflection in cap.
**Dialogue:** *(none — beat panel)*

**Prompt:**
```
close-up teen staring at water bottle cap reflection, internal struggle, beat panel minimal action,
STYLE: KWONS
```

---

### Panel 5.3 — Korea U20
**Scene:** Ethan looks up — first fierce expression.
**Dialogue:** Ethan: "Korea U20 National Team."

**Prompt:**
```
teen boy looking up with fierce determined eyes, first sign of ambition,
dramatic low angle face close-up, dark blue hair, STYLE: KWONS
```

---

### Panel 5.4 — The Ask
**Scene:** Ethan stands, bows slightly awkward.
**Dialogue:** Ethan: "I want to join Kwon's Taekwondo Academy."

**Prompt:**
```
teen standing bowing slightly awkward to taekwondo master, determination and vulnerability,
dojo background, respectful request moment, STYLE: KWONS
```

---

### Panel 5.5 — MV Response
**Scene:** MV doesn't smile big — doesn't dismiss. Considers.
**Dialogue:** MV: "That's not a small dream. We can talk about it."

**Prompt:**
```
taekwondo master thoughtful expression arms crossed not dismissive not overjoyed,
measured response, teen waiting, STYLE: KWONS
```

---

### Panel 5.6 — Not A Small Dream
**Scene:** MV repeats — slower — letting words land.
**Dialogue:** MV: "That's not a small dream."

**Prompt:**
```
master repeating serious statement teen absorbing weight of words,
mentor gravity panel, STYLE: KWONS
```

---

### Panel 5.7 — Ethan Knows
**Scene:** Ethan — fierce again — doesn't back down from scale of goal.
**Dialogue:** Ethan: "I know."

**Prompt:**
```
teen fierce determined expression not backing down from big dream,
low angle face close-up, STYLE: KWONS
```

---

### Panel 5.8 — Small Dreams Die
**Scene:** MV wipes mouth with towel — matter-of-fact coaching wisdom.
**Dialogue:** MV: "Small dreams don't survive hard weeks."

**Prompt:**
```
master with towel around neck coaching wisdom matter-of-fact expression,
teen listening intently sitting on mat, STYLE: KWONS
```

---

### Panel 5.9 — Formal Distance Narrows
**Scene:** MV sits beside Ethan — not above — same mat level.
**Dialogue:** MV: "What do you want from taekwondo — not what you think I want to hear."

**Prompt:**
```
master sitting beside teen on mat equal level honest question,
trust building composition, STYLE: KWONS
```

---

### Panel 5.10 — Ethan Almost Lies Small
**Scene:** Ethan's mouth opens — "to get better" — stops himself.
**Dialogue:** Ethan (internal): *Don't shrink it.*

**Prompt:**
```
teen internal struggle almost saying small safe answer catching himself,
close-up face hesitation, STYLE: KWONS
```

---

### Panel 5.11 — Room Still
**Scene:** Wide — empty dojang — two figures on mat — clock ticks.
**Dialogue:** *(none — beat)*

**Prompt:**
```
wide empty dojang two figures on mat silence clock on wall,
decision atmosphere beat panel, STYLE: KWONS
```

---

### Panel 5.12 — Korea U20 (Repeat Weight)
**Scene:** Same line — but now MV hears the weight. Ethan doesn't look away this time.
**Dialogue:** Ethan: "Korea U20 National Team."

**Prompt:**
```
teen stating ambitious goal eye contact with master not looking away,
dramatic character moment, STYLE: KWONS
```

---

### Panel 5.13 — MV Doesn't Laugh
**Scene:** MV's reaction — no ridicule — slight eyebrow raise — respect.
**Dialogue:** *(none)*

**Prompt:**
```
master reaction no laughter slight eyebrow raise respect not mockery,
reaction panel face close-up, STYLE: KWONS
```

---

### Panel 5.14 — Can I Train Here
**Scene:** Ethan bows from seated position — awkward but sincere.
**Dialogue:** Ethan: "Can I… train here?"

**Prompt:**
```
teen bowing from seated position awkward sincere request,
vulnerable formal ask, STYLE: KWONS
```

---

### Panel 5.15 — No Promise
**Scene:** MV stands — offers hand to help Ethan up.
**Dialogue:** MV: "We'll see if you mean it."

**Prompt:**
```
master offering hand to help teen up no empty promise serious deal,
handshake help-up panel, STYLE: KWONS
```

---

### Panel 5.16 — Ethan Takes Hand
**Scene:** Ethan accepts hand up — first physical trust.
**Dialogue:** *(none)*

**Prompt:**
```
teen accepting master's hand being helped up first physical trust gesture,
hands close-up warm light, STYLE: KWONS
```

---

### Panel 5.17 — Enrollment Paper Simple
**Scene:** Front desk — one-page form. No VIP upsell. Ethan reads — plain language.
**Dialogue:** MV: "Month to month. Leave if we fail you."

**Prompt:**
```
simple one page taekwondo enrollment form no upsell teen reading relieved,
honest business practice panel, STYLE: KWONS
```

---

### Panel 5.18 — Ethan Signs
**Scene:** Ethan signs — hand steady. MV witnesses — no hard sell smile.
**Dialogue:** *(SFX)* *pen scratch*

**Prompt:**
```
teen signing enrollment form steady hand master witnessing no pressure smile,
commitment moment detail, STYLE: KWONS
```

---

### Panel 5.19 — Gear Locker
**Scene:** MV assigns cubby number. Ethan places white backpack inside.
**Dialogue:** MV: "Same spot every day. This is yours."

**Prompt:**
```
master assigning gear locker cubby teen placing white backpack inside belonging moment,
dojo cubby row, STYLE: KWONS
```

---

### Panel 5.20 — Night Exit Hope
**Scene:** Ethan leaves — night air — looks back through window — MV rolling last mat. Golden interior.
**Dialogue:** Ethan (internal): *Maybe.*

**Prompt:**
```
teen leaving dojang at night looking back through window master rolling mats inside golden light,
hopeful ending shot street exterior, STYLE: KWONS
```

---

# Chapter 6 — Why Did You Leave?

---

### Panel 6.1 — Direct Question
**Scene:** MV and Ethan walking mats edge. Other students packing up.
**Dialogue:** MV: "Why did you leave your old school?"

**Prompt:**
```
master and teen walking along edge of dojang mats, quiet after hours, direct conversation,
STYLE: KWONS
```

---

### Panel 6.2 — Deflection
**Scene:** Ethan puts headphones back on one ear.
**Dialogue:** Ethan: "It wasn't home anymore."

**Prompt:**
```
teen putting gold headphones on one ear deflecting, guarded body language,
master listening without pushing, STYLE: KWONS
```

---

### Panel 6.3 — Flash Sting (Money)
**Scene:** Quick flash — Premier instructor's cold face. Hands exchanging cash. Red tint.
**Dialogue:** *(distorted)* "...with us or..."

**Prompt:**
```
traumatic flashback inset cold angry taekwondo instructor face, hands exchanging money,
red desaturated overlay, sharp fragment panel, STYLE: PREMIER
```

---

### Panel 6.4 — MV Backs Off
**Scene:** MV nods — accepts answer for now.
**Dialogue:** MV: "When you're ready to tell me the rest, I'll listen."

**Prompt:**
```
kind taekwondo master nodding accepting answer, respectful distance, teen relieved but tense,
STYLE: KWONS
```

---

### Panel 6.5 — Walking Mats Edge
**Scene:** Ethan and MV walk perimeter — shoes off — evening class cleaning up.
**Dialogue:** MV: "Premier still has your friends on their roster."

**Prompt:**
```
master and teen walking dojang mat edge evening cleanup conversation,
casual serious talk wide shot, STYLE: KWONS
```

---

### Panel 6.6 — Ethan Stiffens
**Scene:** Ethan flinches at school name — headphones hand moves to pocket.
**Dialogue:** Ethan: "They're not my friends if they stay."

**Prompt:**
```
teen flinching at mention of old school hand moving to headphones pocket,
defensive reaction close-up, STYLE: KWONS
```

---

### Panel 6.7 — MV Corrects Gently
**Scene:** MV — calm — doesn't argue.
**Dialogue:** MV: "Some of them followed you out. Give them time."

**Prompt:**
```
master gentle correction calm expression teen stubborn profile,
mentor patience panel, STYLE: KWONS
```

---

### Panel 6.8 — Flash VIP [FLASH]
**Scene:** **FLASH** — paying kid gear adjustment — Ethan on bleachers same memory frame.
**Dialogue:** Instructor (flash): "Investment pays off."

**Prompt:**
```
flashback inset favored student gear adjustment instructor praising,
bleachers lonely teen same memory frame, STYLE: PREMIER flash
```

---

### Panel 6.9 — Present — Jaw Clench
**Scene:** **PRESENT** — Ethan's jaw — knuckles white on belt.
**Dialogue:** *(none)*

**Prompt:**
```
present teen jaw clenched white knuckles on black belt emotional trigger,
close-up detail STYLE: KWONS
```

---

### Panel 6.10 — Direct Question Again
**Scene:** MV stops walking — direct eye contact.
**Dialogue:** MV: "Did someone hurt you?"

**Prompt:**
```
master stopping direct eye contact serious care question,
teen caught off guard, STYLE: KWONS
```

---

### Panel 6.11 — Ethan Opens Mouth
**Scene:** Ethan starts to speak — stops — shame and anger mix.
**Dialogue:** Ethan: "They…"

**Prompt:**
```
teen trying to speak stopping mid word shame anger mixed expression,
vulnerable beat panel, STYLE: KWONS
```

---

### Panel 6.12 — Flash Cash [FLASH]
**Scene:** **FLASH sting** — hands exchanging cash — Ttong cold grin — red overlay.
**Dialogue:** Ttong (distorted): "…with us or…"

**Prompt:**
```
traumatic flash hands exchanging money cold instructor grin red overlay fragment,
STYLE: PREMIER flash sting
```

---

### Panel 6.13 — It Wasn't Home
**Scene:** **PRESENT** — Ethan blurts — then regrets volume.
**Dialogue:** Ethan: "It wasn't home anymore."

**Prompt:**
```
teen blurting emotional truth then immediately guarded,
master listening still, STYLE: KWONS
```

---

### Panel 6.14 — MV Accepts
**Scene:** MV nods — doesn't pry further today.
**Dialogue:** MV: "Home isn't a building. You'll know when you're in one."

**Prompt:**
```
master nodding wise quiet response teen processing,
mentor wisdom two-shot, STYLE: KWONS
```

---

### Panel 6.15 — Cleaning Together
**Scene:** Ethan picks up water bottle someone left — MV notices — doesn't comment.
**Dialogue:** *(none — character action)*

**Prompt:**
```
teen picking up forgotten water bottle helping clean dojang unprompted,
master noticing approving without words, STYLE: KWONS
```

---

### Panel 6.16 — Night Street
**Scene:** Ethan walks home — streetlights — phone dark in pocket.
**Dialogue:** Ethan (internal): *Not yet.*

**Prompt:**
```
teen walking home night streetlights hands in hoodie pocket phone dark,
contemplative solitude, STYLE: KWONS night
```

---

### Panel 6.17 — Premier Text Spam
**Scene:** Phone lights up — spam — *"Come back for black belt test special."* Ethan deletes without opening.
**Dialogue:** (text) **"Limited slots — VIP only."**

**Prompt:**
```
smartphone spam text VIP taekwondo marketing teen deleting without reading,
disgust micro-expression, STYLE: PREMIER cold on phone glow
```

---

### Panel 6.18 — Apartment Quiet
**Scene:** Ethan's room — gear bag by door — medal drawer closed — doesn't open it.
**Dialogue:** *(none)*

**Prompt:**
```
teen bedroom gear bag by door closed medal drawer not opening past trauma,
quiet domestic panel, STYLE: KWONS soft night
```

---

### Panel 6.19 — Mirror — Belt On
**Scene:** Ethan ties silver belt in mirror — practice — not for show.
**Dialogue:** Ethan (internal): *Still mine.*

**Prompt:**
```
teen tying black belt with silver letters in bedroom mirror private ritual,
identity affirmation close-up mirror, STYLE: KWONS soft
```

---

### Panel 6.20 — Sleep — No Nightmare
**Scene:** Ethan in bed — headphones on — eyes close — no smash cut this time.
**Dialogue:** *(none — relief beat)*

**Prompt:**
```
teen falling asleep with headphones calm breathing no nightmare transition,
soft peaceful panel contrast chapter 1, STYLE: KWONS soft
```

---

# Chapter 7 — Flashbacks Begin

**Timeline:** **FLASH Premier** montage (opening day → favoritism) → **PRESENT ANCHOR** panel **7.5** on Kwon's mats.

### Panel 7.1 — Opening Day (Warm)
**Scene:** Flashback — small empty Premier dojang. Younger Ethan (white belt) bows. Instructor smiles genuinely.
**Dialogue:** Instructor: "Welcome to the family."

**Prompt:**
```
flashback small new taekwondo dojang, young white belt boy bowing, warm smiling instructor,
hopeful beginning, soft warm memory filter, STYLE: PREMIER lighter
```

---

### Panel 7.2 — Growth
**Scene:** Time montage — more students enroll. More trophies. Instructor's smile smaller each panel.
**Dialogue:** *(none)*

**Prompt:**
```
montage three panels taekwondo school growing more students more trophies,
instructor smile fading each panel, time passage, STYLE: PREMIER cooling
```

---

### Panel 7.3 — Favoritism Montage
**Scene:** Paying kid gets new gear. Ethan in old gear. Instructor praises paying kid's mediocre kick.
**Dialogue:** Instructor: "Excellent! See — investment pays off."

**Prompt:**
```
taekwondo instructor praising student with expensive gear, another talented teen in worn gear ignored corner,
favoritism visual, STYLE: PREMIER
```

---

### Panel 7.4 — Sidelined
**Scene:** Ethan wins drill — instructor looks at clipboard, calls paying kid for "advanced work."
**Dialogue:** Instructor: "Ethan — sit. Marcus — come here."

**Prompt:**
```
teen winning sparring drill but coach pointing to bench telling him to sit,
less skilled wealthy student called forward instead, injustice panel, STYLE: PREMIER
```

---

### Panel 7.5 — Present Anchor
**Scene:** Snap back — Ethan on Kwon's mats alone after hours. Same drill stance. MV's voice off-panel.
**Dialogue:** MV (off): "Ethan? You okay?"

**Prompt:**
```
present day teen frozen in fighting stance on dojang mats alone, dissociating,
warm dojang, concerned coach voice off panel, STYLE: KWONS
```

---

### Panel 7.6 — MV Enters Frame
**Scene:** MV steps into Ethan's eyeline — doesn't touch — waits.
**Dialogue:** MV: "Flashback or footwork?"

**Prompt:**
```
master stepping into view careful not to startle dissociating teen,
gentle check-in, STYLE: KWONS
```

---

### Panel 7.7 — Ethan Returns
**Scene:** Ethan blinks — exhales — embarrassed.
**Dialogue:** Ethan: "Footwork."

**Prompt:**
```
teen returning to present embarrassed exhale master half-smile not calling lie,
recovery moment, STYLE: KWONS
```

---

### Panel 7.8 — Opening Day Detail [FLASH]
**Scene:** **FLASH** — empty Premier — fresh mats — Ttong younger — genuine smile.
**Dialogue:** Ttong (younger): "Small school. Big heart."

**Prompt:**
```
flashback brand new small taekwondo dojang empty fresh mats younger instructor genuine smile,
hopeful memory filter, STYLE: PREMIER lighter
```

---

### Panel 7.9 — Young Ethan Excited [FLASH]
**Scene:** **FLASH** — white belt Ethan — first uniform — parents proud off-panel.
**Dialogue:** Ethan (V.O.): *I believed him.*

**Prompt:**
```
flashback young white belt boy first taekwondo uniform excited parents blurred proud,
childhood hope, STYLE: PREMIER lighter
```

---

### Panel 7.10 — Enrollment Line [FLASH]
**Scene:** **FLASH montage cell** — enrollment line grows — brochures multiply — **Repeul Kim** silent with stack.
**Dialogue:** *(none)*

**Prompt:**
```
flashback montage enrollment line growing VIP brochures multiplying silent woman background,
commercialization creeping in, STYLE: PREMIER cooling
```

---

### Panel 7.11 — First Trophy [FLASH]
**Scene:** **FLASH** — Ethan wins local medal — Ttong hugs paying kid instead in background.
**Dialogue:** Ethan (V.O.): *I won. He photographed someone else.*

**Prompt:**
```
flashback teen winning medal instructor hugging different student in background for photo,
betrayal seed memory, STYLE: PREMIER
```

---

### Panel 7.12 — Scrimmage King [FLASH]
**Scene:** **FLASH** — Ethan dominates scrimmage — coach claps for paying kid's bad kick.
**Dialogue:** Instructor: "Excellent form, Marcus!"

**Prompt:**
```
flashback sparring teen dominating coach applauding weaker wealthy student instead,
injustice montage cell, STYLE: PREMIER
```

---

### Panel 7.13 — Demo Team Pick [FLASH]
**Scene:** **FLASH** — clipboard — Ethan's name crossed out — paying kid circled.
**Dialogue:** Instructor: "Ethan — sit. Marcus — demo team."

**Prompt:**
```
flashback clipboard names crossed out favored student circled demo team selection,
explicit sideline panel, STYLE: PREMIER
```

---

### Panel 7.14 — Gear Gap [FLASH]
**Scene:** **FLASH split** — new electronic hogus on paying kid — Ethan's worn straps.
**Dialogue:** Ethan (V.O.): *Same patch. Different price tag.*

**Prompt:**
```
flashback split panel expensive new taekwondo gear vs worn gear same school patch,
economic favoritism visual, STYLE: PREMIER
```

---

### Panel 7.15 — Ttong Smile Thin [FLASH]
**Scene:** **FLASH** — Ttong portrait — smile doesn't reach eyes — underbite grin.
**Dialogue:** Ttong: "We're a family."

**Prompt:**
```
flashback instructor portrait smile not reaching eyes predatory undertone,
unsettling promo photo aesthetic, STYLE: PREMIER
```

---

### Panel 7.16 — Present — Ethan Fists
**Scene:** **PRESENT** — Ethan on Kwon's mat — fists unclench when MV speaks.
**Dialogue:** MV: "Breathe. Then move."

**Prompt:**
```
present teen unclenching fists on mat master coaching breathing,
grounding exercise, STYLE: KWONS
```

---

### Panel 7.17 — One Step Drill
**Scene:** MV runs simple one-step — Ethan flows — muscle memory from pain.
**Dialogue:** *(SFX)* *tap — step — kick*

**Prompt:**
```
master running one step self defense drill teen flowing through movements,
therapeutic movement panel, STYLE: KWONS
```

---

### Panel 7.18 — Kind When Empty [V.O.]
**Scene:** Ethan kicks — **FLASH overlay faint** — empty Premier opening day ghosted on present mat.
**Dialogue:** Ethan (V.O.): *He was kind when the room was empty.*

**Prompt:**
```
present kick with faint ghost overlay flash empty dojang opening day double exposure,
poetic memory blend, STYLE: KWONS with PREMIER ghost
```

---

### Panel 7.19 — MV Sees Ghost Too
**Scene:** MV watches Ethan — sees something behind eyes — doesn't name it.
**Dialogue:** MV (internal): *That school left marks.*

**Prompt:**
```
master watching teen train recognizing trauma behind eyes compassionate observation,
mentor POV panel, STYLE: KWONS
```

---

### Panel 7.20 — Bow Out — Present Wins
**Scene:** Ethan bows — present tense — chooses Kwon's air.
**Dialogue:** Ethan (internal): *Room's not empty anymore.*

**Prompt:**
```
teen bowing on kwons mat present tense choosing forward golden light,
arc closure beat chapter 7, STYLE: KWONS
```

---

# Chapter 8 — Hospital Visit

---

### Panel 8.1 — Hospital Hall
**Scene:** Ethan in casual clothes — headphones, hoodie. Hospital corridor. Fluorescent buzz.
**Dialogue:** *(none)*

**Prompt:**
```
teen boy walking hospital corridor hoodie gold headphones around neck,
quiet somber atmosphere, fluorescent lighting, STYLE: PREMIER soft
```

---

### Panel 8.2 — Grandmother
**Scene:** Ethan enters room. Grandmother in bed — frail but smiles when she sees him.
**Dialogue:** Grandmother: "My champion."

**Prompt:**
```
elderly korean grandmother in hospital bed smiling weakly at visiting teen grandson,
tender emotional reunion, soft window light, hospital room, STYLE: PREMIER soft
```

---

### Panel 8.3 — Hand Hold
**Scene:** Ethan holds her hand — too gently, like she's glass.
**Dialogue:** Ethan: "I found a new school."

**Prompt:**
```
close-up teen holding elderly woman's thin hand gently, emotional restraint,
hospital bedsheets, intimate detail shot, STYLE: PREMIER soft
```

---

### Panel 8.4 — Phone Buzz
**Scene:** Phone on side table vibrates — stack of notifications. Ethan's face tightens.
**SFX:** *buzz buzz buzz*

**Prompt:**
```
smartphone vibrating many notification badges, teen's tense face in background blur,
ominous mood shift, hospital room, STYLE: PREMIER
```

---

### Panel 8.5 — Threatening Messages
**Scene:** Phone screen — texts from unknown numbers. *"Stop talking about my school."* *"You're making this worse."*
**Dialogue:** (text) **"I know where you train now."**

**Prompt:**
```
close-up smartphone screen threatening text messages, dark ominous lighting on phone glow,
teen hands gripping phone, no faces, STYLE: PREMIER
```

---

### Panel 8.6 — Silence Phone
**Scene:** Ethan silences phone. Puts in pocket. Returns to holding grandmother's hand. Forces small smile.
**Dialogue:** Ethan: "It's nothing."

**Prompt:**
```
teen silencing phone putting in pocket, returning to hold grandmother hand forced small smile,
protective grandson moment, hospital room, STYLE: PREMIER soft
```

---

### Panel 8.7 — Halmeoni Notices
**Scene:** Grandmother's thin hand squeezes his — she saw the phone.
**Dialogue:** Grandmother: "Bad men on the phone?"

**Prompt:**
```
elderly grandmother squeezing teen hand asking gentle question tired kind eyes,
hospital bed intimate two-shot, STYLE: PREMIER soft
```

---

### Panel 8.8 — Ethan Deflects Korean
**Scene:** Ethan answers in Korean — soft — protective lie.
**Dialogue:** Ethan: "Nothing. Rest."

**Prompt:**
```
teen speaking korean softly to grandmother protective deflection,
cultural intimate dialogue panel, STYLE: PREMIER soft
```

---

### Panel 8.9 — You Came
**Scene:** Grandmother pats his hand — winces less when smiling at him.
**Dialogue:** Grandmother: "You came. That's enough for today."

**Prompt:**
```
grandmother patting grandson hand weak smile enough for today emotional,
tender hospital beat, STYLE: PREMIER soft
```

---

### Panel 8.10 — Window Rain
**Scene:** Rain on hospital window — Ethan watches — reflection overlays his face.
**Dialogue:** *(none)*

**Prompt:**
```
rain on hospital window teen face reflected in glass contemplative,
melancholy atmosphere panel, STYLE: PREMIER soft
```

---

### Panel 8.11 — Voicemail Play [REAL #15]
**Scene:** Ethan steps into hall — alone — plays voicemail — hand over mouth.
**Dialogue:** Ttong (V.O.): "Stop talking about my school. Stop making kids leave."

**Prompt:**
```
teen alone hospital hallway playing voicemail hand over mouth shaken,
threatening audio visual, STYLE: PREMIER harsh
```

---

### Panel 8.12 — Delete Voicemail
**Scene:** Ethan deletes message — block number — hands tremble.
**Dialogue:** *(none)*

**Prompt:**
```
teen deleting voicemail blocking number trembling hands phone screen,
fear and anger panel, STYLE: PREMIER harsh
```

---

### Panel 8.13 — Nurse Passes
**Scene:** Nurse walks by — Ethan straightens — hides phone — trained to look fine.
**Dialogue:** Nurse: "Visiting hours end at eight."

**Prompt:**
```
hospital nurse walking past teen straightening hiding phone performing okay,
masking trauma public space, STYLE: PREMIER soft
```

---

### Panel 8.14 — Return To Room
**Scene:** Ethan returns — smile ready — sits back down.
**Dialogue:** Ethan: "New school has good mats."

**Prompt:**
```
teen returning to hospital room forced gentle smile sitting by grandmother,
protective grandson returning, STYLE: PREMIER soft
```

---

### Panel 8.15 — Photo In Purse
**Scene:** Grandmother shows worn photo — young Ethan white belt — creased edges.
**Dialogue:** Grandmother: "Before the big school."

**Prompt:**
```
elderly woman showing creased photo young grandson white belt in hospital bed,
nostalgic tender detail, STYLE: PREMIER soft
```

---

### Panel 8.16 — Ethan Can't Look
**Scene:** Ethan looks at photo — too long — pain — looks away.
**Dialogue:** Ethan: "That was a long time ago."

**Prompt:**
```
teen looking at childhood photo then looking away pain restrained,
emotional avoidance close-up, STYLE: PREMIER soft
```

---

### Panel 8.17 — Bus Ride Home
**Scene:** Ethan on night bus — forehead on window — city lights streak.
**Dialogue:** Ethan (internal): *I won't bring this to her room again.*

**Prompt:**
```
teen on night bus forehead against window city lights streak exhausted,
transit solitude panel, STYLE: PREMIER soft night
```

---

### Panel 8.18 — Kwon's Text From MV
**Scene:** Phone — new message — MV — *"Door's open tomorrow. Early class if you want."*
**Dialogue:** (text) MV: **"No pressure."**

**Prompt:**
```
smartphone text from taekwondo master kind message door open tomorrow,
warm notification glow on tired teen face bus, STYLE: KWONS soft on phone
```

---

### Panel 8.19 — Small Reply
**Scene:** Ethan types — deletes — types — sends one word.
**Dialogue:** (text) Ethan: **"Early."**

**Prompt:**
```
teen typing short reply on phone careful minimal emotional text,
close-up thumbs screen, STYLE: KWONS soft
```

---

### Panel 8.20 — Hospital Exit Wide
**Scene:** Wide — hospital exterior — Ethan small in frame — dawn breaking.
**Dialogue:** *(none — transition)*

**Prompt:**
```
wide shot hospital exterior dawn breaking small teen figure leaving,
transition hope hard week continues, STYLE: PREMIER soft to KWONS dawn
```

---

# Chapter 9 — Can They Come Too?

---

### Panel 9.1 — The Ask
**Scene:** Ethan and MV after class. Ethan unusually nervous — fidgeting with belt.
**Dialogue:** Ethan: "Some friends... they left Premier too. Can they join?"

**Prompt:**
```
nervous teen fidgeting with black belt asking question, taekwondo master listening after class,
empty dojang, hopeful anxiety, STYLE: KWONS
```

---

### Panel 9.2 — MV Answer
**Scene:** MV — simple nod.
**Dialogue:** MV: "Everyone deserves a home."

**Prompt:**
```
taekwondo master simple kind nod, warm expression, short powerful dialogue moment,
teen visible relief, STYLE: KWONS
```

---

### Panel 9.3 — The Text
**Scene:** Ethan on phone — group chat. Typing. Names visible: **TJ · Kieryn · Logan · Kian · Ariana**
**Dialogue:** (text) Ethan: *"Found a place. Kwon's. He said yes."*

**Prompt:**
```
close-up smartphone group chat typing message, contact names visible,
teen thumbs typing, golden hour through window on hands, STYLE: KWONS
```

---

### Panel 9.4 — Replies Flood
**Scene:** Phone notifications — question marks, fire emojis, "OMW", "FINALLY"
**Dialogue:** (text) Kieryn: *"Took you long enough."*

**Prompt:**
```
smartphone screen flooding with reply notifications excited messages,
comic relief energy, warm lighting, STYLE: KWONS
```

---

### Panel 9.5 — TJ First Reply
**Scene:** Text thread — **TJ** — *"Send address. We're not staying at Premier another week."*
**Dialogue:** (text) TJ: **"Is the mat actually soft or Kieryn will complain."**

**Prompt:**
```
smartphone group chat TJ message confident tone address request,
text UI panel comic energy, STYLE: KWONS
```

---

### Panel 9.6 — Kieryn Sarcasm
**Scene:** Kieryn typing bubble — long — sends anyway.
**Dialogue:** (text) Kieryn: **"Took you long enough, prodigy."**

**Prompt:**
```
smartphone chat kieryn sarcastic reply typing bubble energy,
character voice through text, STYLE: KWONS
```

---

### Panel 9.7 — Logan Sticker Flood
**Scene:** Logan sends food stickers — ramen — spaghetti — question marks.
**Dialogue:** (text) Logan: **"Is there food near there??"**

**Prompt:**
```
smartphone chat logan food emoji stickers flood comic relief,
character personality text only, STYLE: KWONS
```

---

### Panel 9.8 — Kian Short
**Scene:** Kian — one line — no emoji.
**Dialogue:** (text) Kian: **"I owe you a rematch. Send pin."**

**Prompt:**
```
smartphone chat kian short blunt message rematch energy,
minimal text panel, STYLE: KWONS
```

---

### Panel 9.9 — Ariana Read Receipt
**Scene:** Ariana — typing… — stops — **Read 9:42 PM** — no reply yet.
**Dialogue:** *(none — mystery beat)*

**Prompt:**
```
smartphone chat ariana read receipt no reply typing stopped mystery,
quiet character tease, STYLE: KWONS
```

---

### Panel 9.10 — Ethan Stares At Screen
**Scene:** Ethan on dojang steps after class — screen glow — almost smiles.
**Dialogue:** Ethan (internal): *I didn't ask them to follow me. I asked if they could breathe.*

**Prompt:**
```
teen sitting on dojang steps phone glow face almost smiling internal relief,
golden evening, STYLE: KWONS
```

---

### Panel 9.11 — MV Over Shoulder
**Scene:** MV locks door — sees Ethan on steps — doesn't ask who texts.
**Dialogue:** MV: "Friends?"

**Prompt:**
```
master locking dojang door seeing teen on steps simple question,
warm evening two-shot, STYLE: KWONS
```

---

### Panel 9.12 — Ethan Nods
**Scene:** Ethan nods — doesn't hide phone for once.
**Dialogue:** Ethan: "Maybe."

**Prompt:**
```
teen nodding not hiding phone hopeful maybe answer,
trust micro-moment, STYLE: KWONS
```

---

### Panel 9.13 — Everyone Deserves Home (Repeat Weight)
**Scene:** MV repeats earlier line — now Ethan hears full meaning.
**Dialogue:** MV: "Everyone deserves a home. Even the loud ones."

**Prompt:**
```
master repeating kind policy line teen listening full meaning landing,
mentor wisdom evening light, STYLE: KWONS
```

---

### Panel 9.14 — Schedule Check
**Scene:** Ethan pulls up class schedule — screenshots — sends to group.
**Dialogue:** (text) Ethan: **"Saturday 10 AM. Don't be late."**

**Prompt:**
```
teen screenshotting class schedule sending group chat taking charge,
leadership seed panel, STYLE: KWONS
```

---

### Panel 9.15 — Premier Group Chat Muted
**Scene:** Ethan mutes old Premier team chat — 99+ notifications — doesn't open.
**Dialogue:** (text preview) **"Where did Hyun go?"**

**Prompt:**
```
smartphone muting old premier group chat notification badge ignored,
breaking away panel, STYLE: PREMIER cold on KWONS present
```

---

### Panel 9.16 — Ariana Finally Replies
**Scene:** Ariana — one word — lands heavy.
**Dialogue:** (text) Ariana: **"Okay."**

**Prompt:**
```
smartphone single word reply ariana okay minimal emotional weight,
quiet character text beat, STYLE: KWONS
```

---

### Panel 9.17 — Night Before — Ethan Prepares
**Scene:** Ethan lays out extra guest waivers MV left on desk — neat stack.
**Dialogue:** Ethan (internal): *Six chairs. One room.*

**Prompt:**
```
teen preparing guest enrollment forms on dojang desk night before arrivals,
anticipation detail shot, STYLE: KWONS night
```

---

### Panel 9.18 — MV Early Light
**Scene:** MV alone — opens dojang early — turns on lights — extra mats out.
**Dialogue:** MV (internal): *Big day.*

**Prompt:**
```
master opening dojang early morning turning on lights extra mats prepared,
mentor preparation wide shot, STYLE: KWONS dawn
```

---

### Panel 9.19 — Ethan Early Arrival
**Scene:** Ethan already waiting outside — bag packed — headphones off.
**Dialogue:** Ethan: "I couldn't sleep."

**Prompt:**
```
teen waiting outside dojang early morning bag packed no headphones nervous excited,
dawn arrival, STYLE: KWONS
```

---

### Panel 9.20 — Door Unlock
**Scene:** MV unlocks — first inside — Ethan follows — empty mat like promise.
**Dialogue:** MV: "Let's get the room ready."

**Prompt:**
```
master unlocking dojang door teen following inside empty mat morning light ready,
chapter transition to team arrival, STYLE: KWONS dawn
```

---

# Chapter 10 — Welcome to Kwon's

---

### Panel 10.1 — Arrivals Begin
**Scene:** Dojang door — multiple figures arriving. Silhouettes with distinct hair colors.
**Dialogue:** *(none)*

**Prompt:**
```
taekwondo dojang entrance multiple teen silhouettes arriving different colored hair shapes,
hero team arrival composition backlit, STYLE: KWONS
```

---

### Panel 10.2 — TJ Lim
**Scene:** TJ enters — teal hair, headband, muscular, confident grin. Carries himself like he owns the room.
**Dialogue:** TJ: "So this is the famous Kwon's."

**Prompt:**
```
teen boy 15 teal hair headband muscular build confident grin entering dojang,
taekwondo gear bag, champion presence, character reveal, STYLE: KWONS
```

---

### Panel 10.3 — Kieryn Lim
**Scene:** Kieryn — teal/purple hair, asymmetrical bob, arms crossed, smirk.
**Dialogue:** Kieryn: "Smaller than I expected."

**Prompt:**
```
tall teen girl 13 teal hair purple streaks asymmetrical bob arms crossed smirk,
sassy entrance, taekwondo dobok, character reveal, STYLE: KWONS
```

---

### Panel 10.4 — Logan Hyun
**Scene:** Logan — bowl cut, big eyes, waves at everyone including strangers.
**Dialogue:** Logan: "Hi! Hi! Is there food nearby?"

**Prompt:**
```
cheerful teen boy 13 dark blue bowl cut big eyes waving enthusiastically oversized backpack,
friendly energy character reveal, STYLE: KWONS
```

---

### Panel 10.5 — Kian Sang
**Scene:** Kian — white/silver hair, lean, hands in pockets, challenging glance at Ethan.
**Dialogue:** Kian: "...You got here first. Doesn't mean you're ahead."

**Prompt:**
```
teen boy 15 white silver hair low taper fade dark brown skin lean athletic,
hands in pockets challenging smirk looking at another fighter, character reveal, STYLE: KWONS
```

---

### Panel 10.6 — Ethan & Kian Eye Lock
**Scene:** Ethan and Kian — brief stare. Not hatred — spark.
**Dialogue:** *(none)*

**Prompt:**
```
two teen taekwondo fighters eye contact moment, dark blue hair vs white silver hair,
friendly rivalry spark not hatred, medium shot, STYLE: KWONS
```

---

### Panel 10.7 — Ariana Yang
**Scene:** Ariana enters last — quiet, black/red hair, extra bandages on arms visible. Finds corner, starts stretching without a word.
**Dialogue:** *(none)*

**Prompt:**
```
quiet teen girl 15 black hair red streaks chin bob blunt bangs dark brown skin,
extra arm bandages stretching alone in corner silently, stoic character reveal, STYLE: KWONS
```

---

### Panel 10.8 — MV Addresses All
**Scene:** MV stands before full group — Ethan, TJ, Kieryn, Logan, Kian, Ariana. Seven on mat.
**Dialogue:** MV: "Kwon's isn't a business. It's a team. If you work, I work."

**Prompt:**
```
taekwondo master addressing group of six diverse teen students on dojang mats,
team assembly wide shot, mentor speech moment, STYLE: KWONS
```

---

### Panel 10.9 — Ethan Looks Around
**Scene:** Ethan's POV — faces of new family. Headphones in pocket.
**Dialogue:** Ethan (internal): *Home.*

**Prompt:**
```
POV looking at group of teammates smiling talking on taekwondo mats,
warm golden dojang light, emotional found family moment, STYLE: KWONS
```

---

### Panel 10.10 — Final Wide
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

### Panel 10.11 — Team Stretch Circle
**Scene:** MV leads stretch circle — seven students — Ethan not in corner — in ring.
**Dialogue:** MV: "Same rules for everyone."

**Prompt:**
```
taekwondo team stretch circle seven students master leading ethan included in ring,
team chemistry haikyuu warmth, STYLE: KWONS
```

---

### Panel 10.12 — TJ Windows Line
**Scene:** TJ grins at Ethan — callback Ch 2.
**Dialogue:** TJ: "You picked a place with windows. Good call."

**Prompt:**
```
confident teen teal headband grinning at ethan team banter dojang,
character voice panel HAIKYUU warmth, STYLE: KWONS
```

---

### Panel 10.13 — Kieryn Mat Test
**Scene:** Kieryn presses mat with foot — dramatic — actually fine.
**Dialogue:** Kieryn: "If the mats are soft, I'm still leaving."

**Prompt:**
```
sarcastic teen girl testing dojang mat with foot dramatic expression,
comic team intro, STYLE: KWONS
```

---

### Panel 10.14 — Logan Food Question
**Scene:** Logan — bowl cut — backpack overflowing — raises hand like school.
**Dialogue:** Logan: "Is there food later? Important question."

**Prompt:**
```
cheerful small teen bowl cut raising hand asking about food oversized backpack,
comic relief character intro, STYLE: KWONS
```

---

### Panel 10.15 — Kian Rematch
**Scene:** Kian — silver hair — hands in pockets — locks eyes with Ethan.
**Dialogue:** Kian: "You owe me a rematch from Premier."

**Prompt:**
```
silver hair teen challenging smirk hands in pockets facing ethan rivalry spark,
character intro tension friendly, STYLE: KWONS
```

---

### Panel 10.16 — Ariana Silent Stretch
**Scene:** Ariana — red streak bob — stretching alone — doesn't look up — bandages on ankle.
**Dialogue:** *(none)*

**Prompt:**
```
quiet teen girl red hair streak stretching alone extra ankle bandages not looking up,
introverted character intro, STYLE: KWONS
```

---

### Panel 10.17 — MV Team Speech
**Scene:** MV center — team semicircle — Ethan off-center not hiding.
**Dialogue:** MV: "We train hard. We don't tear each other down. You brought family — don't waste it."

**Prompt:**
```
master addressing semicircle team speech ethan visible among peers not spotlight,
mentor team speech wide, STYLE: KWONS
```

---

### Panel 10.18 — Curiosity Not Pity
**Scene:** Team glances at Ethan — curiosity — TJ nudges Kieryn — no pity faces.
**Dialogue:** Kieryn (whisper): "So *that's* the prodigy."

**Prompt:**
```
team glancing at ethan curious not pitying whispered comment,
group reaction panel, STYLE: KWONS
```

---

### Panel 10.19 — First Group Bow
**Scene:** MV calls bow — seven sync — Ethan one beat late — laughs quietly with Logan.
**Dialogue:** All: "Thank you, Master!"

**Prompt:**
```
seven students bowing together ethan slightly late logan stifling laugh team sync,
found family chemistry, STYLE: KWONS HAIKYUU
```

---

### Panel 10.20 — Caption Card
**Scene:** Black hold — white text — same energy as 1.1 title card inverted.
**Caption:** *Welcome to Kwon's.*
**Dialogue:** *(none — end arc 1)*

**Prompt:**
```
title card black background white caption space welcome to kwons text added in post,
arc finale card minimal, STYLE: KWONS
```

---

## Arc 1 Panel Count Summary

| Chapter | Panels | Range |
|---------|--------|-------|
| 1 — Nightmare | 23 | 1.1–1.20 (+ 1.13a-T/R, 1.13b) |
| 2 — Arrival | 20 | 2.1–2.20 |
| 3 — Meeting MV | 20 | 3.1–3.20 |
| 4 — Training | 20 | 4.1–4.20 |
| 5 — The Goal | 20 | 5.1–5.20 |
| 6 — Why Leave | 20 | 6.1–6.20 |
| 7 — Flashbacks | 20 | 7.1–7.20 |
| 8 — Hospital | 20 | 8.1–8.20 |
| 9 — Can They Come | 20 | 9.1–9.20 |
| 10 — Welcome | 20 | 10.1–10.20 |
| **Total** | **203** | |

---

## Next Steps

- **Character reference sheets:** [reference-sheets/](../reference-sheets/README.md) — start with **Ethan** (Google Sheet tab + P0 prompts).
- **Arc 2+ expansion:** Match ~20 panels/chapter when expanding other arcs — see [STORYBOARD-GUIDE.md](./STORYBOARD-GUIDE.md).
- **Batch generation tip:** Generate Ethan reference sheet first (panels 3.4, 4.2, 5.3) and use as image-to-image reference for consistency.
