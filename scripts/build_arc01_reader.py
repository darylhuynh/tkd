#!/usr/bin/env python3
"""Parse Arc 1 panel storyboard and generate chapter reader HTML pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORYBOARD = ROOT / "storyboards" / "arc-01-panel-storyboard.md"
ARC_MD = ROOT / "arcs" / "arc-01-new-beginnings.md"
OUT_DIR = ROOT / "arcs" / "new-beginnings"
DATA_OUT = ROOT / "data" / "arc-01.json"
PANEL_IMG_DIR = ROOT / "gallery" / "panels" / "arc-01"

CHAPTER_TITLES = {
    1: "Nightmare",
    2: "Arrival at Kwon's",
    3: "Meeting Master Viet",
    4: "Training Demonstration",
    5: "The Goal",
    6: "Why Did You Leave?",
    7: "Flashbacks Begin",
    8: "Hospital Visit",
    9: "Can They Come Too?",
    10: "Welcome to Kwon's",
}


def slug(ch: int) -> str:
    return f"chapter-{ch:02d}"


def panel_image(panel_id: str) -> str | None:
    for ext in (".png", ".jpg", ".webp"):
        path = PANEL_IMG_DIR / f"{panel_id}{ext}"
        if path.exists():
            return "../../" + path.relative_to(ROOT).as_posix()
    return None


def parse_storyboard(text: str) -> list[dict]:
    chapters: list[dict] = []
    current_ch: dict | None = None
    current_panel: dict | None = None
    in_prompt = False
    prompt_lines: list[str] = []

    def flush_panel() -> None:
        nonlocal current_panel, in_prompt, prompt_lines
        if current_panel and current_ch is not None:
            if prompt_lines:
                current_panel["prompt"] = "\n".join(prompt_lines).strip()
            pid = current_panel["id"]
            current_panel["image"] = panel_image(pid)
            current_ch["panels"].append(current_panel)
        current_panel = None
        in_prompt = False
        prompt_lines = []

    for line in text.splitlines():
        ch_match = re.match(r"^# Chapter (\d+) — (.+)$", line)
        if ch_match:
            flush_panel()
            num = int(ch_match.group(1))
            current_ch = {
                "num": num,
                "title": CHAPTER_TITLES.get(num, ch_match.group(2).strip()),
                "slug": slug(num),
                "panels": [],
            }
            chapters.append(current_ch)
            continue

        panel_match = re.match(r"^### Panel ([\d.]+(?:[a-zA-Z-]+)?) — (.+)$", line)
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
                break

    flush_panel()
    return chapters


def arc_summary() -> str:
    text = ARC_MD.read_text(encoding="utf-8")
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
    if "FLASH" in panel.get("timeline", "") or "FLASH" in panel.get("title", ""):
        tags.append('<span class="panel-tag flash">FLASH</span>')
    if "[CARD]" in panel.get("title", ""):
        tags.append('<span class="panel-tag card">CARD</span>')
    if "[TEACH]" in panel.get("title", ""):
        tags.append('<span class="panel-tag teach">TEACH</span>')

    tag_html = f'<div class="panel-tags">{"".join(tags)}</div>' if tags else ""

    img_block = ""
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


def write_index(chapters: list[dict]) -> None:
    summary = html.escape(arc_summary())
    cards = []
    for ch in chapters:
        cards.append(f"""
        <a class="chapter-card" href="{ch["slug"]}.html">
          <span class="chapter-num">Chapter {ch["num"]}</span>
          <h2>{html.escape(ch["title"])}</h2>
          <span class="chapter-panels">{len(ch["panels"])} panels</span>
        </a>""")

    page = reader_head("Arc 1 — New Beginnings", depth=2)
    page += f"""
  <header class="reader-header">
    <div class="reader-header-inner">
      <a class="reader-back" href="../../index.html#arcs">← Taekwondo Legends</a>
      <p class="reader-arc-label">Arc 01</p>
      <h1>New Beginnings</h1>
      <p class="reader-summary">{summary}</p>
      <p class="reader-meta">Chapters 1–10 · {sum(len(c["panels"]) for c in chapters)} storyboard panels</p>
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
    (OUT_DIR / "index.html").write_text(page, encoding="utf-8")


def write_chapter(ch: dict, chapters: list[dict]) -> None:
    prev_link = ""
    next_link = ""
    idx = ch["num"] - 1
    if idx > 0:
        prev_ch = chapters[idx - 1]
        prev_link = f'<a class="nav-prev" href="{prev_ch["slug"]}.html">← Ch {prev_ch["num"]}: {html.escape(prev_ch["title"])}</a>'
    if idx < len(chapters) - 1:
        next_ch = chapters[idx + 1]
        next_link = f'<a class="nav-next" href="{next_ch["slug"]}.html">Ch {next_ch["num"]}: {html.escape(next_ch["title"])} →</a>'

    panels_html = "\n".join(render_panel(p) for p in ch["panels"])
    title = f"Ch {ch['num']} — {ch['title']}"

    page = reader_head(title, depth=2)
    page += f"""
  <header class="reader-header reader-header--chapter">
    <div class="reader-header-inner">
      <a class="reader-back" href="index.html">← Arc 1: New Beginnings</a>
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
    (OUT_DIR / f"{ch['slug']}.html").write_text(page, encoding="utf-8")


def main() -> None:
    text = STORYBOARD.read_text(encoding="utf-8")
    chapters = parse_storyboard(text)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PANEL_IMG_DIR.mkdir(parents=True, exist_ok=True)

    DATA_OUT.parent.mkdir(parents=True, exist_ok=True)
    DATA_OUT.write_text(json.dumps({"arc": 1, "title": "New Beginnings", "chapters": chapters}, indent=2) + "\n", encoding="utf-8")

    write_index(chapters)
    for ch in chapters:
        write_chapter(ch, chapters)

    total = sum(len(c["panels"]) for c in chapters)
    print(f"Wrote {OUT_DIR.relative_to(ROOT)}/ ({len(chapters)} chapters, {total} panels)")


if __name__ == "__main__":
    main()
