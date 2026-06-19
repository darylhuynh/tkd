#!/usr/bin/env python3
"""Trim excess white margins from portrait PNGs so card crops frame consistently."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reference-sheets" / "output"

# Portrait files used on fighter cards (from build_pitch_site resolve_portrait)
PORTRAITS = [
    "ethan-hyun/casual-front.png",
    "tj-lim/casual-front.png",
    "kieryn-lim/casual-front.png",
    "logan-hyun/casual-front.png",
    "kian-sang/casual-front.png",
    "ariana-yang/casual-front.png",
    "master-viet/casual-front.png",
    "yuna-park/casual-front.png",
    "ttong-kim/casual-front.png",
    "yeo-woo-kim/casual-front.png",
    "derek-cole/dobok-front.png",
    "maya-ortiz/dobok-front.png",
    "lee-ji-woo/dobok-front.png",
    "kim-min-ho/dobok-front.png",
    "han-do-won/dobok-front.png",
    "park-sung-min/dobok-front.png",
]

WHITE_THRESHOLD = 735
MIN_WIDTH_FILL = 0.42  # trim if character uses less than 42% of canvas width
PAD_RATIO = 0.04


def content_bbox(img: Image.Image) -> tuple[int, int, int, int] | None:
    rgb = img.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    minx, miny, maxx, maxy = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r + g + b < WHITE_THRESHOLD:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
    if maxx <= minx or maxy <= miny:
        return None
    return minx, miny, maxx + 1, maxy + 1


def trim_file(path: Path) -> bool:
    img = Image.open(path)
    bbox = content_bbox(img)
    if not bbox:
        print(f"SKIP {path.name}: no content")
        return False

    w, h = img.size
    minx, miny, maxx, maxy = bbox
    cw = maxx - minx
    if cw / w >= MIN_WIDTH_FILL:
        print(f"OK   {path.parent.name}/{path.name}: already tight ({100 * cw / w:.0f}% fill)")
        return False

    pad_x = int(cw * PAD_RATIO)
    pad_y = int((maxy - miny) * PAD_RATIO)
    crop = (
        max(0, minx - pad_x),
        max(0, miny - pad_y),
        min(w, maxx + pad_x),
        min(h, maxy + pad_y),
    )
    backup = path.with_name(path.stem + ".pre-trim.png")
    if not backup.exists():
        path.replace(backup)
        src = backup
    else:
        src = backup

    trimmed = Image.open(src).crop(crop)
    trimmed.save(path, format="PNG", optimize=True)
    tw, th = trimmed.size
    print(f"TRIM {path.parent.name}/{path.name}: {w}x{h} -> {tw}x{th}")
    return True


def main() -> None:
    changed = 0
    for rel in PORTRAITS:
        path = OUTPUT / rel
        if path.exists() and trim_file(path):
            changed += 1
    print(f"Done — trimmed {changed} portrait(s)")


if __name__ == "__main__":
    main()
