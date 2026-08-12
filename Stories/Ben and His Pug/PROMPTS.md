# Level 3 R4 production prompts

**Generation:** ImageGen built-in. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenPug/ben_pug_reference_sheet.png`, `Characters/Bug/bug_reference_sheet.png`. **Exact shared style/negative:** muted modern K-2 storybook anime, white margin, grounded square scene, no text; no anthropomorphic pug/bug, clothes on animals, montage, floating prop, correctness cue, crop, neon, harsh contrast, 3D/photo.

| File | Exact primary request / QA |
| --- | --- |
| `story_ben_and_his_pug.png` | Ben smiles beside his seated natural fawn pug while one natural ladybug sits on its head. **PASS:** exact comic final beat. |
| `comp_ben_and_his_pug_0.png` | Natural ladybug runs on the rug toward Ben’s shoe. **PASS:** literal “ran to Ben.” |
| `comp_ben_and_his_pug_1.png` | Natural ladybug sits on the seated pug’s head. **PASS:** literal correct ending. |
| `comp_ben_and_his_pug_2.png` | Natural ladybug rests on a tan rug. **PASS:** literal “sat on the rug.” |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass; `comp_0` and `comp_2` corrected at iteration 2. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenPug/ben_pug_reference_sheet.png`, `Characters/Bug/bug_reference_sheet.png`. **Style anchors inspected:** `story_the_dog.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`; no unrelated cap/log/pug content used as a style reference. **Shared negatives:** connected white field; no cap, log, extra insect, extra pug, unrelated animal, room/backdrop, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_ben_and_his_pug.png` | Ben gently pets the seated pug while exactly one small red-and-black bug sits on the pug’s head. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_ben_and_his_pug_0.png` | Exactly one established Ben and one clearly moving red-and-black bug; no cap, log, rug, pug, or extra insect. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_ben_and_his_pug_1.png` | Exactly one small bug sits on the established pug. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_ben_and_his_pug_2.png` | Exactly one small red-and-black bug sits on one small plain tan rug; no cap, log, child, pug, or extra insect. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_ben_and_his_pug.png` | Exactly one Ben, one pug, and one muted-brick ladybug; subdued brown-copper hair and sand shirt. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-8c1d5bb0-9085-4a2d-ac21-e4359b18e989.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_ben_and_his_pug_0.png` | Exactly one Ben and one moving ladybug; subdued brown-copper hair and sand shirt. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-ac8120b5-82c5-4883-b598-a1dec245908e.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/Ben and His Pug/`.
