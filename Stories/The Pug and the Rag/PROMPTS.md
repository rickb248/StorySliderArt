# The Pug and the Rag — accepted prompts

Iteration 1 accepted. References: `Characters/Ben/ben_reference_sheet.png`, `Characters/BenPug/ben_pug_reference_sheet.png`. Ben's pug is distinct from Pip and remains a natural four-legged pug. Global negatives: solid white, no text, crop, edge contact, scenery, face-on-object, cue, photo/3D, or artifacts.

| File | Exact subject prompt |
| --- | --- |
| `story_the_pug_and_the_rag.png` | Ben and his pug gently tug a red rag; Ben lets the pug have it. |
| `comp_the_pug_and_the_rag_0.png` | The pug holds a red cap naturally in its mouth. |
| `comp_the_pug_and_the_rag_1.png` | The pug holds a big tan bun naturally in its mouth. |
| `comp_the_pug_and_the_rag_2.png` | The pug holds the red rag naturally in its mouth. |
# Level 3 R4 regeneration — accepted 2026-08-10

**Generation:** ImageGen built-in, fresh replacement iteration 1. **References:** `Characters/Ben/ben_reference_sheet.png`, `Characters/BenPug/ben_pug_reference_sheet.png`. **Shared negative constraints:** anthropomorphic/clothed pug, montage, rough tugging, floating props, correctness cues, crop, neon, harsh contrast, 3D/photo, text.

| File | Exact primary request / QA |
| --- | --- |
| `story_the_pug_and_the_rag.png` | Ben shares a gentle tug game; his natural fawn pug wins and runs a few steps with the red rag. **PASS:** playful sharing payoff. |
| `comp_the_pug_and_the_rag_0.png` | Natural pug holds a red cap. **PASS:** literal alternative. |
| `comp_the_pug_and_the_rag_1.png` | Natural pug holds a big baked bun. **PASS:** literal alternative. |
| `comp_the_pug_and_the_rag_2.png` | Natural pug holds a red rag. **PASS:** literal correct possession. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass; bun/rag corrected at iteration 2 after duplicated-pug rejection. **Reference:** `Characters/BenPug/ben_pug_reference_sheet.png` (identity only); Ben reference used only for the cover. **Style anchors inspected:** `story_the_dog.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`. **Shared negatives:** connected #FFFFFF field; no extra or duplicated pug, no unrelated animal/person, no room/backdrop, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_pug_and_the_rag.png` | Ben and exactly one fawn pug gently tug one red rag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_0.png` | Exactly one fawn pug holds exactly one red cap. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_1.png` | Exactly one fawn pug holds one child-sized plain golden-brown bread bun; not a pretzel or bagel. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_2.png` | Exactly one fawn pug holds one plain bright red cloth rag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

**Rejected preserved:** `Rejected/level_3_r4_whitefield_revisions_2026-08-10/The Pug and the Rag/comp_the_pug_and_the_rag_{1,2}_rejected_duplicated_pugs.png`.

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_the_pug_and_the_rag.png` | Ben and one pug tug a muted brick rag; subdued brown-copper hair and sand shirt. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-74d761b4-8d68-4056-9967-d798a2f0e99d.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_0.png` | One pug holds a muted brick cap. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-557d998d-35af-403a-9a17-c81a8b774483.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_1.png` | One pug holds a baked-wheat bun. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-635c8a52-ad55-4cd7-a3df-358a085883ac.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_pug_and_the_rag_2.png` | One pug holds a muted brick rag. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-d2330310-94fd-46cd-a75e-073cf1c6387c.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Pug and the Rag/`.
