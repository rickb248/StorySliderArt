# The Funny Fetch — Level 13 R9 Prompt Record

## Production frame used verbatim on every call

Create one square children's reading-app illustration, with a 600×600 master target. Match the StorySlider house style shown by the attached approved anchors: warm picture-book watercolor/gouache rendering, clean soft outlines, expressive faces, natural child and animal proportions, restrained muted palette, and gentle paper-like texture. Keep one tight centered focal cluster isolated on a literal pure #FFFFFF field connected to all four canvas edges, with ample negative space and clear card-scale readability. Do not add a scenic backdrop, horizon, room, wall, sky, landscape, floor plane, decorative border, frame, text, letters, labels, logo, or watermark. Use only the cues explicitly named in the scene payload. Do not add extra characters, animals, or props. Do not crop heads, limbs, or answer objects. Maintain correct anatomy and object construction. Use red, yellow, and green only as small accents, never as dominant fields. When a referenced character or animal appears, preserve the attached reference design exactly.

## Exact scene payloads

- `story_the_funny_fetch.png`: Rose, matching the attached Rose reference, bends toward a small fawn pug matching the attached pug reference. The pug has just brought back a floppy muted straw-yellow sun hat instead of a stick. Rose looks surprised and amused; the pug looks proudly pleased. Keep the hat fully visible between them. One faint oval contact shadow only.
- `comp_the_funny_fetch_0.png`: A single fresh green oval leaf with a short stem, centered and fully visible, object-only answer card. No ground, plant, branch, or extra object.
- `comp_the_funny_fetch_1.png`: A single floppy plain sun hat in subdued straw-beige/ochre, centered and fully visible, object-only answer card. No bright lemon yellow, person, animal, furniture, or extra prop.
- `comp_the_funny_fetch_2.png`: A single short brown forked fetch stick, centered horizontally and fully visible, object-only answer card. No leaves, ground patch, person, animal, or extra prop.

## References supplied

- `Stories/Level 13 Art QA/Anchors/anchor_story_pip_the_pig.png`
- `Stories/Level 13 Art QA/Anchors/anchor_story_the_dig.png`
- `Stories/Level 13 Art QA/Anchors/anchor_level_1_card.png`
- `Stories/Level 13 Art QA/Anchors/anchor_level_2_card.png`
- Cover: `Characters/Rose/rose_reference_sheet.png`, `Characters/Level13Pug/level13_pug_reference_sheet.png`

## Iterations and acceptance

- Cover, leaf, and stick were accepted from generation iteration 1.
- Hat iteration 1 failed calm-palette matching because the yellow was too bright; it is preserved at `Rejected/level_13_r9/The Funny Fetch/comp_the_funny_fetch_1_iter1_palette_fail.png`.
- Hat iteration 2 used a precise ImageGen object edit to mute the hat to straw-beige/ochre and was accepted.
- All four accepted outputs received only deterministic 600×600 sizing/padding and edge-connected near-white-to-`#FFFFFF` normalization after ImageGen; no semantic pixels were added by the normalization step.

## Binary verdicts

| Accepted file | WHITE_FIELD | NO_SCENIC_BACKDROP | TIGHT_FOCAL_CLUSTER | MINIMAL_CUES | CARD_SCALE_MATCH | CALM_PALETTE_MATCH |
|---|---|---|---|---|---|---|
| `story_the_funny_fetch.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_funny_fetch_0.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_funny_fetch_1.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_funny_fetch_2.png` | PASS | PASS | PASS | PASS | PASS | PASS |
