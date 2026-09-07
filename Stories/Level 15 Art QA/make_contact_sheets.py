from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ROWS = [
    ("The Purple Turtle", "the_purple_turtle"),
    ("The Paper Bird", "the_paper_bird"),
    ("Fur for the Crow", "fur_for_the_crow"),
    ("The Big Drop", "the_big_drop"),
    ("The Goat at Dinner", "the_goat_at_dinner"),
    ("The Purple Bell", "the_purple_bell"),
    ("The Letter Train", "the_letter_train"),
    ("The Next Turn", "the_next_turn"),
    ("Her Sister Came Home", "her_sister_came_home"),
    ("The Moth by the Lamp", "the_moth_by_the_lamp"),
]

def make(kind: str, indices: list[int], destination: str):
    cell, label_h = 150, 24
    sheet = Image.new("RGB", (cell * len(indices), (cell + label_h) * len(ROWS)), "white")
    draw = ImageDraw.Draw(sheet)
    for row, (folder, slug) in enumerate(ROWS):
        for col, index in enumerate(indices):
            filename = f"story_{slug}.png" if index == -1 else f"comp_{slug}_{index}.png"
            image = Image.open(ROOT / folder / filename).convert("RGB").resize((cell, cell), Image.Resampling.LANCZOS)
            x, y = col * cell, row * (cell + label_h)
            sheet.paste(image, (x, y))
            draw.text((x + 4, y + cell + 4), f"{row+1:02d} {folder} {'cover' if index == -1 else index}", fill="black")
    sheet.save(Path(__file__).resolve().parent / destination)

make("full", [-1, 0, 1, 2], "LEVEL_15_ART_CONTACT_SHEET_FULL.png")
make("card", [-1, 0, 1, 2], "LEVEL_15_ART_CONTACT_SHEET_CARD.png")
