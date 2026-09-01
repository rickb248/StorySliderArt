# The Little Bunny — Level 13 R9 Prompt Record

## Production frame used verbatim on every call

Create one square children's reading-app illustration, with a 600×600 master target. Match the StorySlider house style shown by the attached approved anchors: warm picture-book watercolor/gouache rendering, clean soft outlines, expressive faces, natural child and animal proportions, restrained muted palette, and gentle paper-like texture. Keep one tight centered focal cluster isolated on a literal pure #FFFFFF field connected to all four canvas edges, with ample negative space and clear card-scale readability. Do not add a scenic backdrop, horizon, room, wall, sky, landscape, floor plane, decorative border, frame, text, letters, labels, logo, or watermark. Use only the cues explicitly named in the scene payload. Do not add extra characters, animals, or props. Do not crop heads, limbs, or answer objects. Maintain correct anatomy and object construction. Use red, yellow, and green only as small accents, never as dominant fields. When a referenced character or animal appears, preserve the attached reference design exactly.

## Exact scene payloads

- `story_the_little_bunny.png`: Skye and Rose, matching the attached references, kneel very still beside a small gray-brown bunny matching the attached bunny reference. The bunny calmly nibbles one green leaf. The children watch quietly with gentle delighted expressions. No garden, hedge, fence, or landscape.
- `comp_the_little_bunny_0.png`: The small gray-brown bunny hops away from a muted brick-red ball resting on a tiny grass tuft. Keep bunny and ball fully visible with restrained motion marks. No child, garden, or extra toy.
- `comp_the_little_bunny_1.png`: The small gray-brown bunny hops away as one short brown twig lies freshly fallen beside it. Keep bunny and twig fully visible with restrained motion marks. No tree, child, garden, or extra object.
- `comp_the_little_bunny_2.png`: A friendly cream goat matching the attached goat reference stands near one tiny sprig of greenery while the small gray-brown bunny hops away. Keep both animals fully visible and the plant cue minimal. No field, fence, barn, child, or scenic hedge.

## References supplied

- The four approved Level 13 anchor copies in `Stories/Level 13 Art QA/Anchors/`
- Cover: `Characters/Skye/skye_reference_sheet.png`, `Characters/Rose/rose_reference_sheet.png`, `Characters/Level13Bunny/level13_bunny_reference_sheet.png`
- Choices: `Characters/Level13Bunny/level13_bunny_reference_sheet.png`; choice 2 also used `Characters/Level13Goat/level13_goat_reference_sheet.png`

## Iterations and acceptance

All four images were accepted from generation iteration 1. Only deterministic 600×600 sizing/padding and edge-connected near-white-to-`#FFFFFF` normalization followed ImageGen.

## Binary verdicts

| Accepted file | WHITE_FIELD | NO_SCENIC_BACKDROP | TIGHT_FOCAL_CLUSTER | MINIMAL_CUES | CARD_SCALE_MATCH | CALM_PALETTE_MATCH |
|---|---|---|---|---|---|---|
| `story_the_little_bunny.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_little_bunny_0.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_little_bunny_1.png` | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_the_little_bunny_2.png` | PASS | PASS | PASS | PASS | PASS | PASS |
