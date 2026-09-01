# The Bottle Flip — Level 13 R9 Prompt Record

## Production frame used verbatim on every call

Create one square children's reading-app illustration, with a 600×600 master target. Match the StorySlider house style shown by the attached approved anchors: warm picture-book watercolor/gouache rendering, clean soft outlines, expressive faces, natural child and animal proportions, restrained muted palette, and gentle paper-like texture. Keep one tight centered focal cluster isolated on a literal pure #FFFFFF field connected to all four canvas edges, with ample negative space and clear card-scale readability. Do not add a scenic backdrop, horizon, room, wall, sky, landscape, floor plane, decorative border, frame, text, letters, labels, logo, or watermark. Use only the cues explicitly named in the scene payload. Do not add extra characters, animals, or props. Do not crop heads, limbs, or answer objects. Maintain correct anatomy and object construction. Use red, yellow, and green only as small accents, never as dominant fields. When a referenced character or animal appears, preserve the attached reference design exactly.

## Exact scene payloads

- `story_the_bottle_flip.png`: Clay and Bea, matching the attached references, do a small joyful victory jig around a clear capped water bottle that has landed upright on its base on one tiny neutral tabletop slab. Keep the bottle central, unmistakably upright, and both children fully visible. No room, wall, complete table or stool, furniture legs, or extra objects.
- `comp_the_bottle_flip_0.png`: A single clear capped water bottle lying on its side on one tiny neutral tabletop slab. Centered and fully visible; no hand, person, table legs, room, or extra object.
- `comp_the_bottle_flip_1.png`: A single clear capped water bottle lying sideways after bumping one small sage-green rectangular box on a tiny neutral tabletop slab. Keep the collision clue readable; no hand, person, table legs, room, or extra object.
- `comp_the_bottle_flip_2.png`: A single clear capped water bottle standing upright on one tiny neutral tabletop slab. Centered and fully visible; no hand, person, table legs, room, or extra object.

## References supplied

- The four approved Level 13 anchor copies in `Stories/Level 13 Art QA/Anchors/`
- Accepted cover: `Characters/Clay/clay_reference_sheet.png`, `Characters/Bea/bea_reference_sheet.png`

## Iterations and acceptance

- The three choice cards were accepted from generation iteration 1.
- Cover iteration 1 failed `MINIMAL_CUES` because ImageGen supplied a complete stool/table with legs; it is preserved at `Rejected/level_13_r9/The Bottle Flip/story_the_bottle_flip_iter1_full_stool_fail.png`.
- Cover iteration 2 used a precise ImageGen object edit replacing the furniture with a tiny neutral tabletop slab, but the source-to-sheet audit found that it depicted the wrong named characters. It is preserved at `Rejected/level_13_r9/The Bottle Flip/story_the_bottle_flip_iter2_wrong_characters_fail.png`.
- Cover iteration 3 was regenerated with Clay and Bea's reference sheets and was accepted.
- All accepted outputs received only deterministic 600×600 sizing/padding and edge-connected near-white-to-`#FFFFFF` normalization after ImageGen.

## Binary verdicts

| Accepted file | WHITE_FIELD | NO_SCENIC_BACKDROP | TIGHT_FOCAL_CLUSTER | MINIMAL_CUES | CARD_SCALE_MATCH | CALM_PALETTE_MATCH |
|---|---|---|---|---|---|---|
| `story_the_bottle_flip.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_bottle_flip_0.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_bottle_flip_1.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_bottle_flip_2.png` | PASS | PASS | PASS | PASS | PASS | PASS |
