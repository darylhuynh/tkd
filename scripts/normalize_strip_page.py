#!/usr/bin/env python3
"""Trim near-white margins from a strip page and scale to target webtoon width."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


def content_bbox(img: Image.Image, threshold: int = 242, padding: int = 4) -> tuple[int, int, int, int]:
    rgb = img.convert("RGB")
    w, h = rgb.size
    pixels = rgb.load()
    min_x, min_y = w, h
    max_x, max_y = 0, 0
    found = False
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                continue
            found = True
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    if not found:
        return 0, 0, w, h
    left = max(0, min_x - padding)
    top = max(0, min_y - padding)
    right = min(w, max_x + padding + 1)
    bottom = min(h, max_y + padding + 1)
    return left, top, right, bottom


def normalize(
    src: Path,
    dst: Path | None = None,
    target_width: int = 1536,
    threshold: int = 242,
    padding: int = 4,
) -> Path:
    if Image is None:
        raise SystemExit("Install Pillow: pip install Pillow")

    src = src if src.is_absolute() else ROOT / src
    if not src.exists():
        raise SystemExit(f"Not found: {src}")

    img = Image.open(src)
    box = content_bbox(img, threshold=threshold, padding=padding)
    cropped = img.crop(box)
    w, h = cropped.size
    if w <= 0 or h <= 0:
        raise SystemExit("Crop produced empty image")

    scale = target_width / w
    new_h = max(1, round(h * scale))
    resized = cropped.resize((target_width, new_h), Image.Resampling.LANCZOS)

    out = dst if dst else src
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    resized.save(out, optimize=True)
    print(f"{src.name}: {img.size} -> trim {box} -> {cropped.size} -> {resized.size}")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Trim margins and normalize strip page width")
    parser.add_argument("strip", help="Path to strip PNG")
    parser.add_argument("--out", default="", help="Output path (default: overwrite)")
    parser.add_argument("--width", type=int, default=1536, help="Target width in px")
    parser.add_argument("--threshold", type=int, default=242, help="White pixel threshold 0-255")
    parser.add_argument("--padding", type=int, default=4, help="Padding px after trim")
    args = parser.parse_args()

    normalize(
        Path(args.strip),
        Path(args.out) if args.out else None,
        target_width=args.width,
        threshold=args.threshold,
        padding=args.padding,
    )


if __name__ == "__main__":
    main()
