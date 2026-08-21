# Dot Hops — replacement prompt history

**Run:** 2026-08-19. **Tool:** built-in ImageGen. **Source:**
`StorySlider/Content/Level 2/Dot Hops/dot_hops.json`. **Character reference:**
`Characters/Dot/CHARACTER.md` plus the accepted `story_dot_hops.png` identity.

## `comp_dot_hops_0.png` — `In a pot`

The prior candidate omitted Dot and added a broad plank. It failed literal-answer accuracy,
`NO_SCENIC_BACKDROP`, and `TIGHT_FOCAL_CLUSTER`.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 2 comprehension answer image, replacement for L2-DOT-C0
Input image: character identity reference only. Preserve Dot as the same joyful six-year-old girl: fair skin, bright blonde pigtails tied with dusty pink bows, rounded young K-2 proportions, pink dress with subtle dots, pale blue leggings, muted red shoes. Do not copy the stepping-stone scene.
Primary request: Depict the literal answer choice “In a pot” to the question “Where did Dot hop?” Show Dot mid-hop into one large ordinary terracotta flower pot, with her lower legs inside the open pot and her upper body clearly above the rim. Her arms are lifted for balance and the hopping action is immediately readable. The pot has no plant and no face.
Style: StorySlider white-field vignette; calm modern K-2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted warm neutrals and dusty pinks.
Composition: square 1:1, one tight Dot-and-pot cluster centered large at card scale, complete subject in frame, small contact shadow only, generous white breathing room, pure solid white #FFFFFF connected to all four edges.
Constraints: one Dot only, one pot only, no room, no floor plane, no garden, no landscape, no flowers, no colored background shape, no text, no check mark, no sparkle/glow/correctness cue, no crop, no saturated primaries, no anthropomorphic object, no watermark. Final intended delivery is 600x600.
```

**Generated source:** `exec-3cde23c6-751c-49e5-a1fb-7bbb2d7bf297.png`.
**SHA-256:** `a9132ff2a9e5b94789c23e0eab1dad0ae2c540f6161a4b3ebd4f291eb290a727`.

## `comp_dot_hops_2.png` — `In the mud`

The prior candidate omitted Dot and constructed a scenic pond/landscape. It failed
literal-answer accuracy, `NO_SCENIC_BACKDROP`, `TIGHT_FOCAL_CLUSTER`, and `MINIMAL_CUES`.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 2 comprehension answer image, replacement for L2-DOT-C2
Input image: character identity reference only. Preserve Dot as the same joyful six-year-old girl: fair skin, bright blonde pigtails tied with dusty pink bows, rounded young K-2 proportions, pink dress with subtle dots, pale blue leggings, muted red shoes. Do not copy the stepping-stone scene.
Primary request: Depict the literal answer choice “In the mud” to the question “Where did Dot hop?” Show Dot at the instant she lands with both shoes in one small shallow muddy patch. Her bent knees, lifted arms, and two restrained mud droplets make the hopping landing immediately clear. Keep her face cheerful but not more celebratory or detailed than the other answer choices.
Style: StorySlider white-field vignette; calm modern K-2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted warm neutrals, dusty pink, and gentle earth tones.
Composition: square 1:1, one tight Dot-and-mud cluster centered large at card scale, complete body visible, only one small irregular mud patch as the necessary support cue, generous white breathing room, pure solid white #FFFFFF connected to all four edges.
Constraints: one Dot only; no pond, no puddle landscape, no grass, no flowers, no trees, no horizon, no sky, no room, no floor plane, no colored background shape, no text, no check mark, no sparkle/glow/correctness cue, no crop, no saturated primaries, no watermark. Final intended delivery is 600x600.
```

**Generated source:** `exec-c3dd9421-86a5-47e4-b506-ebd56e3917d9.png`.
**SHA-256:** `b89caca9af6350e515484b0c2acfd537ea8fd16cac79baebac8b7f04bbfa3e5f`.

Both accepted files were resized to 600×600 PNG and had only their edge-connected
near-white backgrounds normalized to exact `#FFFFFF`.

For both: `WHITE_FIELD=PASS`; `NO_SCENIC_BACKDROP=PASS`;
`TIGHT_FOCAL_CLUSTER=PASS`; `MINIMAL_CUES=PASS`; `CARD_SCALE_MATCH=PASS`;
`CALM_PALETTE_MATCH=PASS`; literal-answer accuracy, Dot identity, and artifact review `PASS`.
