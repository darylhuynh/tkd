#!/usr/bin/env python3
"""Trim near-white margins from a strip page and scale to target webtoon width."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore

try:
    import numpy as np
except ImportError:
    np = None  # type: ignore

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


def row_slices(height: int, rows: int) -> list[tuple[int, int]]:
    row_h = height // rows
    slices: list[tuple[int, int]] = []
    for i in range(rows):
        top = i * row_h
        bottom = height if i == rows - 1 else (i + 1) * row_h
        slices.append((top, bottom))
    return slices


def row_content_bbox(
    slab: "np.ndarray",
    white: int = 248,
    col_white_frac: float = 0.92,
    row_white_frac: float = 0.92,
    padding: int = 0,
) -> tuple[int, int, int, int]:
    """BBox of non-letterbox content inside one row."""
    rh, rw, _ = slab.shape
    is_white = (slab[:, :, 0] >= white) & (slab[:, :, 1] >= white) & (slab[:, :, 2] >= white)
    col_frac = is_white.mean(axis=0)
    art_cols = np.where(col_frac < col_white_frac)[0]
    if len(art_cols) == 0:
        return 0, 0, rw, rh
    left, right = int(art_cols[0]), int(art_cols[-1]) + 1
    row_frac = is_white[:, left:right].mean(axis=1)
    art_rows = np.where(row_frac < row_white_frac)[0]
    if len(art_rows) == 0:
        top, bottom = 0, rh
    else:
        top, bottom = int(art_rows[0]), int(art_rows[-1]) + 1
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(rw, right + padding)
    bottom = min(rh, bottom + padding)
    return left, right, top, bottom


def strip_edge_mats(slab: "np.ndarray", white: int = 248, col_white_frac: float = 0.94) -> "np.ndarray":
    """Paint left/right letterbox columns black so they blend with the webtoon reader."""
    out = slab.copy()
    rh, rw, _ = out.shape
    is_white = (out[:, :, 0] >= white) & (out[:, :, 1] >= white) & (out[:, :, 2] >= white)
    col_frac = is_white.mean(axis=0)
    for x in range(rw):
        if col_frac[x] >= col_white_frac:
            out[:, x] = (0, 0, 0)
        else:
            break
    for x in range(rw - 1, -1, -1):
        if col_frac[x] >= col_white_frac:
            out[:, x] = (0, 0, 0)
        else:
            break
    return out


def flood_edge_mats(arr: "np.ndarray", white: int = 246) -> "np.ndarray":
    """Fill near-white regions connected to the image border with black."""
    from collections import deque

    out = arr.copy()
    h, w, _ = out.shape
    is_white = (out[:, :, 0] >= white) & (out[:, :, 1] >= white) & (out[:, :, 2] >= white)
    visited = np.zeros((h, w), dtype=bool)
    q: deque[tuple[int, int]] = deque()

    for x in range(w):
        if is_white[0, x]:
            q.append((x, 0))
        if is_white[h - 1, x]:
            q.append((x, h - 1))
    for y in range(h):
        if is_white[y, 0]:
            q.append((0, y))
        if is_white[y, w - 1]:
            q.append((w - 1, y))

    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or visited[y, x] or not is_white[y, x]:
            continue
        visited[y, x] = True
        out[y, x] = (0, 0, 0)
        q.append((x + 1, y))
        q.append((x - 1, y))
        q.append((x, y + 1))
        q.append((x, y - 1))

    return out


def center_zoom_row(slab: "np.ndarray", keep_frac: float = 0.88) -> "np.ndarray":
    """Crop center portion horizontally and return zoomed slab."""
    rh, rw, _ = slab.shape
    crop_w = max(1, int(rw * keep_frac))
    left = (rw - crop_w) // 2
    return slab[:, left : left + crop_w]


def pad_row_to_width(slab: "np.ndarray", target_width: int, fill: tuple[int, int, int] = (0, 0, 0)) -> "np.ndarray":
    """Place row art on target-width canvas without upscaling."""
    rh, rw, _ = slab.shape
    if rw >= target_width:
        scale = target_width / rw
        new_h = max(1, round(rh * scale))
        return np.array(Image.fromarray(slab).resize((target_width, new_h), Image.Resampling.LANCZOS))
    canvas = np.zeros((rh, target_width, 3), dtype=np.uint8)
    canvas[:, :] = fill
    offset = (target_width - rw) // 2
    canvas[:, offset : offset + rw] = slab
    return canvas


def normalize_per_row(
    img: Image.Image,
    rows: int,
    target_width: int,
    white: int = 248,
    padding: int = 0,
    matte_edges: bool = True,
    row_zoom: dict[int, float] | None = None,
    flood_matte: bool = False,
    pad_only: bool = False,
) -> Image.Image:
    if np is None:
        raise SystemExit("Install numpy for per-row mode: pip install numpy")

    rgb = img.convert("RGB")
    arr = np.array(rgb)
    if flood_matte:
        arr = flood_edge_mats(arr, white=white)
    h, w = arr.shape[:2]
    out_rows: list["np.ndarray"] = []
    zoom_map = row_zoom or {}

    for i, (top, bottom) in enumerate(row_slices(h, rows)):
        slab = arr[top:bottom]
        if i in zoom_map:
            slab = center_zoom_row(slab, keep_frac=zoom_map[i])
        if matte_edges:
            slab = strip_edge_mats(slab, white=white)
        left, right, t, b = row_content_bbox(slab, white=white, padding=padding)
        crop = slab[t:b, left:right]
        if crop.size == 0:
            continue
        ch, cw = crop.shape[:2]
        if pad_only and cw <= target_width:
            row_arr = pad_row_to_width(crop, target_width)
        else:
            scale = target_width / cw
            new_h = max(1, round(ch * scale))
            row_arr = np.array(Image.fromarray(crop).resize((target_width, new_h), Image.Resampling.LANCZOS))
        out_rows.append(row_arr)

    if not out_rows:
        raise SystemExit("Per-row crop produced no rows")

    stacked = np.vstack(out_rows)
    return Image.fromarray(stacked)


def normalize(
    src: Path,
    dst: Path | None = None,
    target_width: int = 1536,
    threshold: int = 242,
    padding: int = 4,
    per_row: bool = False,
    rows: int = 0,
    matte_edges: bool = True,
    row_zoom: dict[int, float] | None = None,
    flood_matte: bool = False,
    pad_only: bool = False,
) -> Path:
    if Image is None:
        raise SystemExit("Install Pillow: pip install Pillow")

    src = src if src.is_absolute() else ROOT / src
    if not src.exists():
        raise SystemExit(f"Not found: {src}")

    img = Image.open(src)
    if flood_matte and np is not None:
        arr = flood_edge_mats(np.array(img.convert("RGB")), white=threshold)
        img = Image.fromarray(arr)
    if per_row:
        if rows <= 0:
            raise SystemExit("--per-row requires --rows N")
        resized = normalize_per_row(
            img,
            rows=rows,
            target_width=target_width,
            white=threshold,
            padding=padding,
            matte_edges=matte_edges,
            row_zoom=row_zoom,
            flood_matte=flood_matte,
            pad_only=pad_only,
        )
        print(f"{src.name}: {img.size} -> per-row x{rows} -> {resized.size}")
    else:
        box = content_bbox(img, threshold=threshold, padding=padding)
        cropped = img.crop(box)
        w, h = cropped.size
        if w <= 0 or h <= 0:
            raise SystemExit("Crop produced empty image")
        scale = target_width / w
        new_h = max(1, round(h * scale))
        resized = cropped.resize((target_width, new_h), Image.Resampling.LANCZOS)
        print(f"{src.name}: {img.size} -> trim {box} -> {cropped.size} -> {resized.size}")

    out = dst if dst else src
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    resized.save(out, optimize=True)
    return out


def rows_from_config(strip_file: str) -> int:
    config_path = ROOT / "data" / "strips-arc01-ch01.json"
    if not config_path.exists():
        return 0
    data = json.loads(config_path.read_text(encoding="utf-8"))
    for strip in data.get("strips", []):
        if strip.get("file") == strip_file:
            return len(strip.get("panel_ids", []))
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Trim margins and normalize strip page width")
    parser.add_argument("strip", help="Path to strip PNG")
    parser.add_argument("--out", default="", help="Output path (default: overwrite)")
    parser.add_argument("--width", type=int, default=1536, help="Target width in px")
    parser.add_argument("--threshold", type=int, default=248, help="Near-white threshold 0-255")
    parser.add_argument("--padding", type=int, default=0, help="Padding px after trim")
    parser.add_argument("--per-row", action="store_true", help="Crop and scale each row independently")
    parser.add_argument("--rows", type=int, default=0, help="Row count for --per-row (default: from strip config)")
    parser.add_argument("--no-matte-edges", action="store_true", help="Skip painting side letterbox columns black")
    parser.add_argument("--flood-matte", action="store_true", help="Flood-fill border-connected white to black")
    parser.add_argument("--row1-zoom", type=float, default=0.0, help="Center-crop zoom for row 1 (e.g. 0.82)")
    parser.add_argument("--pad-only", action="store_true", help="Crop letterbox then pad to width (no upscale)")
    args = parser.parse_args()

    rows = args.rows
    if args.per_row and rows <= 0:
        rows = rows_from_config(Path(args.strip).name)

    row_zoom = {0: args.row1_zoom} if args.row1_zoom > 0 else None

    normalize(
        Path(args.strip),
        Path(args.out) if args.out else None,
        target_width=args.width,
        threshold=args.threshold,
        padding=args.padding,
        per_row=args.per_row,
        rows=rows,
        matte_edges=not args.no_matte_edges,
        row_zoom=row_zoom,
        flood_matte=args.flood_matte,
        pad_only=args.pad_only,
    )


if __name__ == "__main__":
    main()
