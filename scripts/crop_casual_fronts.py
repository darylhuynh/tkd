#!/usr/bin/env python3
"""Crop multi-view turnaround sheets into single front portraits."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reference-sheets" / "output"

# character_id -> number of horizontal panels in casual-front.png
PANELS = {
    "ethan-hyun": 3,
    "tj-lim": 3,
    "kieryn-lim": 3,
    "logan-hyun": 3,
    "kian-sang": 5,
    "yuna-park": 3,
    "ttong-kim": 3,
    "repeul-kim": 4,
}


def crop_front(char_id: str, panels: int) -> None:
    char_dir = OUTPUT / char_id
    front_path = char_dir / "casual-front.png"
    if not front_path.exists():
        print(f"SKIP {char_id}: no casual-front.png")
        return

    backup = char_dir / "casual-turnaround.png"
    if not backup.exists():
        front_path.replace(backup)
        src = backup
    else:
        src = backup

    img = Image.open(src)
    w, h = img.size
    panel_w = w // panels
    cropped = img.crop((0, 0, panel_w, h))
    cropped.save(front_path, format="PNG", optimize=True)
    print(f"OK {char_id}: {w}x{h} -> front {panel_w}x{h} ({panels} panels)")


def main() -> None:
    for char_id, panels in PANELS.items():
        crop_front(char_id, panels)


if __name__ == "__main__":
    main()
