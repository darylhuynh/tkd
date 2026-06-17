#!/usr/bin/env python3
"""Generate panel art from storyboard prompts and wire into arc readers."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORYBOARDS = ROOT / "storyboards"

GLOBAL_STYLE = (
    "manhwa webtoon, vertical comic panel, clean lineart, cel shading, korean sports manhwa, "
    "solo leveling aesthetic, cinematic lighting, sharp focus, detailed background"
)

GLOBAL_NEGATIVE = (
    "photorealistic, 3d render, western comic style, extra limbs, deformed hands, fused fingers, "
    "blurry, watermark, logo, text overlay, speech bubble, low quality, chibi unless specified"
)

PANEL_HEADER = re.compile(r"^### Panel ([\d.]+(?:[a-zA-Z-]+)?) — (.+)$")
CHAPTER_HEADER = re.compile(r"^# Chapter (\d+) — (.+)$")


def storyboard_path(arc: int) -> Path:
    return STORYBOARDS / f"arc-{arc:02d}-panel-storyboard.md"


def panel_out_dir(arc: int) -> Path:
    return ROOT / "gallery" / "panels" / f"arc-{arc:02d}"


def parse_chapter_panels(text: str, chapter: int) -> list[dict]:
    lines = text.splitlines()
    in_chapter = False
    panels: list[dict] = []
    current: dict | None = None
    in_prompt = False
    prompt_lines: list[str] = []

    def flush() -> None:
        nonlocal current, in_prompt, prompt_lines
        if current:
            if prompt_lines:
                current["prompt"] = "\n".join(prompt_lines).strip()
            panels.append(current)
        current = None
        in_prompt = False
        prompt_lines = []

    for line in lines:
        ch = CHAPTER_HEADER.match(line)
        if ch:
            flush()
            num = int(ch.group(1))
            if in_chapter and num != chapter:
                break
            in_chapter = num == chapter
            continue

        if not in_chapter:
            continue

        pm = PANEL_HEADER.match(line)
        if pm:
            flush()
            current = {
                "id": pm.group(1),
                "title": pm.group(2).strip(),
                "prompt": "",
            }
            continue

        if current is None:
            continue

        if line.strip() == "**Prompt:**":
            in_prompt = True
            continue

        if in_prompt:
            if line.strip().startswith("```"):
                if prompt_lines:
                    in_prompt = False
                elif not prompt_lines and line.strip() == "```":
                    continue
                continue
            prompt_lines.append(line)
            continue

        if current is not None and line.strip().startswith("**Prompt:**"):
            inline = line.strip()[len("**Prompt:**") :].strip()
            if inline.startswith("`") and inline.endswith("`"):
                current["prompt"] = inline.strip("`")
            continue

    flush()
    return panels


def full_prompt(panel: dict) -> str:
    body = panel["prompt"].strip()
    if GLOBAL_STYLE not in body:
        body = f"{body}\n{GLOBAL_STYLE}"
    return body


def save_manifest(arc: int, chapter: int, panels: list[dict], path: Path) -> None:
    payload = {
        "arc": arc,
        "chapter": chapter,
        "global_style": GLOBAL_STYLE,
        "global_negative": GLOBAL_NEGATIVE,
        "panels": [
            {
                "id": p["id"],
                "title": p["title"],
                "prompt": full_prompt(p),
                "output": f"gallery/panels/arc-{arc:02d}/{p['id']}.png",
            }
            for p in panels
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def generate_openai(panel: dict, out_path: Path, *, model: str = "gpt-image-1", size: str = "1024x1536") -> bool:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return False

    try:
        from openai import OpenAI
    except ImportError:
        print("Install openai: pip install openai", file=sys.stderr)
        return False

    client = OpenAI(api_key=api_key)
    prompt = full_prompt(panel)
    print(f"  Generating {panel['id']} — {panel['title']}…")

    result = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality="medium",
        n=1,
    )

    item = result.data[0]
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if getattr(item, "b64_json", None):
        import base64

        out_path.write_bytes(base64.b64decode(item.b64_json))
    elif getattr(item, "url", None):
        req = urllib.request.Request(item.url)
        with urllib.request.urlopen(req, timeout=120) as resp:
            out_path.write_bytes(resp.read())
    else:
        print(f"  No image data for {panel['id']}", file=sys.stderr)
        return False

    return True


def generate_chapter(
    arc: int,
    chapter: int,
    *,
    force: bool = False,
    delay: float = 1.0,
    dry_run: bool = False,
) -> int:
    sb = storyboard_path(arc)
    if not sb.exists():
        print(f"Missing storyboard: {sb}", file=sys.stderr)
        return 1

    panels = parse_chapter_panels(sb.read_text(encoding="utf-8"), chapter)
    if not panels:
        print(f"No panels found for arc {arc} chapter {chapter}", file=sys.stderr)
        return 1

    manifest = ROOT / "data" / f"panels-arc{arc:02d}-ch{chapter:02d}.json"
    save_manifest(arc, chapter, panels, manifest)
    print(f"Manifest: {manifest.relative_to(ROOT)} ({len(panels)} panels)")

    out_dir = panel_out_dir(arc)
    out_dir.mkdir(parents=True, exist_ok=True)

    if dry_run:
        for p in panels:
            print(f"  {p['id']}: {p['title']}")
        return 0

    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "Set OPENAI_API_KEY to generate images, or place PNGs in "
            f"{out_dir.relative_to(ROOT)}/{{panel-id}}.png and run build_arc_reader.py",
            file=sys.stderr,
        )
        return 2

    created = 0
    for p in panels:
        out_path = out_dir / f"{p['id']}.png"
        if out_path.exists() and not force:
            print(f"  skip {p['id']} (exists)")
            continue
        if generate_openai(p, out_path):
            created += 1
            if delay:
                time.sleep(delay)

    print(f"Created {created} new panel(s) in {out_dir.relative_to(ROOT)}/")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate panel art from storyboard prompts")
    parser.add_argument("--arc", type=int, default=1)
    parser.add_argument("--chapter", type=int, default=1)
    parser.add_argument("--force", action="store_true", help="Regenerate even if PNG exists")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between API calls")
    parser.add_argument("--dry-run", action="store_true", help="List panels only")
    parser.add_argument("--manifest-only", action="store_true", help="Write manifest JSON only")
    args = parser.parse_args()

    if args.manifest_only:
        sb = storyboard_path(args.arc)
        panels = parse_chapter_panels(sb.read_text(encoding="utf-8"), args.chapter)
        path = ROOT / "data" / f"panels-arc{args.arc:02d}-ch{args.chapter:02d}.json"
        save_manifest(args.arc, args.chapter, panels, path)
        print(f"Wrote {path.relative_to(ROOT)} ({len(panels)} panels)")
        return

    sys.exit(generate_chapter(args.arc, args.chapter, force=args.force, delay=args.delay, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
