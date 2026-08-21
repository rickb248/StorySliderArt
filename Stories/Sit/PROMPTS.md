# Sit — replacement prompt history

**Run:** 2026-08-19. **Tool:** built-in ImageGen. **Source:**
`StorySlider/Content/Level 2/Sit/sit.json`. **Target:** `comp_sit_1.png` for answer
choice 1, `A mat`.

## Replacement reason

The prior candidate placed the mat on a broad wooden floor/background rectangle. It failed
`NO_SCENIC_BACKDROP` and `MINIMAL_CUES`.

## Accepted generation

**Edit target:** prior `comp_sit_1.png`; the woven mat identity was retained.

**Exact prompt:**

```text
Use case: precise-object-edit
Asset type: StorySlider Level 2 comprehension answer image, replacement for L2-SIT-C1
Input image: edit target; preserve the woven rectangular tan mat's basic identity and handcrafted weave.
Primary request: Remove the entire wooden floor and every scenic/background element. Show only one simple rectangular woven tan mat, fully visible, centered, resting naturally on a pure solid white #FFFFFF field. Use a very small soft contact shadow only.
Style: StorySlider white-field vignette; calm modern K-2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted warm neutral palette.
Composition: square 1:1, one large immediately recognizable mat, generous white breathing room on every side, pure white connected to all four edges, no crop.
Constraints: no child, no pig, no other prop, no floorboards, no broad floor plane, no room, no wall, no background rectangle, no colored panel, no scenery, no text, no watermark, no decorative frame, no saturated colors. Keep the result suitable for final 600x600 delivery.
```

**Generated source:** `exec-f69f93d2-c3dd-494f-afee-e62d629e2503.png`.
**Accepted file:** `comp_sit_1.png`. **SHA-256:**
`def9511fda3e385985f1bebf753ef3189906bb39c60d65130c47536c03fb665e`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`WHITE_FIELD=PASS`; `NO_SCENIC_BACKDROP=PASS`; `TIGHT_FOCAL_CLUSTER=PASS`;
`MINIMAL_CUES=PASS`; `CARD_SCALE_MATCH=PASS`; `CALM_PALETTE_MATCH=PASS`;
literal-answer accuracy and artifact review `PASS`.
