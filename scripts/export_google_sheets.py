#!/usr/bin/env python3
"""Export storyboard panels and character card templates for Google Sheets import."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORYBOARDS = ROOT / "storyboards"
OUT = ROOT / "reference-sheets" / "google-sheets-import"


def parse_storyboard_panels(path: Path) -> list[dict]:
    arc_match = re.search(r"arc-(\d+)", path.name)
    arc = arc_match.group(1) if arc_match else "?"

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    chapter = ""
    panels: list[dict] = []
    i = 0
    panel_re = re.compile(r"^### (?:Panel )?(\d+(?:\.\S+)?) — (.+)$")
    chapter_re = re.compile(r"^##+ Chapter (\d+\S*) — (.+)$")
    section_re = re.compile(r"^## (?:Chapters )?(\d+(?:–\d+)?|\d+\S*) — (.+)$")

    while i < len(lines):
        line = lines[i]

        m_ch = chapter_re.match(line) or section_re.match(line)
        if m_ch:
            chapter = m_ch.group(1).split("—")[0].strip()
            if "—" in m_ch.group(0) and "Chapter" not in line:
                chapter = m_ch.group(1).split("–")[0].strip()

        m_p = panel_re.match(line)
        if m_p:
            panel_id = m_p.group(1)
            title = m_p.group(2).strip()
            block: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith("### ") and not (
                lines[i].startswith("## ") and not lines[i].startswith("###")
            ):
                block.append(lines[i])
                i += 1

            block_text = "\n".join(block)
            timeline = ""
            tl = re.search(r"\*\*Timeline:\*\* (.+)", block_text)
            if tl:
                timeline = tl.group(1).strip()

            dialogue = ""
            for dline in block:
                if dline.startswith("**Dialogue"):
                    dialogue = dline.split(":", 1)[-1].strip().strip("*")
                    break

            tags = []
            if "[CARD]" in title or "[CARD]" in block_text:
                tags.append("CARD")
            if "[TEACH]" in title or "[TEACH]" in block_text:
                tags.append("TEACH")
            if "[ACTION]" in title or "[ACTION]" in block_text:
                tags.append("ACTION")
            if "[HAIKYUU]" in title or "[HAIKYUU]" in block_text:
                tags.append("HAIKYUU")
            if "FLASH" in timeline.upper() or "FLASH" in block_text[:200].upper():
                tags.append("FLASH")
            if "PRESENT" in timeline.upper():
                tags.append("PRESENT")

            ch_from_id = panel_id.split(".")[0]
            panels.append(
                {
                    "arc": arc,
                    "chapter": ch_from_id,
                    "chapter_section": chapter,
                    "panel_id": panel_id,
                    "title": title,
                    "timeline": timeline,
                    "tags": ", ".join(tags),
                    "dialogue": dialogue[:500],
                    "source_file": path.name,
                }
            )
            continue
        i += 1

    return panels


def export_storyboard_index() -> None:
    rows: list[dict] = []
    for path in sorted(STORYBOARDS.glob("arc-*-panel-storyboard.md")):
        rows.extend(parse_storyboard_panels(path))

    out_path = OUT / "Storyboard-Index.csv"
    fieldnames = [
        "arc",
        "chapter",
        "chapter_section",
        "panel_id",
        "title",
        "timeline",
        "tags",
        "dialogue",
        "source_file",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} panels -> {out_path.relative_to(ROOT)}")


def write_card_csv(filename: str, rows: list[tuple[str, str]]) -> None:
    out_path = OUT / filename
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Field", "Value"])
        writer.writerows(rows)
    print(f"Wrote {out_path.relative_to(ROOT)}")


def card_rows(name: str, sections: list[tuple[str, list[tuple[str, str]]]]) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = [(f"CHARACTER CARD — {name}", "")]
    for section_title, items in sections:
        rows.append(("", ""))
        rows.append((section_title, ""))
        rows.extend(items)
    return rows


def export_character_cards() -> None:
    write_card_csv(
        "Ethan-Hyun.csv",
        card_rows(
            "Ethan Hyun",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "15 (→ 17 epilogue)"),
                        ("Nationality", "Korean-American"),
                        ("Height", "5'3\" (160 cm)"),
                        ("Weight", "95 lbs (43 kg)"),
                        ("Division", "Junior −45 kg (→ Collegiate −58 kg epilogue)"),
                        ("Belt Rank", "3rd Dan — silver-letter black belt (only at Kwon's)"),
                        ("Role", "Main Character · The Gifted Broken Prodigy"),
                    ],
                ),
                (
                    "MAIN STATS",
                    [
                        ("Attack", "B+"),
                        ("Defense", "B"),
                        ("Technique", "A"),
                        ("Mobility", "A−"),
                        ("Physical", "B+"),
                    ],
                ),
                (
                    "SECONDARY STATS",
                    [
                        ("Strength", "B−"),
                        ("Endurance", "A"),
                        ("Speed", "A−"),
                        ("Reach", "B"),
                        ("Tenacity", "C"),
                        ("Charisma", "B−"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "Neverending Endurance"),
                        ("Secondary Skill", "Berserker Rage (Arc 5+)"),
                        ("Arc 7 Signature", "Ultimate Counter"),
                        ("Favorite Kicks", "Outside-In Crescent · Counter Backleg Roundhouse"),
                    ],
                ),
                (
                    "APPEARANCE",
                    [
                        ("Hair", "Dark blue shadow-perm"),
                        ("Eyes", "Brown"),
                        ("Gear", "Gold headphones · white gear backpack"),
                        ("Casual", "Oversized navy hoodie · baggy pants"),
                    ],
                ),
                (
                    "PERSONALITY",
                    [
                        ("Traits", "Quiet · introverted · struggles to trust"),
                    ],
                ),
                (
                    "LOVES",
                    [
                        ("", "Sushi · Pineapple Fanta (yellow can only)"),
                    ],
                ),
                (
                    "DRAMA",
                    [
                        ("Arc", "Surviving Prime abuse; learning to trust Kwon's family"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "ETHAN HYUN · Age 15 · 5'3\" · 95 lbs · Junior −45 kg · 3rd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "TJ-Lim.csv",
        card_rows(
            "TJ Lim",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "15"),
                        ("Nationality", "Korean-American"),
                        ("Height", "5'11\" (180 cm)"),
                        ("Weight", "150 lbs (68 kg)"),
                        ("Division", "Junior −68 kg"),
                        ("Belt Rank", "3rd Dan"),
                        ("Role", "Team Ace · The Chosen Champion"),
                    ],
                ),
                (
                    "MAIN STATS",
                    [
                        ("Attack", "A"),
                        ("Defense", "B+"),
                        ("Technique", "B"),
                        ("Mobility", "C+"),
                        ("Physical", "A"),
                    ],
                ),
                (
                    "SECONDARY STATS",
                    [
                        ("Strength", "A"),
                        ("Endurance", "B"),
                        ("Speed", "B"),
                        ("Reach", "A"),
                        ("Tenacity", "B+"),
                        ("Charisma", "A−"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "Emperor's Kick"),
                        ("Arc 7 Signature", "Mountain Strike"),
                        ("Favorite Kicks", "Backleg Roundhouse · Cut Kick"),
                    ],
                ),
                (
                    "APPEARANCE",
                    [
                        ("Hair", "Teal · headband"),
                        ("Build", "Muscular · tallest on team"),
                    ],
                ),
                (
                    "LOVES",
                    [
                        ("", "Hatsune Miku · Fried rice · Rap music"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "TJ LIM · Age 15 · 5'11\" · 150 lbs · Junior −68 kg · 3rd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Kieryn-Lim.csv",
        card_rows(
            "Kieryn Lim",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "13 (→ 15 epilogue)"),
                        ("Nationality", "Korean-American"),
                        ("Height", "5'8\" (173 cm)"),
                        ("Weight", "108 lbs (49 kg)"),
                        ("Division", "Cadet −49 kg"),
                        ("Belt Rank", "2nd Dan"),
                        ("Sibling", "TJ Lim (older brother)"),
                        ("Role", "Female Ace · The Sassy Technician"),
                    ],
                ),
                (
                    "MAIN STATS",
                    [
                        ("Attack", "A−"),
                        ("Defense", "B"),
                        ("Technique", "B−"),
                        ("Mobility", "B+"),
                        ("Physical", "A"),
                    ],
                ),
                (
                    "SECONDARY STATS",
                    [
                        ("Strength", "C+"),
                        ("Endurance", "B−"),
                        ("Speed", "C−"),
                        ("Reach", "A"),
                        ("Tenacity", "B+"),
                        ("Charisma", "B"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "100 Shadow Kick"),
                        ("Arc 7 Signature", "Laser Stab"),
                        ("Favorite Kicks", "Cut Kick · Flop Kick"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "KIERYN LIM · Age 13 · 5'8\" · 108 lbs · Cadet −49 kg · 2nd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Logan-Hyun.csv",
        card_rows(
            "Logan Hyun",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "13 (→ 15 epilogue)"),
                        ("Nationality", "Korean-American"),
                        ("Height", "4'10\" (147 cm)"),
                        ("Weight", "84 lbs (38 kg)"),
                        ("Division", "Cadet −41 kg"),
                        ("Belt Rank", "2nd Dan — plain black belt (no letter)"),
                        ("Sibling", "Ethan Hyun (older brother)"),
                        ("Role", "Heart · The School Mascot"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "Neverending Rage"),
                        ("Favorite Kick", "Flying Side Kick"),
                        ("U20", "Does not compete — corners full-time (Ch 100)"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "LOGAN HYUN · Age 13 · 4'10\" · 84 lbs · Cadet −41 kg · 2nd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Kian-Sang.csv",
        card_rows(
            "Kian Sang",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "15"),
                        ("Nationality", "Korean-American (half Korean · half Indian)"),
                        ("Height", "5'10\" (178 cm)"),
                        ("Weight", "108 lbs (49 kg)"),
                        ("Division", "Junior −49 kg"),
                        ("Belt Rank", "2nd Dan"),
                        ("Role", "Internal Challenger · The Storm"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "Whirlwind Kick"),
                        ("Arc 7 Signature", "Debilitating Combo"),
                        ("Favorite Kicks", "Flop Kick · Clinch Kick"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "KIAN SANG · Age 15 · 5'10\" · 108 lbs · Junior −49 kg · 2nd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Ariana-Yang.csv",
        card_rows(
            "Ariana Yang",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Kwon's Taekwondo Academy"),
                        ("Age", "15"),
                        ("Nationality", "Filipino-American"),
                        ("Height", "4'11\" (150 cm)"),
                        ("Weight", "92 lbs (42 kg)"),
                        ("Division", "Junior −42 kg"),
                        ("Belt Rank", "2nd Dan"),
                        ("Role", "Workhorse · The Unbreakable Daughter"),
                    ],
                ),
                (
                    "COMBAT",
                    [
                        ("Defining Skill", "Supreme Accuracy"),
                        ("Arc 7 Signature", "Whirling Dervish (10-hit · 3 kicks then foot down)"),
                        ("Favorite Attacks", "Punch · Clinch Kick"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "ARIANA YANG · Age 15 · 4'11\" · 92 lbs · Junior −42 kg · 2nd Dan · Kwon's"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Yuna-Park.csv",
        card_rows(
            "Yuna Park",
            [
                (
                    "CORE PROFILE",
                    [
                        ("Discipline", "Poomsae (not Kwon's spar roster)"),
                        ("Age", "15 (→ 17 epilogue)"),
                        ("Nationality", "Korean-American"),
                        ("Height", "5'6\" (168 cm)"),
                        ("Weight", "115 lbs (52 kg)"),
                        ("Belt Rank", "2nd Dan (poomsae)"),
                        ("Role", "Poomsae athlete · slow-burn friendship with Ethan"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "YUNA PARK · Age 15 · 5'6\" · 115 lbs · Poomsae Senior · 2nd Dan"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Master-Viet.csv",
        card_rows(
            "Master Viet (Viet Na)",
            [
                (
                    "CORE PROFILE",
                    [
                        ("Legal name", "Viet Na"),
                        ("Called", "Master Viet"),
                        ("School", "Kwon's Taekwondo Academy (head coach)"),
                        ("Age", "Mid 40s"),
                        ("Height", "5'8\" (173 cm)"),
                        ("Build", "Chubby · kind small eyes"),
                        ("Rank", "Master (Kwon's)"),
                    ],
                ),
                (
                    "NOTES",
                    [
                        ("Teaching", "Individual attention · names adjustments out loud"),
                        ("Theme", "Character over rank"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Ttong-Kim.csv",
        card_rows(
            "Ttong Kim",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Prime Taekwondo Sports Dynasty"),
                        ("Age", "38"),
                        ("Height", "5'8\" (173 cm)"),
                        ("Weight", "198 lbs (90 kg)"),
                        ("Claimed title", "Master"),
                        ("Actual rank", "2nd Dan — Instructor level"),
                        ("Role", "Antagonist (institutional)"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "TTONG KIM · Age 38 · 5'8\" · 198 lbs · 2nd Dan · Prime"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Yeo-Woo-Kim.csv",
        card_rows(
            "Yeo Woo Kim",
            [
                (
                    "CORE PROFILE",
                    [
                        ("School", "Prime (background only)"),
                        ("Age", "37"),
                        ("Height", "5'5\" (165 cm)"),
                        ("Weight", "265 lbs (120 kg)"),
                        ("Hair color", "Brown"),
                        ("Hair style", "Curly, medium-to-long (half-up claw clip)"),
                        ("Role", "Ttong Kim's wife — silent background"),
                        ("Speaks", "NEVER on-page"),
                    ],
                ),
                (
                    "FIGHTER CARD TEXT",
                    [
                        ("Copy-paste", "YEO WOO KIM · Age 37 · 5'5\" · 265 lbs · Prime (background)"),
                    ],
                ),
            ],
        ),
    )

    write_card_csv(
        "Opponents.csv",
        card_rows(
            "Key Opponents",
            [
                (
                    "CH 25 — Derek Cole",
                    [
                        ("Card text", "DEREK COLE · Age 16 · 5'10\" · 128 lbs · Open −54 kg · 2nd Dan · Apex TKD"),
                        ("Notes", "Spinning hook specialist — Ethan loss Arc 3"),
                    ],
                ),
                (
                    "CH 98 — Kim Min-ho",
                    [
                        ("Card text", "KIM MIN-HO · Age 17 · 5'11\" · 132 lbs · U20 −58 kg · 3rd Dan · Korea National TC"),
                        ("Notes", "Left shoulder tell before spin"),
                    ],
                ),
                (
                    "CH 99 — Han Do-won",
                    [
                        ("Card text", "HAN DO-WON · Age 17 · 6'0\" · 158 lbs · U20 −68 kg · 3rd Dan · Korea National TC"),
                        ("Notes", "TJ finals opponent — selected"),
                    ],
                ),
                (
                    "CH 118 — Park Sung-min",
                    [
                        ("Card text", "PARK SUNG-MIN · Age 21 · 5'10\" · 145 lbs · Collegiate −68 kg · 4th Dan · Yonsei"),
                        ("Notes", "Collegiate final — epilogue"),
                    ],
                ),
            ],
        ),
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    export_character_cards()
    export_storyboard_index()
    print(f"\nImport guide: {OUT / 'README.md'}")


if __name__ == "__main__":
    main()
