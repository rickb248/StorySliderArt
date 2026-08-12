# A Bed for the Pig — accepted prompts

Iteration 1 accepted. References: `Characters/Jen/jen_reference_sheet.png`, `Characters/Pip/pip_reference_sheet.png` (natural pink-pig visual reference only). Global negatives: solid white, no text, crop, edge contact, scenery, face-on-object, cue, photo/3D, or artifacts.

| File | Exact subject prompt |
| --- | --- |
| `story_a_bed_for_the_pig.png` | Jen sets a red pet bed in a low fenced pen as a natural pink pig trots to it. |
| `comp_a_bed_for_the_pig_0.png` | Jen sets the red pet bed on a flat blue mat. |
| `comp_a_bed_for_the_pig_1.png` | Jen sets the red pet bed in a low fenced pen. |
| `comp_a_bed_for_the_pig_2.png` | Jen sets the red pet bed in a large white tub. |
# Level 3 R4 regeneration — accepted 2026-08-10

**Generation:** ImageGen built-in, fresh replacement iteration 1. **References:** `Characters/Jen/jen_reference_sheet.png`, `Characters/Pip/pip_reference_sheet.png` (natural pig visual only). **Shared negative constraints:** montage/collage/split scene, unsupported props, object faces, correctness cues, crop, neon, harsh contrast, 3D/photo rendering, text/watermark.

| File | Exact primary request / QA verdict |
| --- | --- |
| `story_a_bed_for_the_pig.png` | Jen watches a natural soft-pink pig curl into the red bed placed in a straw-floored wooden pen. **PASS:** nap hook, natural animal, pen grounding. |
| `comp_a_bed_for_the_pig_0.png` | Red bed resting on a woven tan mat. **PASS:** literal “on the mat.” |
| `comp_a_bed_for_the_pig_1.png` | Red bed resting in a wooden pen. **PASS:** literal “in the pen.” |
| `comp_a_bed_for_the_pig_2.png` | Red bed resting in a bathtub. **PASS:** literal “in the tub.” |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh white-field replacement pass. **References:** `Characters/Jen/jen_reference_sheet.png`, `Characters/Pip/pip_reference_sheet.png` (identity only). **Style anchors inspected:** `story_pip_the_pig.png`, `story_the_log.png`, `level_1_card.png`, `level_2_card.png`. **Shared negative constraints:** pure connected white field; no room, broad floor, landscape, panels, decorative props, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_a_bed_for_the_pig.png` | Jen gently pets one natural sleeping pink pig curled in the red bed in its small pen. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_0.png` | One red pet bed on one tan mat. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_1.png` | One red pet bed inside one small pen. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_2.png` | One red pet bed inside one big white tub. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_a_bed_for_the_pig.png` | Jen, pig, muted brick bed, and straw-tan cues. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-56740b09-5077-43c0-9f5d-a0547528df10.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_0.png` | Muted brick pet bed on oatmeal mat. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-4dc6ae2d-85ee-4078-a5ac-666cdc03adf1.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_1.png` | Muted brick pet bed in a warm wood pen. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-8f330eed-c1c9-4547-9e09-892ab474dfbe.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_a_bed_for_the_pig_2.png` | Muted brick pet bed in a warm white tub. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-63c141c2-d801-40d8-b291-46580ca4d597.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/A Bed for the Pig/`.
