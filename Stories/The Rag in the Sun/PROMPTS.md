# The Rag in the Sun — accepted prompts

Iteration 1 accepted. Reference: `Characters/Jen/jen_reference_sheet.png`.
Global negative constraints for every asset: solid `#FFFFFF`; no text/logo/watermark/frame,
crop, edge contact, scenery, faces on objects, correctness cue, photorealism, 3D, fuzzy or
sketchy linework, or scary imagery.

| File | Exact subject prompt |
| --- | --- |
| `story_the_rag_in_the_sun.png` | Jen carefully places a visibly wet gray rag in hot sunlight before it goes in a tan bag. |
| `comp_the_rag_in_the_sun_0.png` | Jen sets the wet gray rag in the hot sun. |
| `comp_the_rag_in_the_sun_1.png` | Jen sets the wet gray rag on a red bed. |
| `comp_the_rag_in_the_sun_2.png` | Jen sets the wet gray rag in a big blue mug. |
# Level 3 R4 regeneration — accepted 2026-08-10

**Generation:** ImageGen built-in, fresh replacement iteration 1. **References:** `Characters/Jen/jen_reference_sheet.png`. **Shared negative constraints:** montage, triptych, collage, split scene, repeated character, floating/unsupported props, object face, correctness cue, crop, edge contact, neon, harsh contrast, glossy 3D/photo rendering, teen proportions, text/watermark.

| File | Exact primary request / QA verdict |
| --- | --- |
| `story_the_rag_in_the_sun.png` | Jen gently puts a now-dry gray rug into an open floor-supported fabric bag in one sunny warm room moment. **PASS:** Jen identity, dry-rug/bag payoff, grounded focal action. |
| `comp_the_rag_in_the_sun_0.png` | Damp gray rug lies flat on a sunlit grass patch. **PASS:** literal “in the hot sun.” |
| `comp_the_rag_in_the_sun_1.png` | Damp gray rug lies flat on a grounded red bed. **PASS:** literal “on a red bed.” |
| `comp_the_rag_in_the_sun_2.png` | Damp gray rug tucked in a grounded big cream mug on a tabletop. **PASS:** literal “in a big mug.” |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh white-field replacement pass; final coordinator-approved masters. **Character reference:** `Characters/Jen/jen_reference_sheet.png`. **Style anchors inspected:** `story_pip_the_pig.png`, `story_the_log.png`, `level_1_card.png`, `level_2_card.png`; no contaminating anchor image was supplied to object-only choices. **Exact shared wrapper:** “600×600 square K–2 modern storybook-anime illustration; pure #FFFFFF connected to all four edges; one tight, centered focal cluster; only a tiny essential support cue; no text, room, wall, floor plane, furniture grouping, landscape, horizon, backdrop, colored panel, decorative prop, crop, montage, correctness cue, photo, or 3D.”

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_rag_in_the_sun.png` | Jen lowers the dry gray rug into an open beige bag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_rag_in_the_sun_0.png` | Only the wet gray rug lies on a very small plain grass patch beneath a simple sun icon; no pig, flowers, or other prop. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_rag_in_the_sun_1.png` | Only the wet gray rug lies on the red bed. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_rag_in_the_sun_2.png` | Only the wet gray rug is visibly in a big cream mug, with a tiny contact shadow. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `comp_the_rag_in_the_sun_1.png` | Wet gray rag on a muted brick/dusty-rose bed. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-6a2cb632-8d0d-44ed-8009-3fc9f3f79bed.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded master preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Rag in the Sun/`.
