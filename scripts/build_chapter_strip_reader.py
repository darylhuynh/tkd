#!/usr/bin/env python3
"""Build strip-mode chapter reader (vertical strip PNGs + dialogue blocks)."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ARC_OUT: dict[int, str] = {
    1: "new-beginnings",
    2: "the-team",
    3: "first-tournament",
    4: "shadow-school",
    5: "road-to-korea",
    6: "korea-regionals",
    7: "legends",
    8: "closure",
}

ARC_LABEL: dict[int, str] = {
    1: "New Beginnings",
    2: "The Team",
    3: "First Tournament",
    4: "Shadow School",
    5: "Road to Korea",
    6: "Korea Regionals",
    7: "Legends",
    8: "Closure",
}


def load_panels(arc: int, chapter: int) -> dict[str, dict]:
    path = ROOT / "data" / f"panels-arc{arc:02d}-ch{chapter:02d}.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {p["id"]: p for p in data.get("panels", [])}


def load_chapter_title(arc: int, chapter: int) -> str:
    panels_path = ROOT / "data" / f"arc-{arc:02d}.json"
    if panels_path.exists():
        data = json.loads(panels_path.read_text(encoding="utf-8"))
        for ch in data.get("chapters", []):
            if ch.get("num") == chapter:
                return ch.get("title", f"Chapter {chapter}")
    return f"Chapter {chapter}"


def strip_image_path(strip_dir: str, filename: str) -> tuple[str | None, bool]:
    rel = Path(strip_dir) / filename
    full = ROOT / rel
    if full.exists():
        return "../../" + rel.as_posix(), True
    return None, False


def render_panel_copy(panel: dict) -> str:
    parts = []
    if panel.get("title"):
        parts.append(f'<p class="strip-panel-id"><strong>{html.escape(panel["id"])}</strong> — {html.escape(panel["title"])}</p>')
    scene = panel.get("scene") or panel.get("prompt", "").split("\n")[0][:200]
    if scene:
        parts.append(f'<p class="panel-scene">{html.escape(scene)}</p>')
    dialogue = panel.get("dialogue", "")
    if dialogue and dialogue not in ("*(none)*", "(none)"):
        parts.append(f'<p class="panel-dialogue">{html.escape(dialogue)}</p>')
    sfx = panel.get("sfx", "")
    if sfx and sfx not in ("*(none — silence)*", "*(none)*"):
        parts.append(f'<p class="panel-sfx">{html.escape(sfx)}</p>')
    return "\n".join(parts)


def build(arc: int, chapter: int) -> Path:
    config_path = ROOT / "data" / f"strips-arc{arc:02d}-ch{chapter:02d}.json"
    if not config_path.exists():
        raise SystemExit(f"Missing strip config: {config_path.relative_to(ROOT)}")

    config = json.loads(config_path.read_text(encoding="utf-8"))
    panels_by_id = load_panels(arc, chapter)
    out_slug = ARC_OUT[arc]
    out_dir = ROOT / "arcs" / out_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    ch_title = config.get("title") or load_chapter_title(arc, chapter)
    strip_dir = config.get("strip_dir", f"gallery/strips/arc-{arc:02d}")
    (ROOT / strip_dir).mkdir(parents=True, exist_ok=True)

    strip_blocks: list[str] = []
    missing = 0
    live = 0
    for strip in config["strips"]:
        if strip.get("skip"):
            continue
        src, ok = strip_image_path(strip_dir, strip["file"])
        label = html.escape(strip.get("label", strip["id"]))
        pending = strip.get("pending", False)
        if ok and src and not pending:
            live += 1
            img = f'<img src="{html.escape(src)}" alt="{label}" loading="lazy" class="strip-art-img">'
        else:
            missing += 1
            reason = "Coming soon" if pending else f'Drop <code>{html.escape(strip["file"])}</code> into <code>{html.escape(strip_dir)}/</code>'
            img = f"""<div class="strip-art strip-art--empty">
              <span class="strip-id">{html.escape(strip["id"].upper())}</span>
              <span>{reason}</span>
            </div>"""

        dialogue_parts = []
        for pid in strip.get("panel_ids", []):
            p = panels_by_id.get(pid)
            if p:
                dialogue_parts.append(f'<div class="strip-panel-script">{render_panel_copy(p)}</div>')
            else:
                dialogue_parts.append(
                    f'<div class="strip-panel-script"><p class="strip-panel-id">{html.escape(pid)}</p></div>'
                )

        strip_blocks.append(f"""
<section class="strip-segment" id="strip-{html.escape(strip["id"])}">
  <header class="strip-segment-header">
    <h2>{label}</h2>
    <p class="strip-segment-meta">{len(strip.get("panel_ids", []))} panels · {", ".join(html.escape(x) for x in strip["panel_ids"])}</p>
  </header>
  <figure class="strip-art">{img}</figure>
  <div class="strip-script">
    <p class="strip-script-label">Script (not in image)</p>
    {"".join(dialogue_parts)}
  </div>
</section>""")

    ch_slug = f"chapter-{chapter:02d}"
    reader_file = config.get("reader", f"{ch_slug}-strip.html")
    script_reader = config.get("script_reader", f"{ch_slug}.html")
    page_path = out_dir / reader_file
    strip_alias = out_dir / f"{ch_slug}-strip.html"
    arc_label = f"{arc:02d}"

    skipped = config.get("skipped_strips") or []
    skipped_note = ""
    if skipped:
        items = "".join(
            f"<li><strong>{html.escape(s.get('label', s['id']))}</strong>"
            f"{': ' + html.escape(s['note']) if s.get('note') else ''}</li>"
            for s in skipped
        )
        skipped_note = f"""
  <aside class="reader-skipped-note">
    <p class="reader-skipped-note__title">Not in this build</p>
    <ul>{items}</ul>
  </aside>"""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ch {chapter} — {html.escape(ch_title)} · Taekwondo Legends</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/pitch.css">
  <link rel="stylesheet" href="../../assets/css/reader.css">
</head>
<body class="reader-page reader-page--strip">

  <header class="reader-header reader-header--chapter">
    <div class="reader-header-inner">
      <a class="reader-back" href="index.html">← Arc {arc_label}: {html.escape(ARC_LABEL[arc])}</a>
      <p class="reader-arc-label">Chapter {chapter}</p>
      <h1>{html.escape(ch_title)}</h1>
      <p class="reader-meta">{live} pages live · {missing} coming soon · <a href="{script_reader}">Full script</a></p>
    </div>
  </header>

  <nav class="chapter-nav chapter-nav--strip">
    <a class="nav-next" href="chapter-02.html">Ch 2: Arrival at Kwon&#x27;s →</a>
  </nav>

  <main class="webtoon-strip-scroll">
    {skipped_note}
    {"".join(strip_blocks)}
  </main>

  <nav class="chapter-nav chapter-nav--bottom">
    <a class="nav-next" href="chapter-02.html">Ch 2: Arrival at Kwon&#x27;s →</a>
  </nav>
</body>
</html>
"""
    page_path.write_text(page, encoding="utf-8")
    # Back-compat alias for old strip URL
    redirect = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={reader_file}">
  <link rel="canonical" href="{reader_file}">
  <title>Redirecting…</title>
</head>
<body><p><a href="{reader_file}">Continue to Chapter {chapter}</a></p></body>
</html>
"""
    strip_alias.write_text(redirect, encoding="utf-8")
    print(f"Wrote {page_path.relative_to(ROOT)} ({live} live, {missing} pending)")
    return page_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build strip-mode chapter reader")
    parser.add_argument("--arc", type=int, required=True)
    parser.add_argument("--chapter", type=int, required=True)
    args = parser.parse_args()
    build(args.arc, args.chapter)


if __name__ == "__main__":
    main()
