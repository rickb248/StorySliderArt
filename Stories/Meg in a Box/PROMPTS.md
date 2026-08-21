# Level 4 production prompts — Meg in a Box

**Source:** `01_meg_in_a_box.json` (`5982f48d…c3a2d`). **Character reference:**
`Characters/Meg/meg_reference_sheet.png`. **Original generation:** ImageGen, 2026-08-12.

All accepted images use this shared constraint: `Square 1:1 calm modern K–2 storybook anime,
pure solid white to every edge, centered full subject(s), generous whitespace, small soft shadow
only, no crop or edge contact, no scenery/room/background props, no text, letters, numbers,
logos, frames, or watermark.`

| Accepted file | Exact scene prompt | QA |
|---|---|---|
| `story_meg_in_a_box.png` | `Meg, matching the reference, sits in a plain brown cardboard box; a plain white cup and tiny unmarked beige gum piece are the only support cues.` | Pass |
| `comp_meg_in_a_box_0.png` | `Only Meg happily sits fully inside one plain brown cardboard box, hands on the edge; no cup, gum, cab, or tub.` | Pass |
| `comp_meg_in_a_box_1.png` | Replaced 2026-08-19; exact prompt below. | Pass |
| `comp_meg_in_a_box_2.png` | `Only Meg happily sits fully inside one plain white plastic tub; no box, cab, or gum.` | Pass |

## 2026-08-19 replacement — `comp_meg_in_a_box_1.png`

The prior candidate showed Meg standing beside the cab rather than sitting in it. It failed
literal-answer accuracy for `What did Meg sit in?` / `A cab`.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 4 comprehension answer image, replacement for L4-MEG-C1
Input image: Meg identity reference only. Preserve Meg exactly: about seven years old, medium warm-brown skin, black hair in two neat puff buns with dusty-lavender ties, large dark-brown eyes, muted teal cardigan over a cream shirt, dusty-plum skirt-over-leggings, gray-lavender sneakers, rounded young K-2 proportions.
Primary request: Depict the literal answer choice “A cab” to the question “What did Meg sit in?” Show only Meg happily seated fully inside one small simple child-sized yellow toy cab, with her torso and face clearly visible through the open top or large side opening and her hands resting naturally near the steering wheel. It must be unmistakable that Meg is sitting inside the cab, not standing beside it. Show the complete cab including all four wheels.
Style: StorySlider white-field vignette; calm modern K-2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted mustard-yellow cab balanced by Meg’s muted teal and plum clothing.
Composition: square 1:1, one tight Meg-and-cab cluster centered large at card scale, small contact shadow only, complete subject in frame, generous white breathing room, pure solid white #FFFFFF connected to all four edges.
Constraints: only Meg and one ordinary cab; no Max, no other person, no road, no room, no street, no landscape, no floor plane, no colored panel/blob, no text, no taxi sign or lettering, no check mark, no glow/correctness cue, no crop, no vivid lemon yellow, no realistic full-size vehicle, no face on cab, no watermark. Final intended delivery is 600x600.
```

**Generated source:** `exec-e34c50dd-e947-4274-93a2-f33cc9a3616b.png`.
**Accepted SHA-256:** `334ad36e6ad9fb018fcce8ab37460f07556db9079caeba5b1a17d09269863348`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`WHITE_FIELD=PASS`; `NO_SCENIC_BACKDROP=PASS`; `TIGHT_FOCAL_CLUSTER=PASS`;
`MINIMAL_CUES=PASS`; `CARD_SCALE_MATCH=PASS`; `CALM_PALETTE_MATCH=PASS`;
literal-answer accuracy, Meg continuity, and artifact review `PASS`.

## 2026-08-20 semantic correction — `comp_meg_in_a_box_1.png`

The 2026-08-19 replacement incorrectly interpreted `cab` as a child-sized toy car. Level 4
uses `cab` as an actual road-going taxi, so that candidate is superseded. The corrected image
shows Meg seated as a rear passenger inside a real full-size yellow taxi.

**Exact base prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 4 comprehension answer image, corrected replacement for L4-MEG-C1
Input images: Image 1 is the edit target and style/composition reference; replace its toy car with a real full-size taxi. Image 2 is Meg’s identity reference; preserve Meg exactly: about seven years old, medium warm-brown skin, black hair in two neat puff buns with dusty-lavender ties, large dark-brown eyes, muted teal cardigan over a cream shirt, dusty-plum skirt/leggings, gray-lavender sneakers, rounded young K–2 proportions.
Primary request: Depict the literal answer choice “A cab” for the question “What did Meg sit in?” Show Meg clearly seated inside the rear passenger seat of a parked, real full-size yellow taxi/cab. The complete taxi must look unmistakably like an ordinary road-going sedan scaled for adults—not a toy, ride-on car, convertible, go-kart, or child-sized vehicle. Use an enclosed roof, windshield, side windows, four doors, realistic adult-sized wheels, door handles, mirrors, and normal sedan proportions. Let Meg be clearly visible through a large open rear door or open rear side window; she is a passenger, not holding a steering wheel or driving. Keep her body visibly inside the passenger cabin.
Scene/backdrop: StorySlider white-field vignette, pure solid white #FFFFFF connected to all four edges, one small soft contact shadow only.
Style/medium: calm modern K–2 storybook anime digital vector illustration; gentle medium-to-thin dark-charcoal outlines; soft low-contrast cel shading; muted mustard-yellow taxi balanced by Meg’s muted teal and plum clothing.
Composition/framing: square 1:1, centered tight Meg-and-taxi cluster, show the complete taxi without cropping or edge contact, three-quarter side view, generous white breathing room, readable at comprehension-card size.
Constraints: only Meg and one parked real taxi; no driver, no other person, no road, street, room, landscape, floor plane, colored panel/blob, text, letters, numbers, logos, checker lettering, check mark, glow/correctness cue, anthropomorphic vehicle face, or watermark. Do not depict a toy car, child-sized car, convertible, bumper car, or go-kart. Final intended delivery is 600x600 PNG.
```

The first corrected output had correct semantics but touched the left canvas edge. A targeted
follow-up preserved the scene and zoomed the complete vehicle out 15–20 percent, requiring white
clearance around the entire cab.

**Generated sources:** base `exec-dbfec9e3-0cd0-4311-a0dd-0a6f7c462147.png`; accepted framing
correction `exec-83edca52-a50c-4f8f-9277-9b806aebe18c.png`.
**Accepted SHA-256:** `9a979a81d92fb3278552f31382866b80238a40e7e3247605087546cb89f776d7`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`REAL_FULL_SIZE_TAXI=PASS`; `MEG_REAR_PASSENGER=PASS`; `NO_TOY_VEHICLE=PASS`;
`COMPLETE_VEHICLE=PASS`; `NO_EDGE_CONTACT=PASS`; `WHITE_FIELD=PASS`;
`MEG_CONTINUITY=PASS`; `NO_TEXT=PASS`.

## 2026-08-20 door-mechanics correction — `comp_meg_in_a_box_1.png`

The accepted real-taxi candidate still depicted the rear passenger door with implausible hinge
geometry. This correction closes every door and keeps Meg visible through the fully lowered rear
passenger window, removing ambiguity while preserving the literal `A cab` answer.

**Exact prompt:**

```text
Use case: illustration-story
Asset type: StorySlider Level 4 comprehension answer image, mechanical correction for L4-MEG-C1
Input images: Image 1 is the edit target. Preserve its real full-size yellow taxi, three-quarter side view, overall scale, centered framing, complete vehicle, white-field composition, Meg’s rear-passenger placement, palette, and storybook rendering. Image 2 is Meg’s identity reference; preserve Meg’s face, hair in two puff buns with lavender ties, skin tone, teal cardigan, cream shirt, plum clothing, gray-lavender sneakers, age, and expression.
Primary request: Correct only the rear passenger-door presentation. Remove the incorrectly hinged open door and show the rear passenger door fully closed, flush with the car body, with ordinary front-hinged road-car door seams and a normal exterior handle. Roll the rear passenger window fully down so Meg remains clearly visible seated inside the rear passenger seat. Meg may rest one hand naturally near the open window edge, but her torso and legs remain inside the cabin. All four doors are closed; no door is open.
Mechanical accuracy: standard four-door sedan construction; front edge of each rear door is beside the center B-pillar and rear edge is beside the rear wheel/quarter panel; conventional door seams; no rear-hinged or suicide door; no missing pillar; no duplicated door or handle.
Scene/backdrop: pure solid white #FFFFFF connected to all four edges, one small soft contact shadow only.
Style/medium: calm modern K–2 storybook anime digital vector illustration, gentle dark-charcoal outlines, soft low-contrast cel shading, muted mustard-yellow taxi.
Composition/framing: square 1:1, complete taxi and Meg centered with generous white clearance on all sides; no crop or edge contact; readable at comprehension-card size.
Constraints: real adult-sized taxi, not a toy; Meg is a passenger and not driving; only Meg and one taxi; no driver or other person; no road, scenery, floor plane, text, letters, numbers, logos, check mark, glow, or watermark. Change only the faulty door/window area and preserve everything else. Final intended delivery is 600x600 PNG.
```

**Generated source:** `exec-06ad776c-ec8f-4e99-b823-78d1e90badde.png`.
**Accepted SHA-256:** `2d6bd7f650343a8f171db4d53076ed17cca8fe0c4a521078843e64cfded47d99`.

Final processing resized to 600×600 PNG and normalized only the edge-connected near-white
background to exact `#FFFFFF`.

`REAL_FULL_SIZE_TAXI=PASS`; `ALL_DOORS_CLOSED=PASS`; `CONVENTIONAL_DOOR_SEAMS=PASS`;
`MEG_VISIBLE_THROUGH_OPEN_WINDOW=PASS`; `MEG_REAR_PASSENGER=PASS`; `WHITE_FIELD=PASS`;
`NO_EDGE_CONTACT=PASS`; `NO_TEXT=PASS`.

Rejected history includes the original 2026-08-12 candidate that placed Meg beside the cab.
