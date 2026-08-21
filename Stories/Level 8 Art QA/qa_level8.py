#!/usr/bin/env python3
"""Build Level 8 QA contact sheets and machine-readable master diagnostics."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
STORIES = ROOT / "Stories"
QA = STORIES / "Level 8 Art QA"

SETS = [
    ("The Grass Track", "the_grass_track"),
    ("The Two-Top Trick", "the_two_top_trick"),
    ("Chess for Two", "chess_for_two"),
    ("The Frog on the Sock", "the_frog_on_the_sock"),
    ("Hop and Spin", "hop_and_spin"),
    ("A Snack for the Pug", "a_snack_for_the_pug"),
    ("The Black Bat", "the_black_bat"),
    ("The Snug Cap", "the_snug_cap"),
    ("The Club Flag", "the_club_flag"),
    ("The Sock Sled", "the_sock_sled"),
]


def master_paths() -> list[Path]:
    out: list[Path] = []
    for folder, slug in SETS:
        base = STORIES / folder
        out.extend(
            [
                base / f"story_{slug}.png",
                base / f"comp_{slug}_0.png",
                base / f"comp_{slug}_1.png",
                base / f"comp_{slug}_2.png",
            ]
        )
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def diagnostics(path: Path) -> dict[str, object]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
        width, height = image.size
        px = image.load()
        edges = {
            "top": [px[x, 0] for x in range(width)],
            "right": [px[width - 1, y] for y in range(height)],
            "bottom": [px[x, height - 1] for x in range(width)],
            "left": [px[0, y] for y in range(height)],
        }
        fractions = {
            name: round(sum(min(rgb) >= 245 for rgb in values) / len(values), 6)
            for name, values in edges.items()
        }
        border_min = min(min(rgb) for values in edges.values() for rgb in values)
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
        return {
            "path": str(path.relative_to(ROOT)),
            "width": width,
            "height": height,
            "mode": opened.mode,
            "format": opened.format,
            "sha256": sha256(path),
            "border_min_channel": border_min,
            "near_white_fraction_by_edge": fractions,
            "near_white_reaches_all_four_edges": all(v > 0 for v in fractions.values()),
            "nonwhite_bbox_margins": margins,
        }


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
    label_font = font(max(11, label_h - 8))
    for index, path in enumerate(paths):
        row, col = divmod(index, cols)
        with Image.open(path) as opened:
            image = opened.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        x = col * tile
        y = row * (tile + label_h)
        canvas.paste(image, (x, y))
        draw.rectangle((x, y, x + tile - 1, y + tile - 1), outline=(218, 218, 218), width=1)
        draw.text((x + 5, y + tile + 2), path.stem, fill=(45, 45, 45), font=label_font)
    canvas.save(target, "PNG")


def comparison_sheet(paths: list[Path], target: Path) -> None:
    anchors = [
        QA / "anchor_story_pip_the_pig.png",
        QA / "anchor_story_the_dig.png",
        QA / "anchor_level_1_card.png",
        QA / "anchor_level_2_card.png",
    ]
    sheet(anchors + paths, target, tile=180, label_h=24)


def main() -> None:
    paths = master_paths()
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit("Missing masters:\n" + "\n".join(missing))
    report = {
        "accepted_master_count": len(paths),
        "masters": [diagnostics(path) for path in paths],
    }
    (QA / "level8_master_diagnostics.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    sheet(paths, STORIES / "LEVEL_8_FINAL_CONTACT_SHEET_FULL.png", tile=300, label_h=30)
    sheet(paths, STORIES / "LEVEL_8_FINAL_CONTACT_SHEET_CARD.png", tile=120, label_h=20)
    comparison_sheet(paths, STORIES / "LEVEL_8_FINAL_COMPARISON_CONTACT_SHEET.png")
    anchors = [
        QA / "anchor_story_pip_the_pig.png",
        QA / "anchor_story_the_dig.png",
        QA / "anchor_level_1_card.png",
        QA / "anchor_level_2_card.png",
    ]
    sheet(anchors, STORIES / "LEVEL_8_CALIBRATION_CONTACT_SHEET_CARD.png", tile=160, label_h=22)


if __name__ == "__main__":
    main()
