# The Moon by Day — Level 17 prompt and QA record

Source: `01_the_moon_by_day.json`, SHA-256 `e82d67e4e433ff4c0318a916b17e1766dfb8a8ab24f98e05bea7577ad652a08e`.

All masters use the approved StorySlider white-field prompt contract: clean flat K–2 vector/cel illustration; pure #FFFFFF connected to every edge; one centered focal cluster; full subjects and generous margin; calm muted palette; no rooms, scenery, panels, crop, text, or correctness cue. Identity references: `Characters/Dawn/dawn_reference_sheet.png`, `Characters/Drew/drew_reference_sheet.png`. Generation used built-in ImageGen.

| File | Literal visual brief and iteration | QA evidence |
| --- | --- | --- |
| `story_the_moon_by_day.png` | Drew flies a complete muted-butter kite while Dawn watches the reappearing daytime moon. Iteration 1 accepted. | WHITE_FIELD PASS; NO_SCENIC_BACKDROP PASS; TIGHT_FOCAL_CLUSTER PASS; MINIMAL_CUES PASS; CARD_SCALE_MATCH PASS; CALM_PALETTE_MATCH PASS; SEMANTIC_SCALE_MATCH PASS; STRUCTURAL_PLAUSIBILITY N/A; ANIMAL_STYLE_MATCH N/A. |
| `comp_the_moon_by_day_0.png` | Dawn points at the outlined white daytime moon as Drew looks up. Iteration 1 accepted. | WHITE_FIELD PASS; NO_SCENIC_BACKDROP PASS; TIGHT_FOCAL_CLUSTER PASS; MINIMAL_CUES PASS; CARD_SCALE_MATCH PASS; CALM_PALETTE_MATCH PASS; SEMANTIC_SCALE_MATCH PASS; STRUCTURAL_PLAUSIBILITY N/A; ANIMAL_STYLE_MATCH N/A. |
| `comp_the_moon_by_day_1.png` | Drew watches a gray cloud move aside from the outlined white daytime moon. Iteration 2 accepted; no kite or edge contact. | WHITE_FIELD PASS; NO_SCENIC_BACKDROP PASS; TIGHT_FOCAL_CLUSTER PASS; MINIMAL_CUES PASS; CARD_SCALE_MATCH PASS; CALM_PALETTE_MATCH PASS; SEMANTIC_SCALE_MATCH PASS; STRUCTURAL_PLAUSIBILITY N/A; ANIMAL_STYLE_MATCH N/A. Iteration 1 rejected because kite/string touched the top edge and the kite was cropped. |
| `comp_the_moon_by_day_2.png` | Drew waits under a small crescent and two small gray stars on the white field. Iteration 1 accepted. | WHITE_FIELD PASS; NO_SCENIC_BACKDROP PASS; TIGHT_FOCAL_CLUSTER PASS; MINIMAL_CUES PASS; CARD_SCALE_MATCH PASS; CALM_PALETTE_MATCH PASS; SEMANTIC_SCALE_MATCH PASS; STRUCTURAL_PLAUSIBILITY N/A; ANIMAL_STYLE_MATCH N/A. |

## Executed prompt actions and results

Each built-in ImageGen call used the shared contract above together with the following per-image action clause and the Dawn/Drew reference sheets:

| Slot | Executed action clause | Final ImageGen result |
| --- | --- | --- |
| Cover | “Drew flies a complete muted-butter kite while Dawn watches the white daytime moon reappear.” | `/Users/ricky/.codex/generated_images/01a09959-0ec3-7581-b307-53586e2dff4f/exec-53a4f3d6-d0c9-4faa-bdc0-6a079970b587.png` |
| Choice 0 | “Dawn points at the outlined white daytime moon while Drew looks up.” | `/Users/ricky/.codex/generated_images/01a09959-0ec3-7581-b307-53586e2dff4f/exec-012e9b8f-caf2-47ba-a004-ef040c24361b.png` |
| Choice 1, rejected | “Drew watches a gray cloud move aside from the daytime moon, with the kite present.” | `/Users/ricky/.codex/generated_images/01a09959-0ec3-7581-b307-53586e2dff4f/exec-42fd1290-4115-451e-a02c-a8921a03909b.png` |
| Choice 1, final | “Drew watches a gray cloud move aside from the outlined white daytime moon; no kite or line, hands relaxed, all objects inset.” | `/Users/ricky/.codex/generated_images/01a09959-0ec3-7581-b307-53586e2dff4f/exec-3905af33-5b42-46bb-83e6-7b96bc6eda9e.png` |
| Choice 2 | “Drew waits under a small crescent and two small gray stars on the white field.” | `/Users/ricky/.codex/generated_images/01a09959-0ec3-7581-b307-53586e2dff4f/exec-cba36417-3434-4c07-b5ea-a090d81fdd70.png` |
