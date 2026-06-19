#!/usr/bin/env python3
"""Revise Arc 1 Ch1 opening: casual → dobok → full gear. Renumbers to 48 panels."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SB = ROOT / "storyboards" / "arc-01-panel-storyboard.md"

ETHAN = (
  "Ethan Hyun teen boy 15 korean-american 5 foot 3 lean long limbs dark blue Korean shadow perm hair "
  "slightly messy brown eyes soft jawline sharp eyes reserved K-pop visual expression"
)
CASUAL = "oversized black hoodie white undershirt black cargo pants white sneakers gold headphones white backpack NO dobok NO hogu"
DOBOK = "white WT dobok black belt with silver embroidery NO hogu yet"
KIT = (
  "white WT dobok black belt silver embroidery blue electronic hogu blue helmet white forearm guards "
  "white shin guards white foot protectors full Olympic kyorugi kit"
)

OUTFIT_LOCK = """## Chapter 1 — Outfit Lock *(copy into every Ch 1 prompt)*

| Phase | Panels | Ethan look |
|-------|--------|------------|
| **Casual arrival** | 1.1–1.5 | Oversized **black hoodie** · white undershirt · **black cargo pants** · white sneakers · **gold headphones** · **white backpack** · **no dobok / no hogu** |
| **Dobok change** | 1.6–1.7 | White **WT dobok** · **black belt w/ silver embroidery** · · changing area |
| **First full kit** | 1.8–1.14 | Dobok + **blue electronic hogu** + guards + **blue helmet** (mirror reveal **1.14**) |
| **Full kit (present)** | 1.15–1.46 | Same tournament kit as above — **SAME face/hair/kit** every panel |
| **Flash enrollment** | 1.27 | Ttong + Yeo Woo — polo/shorts · multicolor casual |
| **Flash scrimmage** | 1.31 top | White dobok · black belt · guards · **no headgear** · Prime dojang |
| **Bedroom** | 1.47–1.48 | Grey sleep tee · messy dark blue hair · gold headphones on nightstand · **NO dobok** |

| Character | Locked look |
|-----------|-------------|
| **Ttong Kim** | 38 · 5'8" stocky · underbite · **Prime polo + tight black shorts + gold watch** |
| **Yeo Woo Kim** | 37 · 5'5" · brown curly hair · **ugly multicolor casual** · scowl · silent edge of frame |
| **Ring opponent** | Taller older Prime teen · **same blue-hogu kit as Ethan** |

**Visual arc:** casual kid → dobok → athlete → neglected all day → KO → wake.

**Manhwa pages (for multi-panel generation):**
- **PAGE 1 — Arrival:** 1.1–1.8 · splash → van → walk → door reflection → hallway → change → belt → kit reveal
- **PAGE 2 — Preparation:** 1.9–1.16 · hogu → guards → helmet → mirror → warmup neglect
- **PAGE 3 — Isolation:** 1.17+ · gear check → bracket → bleachers → fight → wake

**Rule:** Name **Ethan Hyun** + phase-appropriate outfit in every **Prompt**. Ref: `reference-sheets/output/ethan-hyun/casual-front.png` (1.1–1.5) · `dobok-front.png` (1.6–1.7) · `gear-front.png` (1.8+).

---

## Chapter 1 — Manhwa page layouts *(optional batch gen)*

Use when generating **one PNG per page** (not one PNG per panel). Dialogue stays in HTML reader — **no text in art**.

### PAGE 1 — Arrival (panels 1.1–1.8)
Dynamic Solo Leveling layout · thin gutters · NO readable text.

| Row | Layout | Beats |
|-----|--------|-------|
| 1 | Tall splash ~38% | 1.1 venue · Ethan **casual silhouette** approaching |
| 2 | Wide | 1.2 Prime van · athletes with gear · Ethan **casual** exits last tired |
| 3 | 50\\|50 | 1.3 **casual** walk \\| 1.4 glass doors · **reflection casual** · inside athletes in **full gear** |
| 4 | Full | 1.5 hallway clock **7:00 AM** · Ethan **casual** carrying gear bag |
| 5 | 50\\|50 | 1.6 changing · dobok pants \\| 1.7 tight · tying **silver-embroidered** belt |
| 6 | Full wide | 1.8 **full kit reveal** — dobok · hogu under arm · helmet · toward warmup |

### PAGE 2 — Preparation (panels 1.9–1.16)
| Row | Layout | Beats |
|-----|--------|-------|
| 1–5 | Sequence / splits | 1.9 blue hogu · 1.10 forearms · 1.11 shins · 1.12 foot sensors · 1.13 helmet |
| 6 | Full | 1.14 **mirror** first full reveal |
| 7 | 50\\|50 | 1.15 warmup · coaches with kids \\| 1.16 **Ethan alone** — no coach · no advice |

### PAGE 3+ — Isolation
Continue panel-by-panel from **1.17** in storyboard below.

---
"""

NEW_OPENING = [
  ("1.1", "Title Card — Venue", "Black fade to tournament exterior. Banner: *Prime Taekwondo Sports Dynasty — Regional Open*. Small **Ethan Hyun** silhouette approaching — **casual clothes only**, no gear.", "", "*(none — silence)*", f"empty martial arts tournament venue exterior dawn overcast desaturated wide cinematic establishing shot small Ethan Hyun silhouette approaching entrance {CASUAL} NO gear visible moody banner taekwondo logos STYLE PRIME"),
  ("1.2", "Prime Van", "Prime team van in parking lot. Most athletes already carrying equipment. **Ethan Hyun** exits **last** — still **casual clothes**. Tired.", "", "", f"dawn parking lot Prime team van teens unloading taekwondo gear bags athletes in partial kit Ethan Hyun {ETHAN} {CASUAL} stepping down last tired expression overcast sky wide shot STYLE PRIME"),
  ("1.3", "Parking Walk", "**Ethan Hyun** walking toward venue with team. **Casual clothes**. Backpack. Headphones.", "", "", f"Ethan Hyun {ETHAN} {CASUAL} walking parking lot sidewalk toward tournament venue with Prime teens carrying gear bags dawn mist desaturated wide tracking shot STYLE PRIME"),
  ("1.4", "Door Reflection", "Automatic doors. **Reflection** in glass shows Ethan in **casual clothes**. Through glass: athletes inside in **full sparring gear**. Entering another world.", "Ethan (internal): *Here we go again.*", "", f"tournament venue automatic glass doors Ethan Hyun {ETHAN} {CASUAL} hesitating reflection in glass shows casual clothes interior visible athletes in full blue hogu kyorugi kit visual metaphor threshold emotional low angle STYLE PRIME"),
  ("1.5", "Hallway — Too Early", "Venue hallway. **Ethan still casual** — carrying gear bag. Wall clock **7:00 AM**. Other athletes in kit pass him.", 'Kid A: "Why are we here so early?"', "", f"tournament venue interior wall clock 7 AM Ethan Hyun {ETHAN} {CASUAL} carrying white gear backpack walking hallway athletes in full kyorugi kit passing harsh fluorescent tired expressions wide hallway STYLE PRIME"),
  ("1.6", "Changing — Dobok Pants", "Changing area. **First dobok** — Ethan pulling on white dobok pants. Black tee underneath.", "", "", f"changing area bench Ethan Hyun {ETHAN} pulling on white WT dobok pants black t-shirt underneath tournament venue locker room harsh light first dobok moment STYLE PRIME"),
  ("1.7", "Tying the Belt", "Tight panel. **Ethan Hyun's** hands tying **black belt with silver embroidery** over white dobok.", "", "", f"close-up hands tying black belt with silver embroidery over white WT dobok Ethan Hyun {ETHAN} changing area tight detail panel STYLE PRIME"),
  ("1.8", "Kit Reveal — Toward Warmup", "Full-width. **Ethan transformed:** white dobok · black belt · **blue hogu under arm** · **helmet in hand**. Looking toward warmup area.", "", "", f"Ethan Hyun {ETHAN} white WT dobok black belt silver embroidery blue electronic hogu under arm blue helmet in hand walking toward warmup area full kit reveal wide cinematic first athlete transformation STYLE PRIME"),
  ("1.9", "Chest Protector", "Blue electronic **hogu** going on over dobok.", "", "", f"Ethan Hyun {ETHAN} putting on blue electronic chest hogu over white WT dobok black belt silver embroidery changing area close-up hands STYLE PRIME"),
  ("1.10", "Forearm Guards", "White **forearm guards** strapped on.", "", "", f"Ethan Hyun {ETHAN} strapping white forearm guards {KIT} preparation sequence close-up STYLE PRIME"),
  ("1.11", "Shin Guards", "White **shin guards** secured.", "", "", f"Ethan Hyun {ETHAN} securing white shin guards sitting bench {KIT} preparation detail STYLE PRIME"),
  ("1.12", "Foot Sensors", "White **foot protectors** / sensors on.", "", "", f"Ethan Hyun {ETHAN} fitting white foot protectors sensors {KIT} preparation close-up feet hands STYLE PRIME"),
  ("1.13", "Helmet Clipped", "Blue **helmet** clipped / face shield down.", "", "", f"Ethan Hyun {ETHAN} clipping blue helmet face shield {KIT} preparation profile close-up STYLE PRIME"),
  ("1.14", "Mirror — Full Reveal", "Mirror shot. **First full competition reveal** — complete blue-hogu kit. Reserved expression.", "", "", f"mirror reflection Ethan Hyun {ETHAN} {KIT} full competition reveal first time complete kit sharp eyes reserved expression changing room mirror shot STYLE PRIME"),
  ("1.15", "Warmup Floor — Others Coached", "Warmup area. Other athletes with **coaches** — pads, advice, stretching.", "", "", f"warmup area wide shot athletes in blue hogu kyorugi kit with coaches pad work advice stretching Ethan Hyun {ETHAN} {KIT} background entering neglectful contrast STYLE PRIME"),
  ("1.16", "Ethan Alone — No Warmup", "Same floor. **Ethan Hyun alone.** No coach. No advice. No warmup. Something is wrong.", "", "", f"Ethan Hyun {ETHAN} {KIT} standing alone empty warmup mat no coach no instructor nearby other athletes coached in far background isolated neglectful atmosphere wide shot STYLE PRIME"),
]

# old_id -> drop if in set
DROP = {"1.11", "1.13", "1.40"}

REMAP_ORDER = [
  "1.6", "1.7", "1.8", "1.9", "1.10", "1.12", "1.14", "1.15", "1.16", "1.17",
  "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27",
  "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37",
  "1.38", "1.39",
]


def parse_panels(text: str, chapter: int = 1) -> dict[str, dict]:
  panels: dict[str, dict] = {}
  current: dict | None = None
  in_prompt = False
  prompt_lines: list[str] = []
  extra_lines: list[str] = []
  in_ch = False

  def flush() -> None:
    nonlocal current, in_prompt, prompt_lines, extra_lines
    if current:
      if prompt_lines:
        current["prompt"] = "\n".join(prompt_lines).strip()
      if extra_lines:
        current["extra"] = "\n".join(extra_lines).strip()
      panels[current["id"]] = current
    current = None
    in_prompt = False
    prompt_lines = []
    extra_lines = []

  for line in text.splitlines():
    if line.startswith("# Chapter 2"):
      flush()
      break
    m = re.match(r"^# Chapter (\d+)", line)
    if m:
      flush()
      in_ch = int(m.group(1)) == chapter
      continue
    if not in_ch:
      continue
    pm = re.match(r"^### Panel ([\d.]+(?:[a-zA-Z-]+)?) — (.+)$", line)
    if pm:
      flush()
      current = {"id": pm.group(1), "title": pm.group(2).strip(), "scene": "", "dialogue": "", "sfx": "", "timeline": "", "prompt": "", "extra": ""}
      continue
    if not current:
      continue
    if line.strip() == "**Prompt:**":
      in_prompt = True
      continue
    if in_prompt:
      if line.strip().startswith("```"):
        if prompt_lines:
          in_prompt = False
        continue
      prompt_lines.append(line)
      continue
    for tag in ("**Scene:**", "**Dialogue:**", "**SFX:**", "**Timeline:**"):
      if line.strip().startswith(tag):
        key = tag.strip("*:").lower()
        current[key] = line.split(":", 1)[1].strip()
        break
    else:
      if line.strip().startswith("**") and not line.strip().startswith("---"):
        extra_lines.append(line)

  flush()
  return panels


def kit_substitute(prompt: str) -> str:
  p = prompt
  p = re.sub(r"electronic chest hogu", "blue electronic hogu", p, flags=re.I)
  p = re.sub(r"chest hogu", "blue electronic hogu", p, flags=re.I)
  p = re.sub(r"headgear", "blue helmet", p, flags=re.I)
  if "Ethan Hyun" not in p and "teen" in p.lower():
    p = f"Ethan Hyun {ETHAN}, {p}"
  return p


def format_panel(p: dict) -> str:
  lines = [f"### Panel {p['id']} — {p['title']}", f"**Scene:** {p['scene']}"]
  if p.get("timeline"):
    lines.append(f"**Timeline:** {p['timeline']}")
  if p.get("dialogue"):
    lines.append(f"**Dialogue:** {p['dialogue']}")
  if p.get("sfx"):
    lines.append(f"**SFX:** {p['sfx']}")
  if p.get("extra"):
    lines.append(p["extra"])
  lines.append("")
  lines.append("**Prompt:**")
  lines.append("```")
  lines.append(p["prompt"])
  lines.append("```")
  lines.append("")
  lines.append("---")
  return "\n".join(lines)


def format_new(t: tuple) -> dict:
  pid, title, scene, dialogue, sfx, prompt = t
  return {"id": pid, "title": title, "scene": scene, "dialogue": dialogue, "sfx": sfx, "timeline": "", "prompt": prompt, "extra": ""}


def main() -> None:
  text = SB.read_text(encoding="utf-8")
  old = parse_panels(text)

  new_panels: list[dict] = [format_new(t) for t in NEW_OPENING]
  next_num = 17
  for old_id in REMAP_ORDER:
    if old_id in DROP or old_id not in old:
      continue
    p = dict(old[old_id])
    p["id"] = f"1.{next_num}"
    p["prompt"] = kit_substitute(p.get("prompt", ""))
    new_panels.append(p)
    next_num += 1

  ch1_start = text.index("# Chapter 1 — Nightmare")
  ch2_start = text.index("# Chapter 2 — Arrival at Kwon's")
  header = text[:ch1_start]
  ch2_and_rest = text[ch2_start:]

  # fix header flash refs
  header = header.replace("§ Scene 1 → **1.28**", "§ Scene 1 → **1.37**")
  header = header.replace("§ Scene 2 → **1.29–1.33**", "§ Scene 2 → **1.38–1.42**")
  header = re.sub(
    r"6\. \*\*Montage / flash clarity:\*\*.*",
    "6. **Montage / flash clarity:** [STORYBOARD-CLARITY-GUIDE.md](./STORYBOARD-CLARITY-GUIDE.md) — label **FLASH** vs **PRESENT** (see Ch 1 **1.27–1.31**).",
    header,
  )
  header = header.replace(
    "| **Ethan (gear)** | + **full olympic kyorugi kit:** white dobok, electronic chest hogu, headgear (face shield), forearm guards, shin/foot guards |",
    "| **Ethan (gear)** | + **full olympic kyorugi kit:** white WT dobok · **blue electronic hogu** · **blue helmet** · white forearm/shin/foot guards · black belt **silver embroidery** |",
  )
  header = header.replace(
    "| **Ethan (casual)** | + gold headphones, white backpack, oversized navy hoodie, white tee hanging out, baggy pants |",
    "| **Ethan (casual)** | + gold headphones · white backpack · **oversized black hoodie** · white undershirt · **black cargo pants** · white sneakers |",
  )

  body = "# Chapter 1 — Nightmare\n\n" + OUTFIT_LOCK + "\n"
  body += "\n".join(format_panel(p) for p in new_panels) + "\n\n"

  SB.write_text(header + body + ch2_and_rest, encoding="utf-8")
  print(f"Wrote Chapter 1: {len(new_panels)} panels (1.1–1.{len(new_panels)})")


if __name__ == "__main__":
  main()
