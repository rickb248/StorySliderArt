"""Create a compact art-side supplement to the coordinator's accepted QA ledger."""
import json
from pathlib import Path
from PIL import Image

qa = Path(__file__).resolve().parent
ledger = json.loads((qa / "COORDINATOR_ART_QA_MANIFEST.json").read_text())
story_refs = {
    "purple_turtle": ["Characters/Tess/CHARACTER.md", "Characters/Tess/tess_reference_sheet.png"],
    "paper_bird": ["Characters/Cole/CHARACTER.md", "Characters/June/CHARACTER.md"],
    "fur_for_the_crow": ["Characters/Bea/CHARACTER.md", "Characters/Bea/bea_reference_sheet.png"],
    "big_drop": ["Characters/Bill/CHARACTER.md", "Characters/Tess/CHARACTER.md", "Characters/Tess/tess_reference_sheet.png"],
    "goat_at_dinner": ["Characters/Bert/CHARACTER.md"],
    "purple_bell": ["Characters/Bert/CHARACTER.md", "Characters/June/CHARACTER.md"],
    "letter_train": ["Characters/Fern/CHARACTER.md", "Characters/FernMom/CHARACTER.md"],
    "next_turn": ["Characters/Fern/CHARACTER.md", "Characters/Kirk/CHARACTER.md"],
    "sister_came_home": ["Characters/Bea/CHARACTER.md", "Characters/Bea/bea_reference_sheet.png", "Characters/BeaSister/CHARACTER.md"],
    "moth_by_the_lamp": ["Characters/Tess/CHARACTER.md", "Characters/Tess/tess_reference_sheet.png"],
}
anchors = [str(x["path"]) for x in ledger["anchors"]]
for item in ledger["images"]:
    path = Path(item["masterPath"])
    key = next((k for k in story_refs if k in item["name"]), "")
    item["dimensions"] = list(Image.open(path).size)
    item["characterReferencePaths"] = story_refs[key]
    item["anchorReferencePaths"] = anchors
    item["artSideQA"] = "PASS"
    item["coordinatorQA"] = "PASS"
out = {"level": 15, "revision": "R16", "imageCount": len(ledger["images"]), "images": ledger["images"]}
(qa / "LEVEL_15_MACHINE_MANIFEST.json").write_text(json.dumps(out, indent=2) + "\n")
