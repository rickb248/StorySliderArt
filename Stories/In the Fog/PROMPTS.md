# Level 4 production prompts — In the Fog

**Source:** `08_in_the_fog.json` (`aa6ae1b2…534e`). **References:** `Characters/Meg/meg_reference_sheet.png`, `Characters/Lex/lex_reference_sheet.png`, `Characters/Roz/roz_reference_sheet.png`. **Generation:** ImageGen, 2026-08-12.

Shared constraint: `Square 1:1 calm K–2 modern storybook anime on solid white, exactly specified children, full figures, one small shadow, at most a tiny answer prop and two wispy fog curls, no scenery, text, crop, or watermark.`

| Accepted file | Exact scene prompt | QA |
|---|---|---|
| `story_in_the_fog.png` | `Meg is frontmost and actively leads Lex and Roz toward a tiny wooden hut; two wispy pale-gray fog curls only.` | Pass |
| `comp_in_the_fog_0.png` | `Meg, Lex, and Roz stand beside a compact simple bus; Meg points toward it.` | Pass |
| `comp_in_the_fog_1.png` | `Meg is unmistakably first/frontmost, holds out an arm, and leads Lex and Roz toward one very tiny hut with two wispy fog curls.` | Pass |
| `comp_in_the_fog_2.png` | `Meg, Lex, and Roz stand by one small lab bench with one unmarked flask.` | Pass |

The non-leading-Meg attempts are retained in `rejected/`.


## 2026-10-12 feedback repair: comp_in_the_fog_1

Built-in ImageGen edit, accepted after visual QA. Earlier master is preserved in `History/2026-10-12-levels-4-5-before/`.

Use case: precise-object-edit. Edit this StorySlider answer image to make the HUT unmistakable at thumbnail size. Preserve the exact identities, hairstyles, outfits and gentle style of the three girls and Meg pointing. Recompose as compact vignette: three girls smaller together in left foreground walking toward a LARGE wooden thatched hut in right midground. Hut must occupy roughly 40 percent of canvas width and have a clear door, walls and thatched roof; no tiny distant hut. All girls and full hut visible with white margin. Very faint small fog wisps, no smoke chimney. Same calm palette, soft outlines, plain opaque pure-white field connected to every edge, no scenery or text. Square PNG.

Accepted file: `comp_in_the_fog_1.png`; SHA-256 `63146046fbfcf4f3ab166934a265fb343ebc62aa58bf84d47c5e8365afd43317`. Full generation source and QA record: `History/2026-10-12-levels-4-5-before/art-generation.json` and `art-qa.json`.
