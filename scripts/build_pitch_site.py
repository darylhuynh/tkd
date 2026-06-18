#!/usr/bin/env python3
"""Build pitch-site data from canon.json and character markdown."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "reference-sheets" / "output"
DATA_DIR = ROOT / "data"
CHARACTERS_DIR = ROOT / "characters"

PORTRAIT_PRIORITY = [
    "casual-front.png",
    "poomsae-front.png",
    "polo-front.png",
    "vest-front.png",
    "shorts-front.png",
    "dobok-front.png",
]

FACTION = {
    "ethan-hyun": "kwons",
    "tj-lim": "kwons",
    "kieryn-lim": "kwons",
    "logan-hyun": "kwons",
    "kian-sang": "kwons",
    "ariana-yang": "kwons",
    "master-viet": "coach",
    "yuna-park": "ally",
    "ttong-kim": "prime",
    "repeul-kim": "prime",
    "derek-cole": "rival",
    "maya-ortiz": "rival",
    "lee-ji-woo": "rival",
    "kim-min-ho": "rival",
    "han-do-won": "rival",
    "park-sung-min": "rival",
}

ROLE = {
    "ethan-hyun": "Main Character · The Gifted Broken Prodigy",
    "tj-lim": "Team Ace / Anchor · The Chosen Champion",
    "kieryn-lim": "Female Ace · The Sassy Technician",
    "logan-hyun": "Heart of the Team · The School Mascot",
    "kian-sang": "Internal Challenger · The Storm",
    "ariana-yang": "Workhorse · The Unbreakable Daughter",
    "master-viet": "Head Instructor · Kwon's Taekwondo Academy",
    "yuna-park": "Poomsae Athlete · Ethan's Love Interest",
    "ttong-kim": "Antagonist · Prime Taekwondo Sports Dynasty",
    "repeul-kim": "Background · Ttong's wife (never speaks)",
    "derek-cole": "Arc 3 · Ch 25 opponent",
    "maya-ortiz": "Arc 3 · Ch 33 opponent",
    "lee-ji-woo": "Arc 6 · Ch 77 — Korea regional",
    "kim-min-ho": "Arc 7 · Ch 98 — Ethan's elimination",
    "han-do-won": "Arc 7 · Ch 99 — TJ finals",
    "park-sung-min": "Arc 8 · Ch 118 epilogue",
}

OPPONENT_SKILLS = {
    "derek-cole": [{"name": "Spinning Hook", "unlock": "base"}],
    "maya-ortiz": [{"name": "Cadet Bracket Ace", "unlock": "base"}],
    "kim-min-ho": [
        {"name": "Disciplined Distance", "unlock": "base"},
        {"name": "Shoulder Tell (spin setup)", "unlock": "base"},
    ],
    "han-do-won": [
        {"name": "Pressure Volume", "unlock": "base"},
        {"name": "Body Kick Chains", "unlock": "base"},
    ],
    "lee-ji-woo": [{"name": "Endurance Grind", "unlock": "base"}],
    "park-sung-min": [
        {"name": "Turning Body Kicks", "unlock": "base"},
        {"name": "Feint Spins", "unlock": "base"},
    ],
}

OPPONENT_IDS = {
    "derek-cole", "maya-ortiz", "lee-ji-woo", "kim-min-ho", "han-do-won", "park-sung-min",
}

# Legacy fallback when no canon.json exists yet
OPPONENTS_FALLBACK = [
    {
        "character_id": "derek-cole",
        "canon_name": "Derek Cole",
        "age": 16,
        "height": "5'10\"",
        "weight": "128 lbs",
        "division": "Open -54kg",
        "belt": "2nd Dan",
        "school": "Apex TKD",
        "faction": "rival",
        "role": "Arc 3 · Ch 25 opponent",
        "portrait": None,
    },
    {
        "character_id": "maya-ortiz",
        "canon_name": "Maya Ortiz",
        "age": 14,
        "height": "5'9\"",
        "weight": "112 lbs",
        "division": "Cadet -49kg",
        "belt": "2nd Dan",
        "school": "Valley Martial Arts",
        "faction": "rival",
        "role": "Arc 3 · Ch 33 opponent",
        "portrait": None,
    },
    {
        "character_id": "kim-min-ho",
        "canon_name": "Kim Min-ho",
        "age": 17,
        "height": "5'11\"",
        "weight": "132 lbs",
        "division": "U20 -58kg",
        "belt": "3rd Dan",
        "school": "Korea National TC",
        "faction": "rival",
        "role": "Arc 7 · Ch 98 — Ethan's elimination",
        "portrait": None,
    },
    {
        "character_id": "han-do-won",
        "canon_name": "Han Do-won",
        "age": 17,
        "height": "6'0\"",
        "weight": "158 lbs",
        "division": "U20 -68kg",
        "belt": "3rd Dan",
        "school": "Korea National TC",
        "faction": "rival",
        "role": "Arc 7 · Ch 99 — TJ finals",
        "portrait": None,
    },
    {
        "character_id": "lee-ji-woo",
        "canon_name": "Lee Ji-woo",
        "age": 16,
        "height": "5'6\"",
        "weight": "99 lbs",
        "division": "Junior -45kg",
        "belt": "3rd Dan",
        "school": "Busan Youth Team",
        "faction": "rival",
        "role": "Arc 6 · Ch 77 — Korea regional",
        "portrait": None,
    },
    {
        "character_id": "park-sung-min",
        "canon_name": "Park Sung-min",
        "age": 21,
        "height": "5'10\"",
        "weight": "145 lbs",
        "division": "Collegiate -68kg",
        "belt": "4th Dan",
        "school": "Yonsei Univ.",
        "faction": "rival",
        "role": "Arc 8 · Ch 118 epilogue",
        "portrait": None,
    },
]

ARCS = [
    {
        "num": 1,
        "title": "New Beginnings",
        "chapters": "1–10",
        "tagline": "Nightmare at Prime. Hope at Kwon's.",
        "href": "arcs/new-beginnings/index.html",
        "available": True,
    },
    {"num": 2, "title": "The Team", "chapters": "11–20", "tagline": "Six friends become a family.", "href": "arcs/the-team/index.html", "available": True},
    {"num": 3, "title": "First Tournament", "chapters": "21–35", "tagline": "First blood on the mat.", "href": "arcs/first-tournament/index.html", "available": True},
    {"num": 4, "title": "Shadow School", "chapters": "36–50", "tagline": "Prime doesn't let go easily.", "href": "arcs/shadow-school/index.html", "available": True},
    {"num": 5, "title": "Road to Korea", "chapters": "51–70", "tagline": "The impossible dream takes shape.", "href": "arcs/road-to-korea/index.html", "available": True},
    {"num": 6, "title": "Korea Regionals", "chapters": "71–90", "tagline": "Prove it on foreign soil.", "href": "arcs/korea-regionals/index.html", "available": True},
    {"num": 7, "title": "Legends", "chapters": "91–110", "tagline": "U20 National Team selection.", "href": "arcs/legends/index.html", "available": True},
    {"num": 8, "title": "Closure", "chapters": "111–120", "tagline": "Growth, loss, and what remains.", "href": "arcs/closure/index.html", "available": True},
]


def parse_role_from_md(character_id: str) -> str | None:
    md_path = CHARACTERS_DIR / f"{character_id}.md"
    if not md_path.exists():
        return None
    text = md_path.read_text(encoding="utf-8")
    match = re.search(r"\*\*Role:\*\*\s*(.+)", text)
    return match.group(1).strip() if match else None


def parse_stats_from_md(character_id: str) -> dict[str, str]:
    md_path = CHARACTERS_DIR / f"{character_id}.md"
    if not md_path.exists():
        return {}
    text = md_path.read_text(encoding="utf-8")
    stats: dict[str, str] = {}
    in_main = False
    for line in text.splitlines():
        if line.strip() == "### Main":
            in_main = True
            continue
        if in_main and line.startswith("### "):
            break
        if in_main:
            m = re.match(
                r"\|\s*(?:\*\*)?(.+?)(?:\*\*)?\s*\|\s*([A-Z][+-−]?)\s*\|",
                line,
            )
            if m and m.group(1).strip() != "Stat":
                grade = m.group(2).replace("−", "-")
                stats[m.group(1).strip()] = grade
    return stats


def parse_skills_from_md(character_id: str) -> list[dict[str, str]]:
    md_path = CHARACTERS_DIR / f"{character_id}.md"
    if not md_path.exists():
        return OPPONENT_SKILLS.get(character_id, [])

    text = md_path.read_text(encoding="utf-8")
    skills: list[dict[str, str]] = []

    section = re.search(
        r"### Defining Skills?\s*\n(.*?)(?=\n### |\n---|\Z)",
        text,
        re.DOTALL,
    )
    if not section:
        if canon_skill := _canon_defining_skill(character_id):
            return [{"name": canon_skill, "unlock": "base"}]
        return OPPONENT_SKILLS.get(character_id, [])

    for line in section.group(1).splitlines():
        m = re.match(r"^\-\s+\*\*(.+?)\*\*\s*[—–-]\s*(.+)$", line.strip())
        if not m:
            continue
        name = m.group(1).strip()
        detail = m.group(2).strip()
        unlock = "base"
        if "unlocked" in detail.lower() or "arc 7" in detail.lower():
            unlock = "arc7"
        elif "arc 5" in detail.lower() or "grandmother" in detail.lower():
            unlock = "arc5"
        skills.append({"name": name, "unlock": unlock, "detail": detail})

    return skills or OPPONENT_SKILLS.get(character_id, [])


def _canon_defining_skill(character_id: str) -> str | None:
    canon_path = OUTPUT_DIR / character_id / "canon.json"
    if not canon_path.exists():
        return None
    data = json.loads(canon_path.read_text(encoding="utf-8"))
    return data.get("defining_skill")


def resolve_portrait(char_dir: Path) -> str | None:
    casual = char_dir / "casual-front.png"
    if casual.exists():
        return casual.relative_to(ROOT).as_posix()
    for filename in PORTRAIT_PRIORITY[1:]:
        path = char_dir / filename
        if path.exists():
            return path.relative_to(ROOT).as_posix()
    return None


def load_canon_character(canon_path: Path) -> dict:
    data = json.loads(canon_path.read_text(encoding="utf-8"))
    cid = data["character_id"]
    char_dir = canon_path.parent

    display_name = data.get("canon_name", cid)
    also_known_as = data.get("called")

    views = []
    for filename, caption in (data.get("files") or {}).items():
        path = char_dir / filename
        if path.exists():
            views.append({
                "src": path.relative_to(ROOT).as_posix(),
                "label": filename.replace("-", " ").replace(".png", "").title(),
                "caption": caption,
            })

    return {
        "character_id": cid,
        "canon_name": data.get("canon_name", display_name),
        "display_name": display_name,
        "also_known_as": also_known_as,
        "age": data.get("age"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "division": data.get("division") or data.get("discipline"),
        "belt": data.get("belt") or data.get("rank"),
        "school": data.get("school"),
        "role": ROLE.get(cid) or parse_role_from_md(cid) or data.get("role", ""),
        "faction": FACTION.get(cid, "rival" if cid in OPPONENT_IDS else "kwons"),
        "stats": parse_stats_from_md(cid),
        "skills": parse_skills_from_md(cid),
        "portrait": resolve_portrait(char_dir),
        "views": views,
        "status": data.get("status", "complete" if resolve_portrait(char_dir) else "pending"),
    }


def main() -> None:
    characters: list[dict] = []
    loaded_ids: set[str] = set()

    for canon_path in sorted(OUTPUT_DIR.glob("*/canon.json")):
        entry = load_canon_character(canon_path)
        characters.append(entry)
        loaded_ids.add(entry["character_id"])

    for opp in OPPONENTS_FALLBACK:
        cid = opp["character_id"]
        if cid in loaded_ids:
            continue
        opp["skills"] = parse_skills_from_md(cid)
        opp["stats"] = parse_stats_from_md(cid)
        opp["display_name"] = opp["canon_name"]
        opp["faction"] = FACTION.get(cid, "rival")
        opp["role"] = ROLE.get(cid, "")
        char_dir = OUTPUT_DIR / cid
        if char_dir.is_dir():
            opp["portrait"] = resolve_portrait(char_dir)
        characters.append(opp)

    order = [
        "ethan-hyun", "tj-lim", "kieryn-lim", "logan-hyun", "kian-sang", "ariana-yang",
        "master-viet", "yuna-park",
        "ttong-kim", "repeul-kim",
        "derek-cole", "maya-ortiz", "lee-ji-woo", "kim-min-ho", "han-do-won", "park-sung-min",
    ]
    rank = {cid: i for i, cid in enumerate(order)}
    characters.sort(key=lambda c: rank.get(c["character_id"], 99))

    payload = {
        "title": "Taekwondo Legends",
        "logline": (
            "After leaving a toxic, money-driven school that cares only about the bottom line and "
            "their image, Ethan Hyun and five teammates rebuild under Master Viet at Kwon's "
            "Taekwondo Academy. Together they chase an impossible dream: qualifying for the "
            "Korea U20 National Team."
        ),
        "story_premise": (
            "Ethan walks into Kwon's Taekwondo Academy with elite technique, a silver letter black "
            "belt and scars from an old school. Master Viet doesn't promise miracles - he promises "
            "attention. One by one, five friends leave Prime Taekwondo Sports Dynasty's Shadow "
            "to follow Ethan."
        ),
        "story_premise_2": (
            "The rivalry stays on the tournament floor — rival schools, national camps, and the long "
            "road to Korea. At Kwon's, teammates push each other harder; they don't tear each other "
            "down."
        ),
        "genre": ["Sports Drama", "Coming of Age", "Martial Arts", "Found Family"],
        "arcs": ARCS,
        "characters": characters,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / "site.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} ({len(characters)} characters)")


if __name__ == "__main__":
    main()
