#!/usr/bin/env python3
"""Generate one manhwa PAGE PNG from data/manhwa-pages-arc{AA}-ch{CC}.json via OpenAI Images API."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def config_path(arc: int, chapter: int) -> Path:
    return ROOT / "data" / f"manhwa-pages-arc{arc:02d}-ch{chapter:02d}.json"


def load_page(arc: int, chapter: int, page_id: str) -> dict:
    path = config_path(arc, chapter)
    if not path.exists():
        raise SystemExit(f"Missing {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    for page in data.get("pages", []):
        if page["id"] == page_id:
            return page
    raise SystemExit(f"Page id {page_id!r} not found in {path.name}")


def resolve_ref(rel: str) -> Path:
    p = ROOT / rel.replace("/", os.sep)
    if not p.exists():
        print(f"Warning: reference missing: {p.relative_to(ROOT)}", file=sys.stderr)
    return p


def generate_openai(prompt: str, out_path: Path, *, model: str, size: str, quality: str) -> bool:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY for API generation.", file=sys.stderr)
        return False
    try:
        from openai import OpenAI
    except ImportError:
        print("Install openai: pip install openai", file=sys.stderr)
        return False

    client = OpenAI(api_key=api_key)
    print(f"Generating via {model} ({size}, quality={quality})…")
    result = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )
    item = result.data[0]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if getattr(item, "b64_json", None):
        out_path.write_bytes(base64.b64decode(item.b64_json))
    elif getattr(item, "url", None):
        req = urllib.request.Request(item.url)
        with urllib.request.urlopen(req, timeout=120) as resp:
            out_path.write_bytes(resp.read())
    else:
        print("No image data in response", file=sys.stderr)
        return False
    print(f"Wrote {out_path.relative_to(ROOT)}")
    return True


def sync_strips_manifest(arc: int, chapter: int) -> None:
    """Update data/strips-arc{AA}-ch{CC}.json from manhwa-pages config."""
    cfg_path = config_path(arc, chapter)
    if not cfg_path.exists():
        return
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    strips = []
    for page in cfg.get("pages", []):
        strips.append(
            {
                "id": page["id"],
                "file": page["output"],
                "label": page["label"],
                "panel_ids": page.get("panel_ids", []),
            }
        )
    out = {
        "arc": arc,
        "chapter": chapter,
        "title": cfg.get("title", f"Chapter {chapter}"),
        "strip_dir": cfg.get("strip_dir", f"gallery/strips/arc-{arc:02d}"),
        "layout": "dynamic-manhwa",
        "strips": strips,
    }
    strip_path = ROOT / "data" / f"strips-arc{arc:02d}-ch{chapter:02d}.json"
    strip_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Synced {strip_path.relative_to(ROOT)} ({len(strips)} pages)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate manhwa page art")
    parser.add_argument("--arc", type=int, required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--page", required=True, help="Page id e.g. page1, page2")
    parser.add_argument("--model", default="gpt-image-1")
    parser.add_argument("--size", default="1024x1536", help="Vertical: 1024x1536")
    parser.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    parser.add_argument("--dry-run", action="store_true", help="Print prompt and refs only")
    parser.add_argument("--sync-strips", action="store_true", help="Update strips JSON from pages config")
    args = parser.parse_args()

    if args.sync_strips:
        sync_strips_manifest(args.arc, args.chapter)
        if not args.page:
            return

    page = load_page(args.arc, args.chapter, args.page)
    cfg = json.loads(config_path(args.arc, args.chapter).read_text(encoding="utf-8"))
    strip_dir = ROOT / cfg.get("strip_dir", f"gallery/strips/arc-{args.arc:02d}")
    out_path = strip_dir / page["output"]

    refs = [resolve_ref(r) for r in page.get("reference_images", [])]
    anchor = page.get("style_anchor")
    if anchor:
        refs.append(resolve_ref(anchor))

    print(f"Page: {page['label']}")
    print(f"Output: {out_path.relative_to(ROOT)}")
    print(f"Panel IDs: {', '.join(page.get('panel_ids', []))}")
    print("References:")
    for r in refs:
        print(f"  - {r.relative_to(ROOT) if r.is_relative_to(ROOT) else r}")

    if args.dry_run:
        print("\n--- PROMPT ---\n")
        print(page["prompt"])
        print("\nUse Cursor GenerateImage with reference_image_paths for best continuity.")
        return

    if not generate_openai(page["prompt"], out_path, model=args.model, size=args.size, quality=args.quality):
        sys.exit(1)

    sync_strips_manifest(args.arc, args.chapter)


if __name__ == "__main__":
    main()
