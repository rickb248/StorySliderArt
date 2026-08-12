# Level 3 R4 production prompts

**Generation:** ImageGen built-in. **References:** `Characters/Ned/ned_reference_sheet.png`, `Characters/NedDad/ned_dad_reference_sheet.png`. **Exact shared style/negative:** muted modern K-2 storybook anime, white margin, grounded square scene, no text; no montage, floating prop, correctness cue, crop, neon, harsh contrast, 3D/photo.

| File | Iteration / exact primary request / QA |
| --- | --- |
| `story_dad_came_in.png` | R4 iteration 1: Ned safely hugs his distinct Dad while seated on Dad’s lap on a tan rug. **PASS:** warm family reunion. |
| `comp_dad_came_in_0.png` | R4 iteration 1: Ned visibly sits on Dad’s lap. **PASS:** literal correct location. |
| `comp_dad_came_in_1.png` | R4 iteration 2: established Ned in red hoodie sits visibly on a grounded red bed. **PASS:** literal alternative; replaces empty bed. |
| `comp_dad_came_in_2.png` | R4 iteration 2: established Ned in red hoodie sits visibly in a grounded big white tub. **PASS:** literal alternative; replaces empty tub. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass; full-choice corrections at iteration 2. **References:** `Characters/Ned/ned_reference_sheet.png`, `Characters/NedDad/ned_dad_reference_sheet.png`. **Style anchors inspected:** `story_my_dad.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`. **Shared negatives:** connected white field; no room/backdrop, empty answer prop, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_dad_came_in.png` | Established Ned in red hoodie warmly hugs Dad while seated on Dad’s lap, on a tiny tan rug. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_dad_came_in_0.png` | Established Ned visibly sits on Dad’s lap. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_dad_came_in_1.png` | Established Ned visibly sits on the red bed. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_dad_came_in_2.png` | Established Ned visibly sits inside the big tub. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_dad_came_in.png` | Ned and Dad share a lap hug in muted cranberry, dusty slate, and oatmeal. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-baac8bdb-7246-4d8c-a75f-de14f3cefb35.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_dad_came_in_0.png` | Ned sits on Dad’s lap in calm earth tones. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-18ffe54c-9591-4dcf-8839-6907ac9dcb1b.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_dad_came_in_1.png` | Ned sits on a dusty-rose bed. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-39045b7b-9c60-4dbb-a7f9-720b779d483a.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_dad_came_in_2.png` | Ned sits in a warm-white tub. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-ece51229-2e91-4600-9657-0bc46d572cd5.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/Dad Came In/`.
