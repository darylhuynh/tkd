#!/usr/bin/env python3
"""Build strip-mode chapter reader (vertical webtoon pages + optional footnotes)."""

from __future__ import annotations

import argparse
import html
import json
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
        version = int(full.stat().st_mtime)
        return f"../../{rel.as_posix()}?v={version}", True
    return None, False


def render_panel_footnote(panel: dict) -> str:
    parts = []
    title = panel.get("title", "")
    if title:
        parts.append(
            f'<p class="manhwa-footnote-id"><strong>{html.escape(panel["id"])}</strong> — {html.escape(title)}</p>'
        )
    else:
        parts.append(f'<p class="manhwa-footnote-id"><strong>{html.escape(panel["id"])}</strong></p>')
    scene = panel.get("scene") or panel.get("prompt", "").split("\n")[0][:300]
    if scene:
        parts.append(f'<p class="manhwa-footnote-scene">{html.escape(scene)}</p>')
    dialogue = panel.get("dialogue", "")
    if dialogue and dialogue not in ("*(none)*", "(none)"):
        parts.append(f'<p class="manhwa-footnote-dialogue">{html.escape(dialogue)}</p>')
    sfx = panel.get("sfx", "")
    if sfx and sfx not in ("*(none — silence)*", "*(none)*"):
        parts.append(f'<p class="manhwa-footnote-sfx">{html.escape(sfx)}</p>')
    return f'<div class="manhwa-footnote-panel">{"".join(parts)}</div>'


def render_strip_footnote(label: str, panel_ids: list[str], panels_by_id: dict[str, dict], note: str = "") -> str:
    panels_html = ""
    for pid in panel_ids:
        p = panels_by_id.get(pid)
        if p:
            panels_html += render_panel_footnote(p)
        else:
            panels_html += f'<div class="manhwa-footnote-panel"><p class="manhwa-footnote-id">{html.escape(pid)}</p></div>'
    note_html = f'<p class="manhwa-footnote-note">{html.escape(note)}</p>' if note else ""
    return f"""
<section class="manhwa-footnote-section">
  <h2 class="manhwa-footnote-heading">{html.escape(label)}</h2>
  {note_html}
  {panels_html}
</section>"""


def build_webtoon_blocks(
    config: dict,
    panels_by_id: dict[str, dict],
    strip_dir: str,
) -> tuple[list[str], list[str], int, int]:
    """Return (image_blocks, footnote_blocks, live_count, missing_count)."""
    image_blocks: list[str] = []
    footnote_blocks: list[str] = []
    live = 0
    missing = 0

    for strip in config["strips"]:
        if strip.get("skip"):
            continue
        src, ok = strip_image_path(strip_dir, strip["file"])
        label = strip.get("label", strip["id"])
        pending = strip.get("pending", False)
        panel_ids = strip.get("panel_ids", [])

        if ok and src and not pending:
            live += 1
            image_blocks.append(
                f'<figure class="manhwa-page" id="manhwa-{html.escape(strip["id"])}">'
                f'<img src="{html.escape(src)}" alt="{html.escape(label)}" loading="lazy" class="manhwa-page-img">'
                f"</figure>"
            )
        else:
            missing += 1
            reason = "Art coming soon." if pending else "Art not yet generated."
            footnote_blocks.append(
                render_strip_footnote(label, panel_ids, panels_by_id, reason)
            )

    for skipped in config.get("skipped_strips") or []:
        pass  # skipped pages are omitted from the reader entirely

    return image_blocks, footnote_blocks, live, missing


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

    layout = config.get("layout", "webtoon")
    image_blocks, footnote_blocks, live, missing = build_webtoon_blocks(
        config, panels_by_id, strip_dir
    )

    footnotes_html = ""
    if footnote_blocks:
        footnotes_html = f"""
  <aside class="manhwa-footnotes" aria-label="Script notes for unreleased pages">
    <p class="manhwa-footnotes-label">Unreleased — script reference</p>
    {"".join(footnote_blocks)}
  </aside>"""

    ch_slug = f"chapter-{chapter:02d}"
    reader_file = config.get("reader", f"{ch_slug}-strip.html")
    script_reader = config.get("script_reader", f"{ch_slug}.html")
    page_path = out_dir / reader_file
    strip_alias = out_dir / f"{ch_slug}-strip.html"
    arc_label = f"{arc:02d}"

    body_class = "reader-page reader-page--manhwa" if layout != "strip" else "reader-page reader-page--strip"

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
<body class="{body_class}">

  <header class="reader-header reader-header--manhwa">
    <div class="reader-header-inner">
      <a class="reader-back" href="index.html">← Arc {arc_label}</a>
      <span class="reader-manhwa-title">Ch {chapter} · {html.escape(ch_title)}</span>
      <a class="reader-manhwa-script" href="{script_reader}">Script</a>
    </div>
  </header>

  <main class="webtoon-manhwa">
    {"".join(image_blocks)}
  </main>
  {footnotes_html}

  <nav class="chapter-nav chapter-nav--manhwa">
    <a class="nav-next" href="chapter-02.html">Ch 2: Arrival at Kwon&#x27;s →</a>
  </nav>
</body>
</html>
"""
    page_path.write_text(page, encoding="utf-8")
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
    print(f"Wrote {page_path.relative_to(ROOT)} ({live} pages, {missing} footnotes)")
    return page_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build strip-mode chapter reader")
    parser.add_argument("--arc", type=int, required=True)
    parser.add_argument("--chapter", type=int, required=True)
    args = parser.parse_args()
    build(args.arc, args.chapter)


if __name__ == "__main__":
    main()
