# Sam and the Cat — replacement prompt history

**Run:** 2026-08-19. **Tool:** built-in ImageGen. **Source:**
`StorySlider/Content/Level 1/Sam and the Cat/sam_and_the_cat.json`. **Target:**
`comp_sam_and_the_cat_2.png` for answer choice 2, `On a hat`. **Character reference:**
`Characters/Cat/cat_sitting.png`.

## Replacement reason

The prior candidate showed the cat inside a woven basket rather than sitting on a hat. It
failed literal-answer accuracy.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 1 comprehension answer image, replacement for L1-CAT-C2
Input image: Cat identity reference only. Preserve the same friendly natural orange tabby: warm muted orange fur, subtle darker stripes, cream muzzle/chest accents, large expressive dark anime-style eyes, simple gentle outlines. The cat remains an ordinary four-legged animal with no clothes.
Primary request: Depict the literal answer choice “On a hat” to the question “Where did the cat sit?” Show the orange tabby sitting squarely on top of one large ordinary soft tan wide-brim hat that lies naturally on the ground. The cat’s paws visibly contact and slightly compress the crown/brim, making “on the hat” unmistakable. The hat has no face, eyes, propeller, limbs, ribbon text, or magical traits.
Style: StorySlider white-field vignette; calm modern K-2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted warm orange, tan, and cream palette.
Composition: square 1:1, one tight cat-and-hat cluster centered large at card scale, full cat and complete hat visible, small contact shadow only, generous white breathing room, pure solid white #FFFFFF connected to all four edges.
Constraints: only one cat and one hat; no basket, no room, no floor plane, no furniture, no landscape, no colored panel/blob, no text, no check mark, no glow/correctness cue, no crop, no saturated primaries, no anthropomorphic object, no watermark. Final intended delivery is 600x600.
```

**Generated source:** `exec-cde72d58-fad5-4b8c-8fb3-70353e3f2e98.png`.
**Accepted SHA-256:** `ed83887ec596ae677fe941dfa558fa39d94f174b764f29749abd29e9ba4ba972`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`WHITE_FIELD=PASS`; `NO_SCENIC_BACKDROP=PASS`; `TIGHT_FOCAL_CLUSTER=PASS`;
`MINIMAL_CUES=PASS`; `CARD_SCALE_MATCH=PASS`; `CALM_PALETTE_MATCH=PASS`;
literal-answer accuracy, Cat continuity, ordinary-object treatment, and artifact review `PASS`.

## 2026-08-19 size/aspect correction — `story_sam_and_the_cat.png`

The prior story cover was a 360×540 portrait asset. Because the app presents story covers in
square and near-square frames, it could render narrow in fit layouts, crop differently in fill
layouts, and soften at larger display sizes. This replacement preserves the existing single-cat
cover concept while rebuilding it natively for a square 600×600 canvas.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 1 story-cover replacement for story_sam_and_the_cat; correct a portrait source to a square production asset without redesigning its content.
Input images: Image 1 is the edit target/current cover. Preserve its single-cat concept, seated pose, friendly expression, warm orange-tabby coloring, cream muzzle/chest/paws, rounded K–2 proportions, and clean white-field presentation. Image 2 is the Cat identity reference; use it only to keep the same ordinary orange tabby identity and simple dark outline language.
Primary request: Recreate the same single friendly orange tabby sitting upright, now natively composed for a square 1:1 canvas at high detail. Show the complete cat and full curved tail, centered large enough to read clearly as a story cover, with balanced whitespace on every side. Keep the pose and emotional tone calm and cheerful.
Style/medium: calm modern K–2 storybook anime digital vector illustration, gentle medium dark-charcoal outlines, soft low-contrast cel shading, muted warm orange and cream palette.
Scene/backdrop: pure solid white #FFFFFF extending continuously to all four edges; one small soft neutral contact shadow only.
Composition: square 1:1, centered full-body cat, no crop or edge contact, no large empty portrait-style bands, visually balanced at thumbnail size.
Constraints: only one ordinary cat; no Sam, no mat, no hat, no furniture, no room, no landscape, no colored panel or background blob, no text, letters, logo, frame, or watermark; no clothing or anthropomorphic traits. Do not introduce a new story beat. Final intended delivery is 600x600 PNG.
```

**Generated source:** `exec-919e2a4f-dfb9-4dfb-8628-4270635f6052.png`.
**Accepted SHA-256:** `cdc7318b99092f844f82743e1ec559ada1e7924ee1cd2ad28d6d5e40c71fdd2f`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`SIZE=PASS`; `SQUARE_ASPECT=PASS`; `WHITE_FIELD=PASS`; `NO_SCENIC_BACKDROP=PASS`;
`FULL_SUBJECT=PASS`; `CAT_CONTINUITY=PASS`; `NO_STORY_REDESIGN=PASS`.
