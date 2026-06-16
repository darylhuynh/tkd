#!/usr/bin/env python3
"""Parse arc panel storyboards and generate chapter reader HTML pages."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ARC_CONFIG: dict[int, dict] = {
    1: {
        "storyboard": "arc-01-panel-storyboard.md",
        "arc_md": "arc-01-new-beginnings.md",
        "out_dir": "new-beginnings",
        "label": "New Beginnings",
        "num_label": "01",
        "chapter_re": r"^# Chapter (\d+) — (.+)$",
        "panel_re": r"^### Panel ([\d.]+(?:[a-zA-Z-]+)?) — (.+)$",
    },
    2: {
        "storyboard": "arc-02-panel-storyboard.md",
        "arc_md": "arc-02-the-team.md",
        "out_dir": "the-team",
        "label": "The Team",
        "num_label": "02",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    3: {
        "storyboard": "arc-03-panel-storyboard.md",
        "arc_md": "arc-03-first-tournament.md",
        "out_dir": "first-tournament",
        "label": "First Tournament",
        "num_label": "03",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    4: {
        "storyboard": "arc-04-panel-storyboard.md",
        "arc_md": "arc-04-shadow-school.md",
        "out_dir": "shadow-school",
        "label": "Shadow School",
        "num_label": "04",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    5: {
        "storyboard": "arc-05-panel-storyboard.md",
        "arc_md": "arc-05-road-to-korea.md",
        "out_dir": "road-to-korea",
        "label": "Road to Korea",
        "num_label": "05",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    6: {
        "storyboard": "arc-06-panel-storyboard.md",
        "arc_md": "arc-06-korea-regionals.md",
        "out_dir": "korea-regionals",
        "label": "Korea Regionals",
        "num_label": "06",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    7: {
        "storyboard": "arc-07-panel-storyboard.md",
        "arc_md": "arc-07-legends.md",
        "out_dir": "legends",
        "label": "Legends",
        "num_label": "07",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
    8: {
        "storyboard": "arc-08-panel-storyboard.md",
        "arc_md": "arc-08-closure.md",
        "out_dir": "closure",
        "label": "Closure",
        "num_label": "08",
        "chapter_re": r"^## Chapter (\d+) — (.+)$",
        "panel_re": r"^### (\d+\.\d+(?:\.\d+)?(?:[a-zA-Z]+)?) — (.+)$",
    },
}

GROUP_CHAPTER_RE = re.compile(r"^## Chapters (\d+)–(\d+) — (.+)$")


def slug(ch: int) -> str:
    return f"chapter-{ch:02d}"


def panel_chapter_num(panel_id: str) -> int:
    return int(panel_id.split(".", 1)[0])


def load_chapter_titles(arc_md_path: Path) -> dict[int, str]:
    titles: dict[int, str] = {}
    if not arc_md_path.exists():
        return titles
    text = arc_md_path.read_text(encoding="utf-8")
    for m in re.finditer(r"^### Chapter (\d+) — (.+)$", text, re.M):
        titles[int(m.group(1))] = m.group(2).strip()
    for m in re.finditer(r"^### Chapters (\d+)–(\d+) — (.+)$", text, re.M):
        start, end, title = int(m.group(1)), int(m.group(2)), m.group(3).strip()
        for n in range(start, end + 1):
            if n not in titles:
                titles[n] = title
    return titles


def panel_image(arc_num: int, panel_id: str) -> str | None:
    panel_dir = ROOT / "gallery" / "panels" / f"arc-{arc_num:02d}"
    for ext in (".png", ".jpg", ".webp"):
        path = panel_dir / f"{panel_id}{ext}"
        if path.exists():
            return "../../" + path.relative_to(ROOT).as_posix()
    return None


def parse_storyboard(text: str, cfg: dict, arc_num: int, title_map: dict[int, str]) -> list[dict]:
    chapters_by_num: dict[int, dict] = {}
    current_panel: dict | None = None
    in_prompt = False
    prompt_lines: list[str] = []
    ch_re = re.compile(cfg["chapter_re"])
    panel_re = re.compile(cfg["panel_re"])
    group_titles: dict[int, str] = {}

    def chapter_title(num: int) -> str:
        if num in title_map:
            return title_map[num]
        if num in group_titles:
            return group_titles[num]
        return f"Chapter {num}"

    def ensure_chapter(num: int) -> dict:
        if num not in chapters_by_num:
            chapters_by_num[num] = {
                "num": num,
                "title": chapter_title(num),
                "slug": slug(num),
                "panels": [],
            }
        return chapters_by_num[num]

    def flush_panel() -> None:
        nonlocal current_panel, in_prompt, prompt_lines
        if current_panel is not None:
            if prompt_lines:
                current_panel["prompt"] = "\n".join(prompt_lines).strip()
            pid = current_panel["id"]
            ch = ensure_chapter(panel_chapter_num(pid))
            current_panel["image"] = panel_image(arc_num, pid)
            ch["panels"].append(current_panel)
        current_panel = None
        in_prompt = False
        prompt_lines = []

    for line in text.splitlines():
        group_match = GROUP_CHAPTER_RE.match(line)
        if group_match:
            start, end, title = int(group_match.group(1)), int(group_match.group(2)), group_match.group(3).strip()
            title = re.sub(r"\s*\[.+?\]\s*$", "", title).strip()
            for n in range(start, end + 1):
                group_titles[n] = title
                if n in chapters_by_num:
                    chapters_by_num[n]["title"] = chapter_title(n)
            continue

        ch_match = ch_re.match(line)
        if ch_match:
            num = int(ch_match.group(1))
            title_map[num] = ch_match.group(2).strip()
            if num in chapters_by_num:
                chapters_by_num[num]["title"] = title_map[num]
            continue

        panel_match = panel_re.match(line)
        if panel_match:
            flush_panel()
            current_panel = {
                "id": panel_match.group(1),
                "title": panel_match.group(2).strip(),
                "scene": "",
                "dialogue": "",
                "sfx": "",
                "timeline": "",
                "prompt": "",
                "style": "",
            }
            continue

        if current_panel is None:
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

        for key in ("Scene", "Dialogue", "SFX", "Timeline"):
            prefix = f"**{key}:**"
            if line.startswith(prefix):
                val = line[len(prefix) :].strip()
                field = key.lower()
                current_panel[field] = val
                if "STYLE:" in val:
                    sm = re.search(r"STYLE:\s*(\w+)", val)
                    if sm:
                        current_panel["style"] = sm.group(1)
                if key == "Scene" and "FLASH" in val.upper():
                    current_panel["timeline"] = "FLASH"
                break

    flush_panel()
    return [chapters_by_num[n] for n in sorted(chapters_by_num)]


def arc_summary(arc_md_path: Path) -> str:
    if not arc_md_path.exists():
        return ""
    text = arc_md_path.read_text(encoding="utf-8")
    m = re.search(r"## Arc Summary\s*\n\n(.+?)\n\n---", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def reader_head(title: str, depth: int = 2) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} · Taekwondo Legends</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/css/pitch.css">
  <link rel="stylesheet" href="{prefix}assets/css/reader.css">
</head>
<body class="reader-page">
"""


def render_panel(panel: dict) -> str:
    tags = []
    if panel.get("style"):
        tags.append(f'<span class="panel-tag style-{panel["style"].lower()}">{html.escape(panel["style"])}</span>')
    blob = panel.get("timeline", "") + panel.get("title", "") + panel.get("scene", "")
    if "FLASH" in blob.upper():
        tags.append('<span class="panel-tag flash">FLASH</span>')
    if "[CARD]" in panel.get("title", ""):
        tags.append('<span class="panel-tag card">CARD</span>')
    if "[TEACH]" in panel.get("title", ""):
        tags.append('<span class="panel-tag teach">TEACH</span>')
    if "[HAIKYUU]" in panel.get("title", ""):
        tags.append('<span class="panel-tag haikyuu">TEAM</span>')

    tag_html = f'<div class="panel-tags">{"".join(tags)}</div>' if tags else ""

    if panel.get("image"):
        src = html.escape(panel["image"])
        img_block = f'<figure class="panel-art"><img src="{src}" alt="Panel {html.escape(panel["id"])}" loading="lazy"></figure>'
    else:
        img_block = f"""<figure class="panel-art panel-art--empty">
          <div class="panel-placeholder">
            <span class="panel-id">{html.escape(panel["id"])}</span>
            <span>Panel art pending</span>
          </div>
        </figure>"""

    dialogue = ""
    if panel.get("dialogue") and panel["dialogue"] not in ("*(none)*", "(none)"):
        dialogue = f'<p class="panel-dialogue">{html.escape(panel["dialogue"])}</p>'

    sfx = ""
    if panel.get("sfx") and panel["sfx"] not in ("*(none — silence)*", "*(none)*"):
        sfx = f'<p class="panel-sfx">{html.escape(panel["sfx"])}</p>'

    timeline = ""
    if panel.get("timeline"):
        timeline = f'<p class="panel-timeline">{html.escape(panel["timeline"])}</p>'

    return f"""
<article class="panel" id="panel-{html.escape(panel["id"])}">
  <header class="panel-header">
    <span class="panel-number">{html.escape(panel["id"])}</span>
    <h2>{html.escape(panel["title"])}</h2>
    {tag_html}
  </header>
  {img_block}
  <div class="panel-copy">
    {timeline}
    <p class="panel-scene">{html.escape(panel.get("scene", ""))}</p>
    {dialogue}
    {sfx}
  </div>
</article>"""


def write_index(cfg: dict, arc_num: int, chapters: list[dict], prev_arc: dict | None, next_arc: dict | None) -> None:
    out_dir = ROOT / "arcs" / cfg["out_dir"]
    summary = html.escape(arc_summary(ROOT / "arcs" / cfg["arc_md"]))
    cards = []
    for ch in chapters:
        cards.append(f"""
        <a class="chapter-card" href="{ch["slug"]}.html">
          <span class="chapter-num">Chapter {ch["num"]}</span>
          <h2>{html.escape(ch["title"])}</h2>
          <span class="chapter-panels">{len(ch["panels"])} panels</span>
        </a>""")

    arc_nav = ""
    if prev_arc:
        arc_nav += f'<a class="arc-nav-link" href="../{prev_arc["out_dir"]}/index.html">← Arc {prev_arc["num_label"]}: {html.escape(prev_arc["label"])}</a> '
    if next_arc:
        arc_nav += f'<a class="arc-nav-link" href="../{next_arc["out_dir"]}/index.html">Arc {next_arc["num_label"]}: {html.escape(next_arc["label"])} →</a>'

    ch_range = f"{chapters[0]['num']}–{chapters[-1]['num']}" if chapters else "—"
    total = sum(len(c["panels"]) for c in chapters)
    page = reader_head(f"Arc {arc_num} — {cfg['label']}", depth=2)
    page += f"""
  <header class="reader-header">
    <div class="reader-header-inner">
      <a class="reader-back" href="../../index.html#arcs">← Taekwondo Legends</a>
      <p class="reader-arc-label">Arc {cfg["num_label"]}</p>
      <h1>{html.escape(cfg["label"])}</h1>
      <p class="reader-summary">{summary}</p>
      <p class="reader-meta">Chapters {ch_range} · {total} storyboard panels</p>
      <nav class="arc-nav">{arc_nav}</nav>
    </div>
  </header>
  <main class="reader-main">
    <div class="chapter-grid">
      {"".join(cards)}
    </div>
  </main>
</body>
</html>
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(page, encoding="utf-8")


def write_chapter(cfg: dict, ch: dict, chapters: list[dict], prev_arc: dict | None, next_arc: dict | None) -> None:
    out_dir = ROOT / "arcs" / cfg["out_dir"]
    prev_link = ""
    next_link = ""
    idx = chapters.index(ch)

    if idx > 0:
        prev_ch = chapters[idx - 1]
        prev_link = f'<a class="nav-prev" href="{prev_ch["slug"]}.html">← Ch {prev_ch["num"]}: {html.escape(prev_ch["title"])}</a>'
    elif prev_arc:
        prev_arc_cfg = ARC_CONFIG[prev_arc["num"]]
        prev_chapters = prev_arc.get("_chapters") or []
        if prev_chapters:
            last = prev_chapters[-1]
            prev_link = (
                f'<a class="nav-prev" href="../{prev_arc_cfg["out_dir"]}/{last["slug"]}.html">'
                f'← Ch {last["num"]}: {html.escape(last["title"])}</a>'
            )
        else:
            prev_link = f'<a class="nav-prev" href="../{prev_arc_cfg["out_dir"]}/index.html">← Arc {prev_arc_cfg["num_label"]}</a>'

    if idx < len(chapters) - 1:
        next_ch = chapters[idx + 1]
        next_link = f'<a class="nav-next" href="{next_ch["slug"]}.html">Ch {next_ch["num"]}: {html.escape(next_ch["title"])} →</a>'
    elif next_arc:
        next_arc_cfg = ARC_CONFIG[next_arc["num"]]
        next_link = f'<a class="arc-nav-link nav-next" href="../{next_arc_cfg["out_dir"]}/index.html">Arc {next_arc_cfg["num_label"]}: {html.escape(next_arc_cfg["label"])} →</a>'

    panels_html = "\n".join(render_panel(p) for p in ch["panels"])
    title = f"Ch {ch['num']} — {ch['title']}"

    page = reader_head(title, depth=2)
    page += f"""
  <header class="reader-header reader-header--chapter">
    <div class="reader-header-inner">
      <a class="reader-back" href="index.html">← Arc {cfg["num_label"]}: {html.escape(cfg["label"])}</a>
      <p class="reader-arc-label">Chapter {ch["num"]}</p>
      <h1>{html.escape(ch["title"])}</h1>
      <p class="reader-meta">{len(ch["panels"])} panels · vertical webtoon layout</p>
    </div>
  </header>
  <nav class="chapter-nav">{prev_link}{next_link}</nav>
  <main class="webtoon-scroll">
    {panels_html}
  </main>
  <nav class="chapter-nav chapter-nav--bottom">{prev_link}{next_link}</nav>
</body>
</html>
"""
    (out_dir / f"{ch['slug']}.html").write_text(page, encoding="utf-8")


def build_arc(arc_num: int) -> tuple[int, int]:
    cfg = ARC_CONFIG[arc_num]
    storyboard_path = ROOT / "storyboards" / cfg["storyboard"]
    arc_md_path = ROOT / "arcs" / cfg["arc_md"]
    title_map = load_chapter_titles(arc_md_path)
    text = storyboard_path.read_text(encoding="utf-8")
    chapters = parse_storyboard(text, cfg, arc_num, title_map)

    if not chapters:
        print(f"WARNING: no chapters parsed for arc {arc_num}", file=sys.stderr)
        return 0, 0

    out_dir = ROOT / "arcs" / cfg["out_dir"]
    panel_dir = ROOT / "gallery" / "panels" / f"arc-{arc_num:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    panel_dir.mkdir(parents=True, exist_ok=True)

    data_out = ROOT / "data" / f"arc-{arc_num:02d}.json"
    data_out.write_text(
        json.dumps({"arc": arc_num, "title": cfg["label"], "chapters": chapters}, indent=2) + "\n",
        encoding="utf-8",
    )

    cfg["_chapters"] = chapters
    prev_meta = None
    if arc_num > 1 and ARC_CONFIG[arc_num - 1].get("_chapters"):
        prev_meta = {"num": arc_num - 1, **ARC_CONFIG[arc_num - 1]}
    next_meta = {"num": arc_num + 1, **ARC_CONFIG[arc_num + 1]} if arc_num < 8 else None

    write_index(cfg, arc_num, chapters, prev_meta, next_meta)
    for ch in chapters:
        write_chapter(cfg, ch, chapters, prev_meta, next_meta)

    total = sum(len(c["panels"]) for c in chapters)
    print(f"Arc {arc_num}: {out_dir.relative_to(ROOT)}/ ({len(chapters)} chapters, {total} panels)")
    return len(chapters), total


def main() -> None:
    parser = argparse.ArgumentParser(description="Build arc chapter reader HTML")
    parser.add_argument("arcs", nargs="*", type=int, help="Arc numbers (default: all 1-8)")
    args = parser.parse_args()
    arc_nums = args.arcs or list(range(1, 9))

    grand_ch = 0
    grand_panels = 0
    for n in sorted(arc_nums):
        if n not in ARC_CONFIG:
            print(f"Skip unknown arc {n}", file=sys.stderr)
            continue
        ch_count, panel_count = build_arc(n)
        grand_ch += ch_count
        grand_panels += panel_count

    print(f"Done: {len(arc_nums)} arc(s), {grand_ch} chapters, {grand_panels} panels")


if __name__ == "__main__":
    main()
