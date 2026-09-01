#!/usr/bin/env python3
"""Build Level 13 contact sheets and machine-readable master diagnostics."""

from __future__ import annotations

from collections import deque
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
STORIES = ROOT / "Stories"
QA = STORIES / "Level 13 Art QA"
ANCHORS = QA / "Anchors"

SETS = [
    ("The Funny Fetch", "the_funny_fetch"),
    ("The Silly Story", "the_silly_story"),
    ("The Leaf Stamp", "the_leaf_stamp"),
    ("The Match Judge", "the_match_judge"),
    ("The Kind Note", "the_kind_note"),
    ("The Colt and the Brush", "the_colt_and_the_brush"),
    ("The Gold Puzzle", "the_gold_puzzle"),
    ("The Little Bunny", "the_little_bunny"),
    ("The Bottle Flip", "the_bottle_flip"),
    ("The Puppy and the Drum", "the_puppy_and_the_drum"),
]

ANCHOR_PATHS = [
    ANCHORS / "anchor_story_pip_the_pig.png",
    ANCHORS / "anchor_story_the_dig.png",
    ANCHORS / "anchor_level_1_card.png",
    ANCHORS / "anchor_level_2_card.png",
]


def master_paths() -> list[Path]:
    paths: list[Path] = []
    for folder, slug in SETS:
        base = STORIES / folder
        paths.extend(
            [
                base / f"story_{slug}.png",
                base / f"comp_{slug}_0.png",
                base / f"comp_{slug}_1.png",
                base / f"comp_{slug}_2.png",
            ]
        )
    return paths


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def connected_white_field(image: Image.Image) -> dict[str, object]:
    """Measure the exact #FFFFFF component that reaches the canvas edges."""
    width, height = image.size
    pixels = image.load()
    edge_points = (
        [(x, 0) for x in range(width)]
        + [(width - 1, y) for y in range(height)]
        + [(x, height - 1) for x in range(width)]
        + [(0, y) for y in range(height)]
    )
    seeds = [point for point in edge_points if pixels[point] == (255, 255, 255)]
    if not seeds:
        return {
            "exact_white_component_reaches_all_four_edges": False,
            "exact_white_component_fraction": 0.0,
            "exact_white_edge_fraction": 0.0,
        }

    queue = deque(seeds)
    seen = set(seeds)
    touches = {"top": False, "right": False, "bottom": False, "left": False}
    while queue:
        x, y = queue.popleft()
        if y == 0:
            touches["top"] = True
        if x == width - 1:
            touches["right"] = True
        if y == height - 1:
            touches["bottom"] = True
        if x == 0:
            touches["left"] = True
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            point = (nx, ny)
            if (
                0 <= nx < width
                and 0 <= ny < height
                and point not in seen
                and pixels[point] == (255, 255, 255)
            ):
                seen.add(point)
                queue.append(point)

    unique_edge_points = set(edge_points)
    white_edge_count = sum(pixels[point] == (255, 255, 255) for point in unique_edge_points)
    return {
        "exact_white_component_reaches_all_four_edges": all(touches.values()),
        "exact_white_component_fraction": round(len(seen) / (width * height), 6),
        "exact_white_edge_fraction": round(white_edge_count / len(unique_edge_points), 6),
    }


def diagnostics(path: Path) -> dict[str, object]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
        width, height = image.size
        nonwhite = Image.new("1", image.size)
        nonwhite.putdata([1 if min(rgb) < 245 else 0 for rgb in image.getdata()])
        bbox = nonwhite.getbbox()
        margins = None
        if bbox:
            margins = {
                "left": bbox[0],
                "top": bbox[1],
                "right": width - bbox[2],
                "bottom": height - bbox[3],
            }
        report = {
            "path": str(path.relative_to(ROOT)),
            "width": width,
            "height": height,
            "mode": opened.mode,
            "format": opened.format,
            "sha256": sha256(path),
            "nonwhite_bbox_margins": margins,
        }
        report.update(connected_white_field(image))
        report["machine_contract_pass"] = bool(
            width == 600
            and height == 600
            and opened.format == "PNG"
            and report["exact_white_component_reaches_all_four_edges"]
        )
        return report


def font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def sheet(paths: list[Path], target: Path, tile: int, label_h: int) -> None:
    cols = 4
    rows = (len(paths) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * tile, rows * (tile + label_h)), "white")
    draw = ImageDraw.Draw(canvas)
    label_font = font(max(10, label_h - 9))
    for index, path in enumerate(paths):
        row, col = divmod(index, cols)
        with Image.open(path) as opened:
            image = opened.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        x = col * tile
        y = row * (tile + label_h)
        canvas.paste(image, (x, y))
        draw.rectangle((x, y, x + tile - 1, y + tile - 1), outline=(215, 215, 215), width=1)
        draw.text((x + 5, y + tile + 2), path.stem, fill=(35, 35, 35), font=label_font)
    canvas.save(target, "PNG")


def main() -> None:
    paths = master_paths()
    required = ANCHOR_PATHS + paths
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("Missing required images:\n" + "\n".join(missing))
    reports = [diagnostics(path) for path in paths]
    payload = {
        "accepted_master_count": len(paths),
        "all_machine_contracts_pass": all(item["machine_contract_pass"] for item in reports),
        "masters": reports,
    }
    (QA / "LEVEL_13_MASTER_DIAGNOSTICS.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    comparison = ANCHOR_PATHS + paths
    sheet(comparison, QA / "LEVEL_13_ART_CONTACT_SHEET_FULL.png", tile=300, label_h=32)
    sheet(comparison, QA / "LEVEL_13_ART_CONTACT_SHEET_CARD.png", tile=120, label_h=21)
    print(json.dumps({
        "accepted_master_count": len(paths),
        "all_machine_contracts_pass": payload["all_machine_contracts_pass"],
        "failed": [item["path"] for item in reports if not item["machine_contract_pass"]],
    }, indent=2))


if __name__ == "__main__":
    main()
