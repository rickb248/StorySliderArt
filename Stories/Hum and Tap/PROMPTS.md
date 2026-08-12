# Level 3 R4 production prompts

**Generation:** ImageGen built-in. **References:** `Characters/Sam/sam_standing_anime.png`, `Characters/Ted/ted_reference_sheet.png`. **Exact shared style:** modern K-2 storybook anime vector art; muted warm palette; low-contrast cel shading; softened dark-brown outlines; white canvas margin; grounded square scene; no text. **Negative:** montage, split scene, object face, floating prop, correctness cue, crop, neon, harsh contrast, 3D/photo.

| File | Iteration / exact primary request / QA |
| --- | --- |
| `story_hum_and_tap.png` | R4 iteration 1: Sam and Ted sit on one log; Ted taps his own leg as Sam hums. **PASS:** shared playful rhythm, natural reference identities. |
| `comp_hum_and_tap_0.png` | R4 iteration 2: Ted sits on a log and taps a big cream mug resting on a low table. **PASS:** literal “a big mug,” comparable action framing. |
| `comp_hum_and_tap_1.png` | R4 iteration 2: Ted sits on a log and taps a red rug lying flat on ground. **PASS:** literal “a red rug,” comparable action framing. |
| `comp_hum_and_tap_2.png` | R4 iteration 1: Ted sits on a log and taps his own leg. **PASS:** literal “his leg.” |

## R4 white-field vignette master — 2026-08-10

**Iteration:** fresh replacement pass; mug/rug action corrections at iteration 2. **References:** `Characters/Sam/sam_standing_anime.png`, `Characters/Ted/ted_reference_sheet.png`. **Style anchors inspected:** `story_the_log.png`, `story_sit.png`, `level_1_card.png`, `level_2_card.png`. **Shared negatives:** connected white field; no room/backdrop, bare answer object, unrelated cast, text, crop, montage, cue, photo, or 3D.

| Accepted master | Exact target prompt | Verdict |
| --- | --- | --- |
| `story_hum_and_tap.png` | Sam and Ted hum together on one log while Ted taps his own leg. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_hum_and_tap_0.png` | Established Ted visibly taps one big mug. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_hum_and_tap_1.png` | Established Ted visibly taps one red rug. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |
| `comp_hum_and_tap_2.png` | Established Ted visibly taps his own leg. | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS` |

## Calm-palette regeneration — 2026-08-11

**Exact shared palette instruction:** Preserve the approved white-field vignette, character identity, action, answer semantics, linework, and focal framing. Use warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and low-to-medium contrast. Literal red becomes brick, cranberry, terracotta, or dusty rose; yellow becomes mustard, ochre, butter, straw, or sand; orange becomes clay, burnt orange, muted apricot, or subdued brown-copper. Playfulness comes from pose, expression, and action—not saturation. No fire-engine red, lemon yellow, vivid orange, candy color, neon saturation, scenic backdrop, extra subject, text, or border.

| Installed master | Story-specific preserved target / palette | Accepted ImageGen candidate | Six-gate verdict |
| --- | --- | --- | --- |
| `story_hum_and_tap.png` | Sam and Ted on the log in dusty slate, sage, warm brown, and muted brick. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-04a8794a-63aa-4ae2-b200-ca3131d829ba.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_hum_and_tap_0.png` | Ted taps a cream mug. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-487cd895-92b8-47b7-9a3a-ae82cb5a7ca4.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_hum_and_tap_1.png` | Ted taps a muted brick rug. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-97a892bf-dcd8-4863-a3a7-8150c97e8c03.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |
| `comp_hum_and_tap_2.png` | Ted taps his leg in sage and dusty navy. | `/Users/ricky/.codex/generated_images/019feef2-08ad-70e1-8164-2f516fb011fd/exec-3de124de-d6f7-489c-b239-efb0ffa3c5d7.png` | `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS` |

**Archive:** superseded masters preserved under `Rejected/level_3_r4_pre_calm_palette_2026-08-11/Hum and Tap/`.
