# Sam - Image Generation Prompts

## Cover Image
*Exists previously*

## Comprehension Answer Images

### Answer 0: On a cat
**Prompt:**
```markdown
Subject: Sam, a 6-year-old boy with messy brown hair and a blue sweatshirt, sitting on a cat. The cat looks surprised or annoyed.
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear thin black outlines, simple cel-shading, large expressive eyes.
Format: 11:10 aspect ratio, solid white background #FFFFFF, centered full view.
Negative: cropped, cut off, realistic photo, 3d render, scary, dark, neon.
```
**Result:** [comp_sam_0.png](file:///Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_sam_0.imageset/comp_sam_0.png)

### Answer 1: On a mat (Correct)
**Prompt:**
```markdown
Subject: Sam, a 6-year-old boy with messy brown hair and a blue sweatshirt, sitting comfortably on a colorful rug or mat on the floor. He looks happy.
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear thin black outlines, simple cel-shading, large expressive eyes.
Format: 11:10 aspect ratio, solid white background #FFFFFF, centered full view.
Negative: cropped, cut off, realistic photo, 3d render, scary, dark, neon.
```
**Result:** [comp_sam_1.png](file:///Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_sam_1.imageset/comp_sam_1.png)

### Answer 2: On a hat
**Prompt:**
```markdown
Subject: Sam, a 6-year-old boy with messy brown hair and a blue sweatshirt, sitting on top of a large, funny-looking hat. He looks silly.
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear thin black outlines, simple cel-shading, large expressive eyes.
Format: 11:10 aspect ratio, solid white background #FFFFFF, centered full view.
Negative: cropped, cut off, realistic photo, 3d render, scary, dark, neon.
```
**Result:** [comp_sam_2.png](file:///Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_sam_2.imageset/comp_sam_2.png)

## 2026-09-23 — Comprehension Set Regeneration

Reason: replace the visually inconsistent first-story answer set while preserving its gentle absurdity. The three images were generated as one coordinated set and imported at 600 × 600.

### Shared Prompt Block

```markdown
Use case: illustration-story
Asset type: StorySlider comprehension answer card for K–2 readers
Input images: Image 1 is the canonical current Sam identity reference and controls Sam's face, hair, age, and outfit. Image 2 is a sitting-pose reference only. Do not copy its mat unless explicitly requested.
House style: StorySlider white-field vignette; clean digital vector illustration, modern storybook anime, rounded six-year-old proportions, large expressive brown eyes, clean medium-to-thin softened dark-brown outlines, gentle low-contrast cel shading, calm muted storybook palette.
Character lock: Sam must remain the same child in every card: soft messy medium-brown hair, rounded six-year-old face, blue hooded jacket over a cream shirt, khaki cargo shorts, red sneakers. Friendly calm expression; no teeth-baring grin.
Format: square 1:1; pure solid white #FFFFFF connected to all four edges; one tight centered subject/action cluster; complete body and complete prop fully in frame; generous white breathing room on every side; soft contact shadow only.
Set consistency: match the companion answer cards in scale, camera angle, line weight, finish, lighting, and emotional energy. No image may look more rewarding or more polished than another.
Constraints: no text, letters, labels, badge, check mark, glow, pointing gesture, symbols, watermark, scenery, room, wall, window, horizon, landscape, floor plane, colored panel, circle or blob backdrop, decorative frame, extra characters, extra props, montage, split scene, object face, crop, edge contact, floating parts, malformed hands, teen-like proportions, neon or candy colors, heavy black outlines, glossy 3D, photorealism.
```

References used:

- Identity: `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_sam.imageset/story_sam.png`
- Sitting pose: `/Users/ricky/workspace/StorySliderArt/Characters/Sam/sam_sitting.jpeg`
- Visual calibration: `story_pip_the_pig.png`, `story_the_dig.png`, `level_1_card.png`, and `level_2_card.png`

### Answer 0: On a cat

```markdown
Primary request: Illustrate the literal answer choice “On a cat” for the question “Where did Sam sit?”
Subject/action: Sam sits gently and securely astride the back of one unusually large but unmistakably ordinary orange tabby cat. The cat stands naturally on all four paws with a calm, mildly puzzled expression; it is safe and friendly, not distressed, sweating, frightened, squashed, or treated like a vehicle. Sam's hands rest lightly near the cat's shoulders and both legs hang visibly to either side.
Animal style: rounded simplified K–2 cat anatomy matching the child illustration's outline weight and gentle shading; minimal fur detail; ordinary animal with no clothes, accessories, or human behavior.
Semantic clarity: Sam is visibly sitting ON the cat, not beside it. The absurd scale supplies a small gentle joke, but the result should look intentionally art-directed rather than zany.
Palette: muted apricot/orange tabby balanced by Sam's muted blue jacket, warm neutrals, and restrained red shoes.
```

Accepted master: `comp_sam_0.png`

### Answer 1: On a mat

```markdown
Primary request: Illustrate the literal answer choice “On a mat” for the question “Where did Sam sit?”
Subject/action: Sam sits comfortably cross-legged on one simple rectangular woven mat. Both hands rest naturally near his knees. The mat is low, flat, and fully visible around him, with rounded corners, a thin muted tan border, and a quiet cream center. Sam's seated pose is stable and anatomically natural.
Semantic clarity: Sam is visibly sitting ON the mat. This is the correct choice, but include no correctness cue and do not make Sam happier, brighter, larger, or more detailed than in the companion cards.
Palette: muted blue jacket, cream shirt and mat, warm tan shorts, restrained dusty red sneakers; no rainbow pattern or saturated primaries.
```

Accepted master: `comp_sam_1.png`

### Answer 2: On a hat

```markdown
Primary request: Illustrate the literal answer choice “On a hat” for the question “Where did Sam sit?”
Subject/action: Sam sits securely on the crown and brim of one oversized but otherwise ordinary soft wide-brim hat resting on the ground. The complete hat is easy to recognize: a softly dented rounded crown, continuous wide brim, and one simple muted blue band. Sam sits calmly with knees bent and hands resting naturally; his body clearly contacts the hat.
Structural plausibility: the soft hat compresses slightly under Sam while keeping a coherent crown and brim. No propeller, patchwork, eyes, mouth, face, mechanical pieces, costume elements, or toy-vehicle styling.
Semantic clarity: Sam is visibly sitting ON the hat. The scale is gently silly but restrained and intentional.
Palette: warm oatmeal/tan hat with a muted blue band, balanced with Sam's calm blue jacket and warm neutrals.
```

Accepted master: `comp_sam_2.png`

### QA Verdicts

| Image | WHITE_FIELD | NO_SCENIC_BACKDROP | TIGHT_FOCAL_CLUSTER | MINIMAL_CUES | CARD_SCALE_MATCH | CALM_PALETTE_MATCH | SEMANTIC_SCALE_MATCH | STRUCTURAL_PLAUSIBILITY | ANIMAL_STYLE_MATCH |
|---|---|---|---|---|---|---|---|---|---|
| `comp_sam_0.png` | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| `comp_sam_1.png` | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | N/A |
| `comp_sam_2.png` | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | N/A |

All three final assets have an exact 600 × 600 canvas and pure-white pixels along all four outer edges. Full-size and 120 px card-size contact-sheet comparison passed against the four calibration anchors. The answer choices contain no correctness cues and use the same Sam identity, rendering treatment, and emotional energy.
