# Level 3 R4 production prompts

**Generation:** ImageGen built-in. **References:** `Characters/Jen/jen_reference_sheet.png`, `Characters/JenMom/jen_mom_reference_sheet.png`. **Exact shared style/negative:** muted modern K-2 storybook anime, white margin, grounded square scene, no text; no bus face, montage, floating prop, correctness cue, crop, neon, harsh contrast, 3D/photo.

| File | Exact primary request / QA |
| --- | --- |
| `story_the_red_bag.png` | Jen discovers and zips a large red toy bus on a rug while her distinct Mom holds the open red bag. **PASS:** bright one-moment reveal, grounded faceless toy bus. |
| `comp_the_red_bag_0.png` | A red mug visibly inside an open grounded red bag. **PASS:** literal alternative. |
| `comp_the_red_bag_1.png` | A wet gray rag visibly inside an open grounded red bag. **PASS:** literal alternative. |
| `comp_the_red_bag_2.png` | A big faceless red toy bus visibly inside an open grounded red bag. **PASS:** literal correct object. |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass. **References:** `Characters/Jen/jen_reference_sheet.png`, `Characters/JenMom/jen_mom_reference_sheet.png`. **Style anchors inspected:** `story_sit.png`, `story_my_dad.png`, `level_1_card.png`, `level_2_card.png`; object choices used a neutral level-card/object calibration only. **Shared negatives:** connected #FFFFFF field; no room/backdrop, bus face, unrelated cast, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_the_red_bag.png` | Jen and her Mom open the big red bag to reveal the big red bus. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_red_bag_0.png` | One red mug visibly inside one open red bag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_red_bag_1.png` | One wet gray rag visibly inside one open red bag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_the_red_bag_2.png` | One big red toy bus visibly inside one open red bag. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_the_red_bag.png` | Jen and Mom reveal a bus with a muted brick bag; dusty rose, sage, and muted teal. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-b0a4e583-4bf7-471d-8ce3-4a66f942fc6f.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_red_bag_0.png` | Dusty-rose mug in a deeper cranberry bag. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-2f9f0796-f797-4f53-9acf-f97aa66d56ac.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_red_bag_1.png` | Wet warm-gray rag in a muted cranberry bag. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-95936d68-3f17-44bb-a0dc-255a0fee8d8b.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_the_red_bag_2.png` | Muted brick bus in a distinct dusty-red bag. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-f3b94db5-9048-4b74-8250-83b730b06884.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/The Red Bag/`.

## Targeted red separation and bag-geometry repair — 2026-08-11

The approved source explicitly says `A big red bus was in the bag.`, and the correct answer is `A big red bus.`; the bus therefore remains recognizably red. The repair separates the two required reds by hue, value, material, and edge definition.

### `story_the_red_bag.png`

**Exact edit prompt:** Keep Jen, Mom, their faces, bodies, poses, clothing, expressions, and the white-field composition unchanged. Repair only the red bag and red toy bus so they no longer look like the same color. The bag is deep dusty-cranberry fabric, clearly darker and cooler than the bus, with a believable open tote rim and fabric folds. The bus is lighter muted terracotta/brick red, with dusty-navy windows, charcoal wheels, and warm-cream lights. Preserve one Mom, one Jen, one bus, one bag, the tight focal cluster, and generous white breathing room. No same-color bag and bus, fire-engine red, vivid orange, glossy plastic, merged geometry, malformed handles, zipper, backpack, scenic background, extra props, crop, border, text, or bus face.

**Accepted candidate:** `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-0b6f2f9c-0709-442c-9af0-473cc44527f1.png`

### `comp_the_red_bag_2.png`

**Exact replacement prompt:** Replace the AI-looking zippered case/backpack with one simple, believable open red shopping tote matching the clean construction of choice 0. Show one big red toy bus visibly sitting inside the tote. The bag is deep dusty-cranberry fabric or matte paper with a clean trapezoidal body, clear open rim, and simple loop handles attached at believable points; no zipper or backpack shape. The bus is lighter muted terracotta/brick red with dusty-navy windows, charcoal wheels, and warm-cream lights. Its lower portion is naturally contained by the bag; it is not fused into or replacing the bag. Keep one centered object cluster on pure white with only a small contact shadow. No same-color bag and bus, giant mouth opening, impossible seams, malformed/floating handles, merged geometry, extra bus, bus face, fire-engine red, vivid orange, glossy 3D, scenic background, colored panel, crop, border, text, or correctness cue.

**Accepted candidate:** `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-9e8a13e0-9131-4ea3-b689-2d1ee961622a.png`

**Verdict for both:** `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS`.

**Archive:** superseded files preserved under `Rejected/level_3_r4_targeted_red_bag_repair_2026-08-11/The Red Bag/`.
