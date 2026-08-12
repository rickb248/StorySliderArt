---
description: Used to generate consistent art.
---

# Story Slider Art Generation Guidelines

This document serves as the source of truth for generating images for the Story Slider project. The target audience is children in grades K-2 (ages 5-8).

## Core Art Style Definition

The house style is the **StorySlider White-Field Vignette**: a simple, playful, modern storybook-anime illustration centered on the most important person, animal, object, relationship, or action. It is not a full scenic illustration.

**Key Characteristics:**
*   **Medium/Technique:** Digital vector illustration with clean, crisp edges.
*   **Line Work:** Clean, consistent dark-charcoal or softened dark-brown outlines. Keep contours medium-to-thin and visually gentle while preserving card-scale clarity. Avoid heavy pitch-black contouring, harsh line-weight jumps, lineless edges, fuzziness, or sketchiness.
*   **Color Palette:** Muted, warm, softly saturated storybook colors.
    *   Use: Warm neutrals, muted blues and greens, dusty secondary colors, gentle earth tones, and restrained low-contrast accents.
    *   Preserve literal colors calmly: render story-required red as brick, cranberry, terracotta, dusty red, or muted coral; yellow as mustard, ochre, butter, or straw; orange as clay, burnt orange, or muted apricot. Keep the named color recognizable.
    *   If a large named-color object is necessary, lower its saturation and balance it with neutrals rather than making it brighter.
    *   Avoid: Neon, large areas or repeated accents of fire-engine red, lemon yellow, vivid orange, candy primaries, multiple competing high-saturation warm colors, stark contrast, muddy color, or a glossy digital-primary look.
    *   Playfulness comes from pose, expression, silhouette, scale, and action—not color intensity.
*   **Characters:** Anime-influenced designs.
    *   **Eyes:** Large, expressive anime-style eyes with clear highlights and distinct pupils. They should look like the characters in the `Inspiration/` folder (e.g., `sam_standing.jpeg`).
    *   **Hair:** Stylized but clean hair shapes with simple highlights and shadows.
    *   **Proportions:** Young, rounded K-2 storybook proportions: slightly larger head and eyes, soft cheeks and silhouettes, compact limbs, and unmistakably child-aged bodies. Avoid extreme Chibi, tall or slender teen-like children, fashion-illustration anatomy, or semi-realistic adult proportions.
    *   **Friendly & Approachable:** Characters should have warm, kind energy.
*   **Shading & Lighting:** Soft, low-contrast cel-shading.
    *   Use: 1-2 gentle shadow levels to show form, with soft highlights on hair and eyes and warm ambient light when appropriate.
    *   Avoid: Deep dramatic shadows, glossy highlights, complex gradients, realistic textures, or frightening high-contrast lighting. Gentle dusk, bedtime, or night cues are allowed when the story requires them and the subject remains clear.
*   **Realism Level:** Stylized Anime Realism.
    *   **No Decorative Anthropomorphism:** Ordinary objects (buses, trees, clouds) do **NOT** have faces or human traits. An approved story may explicitly establish a living fantasy object; depict only the traits the prose and art brief support.
*   **Composition & Format:**
    *   **Image Size:** Always generate images at **600px × 600px** (square).
    *   **Aspect Ratio:** Always maintain a **1:1 square** aspect ratio.
    *   **White Field:** Pure white (**#FFFFFF**) must remain visually connected to all four canvas edges around the complete illustration cluster. This is blocking, not a preference.
    *   **Focused Vignette:** Show one tight cluster: normally one to three characters plus only the props necessary to understand the beat. The subject/action should carry roughly 70-85% of the visual attention.
    *   **Cue Budget:** Use zero to two small support cues. Good cues include a contact shadow, a small grass/dirt/rug patch, one log, or a short tabletop fragment when the story requires it. Remove any cue that does not explain the action.
    *   **Forbidden Scenery:** Do not show a room interior, wall, window, corner, broad floor plane, bed-and-furniture arrangement, cabinets, shelves, kitchen, bedroom, dining room, horizon, landscape, scenic lighting field, background rectangle, colored panel, circle, blob, or decorative frame unless a human explicitly approves a rare exception before generation.
    *   **Whitespace & Composition:** Keep every subject completely in view and centered as a cohesive vignette, with visible white breathing room on all sides.
    *   **No Crops:** Portions of the characters or objects (feet, ears, tails, wheels) must **NEVER** go off-screen.
    *   **Intentional Framing:** Usually show the full subject. A closer view is allowed when it makes the story action or emotion clearer, but never crop essential body parts, props, or the action itself.
    *   **Card-Scale Readability:** Compose for the app's small story and answer cards. Avoid wide establishing shots. Make the character, animal, object, relationship, or action—not its setting—the first and dominant read.
    *   **Single-Scene Covers:** Every cover shows one continuous scene at one moment. Do not use montages, triptychs, collages, storyboards, split scenes, repeated characters, or multiple stages of an action.
    *   **Physical Grounding:** Props must have believable gravity. Prefer a hand, container, contact shadow, or cropped support fragment. Do not add a full room or floor merely to support a prop.
    *   **Narrative Focal Point:** One action or relationship is immediately dominant. Pose, gaze, expression, prop placement, and the minimal setting cues should explain what matters without visual clutter.
    *   **Cohesive Vignette:** Characters and props must share believable scale, light, contact, and spatial relationships. Cohesion comes from pose, overlap, contact, gaze, and a shared shadow—not from constructing an environment.
    *   **Story-Specific Delight:** When the approved story is playful, show its exact comic escalation, surprise, reversal, pretend transformation, animal agency, or visual incongruity. Do not manufacture whimsy with decorative confetti or object faces.

## Approved House-Style Calibration

Before writing a prompt or approving an image, open at least four approved anchors: two Level 1-2 story covers and two level cards. Use these primary composition anchors:

* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_pip_the_pig.imageset/story_pip_the_pig.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_the_dig.imageset/story_the_dig.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_a_bell_for_the_pup.imageset/story_a_bell_for_the_pup.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_the_log.imageset/story_the_log.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_my_dad.imageset/story_my_dad.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_dot_hops.imageset/story_dot_hops.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_sit.imageset/story_sit.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_the_dog.imageset/story_the_dog.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/level_1_card.imageset/level_1_card.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/level_2_card.imageset/level_2_card.png`
* `/Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/level_3_card.imageset/level_3_card.png`

Use these anchors for composition, white-field treatment, simplicity, palette, contrast, line weight, child proportions, and softness. Use `Characters/` reference images only for identity. `story_a_dot_on_the_map` and any other full-scene image are not composition or background references. Do not use legacy Level 3 or Level 4 images as style exemplars unless a human explicitly approved that individual image under this vignette gate.

Palette matching is blocking. Compare each candidate with the Level 1-2 anchors at full size and card size. Fail an image that reads noticeably hotter, brighter, or more saturated, even if the story names a warm color and all story facts are correct.

When the image tool accepts references, include the most relevant style anchor separately from character references and state that the style anchor controls composition while character references control identity. Prevent semantic contamination: never attach a style anchor containing a person, animal, or distinctive prop that is absent from the target. For object-only images, prefer a semantically neutral level-card or object anchor. For character images, prefer an anchor with the same subject type and no unrelated cast. Reject any generated character, animal, or prop copied from an anchor but absent from the approved target. Perform a side-by-side contact-sheet check at full size and card size. Reject a candidate that becomes a room, landscape, broad floor plane, or backdrop; contains nonessential scenery; or is noticeably more saturated, contrasty, heavily outlined, realistic, or tall/slender than the anchors even when its story facts are correct.

## Diversity and Inclusion

The Story Slider project aims to be diverse and inclusive, representing a wide range of ethnicities, skin tones, and backgrounds. 

**Guidelines:**
*   **Skin Tones:** Use a variety of skin tones across the character roster (e.g., deep espresso, warm mahogany, golden tan, fair porcelain, olive tones). 
*   **Hair Textures and Styles:** Include various hair types (curly, coily, wavy, straight) and styles (braids, locs, afros, bobs, short cuts).
*   **Representation:** When introducing new characters, consider how they contribute to the overall diversity of the story world.
*   **Avoid Stereotypes:** Ensure all characters are portrayed with the same level of care, friendliness, and quality, avoiding any ethnic or cultural stereotypes.

## Character Consistency

When generating images including specific characters, ensure consistency with established designs found in the `Characters/` directory.

### Character Reference Files
For any character (e.g., Sam), always check their specific directory for:
1.  **`CHARACTER.md`**: Detailed physical description and personality traits.
2.  **`PROMPTS.md`**: Successful prompts used for previous generations to maintain style consistency.

### Multi-Pose & Emotion Reference Sheet
To ensure consistency, generate character reference sheets with the following variations:
*   **Poses:**
    *   Standing (front view, 3/4 view)
    *   Sitting (cross-legged, on a chair)
*   **Emotions:**
    *   Normal/Neutral (calm, attentive)
    *   Happy (smiling, joyful)

**Prompting for Reference Sheets:**
```markdown
**Subject:** [Character Name] character sheet, multiple poses and expressions.
**Poses:** standing, sitting cross-legged.
**Expressions:** happy, neutral.
**Style Modifiers:** [Standard Style Modifiers], white background, character design sheet.
```

### Sam
*   **Reference Files:** Check `Characters/Sam/CHARACTER.md` and `Characters/Sam/PROMPTS.md`.
*   **Key References:** [sam_sitting.png](file:///Users/ricky/workspace/StorySliderArt/Characters/Sam/sam_sitting.png), [sam_standing.png](file:///Users/ricky/workspace/StorySliderArt/Characters/Sam/sam_standing.png).

## Prompting Strategy

When creating prompts, follow this structure to maintain the Modern Storybook Anime style:

```markdown
**House Style:** StorySlider white-field vignette. Pure white background extends uninterrupted to every edge. Show only one tight subject/action cluster.
**Subject:** [Character Name] doing [Action] with [essential prop or relationship only].
**Story Beat:** [Approved child hook and signature visual beat]. Show [single focal action] with [specific readable emotion or anticipation].
**Composition:** One cohesive vignette, not a scenic illustration. [Zero to two essential support cues]. The subject/action carries 70-85% of the visual attention. Ground with contact, overlap, a small shadow, or one support fragment; do not build a setting.
**Palette:** Match the calming Level 1-2 anchors: warm neutrals, muted blues/greens, dusty secondary colors, gentle earth tones, restrained warm accents, and low-contrast color relationships. If prose names red/yellow/orange, use a recognizable brick/cranberry/terracotta, mustard/ochre/butter/straw, or clay/burnt-orange/muted-apricot variant. Mute large colored objects and balance them with neutrals.
**Style Modifiers:** digital vector illustration, modern storybook anime style, high quality, K-2 audience, playful readable pose, calm muted storybook palette, gentle low-contrast cel-shading, clean medium-to-thin dark-charcoal outlines, rounded young child proportions, large expressive eyes.
**Format:** 600px × 600px, 1:1 square, pure solid white background #FFFFFF connected to all four edges, complete subject in frame, white breathing room on every side.
**Negative Prompts:** room interior, wall, window, corner, broad floor plane, bedroom, kitchen, dining room, cabinets, shelves, bed-and-furniture arrangement, horizon, landscape, scenic backdrop, background rectangle, colored panel, circle backdrop, blob backdrop, decorative frame, excessive props, montage, triptych, collage, storyboard, split scene, repeated character, multiple moments, wide establishing shot, panoramic view, tiny subject, generic standing pose, floating object, unsupported prop, cropped essential action, cut off, bleeding edges, touching edges, heavy pitch-black outlines, harsh contrast, fire-engine red, lemon yellow, vivid orange, traffic-cone orange, candy-color saturation, multiple competing saturated warm colors, fully saturated primary color blocks, glossy plastic rendering, lineless, fuzzy, 3d render, realistic photo, shiny, complex textures, frightening, neon, messy lines, sketch, face on object, extreme muscle definition, tall teen-like child, slender fashion proportions, adult-like child anatomy, extreme Chibi proportions.
```

## Examples of Usage
*   *Correct:* A yellow school bus with two small motion marks and a soft contact shadow on white.
*   *Incorrect:* A smiling school bus waving hello. (No faces on objects).
*   *Correct:* Sam reading a book on a tiny grass patch with one tree-trunk fragment on white.
*   *Incorrect:* Sam fighting a dragon with explosions. (Too violent and visually chaotic for the audience.)
