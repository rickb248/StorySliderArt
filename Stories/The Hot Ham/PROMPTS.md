# The Hot Ham — accepted prompts

Iteration 1 accepted for cover and choice 0; iteration 2 accepted for choices 1–2 after a character-identity correction. References: `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png`. Dad handles the food; Ben waits until it is safe. Global negatives: solid white, no text, crop, edge contact, scenery, face-on-object, cue, photo/3D, or artifacts.

| File | Exact subject prompt |
| --- | --- |
| `story_the_hot_ham.png` | Ben's Dad safely offers cooled ham to Ben after it sat in a red pan. |
| `comp_the_hot_ham_0.png` | Ben takes a small safe bite of ham. |
| `comp_the_hot_ham_1.png` | Ben takes a small bite of a red bun. |
| `comp_the_hot_ham_2.png` | Ben takes a small bite of a big purple fig. |
# Level 3 R4 regeneration — accepted 2026-08-10

**Generation:** ImageGen built-in. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png`. **Shared negative constraints:** unsafe child/pan contact, montage, object face, correctness cue, crop, neon, harsh contrast, 3D/photo, text.

| File | Iteration / exact primary request / QA |
| --- | --- |
| `story_the_hot_ham.png` | R4 iteration 1: Dad safely hands Ben cooled ham on a plate while the red pan remains on the counter. **PASS:** safe handoff and eager Yum payoff. |
| `comp_the_hot_ham_0.png` | R4 iteration 1: one slice of ham on a plate. **PASS:** literal ham. |
| `comp_the_hot_ham_1.png` | R4 iteration 2: one unmistakable round baked bread bun, domed with two shallow score cuts and warm red-tinted crust, on a plate. **PASS:** literal red bun; supersedes tomato-like iteration. |
| `comp_the_hot_ham_2.png` | R4 iteration 1: one large purple fig on a plate. **PASS:** literal big fig. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh white-field replacement pass; final corrections are iterations 3–4. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenDad/ben_dad_reference_sheet.png`. **Style anchors inspected:** `story_my_dad.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`; no animal anchor was used. **Shared negative constraints:** connected white field; no room/table setting, unrelated adult/animal, extra hand, oversized food, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_hot_ham.png` | Clean-shaven Dad holds the plate while Ben takes one small safe bite of ham, pleased. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_hot_ham_0.png` | Only Ben holds and visibly bites one small ham slice; no adult or plate hand. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_hot_ham_1.png` | Ben holds and bites one palm-sized red bread roll with visible crumb at the bite. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_hot_ham_2.png` | Ben holds and bites one small halved purple fig with a reddish seeded interior. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_the_hot_ham.png` | Ben bites rosy-brown ham while Dad holds the plate; sage, cream, ochre, and dusty blue. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-8c0ab2f6-4139-4164-8426-b3453b1df823.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_hot_ham_0.png` | Ben bites rosy-brown ham; subdued brown-copper hair. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-b6b84de6-b4ae-4749-be36-283cd02e6055.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_hot_ham_1.png` | Ben bites a muted cranberry bread bun. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-417eb77a-9c07-4753-afed-37d421dce840.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_hot_ham_2.png` | Ben bites a dusty-plum fig. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-ee28912c-e766-4a3e-82c6-d33436241345.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Hot Ham/`.
