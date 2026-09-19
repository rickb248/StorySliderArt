from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[2]
qa = Path(__file__).resolve().parent
rows = [line.rstrip("\n").split("\t") for line in (qa / "ASSET_SOURCES.tsv").read_text().splitlines()]

for cell, destination in ((180, "LEVEL_19_ART_CONTACT_SHEET_FULL.png"), (96, "LEVEL_19_ART_CONTACT_SHEET_CARD.png")):
    label = 30
    sheet = Image.new("RGB", (4 * cell, 11 * (cell + label)), "white")
    draw = ImageDraw.Draw(sheet)
    anchors = [
        ("story pip", root / "Stories/Level 19 Art QA/Anchors/story_pip_the_pig.png"),
        ("story dig", root / "Stories/Level 19 Art QA/Anchors/story_the_dig.png"),
        ("level 1", root / "Stories/Level 19 Art QA/Anchors/level_1_card.png"),
        ("level 2", root / "Stories/Level 19 Art QA/Anchors/level_2_card.png"),
    ]
    for column, (name, path) in enumerate(anchors):
        image = Image.open(path).convert("RGB").resize((cell, cell), Image.Resampling.LANCZOS)
        sheet.paste(image, (column * cell, 0))
        draw.text((column * cell + 3, cell + 4), f"anchor {name}", fill="black")
    for number in range(10):
        for column, (_, _, rel) in enumerate(rows[number * 4:number * 4 + 4]):
            image = Image.open(root / rel).convert("RGB").resize((cell, cell), Image.Resampling.LANCZOS)
            x, y = column * cell, (number + 1) * (cell + label)
            sheet.paste(image, (x, y))
            tag = "cover" if column == 0 else f"answer {column - 1}"
            draw.text((x + 3, y + cell + 4), f"{number + 1:02d} {tag}", fill="black")
    sheet.save(qa / destination)
