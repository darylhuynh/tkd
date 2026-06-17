#!/usr/bin/env python3
"""Slice a vertical strip PNG into individual panel files (optional post-approval step).

WARNING: Only works for equal-height grid strips. Dynamic manhwa layouts (splash +
split rows) need manual crop coordinates — do not use equal slicing on those pages.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Slice strip PNG into panel files")
    parser.add_argument("--config", default="", help="strips-arc01-ch01.json path")
    parser.add_argument("--strip-id", required=True, help="Strip id e.g. a")
    parser.add_argument("--strip", required=True, help="Path to strip PNG")
    parser.add_argument("--panels", type=int, default=0, help="Override panel count")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if Image is None:
        raise SystemExit("Install Pillow: pip install Pillow")

    strip_path = Path(args.strip)
    if not strip_path.is_absolute():
        strip_path = ROOT / strip_path
    if not strip_path.exists():
        raise SystemExit(f"Strip not found: {strip_path}")

    config_path = Path(args.config) if args.config else ROOT / "data" / "strips-arc01-ch01.json"
    if not config_path.is_absolute():
        config_path = ROOT / config_path

    cfg: dict = {}
    panel_ids: list[str] = []
    if config_path.exists():
        cfg = json.loads(config_path.read_text(encoding="utf-8"))
        for s in cfg["strips"]:
            if s["id"] == args.strip_id:
                panel_ids = s["panel_ids"]
                break
    if not panel_ids:
        raise SystemExit(f"Strip id {args.strip_id!r} not found in config")

    n = args.panels or len(panel_ids)
    if n != len(panel_ids):
        print(f"Warning: slicing into {n} rows but config has {len(panel_ids)} panel ids")

    img = Image.open(strip_path)
    w, h = img.size
    row_h = h // n
    out_dir = ROOT / "gallery" / "panels" / f"arc-{int(cfg.get('arc', 1)):02d}"
    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(n):
        top = i * row_h
        bottom = h if i == n - 1 else (i + 1) * row_h
        crop = img.crop((0, top, w, bottom))
        pid = panel_ids[i] if i < len(panel_ids) else f"unknown-{i+1}"
        out = out_dir / f"{pid}.png"
        if args.dry_run:
            print(f"Would write {out.relative_to(ROOT)} ({w}x{bottom-top})")
        else:
            crop.save(out)
            print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
