# The Big Red Hat — accepted prompts

Iteration 1 accepted. References: `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png`, `Characters/Jen/jen_reference_sheet.png`. Global negatives: solid white, no text, crop, edge contact, scenery, face-on-object, cue, photo/3D, or artifacts.

| File | Exact subject prompt |
| --- | --- |
| `story_the_big_red_hat.png` | Ben's Dad wears Ben's oversized plain red hat; it visibly fits Dad. |
| `comp_the_big_red_hat_0.png` | Ben wears a fitting red cap. |
| `comp_the_big_red_hat_1.png` | Ben's Dad wears the big red hat. |
| `comp_the_big_red_hat_2.png` | Jen wears a red wig. |
# Level 3 R4 regeneration — accepted 2026-08-10

**Generation:** ImageGen built-in. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png`. **Shared negative constraints:** beard/facial-hair drift, montage, unsupported hat/props, correctness cues, crop, neon, harsh contrast, 3D/photo, text.

| File | Iteration / exact primary request / QA |
| --- | --- |
| `story_the_big_red_hat.png` | R4 iteration 1: Ben watches his clean-shaven Dad wear the oversized red hat that fits him. **PASS:** one comic fit reveal. |
| `comp_the_big_red_hat_0.png` | R4 iteration 1: Dad sits on a grounded red bed. **PASS:** literal distractor. |
| `comp_the_big_red_hat_1.png` | R4 iteration 2: established clean-shaven Dad in green cardigan puts the big red hat on his own head. **PASS:** literal correct action; replaces bearded drift. |
| `comp_the_big_red_hat_2.png` | R4 iteration 2: established clean-shaven Dad puts a small red cap into a grounded beige bag. **PASS:** literal distractor; replaces wrong-child candidate. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass; choice corrections at iteration 2. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png` (clean-shaven Dad only). **Style anchors inspected:** `story_my_dad.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`. **Shared negatives:** connected white field; no room/backdrop, bearded adult, unrelated child, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_big_red_hat.png` | Clean-shaven Dad wears the enormous red hat as Ben reacts with delighted surprise. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_big_red_hat_0.png` | Clean-shaven Dad sits on the red bed. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_big_red_hat_1.png` | Clean-shaven Dad puts on the big red hat. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_big_red_hat_2.png` | Clean-shaven Dad puts the red cap in a bag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_the_big_red_hat.png` | Dad wears an enormous muted cranberry hat beside Ben. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-b8177aae-4bb5-4230-b1b0-3d3ea2ab9c56.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_big_red_hat_0.png` | Dad sits on a muted brick bed. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-9f5da55c-3daa-4944-bc16-b253126e1aea.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_big_red_hat_1.png` | Dad puts on a muted cranberry hat. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-5f4380b1-6699-4906-9ff6-9df87811f679.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_big_red_hat_2.png` | Dad puts a muted brick cap in an oatmeal bag. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-e7d50727-d057-4998-8c88-8878c04b3073.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Big Red Hat/`.
