# Level 3 R4 production prompts

**Generation:** ImageGen built-in, fresh replacement iteration 1. **Reference:** `Characters/Ken/ken_reference_sheet.png`. **Exact non-negotiables:** 600px square after production resize; modern K-2 storybook anime vector art; muted warm palette, low-contrast cel shading, softened dark-brown outlines, white outer border, no text. Negative: montage, collage, split scene, actual flight, floating/unsupported tub, object faces, correctness cues, crop, neon, harsh contrast, 3D/photo.

| File | Exact primary request / QA |
| --- | --- |
| `story_the_tub_jet.png` | Ken sits in a red tub that rests completely flat on a tan rug, points up with pretend-pilot delight, and only faint imagination swooshes suggest a jet. **PASS:** grounded real tub and literal pretend flight. |
| `comp_the_tub_jet_0.png` | A big child bed grounded on a floor. **PASS:** literal big bed. |
| `comp_the_tub_jet_1.png` | A red toy bus grounded on a tan rug, with no face. **PASS:** literal red bus. |
| `comp_the_tub_jet_2.png` | An empty red plastic tub grounded on a tan rug. **PASS:** literal red tub. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh white-field replacement pass. **Reference:** `Characters/Ken/ken_reference_sheet.png` (identity only). **Style anchors inspected:** `story_the_log.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`; no pig anchor was attached. **Shared negative constraints:** connected #FFFFFF field; no room/backdrop, broad floor, text, crop, montage, actual flying tub, unrelated animal/prop, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_tub_jet.png` | Ken sits in the physically grounded red tub on a tiny rug, pointing up in pretend-jet delight; faint motion swooshes only. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_tub_jet_0.png` | Established Ken visibly sits on the big bed. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_tub_jet_1.png` | Established Ken visibly sits in the red bus. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_tub_jet_2.png` | Established Ken visibly sits in the red tub. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_the_tub_jet.png` | Ken in a muted brick tub with clay, dusty-blue, and oatmeal accents. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-09c23a88-61bf-4a40-87ad-1b09a47d0930.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_tub_jet_0.png` | Ken on a dusty-blue bed. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-8fd3b4fd-3f0a-4dce-bc2e-84ecc7009160.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_tub_jet_1.png` | Ken in a muted brick bus. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-ec990bf6-1c28-4aca-8724-e0d8a7e57c37.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_tub_jet_2.png` | Ken in a muted brick tub. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-bced0f8b-5649-4793-b92c-27d3c97cda87.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Tub Jet/`.
