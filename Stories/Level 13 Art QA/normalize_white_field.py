#!/usr/bin/env python3
"""Normalize only the edge-connected near-white field to exact #FFFFFF."""

from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

from qa_level13 import master_paths


def normalize(path: Path, threshold: int = 245) -> int:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
    width, height = image.size
    pixels = image.load()
    edge_points = (
        [(x, 0) for x in range(width)]
        + [(width - 1, y) for y in range(height)]
        + [(x, height - 1) for x in range(width)]
        + [(0, y) for y in range(height)]
    )
    seeds = [point for point in edge_points if min(pixels[point]) >= threshold]
    queue = deque(seeds)
    seen = set(seeds)
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            point = (nx, ny)
            if (
                0 <= nx < width
                and 0 <= ny < height
                and point not in seen
                and min(pixels[point]) >= threshold
            ):
                seen.add(point)
                queue.append(point)
    changed = 0
    for point in seen:
        if pixels[point] != (255, 255, 255):
            pixels[point] = (255, 255, 255)
            changed += 1
    if changed:
        image.save(path, "PNG")
    return changed


def main() -> None:
    for path in master_paths():
        print(f"{path}: {normalize(path)} normalized pixels")


if __name__ == "__main__":
    main()
