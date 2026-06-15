# Arc 1 — Panel Storyboard (Chapters 1–10)

**New Beginnings** · Premier trauma → Kwon's sanctuary → team reveal.

Append [Global Style from STORYBOARD-GUIDE](./STORYBOARD-GUIDE.md) to all prompts unless a panel specifies `STYLE: PREMIER` or `STYLE: KWONS`.

**Reference sheets:** [reference-sheets/](../reference-sheets/README.md) — attach Ethan, MV, Ttong Kim refs for Ch 1–10 batch gen.

**Premier flash (extended):** [flash-premier-knockout-bounty.md](../scripts/flash-premier-knockout-bounty.md) § Scene 1 → **1.13b** · § Scene 2 → **1.14–1.16** bridge.

---

## How to Use

1. Generate panels in order (`1.1` → `10.10`).
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

## Arc 1 Panel Count Summary

| Chapter | Panels | Range |
|---------|--------|-------|
| 1 — Nightmare | 20 | 1.1–1.20 |
| 2 — Arrival | 5 | 2.1–2.5 |
| 3 — Meeting MV | 4 | 3.1–3.4 |
| 4 — Training | 6 | 4.1–4.6 |
| 5 — The Goal | 5 | 5.1–5.5 |
| 6 — Why Leave | 4 | 6.1–6.4 |
| 7 — Flashbacks | 5 | 7.1–7.5 |
| 8 — Hospital | 6 | 8.1–8.6 |
| 9 — Can They Come | 4 | 9.1–9.4 |
| 10 — Welcome | 10 | 10.1–10.10 |
| **Total** | **69** | |

---

## Next Steps

- **Character reference sheets:** [reference-sheets/](../reference-sheets/README.md) — start with **Ethan** (Google Sheet tab + P0 prompts).
- **Expand thin chapters** (2–6) with more panels if you want ~10–15 panels per chapter for a full webtoon episode length.
- **Batch generation tip:** Generate Ethan reference sheet first (panels 3.4, 4.2, 5.3) and use as image-to-image reference for consistency.
