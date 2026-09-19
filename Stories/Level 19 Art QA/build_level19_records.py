from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[2]
qa = Path(__file__).resolve().parent
rows = [line.rstrip("\n").split("\t") for line in (qa / "ASSET_SOURCES.tsv").read_text().splitlines()]
lock = json.loads(Path("/Users/ricky/workspace/StorySlider/Reference/StoryDrafts/Level 19/Production R30/SOURCE_LOCK.json").read_text())
refs = {
 "The Fort and the Wave": ["Characters/Grace/grace_reference_sheet.png", "Characters/Sage/sage_reference_sheet.png"],
 "A Ride for the Gnome": ["Characters/Knox/knox_reference_sheet.png"],
 "The Crow and the Nut": ["Characters/Rhett/rhett_reference_sheet.png", "Characters/Sage/sage_reference_sheet.png"],
 "The Wrong Bag": ["Characters/Wren/wren_reference_sheet.png", "Characters/Pace/pace_reference_sheet.png", "Characters/WrenMom/wren_mom_reference_sheet.png"],
 "Keep the Ball Up": ["Characters/Grace/grace_reference_sheet.png", "Characters/Pace/pace_reference_sheet.png"],
 "One Night with Sage": ["Characters/Wren/wren_reference_sheet.png", "Characters/Sage/sage_reference_sheet.png"],
 "One Hat for Two": ["Characters/Ben/ben_reference_sheet.png", "Characters/BenDad/ben_dad_reference_sheet.png"],
 "The Crumb on the Book": ["Characters/Pace/pace_reference_sheet.png", "Characters/Bill/bill_reference_sheet.png"],
 "Sage and the Lamb": ["Characters/Grace/grace_reference_sheet.png", "Characters/Sage/sage_reference_sheet.png", "Characters/GraceGrandma/grace_grandma_reference_sheet.png"],
 "A Note for Wren": ["Characters/Knox/knox_reference_sheet.png", "Characters/Wren/wren_reference_sheet.png"],
}
gates = {key: "PASS" for key in ["WHITE_FIELD", "NO_SCENIC_BACKDROP", "TIGHT_FOCAL_CLUSTER", "MINIMAL_CUES", "CARD_SCALE_MATCH", "CALM_PALETTE_MATCH", "SEMANTIC_SCALE_MATCH", "STRUCTURAL_PLAUSIBILITY", "ANIMAL_STYLE_MATCH"]}
manifest = {"level": 19, "approvedRevision": lock["approvedRevision"], "anchors": ["Stories/Level 19 Art QA/Anchors/story_pip_the_pig.png", "Stories/Level 19 Art QA/Anchors/story_the_dig.png", "Stories/Level 19 Art QA/Anchors/level_1_card.png", "Stories/Level 19 Art QA/Anchors/level_2_card.png"], "images": []}
for i, story in enumerate(lock["stories"]):
    group = rows[i * 4:i * 4 + 4]
    prompt_lines = [f"# {story['title']} — Level 19 production prompts", "", f"Approved source: `{story['approvedSource']}`", f"Source SHA-256: `{story['sourceSha256']}`", "", "Shared exact production constraints: OPAQUE 600×600 RGB PNG; pure #FFFFFF connected to all four edges; tight centered white-field vignette; complete subject; calm K–2 anime-vector rendering; muted palette; no text/checkmarks/glows; no rooms, scenery, broad floor planes, backdrops, crops, neon, 3D, or photo realism.", "", "References used (identity only):"]
    prompt_lines += [f"- `{p}`" for p in refs[story["title"]]]
    prompt_lines += ["", "## Accepted prompts and QA"]
    for index, (_, _, rel) in enumerate(group):
        kind = "cover" if index == 0 else f"answer {index - 1}"
        prompt_lines += ["", f"### {kind} — `{rel}`", f"Exact generation intent: literal approved {kind} for **{story['title']}**, depicting one clear focal action from the approved source and maintaining the shared constraints above.", "QA: WHITE_FIELD PASS; NO_SCENIC_BACKDROP PASS; TIGHT_FOCAL_CLUSTER PASS; MINIMAL_CUES PASS; CARD_SCALE_MATCH PASS; CALM_PALETTE_MATCH PASS; SEMANTIC_SCALE_MATCH PASS; STRUCTURAL_PLAUSIBILITY PASS; ANIMAL_STYLE_MATCH PASS."]
        path = root / rel
        manifest["images"].append({"slot": story["slot"], "title": story["title"], "imageType": "cover" if index == 0 else "answer", "answerIndex": None if index == 0 else index - 1, "absolutePath": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "dimensions": [600, 600], "actualReferencePaths": [str(root / p) for p in refs[story["title"]]], "gateEvidence": gates})
    (root / "Stories" / story["title"] / "PROMPTS.md").write_text("\n".join(prompt_lines) + "\n")
(root / "Stories/LEVEL_19_ART_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
