#!/usr/bin/env python3
"""Expand Arc 1 panel storyboard to 40 panels per chapter (400 total)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORYBOARD = ROOT / "storyboards" / "arc-01-panel-storyboard.md"

PANEL_HEADER = re.compile(r"^### Panel ([\d.]+(?:[a-zA-Z-]+)?) — (.+)$")
CHAPTER_HEADER = re.compile(r"^# Chapter (\d+) — (.+)$")
FIELD_LINE = re.compile(
  r"^\*\*(Scene|Dialogue|SFX|Timeline|Post text|Script|Note|Caption):\*\*(.*)$"
)

# --- Character prompt fragments (Chapter 1 outfit lock) ---
ETHAN_BASE = (
  "Ethan Hyun teen boy 15 korean-american 5 foot 3 dark blue shadow perm hair brown eyes"
)
ETHAN_GEAR = (
  f"{ETHAN_BASE}, full Olympic kyorugi kit white dobok electronic chest hogu headgear "
  "forearm shin foot guards plain white dobok NO arm patch black belt"
)
ETHAN_BEDROOM = (
  f"{ETHAN_BASE}, grey sleep tee messy dark blue hair gold headphones on nightstand NOT dobok"
)
ETHAN_CASUAL = (
  f"{ETHAN_BASE}, gold headphones white gear backpack oversized navy hoodie white tee baggy pants"
)
ETHAN_DOBOK = (
  f"{ETHAN_BASE}, standard white dobok guards under silver-letter black belt"
)
MV = "Master Viet chubby 5 foot 8 kind small eyes kwon vest or white dobok black neck stripes"

# --- Chapter 1: hand-built merge sequence (40 panels) ---
CH1_NEW_PANELS: dict[str, dict] = {
  "team-bus-arrival": {
    "title": "Team Bus Arrival",
    "scene": (
      "Prime team van in tournament parking lot at dawn. Kids unloading gear bags. "
      "**Ethan Hyun** last off, kit bag heavy."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"dawn parking lot Prime team van logo teens unloading taekwondo gear bags, "
      f"{ETHAN_GEAR} stepping down last tired expression overcast sky wide establishing shot, "
      "STYLE: PRIME"
    ),
  },
  "parking-walk": {
    "title": "Parking Walk",
    "scene": (
      "**Ethan Hyun** walking from lot toward venue with Prime teens in **full kyorugi kits**. "
      "Long empty sidewalk."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} walking parking lot sidewalk toward tournament venue entrance "
      "with Prime teens same full Olympic kyorugi kits gear bags dawn mist desaturated wide shot, "
      "STYLE: PRIME"
    ),
  },
  "entrance-threshold": {
    "title": "Entrance Threshold",
    "scene": (
      "Automatic doors. Banner overhead: *Regional Open*. **Ethan Hyun** hesitates on the threshold — "
      "one foot raised."
    ),
    "dialogue": "Ethan (internal): *Here we go again.*",
    "prompt": (
      f"tournament venue automatic glass doors banner overhead {ETHAN_GEAR} hesitating on threshold "
      "one foot raised harsh fluorescent light spilling out emotional threshold shot low angle, "
      "STYLE: PRIME"
    ),
  },
  "gear-check-line": {
    "title": "Gear Check Line",
    "scene": (
      "Wristband table. Official scanning athletes. **Ethan Hyun** waiting in line in **full kit**, "
      "adjusting forearm guard strap."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"tournament gear check wristband table official scanning athletes queue "
      f"{ETHAN_GEAR} waiting adjusting forearm guard strap fluorescent hallway, "
      "STYLE: PRIME"
    ),
  },
  "empty-warmup-floor": {
    "title": "Empty Warmup Floor",
    "scene": (
      "**Ethan Hyun** passes open mats — no instructor. Kids sitting on floor in hogus, scrolling phones."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} walking past empty warmup mats no coach teens sitting on gym floor in kyorugi gear "
      "on phones neglectful atmosphere wide shot, STYLE: PRIME"
    ),
  },
  "walking-bleachers": {
    "title": "Walking to Bleachers",
    "scene": "POV climbing metal bleacher steps in **hogu**. Crowd noise above. **Ethan Hyun's** guarded knees in frame.",
    "dialogue": "*(none)*",
    "prompt": (
      f"POV climbing metal bleacher steps Olympic chest hogu forearm shin guards in frame "
      "tournament gymnasium crowd above {ETHAN_GEAR} perspective immersive shot, STYLE: PRIME"
    ),
  },
  "finding-seat": {
    "title": "Finding Seat",
    "scene": (
      "**Ethan Hyun** squeezing past legs along bleacher row. Finds isolated seat. Sets kit bag down."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} squeezing past seated spectators on metal bleachers finding empty isolated seat "
      "setting gear bag down awkward polite expression, STYLE: PRIME"
    ),
  },
  "gear-adjustment-alone": {
    "title": "Gear Adjustment Alone",
    "scene": (
      "**Ethan Hyun** alone fixing headgear strap. No coach nearby. Mirror of neglect — "
      "fumbling buckle."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"close-up {ETHAN_GEAR} alone on bleachers fumbling headgear strap buckle no instructor nearby "
      "isolated neglectful atmosphere, STYLE: PRIME"
    ),
  },
  "vending-run": {
    "title": "Vending Run",
    "scene": (
      "**Ethan Hyun** walking concourse in **full kit**. Returns to bleachers with snack wrapper, "
      "still alone."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} walking tournament concourse vending machines returning to bleachers "
      "crumpled snack wrapper in hand empty corridor afternoon, STYLE: PRIME"
    ),
  },
  "legs-asleep": {
    "title": "Legs Asleep",
    "scene": (
      "**Ethan Hyun** on bleachers shaking leg — pins and needles. Grimace. Clock still hours from his match."
    ),
    "dialogue": "Ethan (internal): *Come on.*",
    "prompt": (
      f"{ETHAN_GEAR} sitting on bleachers shaking stiff leg pins and needles grimacing "
      "afternoon wall clock background bored exhausted, STYLE: PRIME"
    ),
  },
  "corridor-staging": {
    "title": "Corridor to Staging",
    "scene": (
      "**Ethan Hyun** walking through crowd in **full kit** toward staging area. Shoulders tight."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} walking crowded tournament corridor toward staging area athletes passing "
      "tense shoulders afternoon harsh light tracking shot, STYLE: PRIME"
    ),
  },
  "staging-line": {
    "title": "Staging Line",
    "scene": (
      "Officials checking gear. **Ethan Hyun** in queue — chest sensor tap, headgear check."
    ),
    "dialogue": "Official: \"Next.\"",
    "prompt": (
      f"tournament staging line officials checking electronic hogu headgear "
      f"{ETHAN_GEAR} waiting in queue tense expression gear inspection, STYLE: PRIME"
    ),
  },
  "walk-to-ring": {
    "title": "Walk to Ring",
    "scene": "**Ethan Hyun** in corridor toward competition floor. Referee whistle distant. Legs still stiff.",
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_GEAR} walking corridor toward competition floor distant referee whistle "
      "stiff gait overhead arena lights dramatic depth, STYLE: PRIME"
    ),
  },
  "ring-threshold": {
    "title": "Ring Threshold",
    "scene": (
      "**Ethan Hyun** stepping over boundary tape onto competition mat. Opponent warming up ahead."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"close-up feet stepping over competition ring boundary tape onto mat "
      f"{ETHAN_GEAR} entering ring opponent warming up background low angle threshold moment, "
      "STYLE: PRIME"
    ),
  },
  "fade-to-black": {
    "title": "Fade to Black",
    "scene": (
      "After KO — traumatic fade. **Ethan Hyun** falling out of frame. Soundless black closing in. "
      "Not bedroom yet."
    ),
    "dialogue": "*(silence)*",
    "prompt": (
      f"traumatic fade to black Ethan Hyun falling after head kick silhouette disappearing "
      "soundless horror muted desaturated vignette closing NOT bedroom yet, STYLE: PRIME"
    ),
  },
  "slow-breath": {
    "title": "Slow Breath",
    "scene": (
      "**Ethan Hyun** in bed — hands on chest. Breath slowing. Dawn birds outside. "
      "Grey sleep tee. Calming after gasp."
    ),
    "dialogue": "*(none)*",
    "prompt": (
      f"{ETHAN_BEDROOM} lying in bed hands on chest slow breathing calming dawn birds outside window "
      "soft grey morning light emotional recovery beat, STYLE: neutral"
    ),
  },
  "window-dawn": {
    "title": "Window Dawn",
    "scene": (
      "Bedroom window — grey dawn light. **Plain gear bag** on chair — memory object. "
      "**Ethan Hyun** small in bed."
    ),
    "dialogue": "Ethan (internal): *Still here.*",
    "prompt": (
      f"bedroom window grey dawn light plain gear bag on chair foreground no patches "
      f"{ETHAN_BEDROOM} small in bed background quiet aftermath wide shot, STYLE: neutral"
    ),
  },
}

CH1_SEQUENCE: list[tuple[str, str]] = [
  ("orig", "1.1"),
  ("new", "team-bus-arrival"),
  ("new", "parking-walk"),
  ("new", "entrance-threshold"),
  ("orig", "1.2"),
  ("new", "gear-check-line"),
  ("new", "empty-warmup-floor"),
  ("orig", "1.3"),
  ("new", "walking-bleachers"),
  ("orig", "1.4"),
  ("new", "finding-seat"),
  ("orig", "1.5"),
  ("new", "gear-adjustment-alone"),
  ("orig", "1.6"),
  ("new", "vending-run"),
  ("orig", "1.7"),
  ("new", "legs-asleep"),
  ("orig", "1.8"),
  ("orig", "1.9"),
  ("orig", "1.10"),
  ("orig", "1.11"),
  ("orig", "1.12"),
  ("orig", "1.13"),
  ("new", "corridor-staging"),
  ("new", "staging-line"),
  ("orig", "1.13a-T"),
  ("orig", "1.13a-R"),
  ("orig", "1.13b"),
  ("orig", "1.14"),
  ("new", "walk-to-ring"),
  ("new", "ring-threshold"),
  ("orig", "1.15"),
  ("orig", "1.16"),
  ("orig", "1.17"),
  ("orig", "1.18"),
  ("new", "fade-to-black"),
  ("orig", "1.19"),
  ("orig", "1.20"),
  ("new", "slow-breath"),
  ("new", "window-dawn"),
]

# --- Chapters 2–10: 20 transition panels each (interleaved before originals) ---
CH_TRANSITIONS: dict[int, list[dict]] = {
  2: [
    {
      "title": "Morning Crosswalk",
      "scene": f"**Ethan Hyun** at crosswalk. White gear backpack. Light traffic. Kwon's direction ahead.",
      "prompt": f"{ETHAN_CASUAL} waiting at suburban crosswalk morning light headphones around neck quiet determination, STYLE: KWONS",
    },
    {
      "title": "Slowing Near Sign",
      "scene": "Ethan slows as Kwon's Taekwondo sign comes into view. Steps shorten.",
      "prompt": f"teen boy slowing walk Kwon's taekwondo academy sign coming into view street level {ETHAN_CASUAL}, STYLE: KWONS",
    },
    {
      "title": "Reading Sign Exterior",
      "scene": "Close on sign — clean logo, hours, no Prime branding. Ethan reads from sidewalk.",
      "dialogue": "Ethan (internal): *Different name. Different air.*",
      "prompt": "Kwon's taekwondo academy exterior sign close-up clean logo warm wood trim no Prime branding observer silhouette below, STYLE: KWONS",
    },
    {
      "title": "Stepping Back From Window",
      "scene": "Ethan steps back from dojang glass after peeking — breath visible. Decision pause.",
      "prompt": f"{ETHAN_CASUAL} stepping back from dojang window hands in hoodie pocket hesitant exhale warm interior glow reflection, STYLE: KWONS",
    },
    {
      "title": "Second Door Approach",
      "scene": "Ethan approaches entrance again — headphones now around neck. Hand rises to handle.",
      "prompt": f"teen approaching dojang door second time {ETHAN_CASUAL} hand reaching door handle threshold moment warm light leak, STYLE: KWONS",
    },
    {
      "title": "Foyer Entry Walk",
      "scene": "Ethan walks through small foyer — shoe racks, bulletin board, quiet.",
      "prompt": f"{ETHAN_CASUAL} walking small dojang foyer shoe racks bulletin board clean quiet atmosphere, STYLE: KWONS",
    },
    {
      "title": "Hallway to Shoe Rack",
      "scene": "Short hallway. Ethan spots shoe cubbies. Pauses at Prime-habit speed.",
      "prompt": f"{ETHAN_CASUAL} short hallway approaching shoe cubby wall pausing old habit tension, STYLE: KWONS",
    },
    {
      "title": "Walking to Wall Spot",
      "scene": "Ethan walks to open wall space — not on mat yet. Bag down. Observing.",
      "prompt": f"{ETHAN_CASUAL} setting white gear backpack against wall watching class from edge not on mat yet, STYLE: KWONS",
    },
    {
      "title": "Glance at Restroom Door",
      "scene": "Ethan glances at changing room door — dobok inside bag. Not ready yet.",
      "prompt": f"{ETHAN_CASUAL} glance at changing room door gear bag at feet hesitation quiet dojang background, STYLE: KWONS",
    },
    {
      "title": "Shifting Weight at Cubbies",
      "scene": "Ethan shifts weight at cubbies — MV drilling in background blur.",
      "prompt": f"{ETHAN_CASUAL} shifting weight near shoe cubbies {MV} coaching blurred background warm floor light, STYLE: KWONS",
    },
    {
      "title": "Following MV Gesture",
      "scene": "MV subtle gesture — *you can sit there*. Ethan nods micro, moves.",
      "prompt": f"{MV} subtle welcoming gesture toward wall spot {ETHAN_CASUAL} small nod moving to sit respectful distance, STYLE: KWONS",
    },
    {
      "title": "Sunset Light Shift",
      "scene": "Golden hour light crawls across mat. Class time passing. Ethan still watching.",
      "prompt": "dojang wooden floor sunset light band moving across mat time passage warm amber student training silhouette, STYLE: KWONS",
    },
    {
      "title": "Student File Past",
      "scene": "Student files past Ethan — polite nod. Ethan nods back — first social beat.",
      "prompt": f"dojang student walking past {ETHAN_CASUAL} polite nod exchange warm corridor light found-family seed, STYLE: KWONS",
    },
    {
      "title": "Class Ends — Ethan Stands",
      "scene": "Students bow out. Ethan stands when class ends — unsure if he should.",
      "prompt": f"students bowing out end of class {ETHAN_CASUAL} standing uncertain whether to join warm dojang, STYLE: KWONS",
    },
    {
      "title": "Exit Walk Stops",
      "scene": "Ethan walks toward exit — stops mid-step. Hand on bag strap.",
      "dialogue": "Ethan (internal): *…*",
      "prompt": f"{ETHAN_CASUAL} walking toward dojang exit stopping mid-step hand on backpack strap threshold indecision, STYLE: KWONS",
    },
    {
      "title": "Looking Back at Mat",
      "scene": "Ethan looks back at empty mat — MV rolling shoulders. Quiet.",
      "prompt": f"{ETHAN_CASUAL} looking back at empty training mat {MV} rolling shoulders end of day quiet emotional beat, STYLE: KWONS",
    },
    {
      "title": "MV Rolling Mat",
      "scene": "MV rolls mat in background. Ethan still at door. Unspoken permission to stay.",
      "prompt": f"{MV} rolling up training mat background {ETHAN_CASUAL} silhouette at doorway golden hour light, STYLE: KWONS",
    },
    {
      "title": "Street Outside Golden Hour",
      "scene": "Kwon's exterior — golden hour. Ethan exits small in frame.",
      "prompt": "Kwon's taekwondo academy exterior golden hour street warm light small teen exiting doorway peaceful suburban, STYLE: KWONS",
    },
    {
      "title": "Sidewalk Pause",
      "scene": "Ethan pauses on sidewalk. Looks back at dojang window glow.",
      "prompt": f"{ETHAN_CASUAL} pausing on sidewalk looking back at glowing dojang window evening peaceful expression, STYLE: KWONS",
    },
    {
      "title": "Phone Buzz — Deep Breath",
      "scene": "Phone buzzes — Ethan ignores. Deep breath. Hint of next day.",
      "dialogue": "Ethan (internal): *Tomorrow.*",
      "prompt": f"{ETHAN_CASUAL} phone buzzing in pocket ignored deep breath evening street soft sky tomorrow hint, STYLE: KWONS",
    },
  ],
  3: [
    {
      "title": "Silver Belt Close",
      "scene": "Close on **Ethan Hyun's** silver-letter black belt — before MV approaches.",
      "prompt": f"close-up silver-letter black belt on white dobok waist {ETHAN_DOBOK} hands at sides dojang floor, STYLE: KWONS",
    },
    {
      "title": "MV Crossing Mat",
      "scene": f"{MV} crosses mat toward Ethan — unhurried. Other students quiet.",
      "prompt": f"{MV} walking across wooden mat toward teen student other students quiet watching warm light, STYLE: KWONS",
    },
    {
      "title": "Mirroring Bow Distance",
      "scene": "Ethan mirrors bow distance — formal. MV matches. Respect established.",
      "prompt": f"{ETHAN_DOBOK} and {MV} bowing at respectful distance formal introduction mirror symmetry, STYLE: KWONS",
    },
    {
      "title": "Changing Room Door",
      "scene": "Ethan at changing room door — hand on frame. Dobok inside now.",
      "prompt": f"{ETHAN_CASUAL} hand on changing room door frame white dobok visible inside decision moment, STYLE: KWONS",
    },
    {
      "title": "Dobok Tie Hands",
      "scene": "Close — Ethan's hands tying dobok belt. Silver letters visible.",
      "prompt": f"close-up hands tying white dobok belt silver lettering {ETHAN_DOBOK} changing room mirror edge, STYLE: KWONS",
    },
    {
      "title": "Return to Main Mat",
      "scene": "Ethan walks back to main mat — dobok on. MV nods once.",
      "prompt": f"{ETHAN_DOBOK} walking back to main training mat {MV} single approving nod warm dojang, STYLE: KWONS",
    },
    {
      "title": "First Step on Mat",
      "scene": "Close-up — Ethan's bare foot on wood. First official step on Kwon's mat.",
      "prompt": f"close-up bare foot stepping onto polished wooden dojang mat first step {ETHAN_DOBOK} symbolic beat, STYLE: KWONS",
    },
    {
      "title": "Class Circle Wide",
      "scene": "Wide — class in loose circle. Ethan at assigned edge. MV center.",
      "prompt": f"wide shot dojang class loose circle formation {MV} center {ETHAN_DOBOK} at edge attentive warm light, STYLE: KWONS",
    },
    {
      "title": "MV Pointing Lane",
      "scene": "MV points to training lane. Ethan watches direction.",
      "prompt": f"{MV} pointing to marked training lane {ETHAN_DOBOK} watching attentive coaching gesture, STYLE: KWONS",
    },
    {
      "title": "Walking to Lane",
      "scene": "Ethan walks to assigned lane. Shoulders lower — slightly less guarded.",
      "prompt": f"{ETHAN_DOBOK} walking to assigned training lane shoulders relaxing slightly warm floor, STYLE: KWONS",
    },
    {
      "title": "Feet on Tape Marks",
      "scene": "Ethan's feet on floor tape marks. Stance setup.",
      "prompt": f"close-up feet on dojang floor tape marks fighting stance setup {ETHAN_DOBOK} precise foot placement, STYLE: KWONS",
    },
    {
      "title": "Student Passing Nod",
      "scene": "Another student passes — small nod. Ethan returns it.",
      "prompt": f"dojang student passing nod {ETHAN_DOBOK} returning nod brief friendly exchange background class, STYLE: KWONS",
    },
    {
      "title": "MV Demo Kick — Ethan Watches",
      "scene": "MV demonstrates kick — clean chamber. Ethan watches eyes tracking.",
      "prompt": f"{MV} demonstrating roundhouse kick clean chamber {ETHAN_DOBOK} watching intently tracking movement teaching moment, STYLE: KWONS",
    },
    {
      "title": "Slow Chamber Copy",
      "scene": "Ethan copies chamber — deliberately slow. MV observes without interrupting.",
      "prompt": f"{ETHAN_DOBOK} copying kick chamber slowly deliberate form {MV} observing patient coaching distance, STYLE: KWONS",
    },
    {
      "title": "Sweat Towel Beat",
      "scene": "Ethan wipes sweat with towel. First real exertion at Kwon's.",
      "prompt": f"{ETHAN_DOBOK} wiping sweat with small towel first training exertion tired satisfied micro-expression, STYLE: KWONS",
    },
    {
      "title": "Water Fountain Walk",
      "scene": "Ethan walks to water fountain — hallway quiet. Breath steady.",
      "prompt": f"{ETHAN_DOBOK} walking to hallway water fountain short break steady breathing dojang corridor, STYLE: KWONS",
    },
    {
      "title": "Bench Rest",
      "scene": "Ethan on bench rest — water bottle. Watching class through doorway.",
      "prompt": f"{ETHAN_DOBOK} sitting bench rest water bottle watching class through doorway warm light, STYLE: KWONS",
    },
    {
      "title": "MV Approaching Again",
      "scene": "MV approaches again — crouches to Ethan's eye level.",
      "prompt": f"{MV} approaching crouching to teen eye level kind expression {ETHAN_DOBOK} listening respectful, STYLE: KWONS",
    },
    {
      "title": "Evening Long Shadows",
      "scene": "Evening — longer shadows on mat. Class winding down.",
      "prompt": "dojang wooden floor long evening shadows class winding down warm amber window light time passage, STYLE: KWONS",
    },
    {
      "title": "Last Bow Out Walk",
      "scene": "Ethan bows out with class — walks to changing room. Lighter step.",
      "prompt": f"{ETHAN_DOBOK} bowing out with class walking toward changing room lighter step end of session, STYLE: KWONS",
    },
  ],
  4: [
    {
      "title": "Glove Wrap Hands",
      "scene": "Close — Ethan wrapping hands for pad work. Focused.",
      "prompt": f"close-up wrapping hands for pad work tape {ETHAN_DOBOK} focused expression preparation beat, STYLE: KWONS",
    },
    {
      "title": "Walking to Pad Lane",
      "scene": "Ethan walks to pad lane — MV already turning with mitts.",
      "prompt": f"{ETHAN_DOBOK} walking to pad training lane {MV} turning with focus mitts ready coaching setup, STYLE: KWONS",
    },
    {
      "title": "MV Holding Pads Approach",
      "scene": "MV holds pads at perfect height. Ethan squares shoulders.",
      "prompt": f"{MV} holding focus mitts at proper height {ETHAN_DOBOK} squaring shoulders ready stance coaching intimacy, STYLE: KWONS",
    },
    {
      "title": "Reset Walk Between Combos",
      "scene": "Reset between combos — Ethan walks two steps back. Breath control.",
      "prompt": f"{ETHAN_DOBOK} stepping back between combo resets controlled breathing {MV} waiting patient pads down, STYLE: KWONS",
    },
    {
      "title": "Shield Pickup",
      "scene": "Ethan picks up kicking shield — weight familiar from Prime, context different.",
      "prompt": f"{ETHAN_DOBOK} picking up large kicking shield familiar weight new peaceful dojang context, STYLE: KWONS",
    },
    {
      "title": "Rotation Wait Turn",
      "scene": "Class rotation — Ethan waits turn against wall. Watching senior.",
      "prompt": f"{ETHAN_DOBOK} waiting against wall during class rotation watching senior student train attentive, STYLE: KWONS",
    },
    {
      "title": "Watching Senior Kick",
      "scene": "Senior student kicks — clean snap. Ethan files movement.",
      "prompt": f"senior student clean snapping kick demo {ETHAN_DOBOK} watching from sideline studying form, STYLE: KWONS",
    },
    {
      "title": "Back to Pads Focus",
      "scene": "Back to pads — Ethan's eyes narrow. Focus returns.",
      "prompt": f"{ETHAN_DOBOK} returning to focus mitts intense eyes narrow ready stance {MV} holding pads, STYLE: KWONS",
    },
    {
      "title": "Mat Scuff Detail",
      "scene": "Close — mat scuff from pivot. Evidence of real work.",
      "prompt": "close-up wooden dojang mat scuff mark from pivot foot training wear detail authentic practice, STYLE: KWONS",
    },
    {
      "title": "MV Nod Continue",
      "scene": "MV nods — *continue*. Ethan chambers again.",
      "prompt": f"{MV} nodding continue gesture {ETHAN_DOBOK} chambering kick again coaching rhythm trust building, STYLE: KWONS",
    },
    {
      "title": "Electronic Hogu Door Peek",
      "scene": "Ethan peeks into electronic hogu room — sensors on wall.",
      "dialogue": "MV (O.S.): \"Sport mind stays with you.\"",
      "prompt": f"{ETHAN_DOBOK} peeking into electronic hogu training room sensors on wall curious respectful, STYLE: KWONS",
    },
    {
      "title": "Walking to Sensor Zone",
      "scene": "Ethan walks to sensor zone — one practice kick. Light registers.",
      "prompt": f"{ETHAN_DOBOK} walking to electronic scoring sensor zone practice kick light registering sport training, STYLE: KWONS",
    },
    {
      "title": "Return to Main Mat",
      "scene": "Ethan returns to main mat — MV already resetting shields.",
      "prompt": f"{ETHAN_DOBOK} walking back to main mat {MV} resetting kicking shields background routine coaching, STYLE: KWONS",
    },
    {
      "title": "Cool Down Perimeter Walk",
      "scene": "Cool down — Ethan walks mat perimeter. Slow steps.",
      "prompt": f"{ETHAN_DOBOK} cool down walking dojang mat perimeter slow steps relaxed shoulders, STYLE: KWONS",
    },
    {
      "title": "Bow to MV Close",
      "scene": "Close — Ethan bows to MV. MV returns deeper bow.",
      "prompt": f"close-up mutual bow {ETHAN_DOBOK} and {MV} respectful deep formal gratitude moment, STYLE: KWONS",
    },
    {
      "title": "Gear Bag Zip",
      "scene": "Ethan zips gear bag — satisfied tired. Locker number visible.",
      "prompt": f"{ETHAN_CASUAL} zipping white gear backpack satisfied tired expression locker area end of training, STYLE: KWONS",
    },
    {
      "title": "Exit Mat Backward Bow",
      "scene": "Ethan exits mat with backward bow tradition — MV watches approving.",
      "prompt": f"{ETHAN_DOBOK} exiting mat backward bow tradition {MV} watching approving small smile warm light, STYLE: KWONS",
    },
    {
      "title": "Water Bottle Break",
      "scene": "Water bottle break — Ethan drinks. MV resets shields in background.",
      "prompt": f"{ETHAN_DOBOK} water bottle break drinking {MV} resetting kicking shields background end of pad session, STYLE: KWONS",
    },
    {
      "title": "MV Resetting Shields",
      "scene": "MV stacks shields against wall — class winding down.",
      "prompt": f"{MV} stacking kicking shields against wall class winding down {ETHAN_DOBOK} toweling off background, STYLE: KWONS",
    },
    {
      "title": "Hallway Bow Exit",
      "scene": "Ethan bows toward mat from hallway door — last look.",
      "prompt": f"{ETHAN_CASUAL} bowing toward training mat from hallway doorway last look respectful habit forming, STYLE: KWONS",
    },
  ],
  5: [
    {
      "title": "MV Question Silence Wide",
      "scene": "Wide — MV's question hangs. Ethan silent center frame.",
      "prompt": f"wide shot dojang {MV} asking question {ETHAN_DOBOK} silent center frame heavy emotional stillness, STYLE: KWONS",
    },
    {
      "title": "Staring at Floor Tiles",
      "scene": "Ethan staring at floor tiles — jaw tight.",
      "prompt": f"{ETHAN_DOBOK} staring down at wooden floor tiles jaw tight internal conflict close angle, STYLE: KWONS",
    },
    {
      "title": "Korea U20 Poster Glance",
      "scene": "Ethan glances at Korea U20 poster on wall — dream object.",
      "prompt": f"{ETHAN_DOBOK} glancing at Korea U20 taekwondo poster on dojang wall dream aspiration detail, STYLE: KWONS",
    },
    {
      "title": "Window City View",
      "scene": "Ethan at window — city view. MV small in reflection.",
      "prompt": f"{ETHAN_DOBOK} at dojang window city view reflection {MV} small behind thoughtful wide shot, STYLE: KWONS",
    },
    {
      "title": "Fist Unclench",
      "scene": "Close — Ethan's fist unclenches at window sill.",
      "prompt": f"close-up fist unclenching on window sill {ETHAN_DOBOK} emotional release decision forming, STYLE: KWONS",
    },
    {
      "title": "Enrollment Desk Walk",
      "scene": "Ethan walks to simple enrollment desk — papers ready.",
      "prompt": f"{ETHAN_DOBOK} walking to simple front desk enrollment papers ready small dojang office, STYLE: KWONS",
    },
    {
      "title": "Pen Hover",
      "scene": "Pen hovers over signature line — tremor stills.",
      "dialogue": "Ethan (internal): *Not small.*",
      "prompt": f"close-up pen hovering over enrollment signature line hand steadying {ETHAN_DOBOK} decisive moment, STYLE: KWONS",
    },
    {
      "title": "Signature Close-Up",
      "scene": "Signature close-up — Ethan Hyun. Ink wet.",
      "prompt": "close-up signing enrollment form signature Ethan Hyun wet ink simple paper warm desk light, STYLE: KWONS",
    },
    {
      "title": "Copy Paper Fold",
      "scene": "MV folds copy paper — hands Ethan his. Matter-of-fact kindness.",
      "prompt": f"{MV} folding enrollment copy handing to {ETHAN_DOBOK} matter-of-fact kindness simple ritual, STYLE: KWONS",
    },
    {
      "title": "Locker Number 14",
      "scene": "Locker number **14** — Ethan reads tag.",
      "prompt": f"locker number 14 tag close-up {ETHAN_CASUAL} reading assigned locker belonging beat, STYLE: KWONS",
    },
    {
      "title": "Empty Locker Open",
      "scene": "Ethan opens empty locker — echo inside metal.",
      "prompt": f"{ETHAN_CASUAL} opening empty gym locker echo inside metal new beginning space, STYLE: KWONS",
    },
    {
      "title": "Placing Silver Belt Inside",
      "scene": "Ethan places silver-letter belt inside locker — deliberate.",
      "prompt": f"{ETHAN_CASUAL} placing silver-letter black belt inside locker deliberate careful ritual belonging, STYLE: KWONS",
    },
    {
      "title": "Hallway Exit Night",
      "scene": "Hallway exit — night. Ethan walks toward door light.",
      "prompt": f"{ETHAN_CASUAL} walking dojang hallway toward exit door night interior warm hope, STYLE: KWONS",
    },
    {
      "title": "Streetlight Walk Home",
      "scene": "Streetlight walk — slower pace. Looking up.",
      "prompt": f"{ETHAN_CASUAL} walking home under streetlights slower pace looking up quiet hope night, STYLE: KWONS",
    },
    {
      "title": "Apartment Door Unlock",
      "scene": "Apartment door unlock — same keys, new chapter feeling.",
      "prompt": f"{ETHAN_CASUAL} unlocking apartment door keys in hand new chapter quiet hope expression, STYLE: KWONS",
    },
    {
      "title": "Kitchen Water Glass",
      "scene": "Kitchen — Ethan drinks water. Apartment still. Calmer than before.",
      "prompt": f"{ETHAN_CASUAL} drinking water glass kitchen apartment still calm evening domestic peace, STYLE: KWONS",
    },
    {
      "title": "Bed Stare Calmer",
      "scene": "Ethan on bed staring at ceiling — calmer than Ch 1 nightmare aftermath.",
      "dialogue": "Ethan (internal): *I said it out loud.*",
      "prompt": f"{ETHAN_BEDROOM} lying on bed staring ceiling calmer expression soft night light contrast chapter 1 trauma, STYLE: KWONS soft",
    },
    {
      "title": "Locker Door Close",
      "scene": "Locker door closes on silver belt — click. Belonging sealed.",
      "prompt": f"close-up locker door closing on silver-letter black belt inside click sound belonging sealed, STYLE: KWONS",
    },
    {
      "title": "Apartment Light Off",
      "scene": "Ethan flips apartment light off — hallway dark. Day done.",
      "prompt": f"{ETHAN_CASUAL} flipping apartment light switch off hallway going dark end of enrollment day, STYLE: KWONS soft",
    },
    {
      "title": "Dawn Without Alarm",
      "scene": "Dawn without alarm — Ethan wakes naturally. No gasp.",
      "prompt": f"dawn waking naturally no alarm {ETHAN_BEDROOM} calm eyes opening new routine hope, STYLE: KWONS soft",
    },
  ],
  6: [
    {
      "title": "MV Direct Question Close",
      "scene": "Close — MV's direct question. Kind eyes, no flinch.",
      "prompt": f"close-up {MV} direct kind question expression patient eyes no judgment coaching intimacy, STYLE: KWONS",
    },
    {
      "title": "Jaw Working",
      "scene": "Ethan's jaw working — words stuck.",
      "prompt": f"close-up {ETHAN_DOBOK} jaw clenching working words stuck internal struggle, STYLE: KWONS",
    },
    {
      "title": "Mat Edge Walk Slow",
      "scene": "Ethan walks mat edge slowly — fingers trail wall.",
      "prompt": f"{ETHAN_DOBOK} walking slowly along dojang mat edge fingers trailing wall heavy steps, STYLE: KWONS",
    },
    {
      "title": "Flash Trigger Doorway",
      "scene": "Doorway triggers flash — Prime logo ghost. Ethan flinches micro.",
      "prompt": f"doorway frame triggering memory {ETHAN_DOBOK} micro flinch Prime logo ghost overlay desaturated flash edge, STYLE: PRIME flash inset",
    },
    {
      "title": "Present Feet on Wood",
      "scene": "Present anchor — Ethan's feet on Kwon's wood. Solid.",
      "prompt": f"close-up feet planted on warm wooden dojang floor present anchor {ETHAN_DOBOK} grounding beat, STYLE: KWONS",
    },
    {
      "title": "Cleaning Bucket Walk",
      "scene": "Ethan carries cleaning bucket — MV hands him rag. Shared work.",
      "prompt": f"{ETHAN_DOBOK} carrying cleaning bucket {MV} handing rag shared dojang maintenance quiet bonding, STYLE: KWONS",
    },
    {
      "title": "Mop Stroke",
      "scene": "Mop stroke across mat — rhythmic. Conversation optional.",
      "prompt": f"{ETHAN_DOBOK} mopping wooden dojang mat rhythmic stroke {MV} nearby quiet companionship, STYLE: KWONS",
    },
    {
      "title": "Window Prime Logo Memory",
      "scene": "Window reflection — Prime logo memory overlay. Ethan blinks it away.",
      "prompt": f"dojang window reflection Prime logo memory overlay {ETHAN_DOBOK} blinking away returning to present, STYLE: PRIME flash inset",
    },
    {
      "title": "Phone Face Down Table",
      "scene": "Phone face-down on table — Prime spam incoming.",
      "prompt": "smartphone face-down on table Prime spam notifications vibrating ignored boundary setting, STYLE: KWONS",
    },
    {
      "title": "Spam Texts Blur",
      "scene": "Spam texts blur on screen edge before Ethan flips phone over.",
      "prompt": f"smartphone screen edge blurred Prime spam group texts {ETHAN_CASUAL} flipping phone face-down refusal, STYLE: PRIME soft",
    },
    {
      "title": "Apartment Quiet Wide",
      "scene": "Apartment wide — quiet. Ethan small on couch. City hum.",
      "prompt": f"wide shot small apartment quiet {ETHAN_CASUAL} on couch city hum evening solitude not lonely, STYLE: KWONS soft",
    },
    {
      "title": "Mirror Belt Ritual",
      "scene": "Mirror — Ethan ties belt. Same silver letters. Different home.",
      "prompt": f"{ETHAN_DOBOK} tying belt before mirror silver letters same belt different home ritual calm, STYLE: KWONS",
    },
    {
      "title": "Sleep Dark Room",
      "scene": "Dark room — Ethan asleep. No nightmare sweat.",
      "prompt": f"dark bedroom sleeping peacefully {ETHAN_BEDROOM} no sweat no nightmare soft blanket calm, STYLE: KWONS soft",
    },
    {
      "title": "Dawn Without Gasp",
      "scene": "Dawn light — Ethan wakes without gasp. Contrast Ch 1.",
      "prompt": f"dawn light waking gently {ETHAN_BEDROOM} no gasp no jolt calm eyes opening contrast chapter 1 nightmare, STYLE: KWONS soft",
    },
    {
      "title": "Morning Street Routine",
      "scene": "Morning street — Ethan walks to Kwon's. Routine forming.",
      "prompt": f"{ETHAN_CASUAL} morning walk to dojang routine forming familiar street peaceful determination, STYLE: KWONS",
    },
    {
      "title": "Dojang Key Jingle",
      "scene": "Close — keys jingle. Ethan opens door — early.",
      "prompt": f"close-up keys in hand opening dojang door early morning {ETHAN_CASUAL} responsible routine, STYLE: KWONS dawn",
    },
    {
      "title": "Lights Flip On",
      "scene": "Lights flip on — empty mat glow. Ethan exhales.",
      "prompt": f"{ETHAN_CASUAL} flipping on dojang lights empty mat glowing exhale ownership feeling, STYLE: KWONS dawn",
    },
    {
      "title": "Mat Straighten",
      "scene": "Ethan straightens mat corner — small care task.",
      "prompt": f"{ETHAN_DOBOK} straightening training mat corner small care task quiet pride, STYLE: KWONS",
    },
    {
      "title": "Window Rain Start",
      "scene": "Window — rain starts. Ethan watches without flinching.",
      "prompt": f"{ETHAN_DOBOK} watching rain begin on dojang window calm expression no trauma flinch, STYLE: KWONS",
    },
    {
      "title": "MV Arrives Nod",
      "scene": "MV arrives — nods at Ethan's work. No lecture.",
      "prompt": f"{MV} arriving nodding at straightened mat {ETHAN_DOBOK} slight proud nod exchange morning, STYLE: KWONS",
    },
  ],
  7: [
    {
      "title": "Young Ethan Doorway Flash",
      "scene": "**FLASH** — young Ethan in Prime doorway — excited. Smaller frame.",
      "prompt": "FLASH young Ethan Hyun excited smaller frame Prime dojang doorway enrollment day bright hopeful, STYLE: PRIME flashback",
    },
    {
      "title": "Present Flinch",
      "scene": "**PRESENT** — Ethan flinches at same door memory. MV steady beside.",
      "prompt": f"PRESENT {ETHAN_DOBOK} micro flinch at doorway memory {MV} steady beside grounding present, STYLE: KWONS",
    },
    {
      "title": "MV Breathing Demo",
      "scene": "MV demonstrates breathing — hand on own chest. Slow.",
      "prompt": f"{MV} demonstrating slow breathing hand on chest coaching calm {ETHAN_DOBOK} watching, STYLE: KWONS",
    },
    {
      "title": "Ethan Copying Inhale",
      "scene": "Ethan copies inhale — eyes closed. Shoulders drop.",
      "prompt": f"{ETHAN_DOBOK} copying breathing inhale eyes closed shoulders dropping release exercise, STYLE: KWONS",
    },
    {
      "title": "One-Step Slide Foot",
      "scene": "One-step drill — Ethan slides foot. Present focus.",
      "prompt": f"{ETHAN_DOBOK} one-step sparring drill sliding foot precise present focus {MV} guiding, STYLE: KWONS",
    },
    {
      "title": "Partner Shadow Imaginary",
      "scene": "Ethan practices against imaginary partner — shadow on mat.",
      "prompt": f"{ETHAN_DOBOK} practicing footwork shadow partner on wooden mat focused solitary drill, STYLE: KWONS",
    },
    {
      "title": "Flash Trophy Shelf Prime",
      "scene": "**FLASH** — Prime trophy shelf — young Ethan reflected in glass.",
      "prompt": "FLASH Prime dojang trophy shelf young Ethan Hyun reflection in glass early pride before neglect, STYLE: PRIME flashback",
    },
    {
      "title": "Present Fist Unclench Mat",
      "scene": "**PRESENT** — fist unclenches on mat. Ghost fading.",
      "prompt": f"PRESENT {ETHAN_DOBOK} fist unclenching on mat ghost memory fading warm light winning, STYLE: KWONS",
    },
    {
      "title": "Window Ledge Walk",
      "scene": "Ethan walks to window ledge — city traffic below.",
      "prompt": f"{ETHAN_DOBOK} walking to dojang window ledge city traffic below contemplative wide shot, STYLE: KWONS",
    },
    {
      "title": "City Traffic Below",
      "scene": "POV — traffic below. Scale. Ethan's small reflection.",
      "prompt": "POV city traffic below dojang window small teen reflection in glass contemplative scale shot, STYLE: KWONS",
    },
    {
      "title": "MV Hand on Shoulder",
      "scene": "MV hand on shoulder — brief. Ethan doesn't shrug off.",
      "prompt": f"{MV} hand on shoulder brief supportive gesture {ETHAN_DOBOK} accepting not shrugging off, STYLE: KWONS",
    },
    {
      "title": "Ethan Minimal Nod",
      "scene": "Ethan minimal nod — gratitude without words.",
      "prompt": f"close-up {ETHAN_DOBOK} minimal nod quiet gratitude no words emotional beat, STYLE: KWONS",
    },
    {
      "title": "Bow Together",
      "scene": "Ethan and MV bow together — matched depth.",
      "prompt": f"{ETHAN_DOBOK} and {MV} bowing together matched depth mutual respect flashback session close, STYLE: KWONS",
    },
    {
      "title": "Ghost Flash Fade",
      "scene": "Prime ghost flash fades — trophy shelf dissolves to Kwon's wood.",
      "prompt": "Prime trophy flash dissolving into warm Kwon's wooden floor ghost memory fading transition, STYLE: PRIME to KWONS",
    },
    {
      "title": "Present Color Warmer",
      "scene": "Present frame warms — amber returns. Ethan exhales.",
      "prompt": f"{ETHAN_DOBOK} present frame warming amber light returning exhale relief after flashback, STYLE: KWONS",
    },
    {
      "title": "Class Joins Wide",
      "scene": "Wide — class resumes. Ethan in line. Not sidelined.",
      "prompt": f"wide shot class training line {ETHAN_DOBOK} included not sidelined warm dojang community, STYLE: KWONS",
    },
    {
      "title": "Partner Bow Exchange",
      "scene": "Partner bow exchange — Ethan included.",
      "prompt": f"{ETHAN_DOBOK} bowing with training partner included exchange respectful class rhythm, STYLE: KWONS",
    },
    {
      "title": "MV Counts Combo",
      "scene": "MV counts combo — Ethan keeps pace.",
      "prompt": f"{MV} counting combination {ETHAN_DOBOK} keeping pace focused training flow, STYLE: KWONS",
    },
    {
      "title": "Sunset Bow Out",
      "scene": "Sunset bow out — Ethan last to rise. Slower, not excluded.",
      "prompt": f"sunset class bow out {ETHAN_DOBOK} last to rise slower not excluded warm light, STYLE: KWONS",
    },
    {
      "title": "Street Peace After Flash",
      "scene": "Street outside — Ethan walks peaceful. Flash session digested.",
      "prompt": f"{ETHAN_CASUAL} walking evening street peaceful expression after heavy flashback session, STYLE: KWONS",
    },
  ],
  8: [
    {
      "title": "Hospital Elevator Numbers",
      "scene": "Elevator numbers climb — Ethan watches floor indicator.",
      "prompt": f"{ETHAN_CASUAL} watching hospital elevator floor numbers climb tense quiet fluorescent, STYLE: PRIME soft",
    },
    {
      "title": "Hall Walk to Room",
      "scene": "Ethan walks hall to room — shoes quiet on linoleum.",
      "prompt": f"{ETHAN_CASUAL} walking hospital corridor toward room quiet linoleum long hallway soft dread, STYLE: PRIME soft",
    },
    {
      "title": "Hand Sanitizer Stop",
      "scene": "Hand sanitizer dispenser — Ethan pauses, pumps twice.",
      "prompt": f"{ETHAN_CASUAL} pausing at hospital hand sanitizer dispenser pumping twice ritual delay, STYLE: PRIME soft",
    },
    {
      "title": "Door Half Open",
      "scene": "Room door half open — warm light inside. Ethan hesitates.",
      "prompt": f"hospital room door half open warm light inside {ETHAN_CASUAL} hesitating threshold emotional, STYLE: PRIME soft",
    },
    {
      "title": "Chair Scrape Sit",
      "scene": "Chair scrape — Ethan sits bedside. Small in room.",
      "prompt": f"{ETHAN_CASUAL} pulling chair scraping sitting bedside small figure hospital room gentle, STYLE: PRIME soft",
    },
    {
      "title": "Bedside Table Flowers",
      "scene": "Bedside table — flowers, water cup. Domestic detail in clinical space.",
      "prompt": "hospital bedside table flowers water cup domestic detail clinical room soft focus background, STYLE: PRIME soft",
    },
    {
      "title": "Window Rain Streak",
      "scene": "Window — rain streak. Ethan's reflection layered on glass.",
      "prompt": f"hospital window rain streaks {ETHAN_CASUAL} reflection layered on glass melancholy wide, STYLE: PRIME soft",
    },
    {
      "title": "Phone Buzz Pocket",
      "scene": "Phone buzzes in pocket — Ethan stiffens. Doesn't look yet.",
      "prompt": f"{ETHAN_CASUAL} phone buzzing in pocket stiffening not looking yet hospital bedside tension, STYLE: PRIME soft",
    },
    {
      "title": "Voicemail Waveform",
      "scene": "Phone screen — voicemail waveform. Ttong Kim name visible.",
      "prompt": "smartphone voicemail waveform playing threatening message screen glow Ethan hand tense hospital, STYLE: PRIME",
    },
    {
      "title": "Delete Confirm Thumb",
      "scene": "Delete confirm — thumb hovers, then taps.",
      "dialogue": "Ethan (internal): *Not today.*",
      "prompt": f"close-up thumb hovering delete voicemail confirm button {ETHAN_CASUAL} decisive tap hospital, STYLE: PRIME soft",
    },
    {
      "title": "Nurse Shadow Pass",
      "scene": "Nurse shadow passes doorway — Ethan glances, returns to grandmother.",
      "prompt": f"nurse shadow passing hospital doorway {ETHAN_CASUAL} glancing back to grandmother bedside, STYLE: PRIME soft",
    },
    {
      "title": "Hallway Bench Alone",
      "scene": "Hallway bench — Ethan sits alone after room visit. Head down.",
      "prompt": f"{ETHAN_CASUAL} sitting alone hospital hallway bench head down exhausted grief quiet, STYLE: PRIME soft",
    },
    {
      "title": "Bus Stop Wait",
      "scene": "Bus stop — Ethan waits. Rain on hood.",
      "prompt": f"{ETHAN_CASUAL} waiting at bus stop rain on hoodie hood evening city melancholy, STYLE: PRIME soft to KWONS",
    },
    {
      "title": "Rain on Hood",
      "scene": "Close — raindrops on hood fabric. Breath fog.",
      "prompt": f"close-up raindrops on hoodie fabric breath fog {ETHAN_CASUAL} cold evening detail shot, STYLE: PRIME soft",
    },
    {
      "title": "Kwon's Text Glow",
      "scene": "Phone glow — text from MV at Kwon's. Warm notification tone.",
      "prompt": f"smartphone screen glow kind text message from Master Viet warm notification {ETHAN_CASUAL} rain background, STYLE: KWONS soft",
    },
    {
      "title": "Reply Thumb Hover",
      "scene": "Reply thumb hovers — small smile trying.",
      "prompt": f"close-up thumb hovering over reply send button {ETHAN_CASUAL} small smile forming rain bus stop, STYLE: KWONS soft",
    },
    {
      "title": "Send Small Smile Lost",
      "scene": "Send — smile fades to tired. Message sent.",
      "prompt": f"{ETHAN_CASUAL} sending text small smile fading to tired relief message sent bus stop rain, STYLE: KWONS soft",
    },
    {
      "title": "Bus Arrival Lights",
      "scene": "Bus arrival lights — Ethan boards. Chapter exhale.",
      "prompt": f"city bus arrival lights {ETHAN_CASUAL} boarding rain evening transition exhale, STYLE: PRIME soft to KWONS",
    },
    {
      "title": "Apartment Window Night",
      "scene": "Apartment window night — Ethan home. City lights bokeh.",
      "prompt": f"apartment window night {ETHAN_CASUAL} silhouette city lights bokeh exhausted safe home, STYLE: KWONS soft",
    },
    {
      "title": "Hospital Exit Wide Dawn",
      "scene": "Wide — hospital exterior dawn breaking. Small figure leaving.",
      "dialogue": "*(none — transition)*",
      "prompt": "wide shot hospital exterior dawn breaking small teen figure leaving transition hope hard week continues, STYLE: PRIME soft to KWONS dawn",
    },
  ],
  9: [
    {
      "title": "MV Answer Gentle",
      "scene": "MV answers gently — open hands. Ethan listens.",
      "prompt": f"{MV} answering gently open hands kind expression {ETHAN_DOBOK} listening hopeful, STYLE: KWONS",
    },
    {
      "title": "Phone Unlock",
      "scene": "Ethan unlocks phone — contact list scroll begins.",
      "prompt": f"{ETHAN_DOBOK} unlocking smartphone beginning contact scroll nervous hope, STYLE: KWONS",
    },
    {
      "title": "Prime Names Scroll",
      "scene": "Contact list — Prime names scroll. Old team.",
      "prompt": "smartphone contact list scrolling Prime taekwondo team names old connections emotional weight, STYLE: PRIME soft",
    },
    {
      "title": "Group Chat Icon",
      "scene": "Group chat icon — cursor/thumb hovers. MV nods background.",
      "prompt": f"smartphone group chat icon hover {MV} nodding background {ETHAN_DOBOK} nervous invitation moment, STYLE: KWONS",
    },
    {
      "title": "Typing Bubble",
      "scene": "Typing bubble — message draft to team.",
      "dialogue": "Ethan (typing): \"Practice at Kwon's Saturday…\"",
      "prompt": f"smartphone typing message bubble draft invitation {ETHAN_DOBOK} focused screen glow, STYLE: KWONS",
    },
    {
      "title": "Send Arrow Tap",
      "scene": "Send arrow tap — message gone. Ethan holds breath.",
      "prompt": f"close-up send arrow tap smartphone message sent {ETHAN_DOBOK} holding breath anticipation, STYLE: KWONS",
    },
    {
      "title": "Waiting Clock Wall",
      "scene": "Wall clock — waiting. Phone face up — no replies yet.",
      "prompt": f"dojang wall clock waiting {ETHAN_DOBOK} phone face up no replies yet anxious patience, STYLE: KWONS",
    },
    {
      "title": "MV Preparing Mats Early",
      "scene": "MV preparing mats early — alone. Dawn light.",
      "prompt": f"{MV} preparing training mats early morning alone dawn light through windows dedication, STYLE: KWONS dawn",
    },
    {
      "title": "Ethan Early Street Walk",
      "scene": "Ethan early walk on street — same route, lighter step.",
      "prompt": f"{ETHAN_CASUAL} early morning street walk to dojang lighter step anticipation, STYLE: KWONS dawn",
    },
    {
      "title": "Key Turn Door",
      "scene": "Key turn — dojang door. Ethan first inside.",
      "prompt": f"{ETHAN_CASUAL} turning key opening dojang door early arrival first inside dawn, STYLE: KWONS dawn",
    },
    {
      "title": "Lights Flip On",
      "scene": "Lights flip on — empty mat. Team day approaching.",
      "prompt": "dojang lights flipping on empty training mat team day approaching wide dawn shot, STYLE: KWONS dawn",
    },
    {
      "title": "Mat Layout Straighten",
      "scene": "Ethan straightens mat layout — parallel lines.",
      "prompt": f"{ETHAN_DOBOK} straightening mat layout parallel lines responsible preparation team day, STYLE: KWONS dawn",
    },
    {
      "title": "Text Reply Vibration",
      "scene": "Phone vibrates — reply incoming. Ethan's eyes widen micro.",
      "prompt": f"smartphone vibration reply notification {ETHAN_DOBOK} eyes widening micro hope team response, STYLE: KWONS",
    },
    {
      "title": "Ariana Typing Finally",
      "scene": "Screen — Ariana typing indicator finally appears.",
      "prompt": "smartphone screen Ariana typing indicator finally appearing group chat hope beat, STYLE: KWONS",
    },
    {
      "title": "Ethan Small Exhale",
      "scene": "Ethan small exhale — shoulders drop. Not alone.",
      "prompt": f"{ETHAN_DOBOK} small exhale shoulders dropping relief not alone anymore emotional beat, STYLE: KWONS",
    },
    {
      "title": "Replies Flood Montage",
      "scene": "Montage hint — multiple reply bubbles stacking.",
      "prompt": "smartphone montage multiple reply bubbles stacking team responses warming screen glow, STYLE: KWONS",
    },
    {
      "title": "MV Over Shoulder Check",
      "scene": "MV over shoulder — checks Ethan's face. Small proud nod.",
      "prompt": f"{MV} over shoulder checking {ETHAN_DOBOK} face small proud nod mentor approval, STYLE: KWONS",
    },
    {
      "title": "Evening Gear Prep",
      "scene": "Evening — Ethan lays out extra guest gear. Anticipation.",
      "prompt": f"{ETHAN_DOBOK} laying out extra guest training gear evening anticipation team visit prep, STYLE: KWONS",
    },
    {
      "title": "Night Before Window",
      "scene": "Night before — Ethan at window. Street quiet.",
      "dialogue": "Ethan (internal): *They might come.*",
      "prompt": f"{ETHAN_CASUAL} at apartment window night before team day quiet street reflective hope, STYLE: KWONS soft",
    },
    {
      "title": "Dawn Team Day Hint Wide",
      "scene": "Dawn wide — dojang exterior. Team day hint. Caption space.",
      "prompt": "wide shot Kwon's dojang exterior dawn team day approaching hopeful golden light caption space, STYLE: KWONS dawn",
    },
  ],
  10: [
    {
      "title": "Parking Lot Arrivals Montage",
      "scene": "Parking lot — multiple arrivals montage walk. Saturday morning.",
      "prompt": "suburban dojang parking lot Saturday morning multiple arrivals montage teens approaching warm light, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "TJ Door Open Grin",
      "scene": "**TJ Lim** — door open grin. Teal headband. Energy spike.",
      "prompt": "TJ Lim teen boy teal headband cheerful grin opening dojang door energetic entrance, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Kieryn Mat Toe Test",
      "scene": "**Kieryn Lim** tests mat with toe — teal-purple bob. Critical eye.",
      "prompt": "Kieryn Lim teen girl teal purple bob hair testing wooden mat with toe critical expression, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Logan Snack Bag",
      "scene": "**Logan Hyun** — snack bag already open. Bowl cut bounce.",
      "prompt": "Logan Hyun teen boy bowl cut hair snack bag open cheerful hungry expression dojang entrance, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Kian Shadow Box Air",
      "scene": "**Kian Sang** shadow boxes air — silver hair catch light.",
      "prompt": "Kian Sang teen boy silver white hair shadow boxing air confident entrance athletic, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Ariana Last Through Door",
      "scene": "**Ariana Yang** last through door — red streak bob. Scanning room.",
      "prompt": "Ariana Yang teen girl red streak bob hair last through dojang door scanning room guarded expression, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Ethan Introducing MV",
      "scene": "**Ethan Hyun** introduces **MV** to arriving team — small gesture.",
      "prompt": f"{ETHAN_DOBOK} introducing {MV} to arriving Prime teens team bridge gesture warm dojang, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Team Shoe Line",
      "scene": "Team shoe line — chaotic polite. Multiple pairs at cubbies.",
      "prompt": "teen taekwondo team shoes lined at cubby wall chaotic polite arrivals Saturday morning, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Stretch Row Formation",
      "scene": "Stretch row formation — uneven spacing. MV corrects one arm.",
      "prompt": f"team stretch row formation uneven spacing {MV} correcting one arm warm dojang group, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "MV Center Circle",
      "scene": "MV center circle — team around. Ethan opposite MV.",
      "prompt": f"{MV} center of team circle seven teens around {ETHAN_DOBOK} opposite mentor group formation, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Group Bow Low",
      "scene": "Group bow low — synchronized enough. Found-family chemistry.",
      "prompt": "seven teen taekwondo students group bow low synchronized enough found family chemistry, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "TJ Joke Whisper",
      "scene": "TJ whispers joke — Kieryn eye roll incoming.",
      "prompt": "TJ Lim whispering joke to teammate Kieryn Lim eye roll incoming comic beat team dynamic, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Kieryn Eye Roll",
      "scene": "Kieryn eye roll — tries not to smile.",
      "prompt": "Kieryn Lim eye roll trying not to smile sibling dynamic team stretch background, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Logan Stretch Wrong",
      "scene": "Logan stretches wrong — MV gentle correction.",
      "prompt": f"Logan Hyun stretching incorrectly {MV} gentle correction hand on shoulder comic team moment, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Kian Ethan Stare",
      "scene": "**Kian** and **Ethan** stare — rematch energy. Respect.",
      "prompt": f"Kian Sang and {ETHAN_DOBOK} eye lock rematch energy mutual respect team circle, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Ariana Corner Stretch",
      "scene": "Ariana corner stretch — alone in crowd. Ethan notices.",
      "prompt": f"Ariana Yang stretching alone in corner guarded {ETHAN_DOBOK} noticing team wide shot, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "MV Team Speech Wide",
      "scene": "MV team speech wide — hands open. Everyone listening.",
      "prompt": f"{MV} team speech wide shot hands open everyone listening Saturday welcome energy, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Team First Unified Bow",
      "scene": "Team first unified bow — Ethan slightly late. Logan stifles laugh.",
      "prompt": f"team first unified bow {ETHAN_DOBOK} slightly late Logan Hyun stifling laugh group sync, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Curiosity Not Pity Beat",
      "scene": "Faces — curiosity not pity. Ethan reads it.",
      "prompt": f"team teen faces curious not pitying {ETHAN_DOBOK} reading expressions found family seed, STYLE: KWONS HAIKYUU",
    },
    {
      "title": "Caption Wide Hero",
      "scene": "Wide hero — team on mat. Caption space. Arc 1 crescendo.",
      "prompt": "wide hero shot full team on dojang mat caption space arc finale crescendo warm golden light, STYLE: KWONS HAIKYUU",
    },
  ],
}

CHAPTER_NAMES = {
  1: "Nightmare",
  2: "Arrival at Kwon's",
  3: "Meeting MV",
  4: "Training",
  5: "The Goal",
  6: "Why Leave",
  7: "Flashbacks",
  8: "Hospital",
  9: "Can They Come",
  10: "Welcome",
}

OUTFIT_LOCK_TEMPLATE = """## Chapter 1 — Outfit Lock *(copy into every Ch 1 prompt)*

| Context | Character | Locked look |
|---------|-----------|-------------|
| **Tournament day** (1.2–1.18 present) | **Ethan Hyun** | 15 · 5'3" · dark blue shadow perm hair · brown eyes · **full Olympic kyorugi kit:** white dobok · electronic chest hogu · headgear · forearm/shin/foot guards · · black belt |
| **Tournament day** | **Ttong Kim** | 38 · 5'8" stocky · square face · **obvious underbite · teeth showing** · **Prime polo + tight black shorts + gold watch** |
| **Tournament day** | **Repeul Kim** | 37 · 5'5" overweight woman · **brown curly hair** · **ugly clashing multicolor casual** · mean sour scowl · **silent · edge of frame** |
| **Flash enrollment** (1.8) | Ttong + Repeul | Same as tournament street wear (polo/shorts · multicolor casual) |
| **Flash scrimmage** (1.12 top) | **Ethan Hyun** | White dobok · black belt · · forearm/shin guards · **no headgear** · Prime dojang |
| **Bedroom** (1.19–1.20) | **Ethan Hyun** | Grey sleep tee · messy dark blue hair · **gold headphones on nightstand** |
| **Ring opponent** | *(unnamed)* | Taller older Prime teen · **same full kyorugi kit as Ethan** |

**Rule:** Name every recurring character in the **Prompt** line. Attach ref sheet **front** view when batch-generating (Ethan `gear-front`, Ttong `shorts-front`, Repeul `casual-front`)."""


def parse_storyboard(text: str) -> tuple[str, dict[int, list[dict]]]:
  """Return preamble (before Ch 1) and panels keyed by chapter number."""
  text = text.replace("\r\n", "\n")
  lines = text.splitlines()
  ch1_match = CHAPTER_HEADER.match(lines[0] if lines else "")
  # Preamble ends before first `# Chapter 1`
  preamble_end = 0
  for i, line in enumerate(lines):
    m = CHAPTER_HEADER.match(line)
    if m and int(m.group(1)) == 1:
      preamble_end = i
      break
  preamble = "\n".join(lines[:preamble_end])
  if preamble_end and not preamble.endswith("\n"):
    preamble += "\n"

  chapters: dict[int, list[dict]] = {}
  current_ch: int | None = None
  current_panel: dict | None = None
  current_field: str | None = None
  in_prompt = False
  prompt_lines: list[str] = []

  def flush_panel() -> None:
    nonlocal current_panel, current_field, in_prompt, prompt_lines
    if current_panel is None or current_ch is None:
      return
    if prompt_lines:
      current_panel["fields"].append(("prompt", "\n".join(prompt_lines).strip()))
    chapters.setdefault(current_ch, []).append(current_panel)
    current_panel = None
    current_field = None
    in_prompt = False
    prompt_lines = []

  for line in lines[preamble_end:]:
    ch_m = CHAPTER_HEADER.match(line)
    if ch_m:
      flush_panel()
      current_ch = int(ch_m.group(1))
      continue

    pm = PANEL_HEADER.match(line)
    if pm:
      flush_panel()
      current_panel = {
        "old_id": pm.group(1),
        "title": pm.group(2).strip(),
        "fields": [],
      }
      continue

    if current_panel is None:
      continue

    if line.strip() == "**Prompt:**":
      in_prompt = True
      current_field = None
      continue

    if in_prompt:
      if line.strip().startswith("```"):
        if prompt_lines:
          in_prompt = False
        continue
      prompt_lines.append(line)
      continue

    fm = FIELD_LINE.match(line)
    if fm:
      key = fm.group(1).lower().replace(" ", "_")
      value = fm.group(2).strip()
      current_panel["fields"].append((key, value))
      current_field = key
      continue

    if current_field and line.strip() and not line.startswith("---"):
      # Continuation line for multi-line fields (rare)
      idx = len(current_panel["fields"]) - 1
      fk, fv = current_panel["fields"][idx]
      current_panel["fields"][idx] = (fk, f"{fv}\n{line.strip()}")

  flush_panel()
  return preamble, chapters


def panel_from_new(spec: dict) -> dict:
  fields: list[tuple[str, str]] = []
  for key in ("scene", "dialogue", "sfx", "timeline", "caption"):
    if key in spec and spec[key]:
      fields.append((key, spec[key]))
  for key in ("post_text", "script", "note"):
    if key in spec and spec[key]:
      fields.append((key, spec[key]))
  fields.append(("prompt", spec["prompt"]))
  return {"old_id": None, "title": spec["title"], "fields": fields}


def copy_original(panel: dict) -> dict:
  return {
    "old_id": panel["old_id"],
    "title": panel["title"],
    "fields": list(panel["fields"]),
  }


def expand_chapter_1(originals: list[dict]) -> list[dict]:
  by_id = {p["old_id"]: p for p in originals}
  expanded: list[dict] = []
  for kind, ref in CH1_SEQUENCE:
    if kind == "orig":
      if ref not in by_id:
        raise KeyError(f"Chapter 1 missing panel {ref}")
      expanded.append(copy_original(by_id[ref]))
    else:
      expanded.append(panel_from_new(CH1_NEW_PANELS[ref]))
  if len(expanded) != 40:
    raise ValueError(f"Chapter 1 expansion produced {len(expanded)} panels, expected 40")
  return expanded


def expand_chapter_interleaved(chapter: int, originals: list[dict]) -> list[dict]:
  transitions = CH_TRANSITIONS[chapter]
  if len(originals) != 20:
    raise ValueError(f"Chapter {chapter} has {len(originals)} panels, expected 20")
  if len(transitions) != 20:
    raise ValueError(f"Chapter {chapter} transitions: {len(transitions)}, expected 20")
  expanded: list[dict] = []
  for i in range(20):
    expanded.append(panel_from_new(transitions[i]))
    expanded.append(copy_original(originals[i]))
  return expanded


def renumber_chapter(chapter: int, panels: list[dict]) -> list[dict]:
  for i, panel in enumerate(panels, start=1):
    panel["id"] = f"{chapter}.{i}"
  return panels


def format_field_key(key: str) -> str:
  mapping = {
    "scene": "Scene",
    "dialogue": "Dialogue",
    "sfx": "SFX",
    "timeline": "Timeline",
    "post_text": "Post text",
    "script": "Script",
    "note": "Note",
    "caption": "Caption",
  }
  return mapping.get(key, key.title())


def format_panel(panel: dict) -> str:
  lines = [f"### Panel {panel['id']} — {panel['title']}"]
  for key, value in panel["fields"]:
    if key == "prompt":
      continue
    lines.append(f"**{format_field_key(key)}:** {value}")
  lines.append("")
  lines.append("**Prompt:**")
  lines.append("```")
  prompt = next((v for k, v in panel["fields"] if k == "prompt"), "")
  lines.append(prompt)
  lines.append("```")
  lines.append("")
  lines.append("---")
  return "\n".join(lines)


def format_chapter_section(chapter: int, panels: list[dict], outfit_lock: str | None = None) -> str:
  name = CHAPTER_NAMES[chapter]
  parts = [f"# Chapter {chapter} — {name}", ""]
  if outfit_lock:
    parts.append(outfit_lock.rstrip())
    parts.append("")
    parts.append("---")
    parts.append("")
  for panel in panels:
    parts.append(format_panel(panel))
  return "\n".join(parts).rstrip() + "\n"


def extract_ch1_outfit_lock(text: str) -> str:
  """Extract outfit lock block from existing Ch 1 section, or use template."""
  normalized = text.replace("\r\n", "\n")
  start = normalized.find("## Chapter 1 — Outfit Lock")
  if start == -1:
    return OUTFIT_LOCK_TEMPLATE
  end = normalized.find("---\n\n### Panel", start)
  if end == -1:
    return OUTFIT_LOCK_TEMPLATE
  return normalized[start:end].rstrip()


def update_outfit_lock(outfit_lock: str, id_map: dict[str, str], ch1_last_id: str) -> str:
  """Update panel range references in outfit lock table."""
  result = outfit_lock
  if "1.2" in id_map and "1.18" in id_map:
    result = re.sub(
      r"\(1\.2–1\.18 present\)",
      f"({id_map['1.2']}–{id_map['1.18']} present)",
      result,
    )
  if "1.8" in id_map:
    result = result.replace("(1.8)", f"({id_map['1.8']})")
  if "1.12" in id_map:
    result = result.replace("(1.12 top)", f"({id_map['1.12']} top)")
  if "1.19" in id_map:
    result = re.sub(
      r"\(1\.19–1\.20\)",
      f"({id_map['1.19']}–{ch1_last_id})",
      result,
    )
  return result


def build_ch1_id_map(panels: list[dict]) -> dict[str, str]:
  mapping: dict[str, str] = {}
  for panel in panels:
    if panel.get("old_id"):
      mapping[panel["old_id"]] = panel["id"]
  return mapping


def update_preamble(preamble: str, ch1_map: dict[str, str]) -> str:
  text = preamble
  continuity = (
    "4. **Character continuity:** Always use **canon names + locked outfit** in prompts "
    '(never generic "instructor" / "teen boy"). See **Chapter 1 — Outfit Lock** below and '
    "[STORYBOARD-GUIDE § Continuity](./STORYBOARD-GUIDE.md#panel-prompt-continuity)."
  )
  if "Character continuity" not in text:
    text = text.replace(
      "3. For dialogue, add text in your editor after generation — most AI tools render text poorly.\n",
      "3. For dialogue, add text in your editor after generation — most AI tools render text poorly.\n"
      f"{continuity}\n",
    )
    text = text.replace(
      "4. **Aspect ratio:**",
      "5. **Aspect ratio:**",
    )
    text = text.replace(
      "5. **Montage / flash clarity:**",
      "6. **Montage / flash clarity:**",
    )
  text = text.replace("`1.1` → `10.20`", "`1.1` → `10.40`")
  text = text.replace("in order (`1.1` → `10.20`)", "in order (`1.1` → `10.40`)")
  if "1.13b" in ch1_map:
    text = text.replace("**1.13b**", f"**{ch1_map['1.13b']}**")
  if "1.14" in ch1_map and "1.16" in ch1_map:
    text = re.sub(
      r"\*\*1\.14–1\.16\*\*",
      f"**{ch1_map['1.14']}–{ch1_map['1.16']}**",
      text,
    )
  if "1.8" in ch1_map and "1.12" in ch1_map:
    text = re.sub(
      r"\*\*1\.8–1\.12\*\*",
      f"**{ch1_map['1.8']}–{ch1_map['1.12']}**",
      text,
    )
  text = text.replace("203 panels", "400 panels")
  return text


def format_footer() -> str:
  return """---

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
"""


def expand_all(chapters: dict[int, list[dict]]) -> dict[int, list[dict]]:
  result: dict[int, list[dict]] = {}
  result[1] = renumber_chapter(1, expand_chapter_1(chapters[1]))
  for ch in range(2, 11):
    result[ch] = renumber_chapter(ch, expand_chapter_interleaved(ch, chapters[ch]))
  return result


def main() -> None:
  text = STORYBOARD.read_text(encoding="utf-8")
  preamble, chapters = parse_storyboard(text)
  outfit_lock = extract_ch1_outfit_lock(text)

  expanded = expand_all(chapters)
  ch1_map = build_ch1_id_map(expanded[1])
  outfit_lock = update_outfit_lock(outfit_lock, ch1_map, expanded[1][-1]["id"])
  preamble = update_preamble(preamble, ch1_map)

  parts = [preamble.rstrip(), ""]
  parts.append(format_chapter_section(1, expanded[1], outfit_lock))
  for ch in range(2, 11):
    parts.append(format_chapter_section(ch, expanded[ch]))
  parts.append(format_footer())

  STORYBOARD.write_text("\n".join(parts), encoding="utf-8")

  print(f"Wrote {STORYBOARD}")
  print("Panel counts per chapter:")
  total = 0
  for ch in range(1, 11):
    count = len(expanded[ch])
    total += count
    print(f" Chapter {ch}: {count} panels ({ch}.1–{ch}.{count})")
  print(f" Total: {total} panels")


if __name__ == "__main__":
  main()
