---
description: Used to generate consistent art.
---

# Story Slider Art Generation Guidelines

This document serves as the source of truth for generating images for the Story Slider project. The target audience is children in grades K-2 (ages 5-8).

## Core Art Style Definition

The art style is **Modern Storybook Anime**. It is designed to be **inviting, clear, emotionally readable, and high-quality**, featuring anime-influenced character designs with a crisp vector look.

**Key Characteristics:**
*   **Medium/Technique:** Digital vector illustration with clean, crisp edges.
*   **Line Work:** Clear black outlines. Use distinct, consistent black strokes (like a clean ink felt-pen) to define all shapes and features. Avoid lineless, fuzzy, or sketchy edges.
*   **Color Palette:** Clean, vibrant but calm colors.
    *   Use: Soft primary colors, warm earth tones, and clear secondary colors.
    *   Avoid: Neon, overly muted/muddy tones, or complex textures.
*   **Characters:** Anime-influenced designs.
    *   **Eyes:** Large, expressive anime-style eyes with clear highlights and distinct pupils. They should look like the characters in the `Inspiration/` folder (e.g., `sam_standing.jpeg`).
    *   **Hair:** Stylized but clean hair shapes with simple highlights and shadows.
    *   **Proportions:** Slightly stylized but balanced (no extreme Chibi or abstract proportions).
    *   **Friendly & Approachable:** Characters should have warm, kind energy.
*   **Shading & Lighting:** Simple cel-shading.
    *   Use: 1-2 levels of flat shadow to show form. Soft highlights on hair and eyes.
    *   Avoid: Complex gradients, realistic textures, or frightening high-contrast lighting. Gentle dusk, bedtime, or night cues are allowed when the story requires them and the subject remains clear.
*   **Realism Level:** Stylized Anime Realism.
    *   **No Decorative Anthropomorphism:** Ordinary objects (buses, trees, clouds) do **NOT** have faces or human traits. An approved story may explicitly establish a living fantasy object; depict only the traits the prose and art brief support.
*   **Composition & Format:**
    *   **Image Size:** Always generate images at **600px × 600px** (square).
    *   **Aspect Ratio:** Always maintain a **1:1 square** aspect ratio.
    *   **Background:** Always use a solid white background (**#FFFFFF**).
    *   **Whitespace & Composition:** The subject must be **completely in view** and centered. Ensure there is visible whitespace (breathing room) on all sides of the subject. 
    *   **No Crops:** Portions of the characters or objects (feet, ears, tails, wheels) must **NEVER** go off-screen.
    *   **Intentional Framing:** Usually show the full subject. A closer view is allowed when it makes the story action or emotion clearer, but never crop essential body parts, props, or the action itself.
    *   **Card-Scale Readability:** Compose for the app's small story and answer cards. Avoid wide establishing shots that make characters or key actions tiny; normally size the main subject/action cluster to about 65–80% of the canvas while retaining the white border.
    *   **Single-Scene Covers:** Every cover shows one continuous scene at one moment. Do not use montages, triptychs, collages, storyboards, split scenes, repeated characters, or multiple stages of an action.
    *   **Physical Grounding:** Props must have clear support and believable gravity. A pan rests on a table or is firmly held; a bag rests on the ground or is carried; no object may float or appear accidentally airborne.
    *   **Narrative Focal Point:** One action or relationship is immediately dominant. Pose, gaze, expression, and prop placement should explain what matters without visual clutter.
    *   **Story-Specific Delight:** When the approved story is playful, show its exact comic escalation, surprise, reversal, pretend transformation, animal agency, or visual incongruity. Do not manufacture whimsy with decorative confetti or object faces.

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
**Subject:** [Character Name] doing [Action] in [Setting].
**Story Beat:** [Approved child hook and signature visual beat]. Show [single focal action] with [specific readable emotion or anticipation].
**Style Modifiers:** digital vector illustration, modern storybook anime style, high quality, K-2 audience, story-appropriate emotional energy, clean vibrant colors, clear black outlines, simple cel-shading, large expressive eyes.
**Format:** 600px × 600px, 1:1 square, pure solid white background #FFFFFF. The illustration has a clear white border on all four edges. No element touches or bleeds off the canvas.
**Negative Prompts:** montage, triptych, collage, storyboard, split scene, repeated character, multiple moments, wide establishing shot, panoramic view, tiny subject, generic standing pose, floating object, unsupported prop, circular frame, vignette, framed background, cropped essential action, cut off, bleeding edges, touching edges, lineless, fuzzy, 3d render, realistic photo, shiny, complex textures, frightening, neon, messy lines, sketch, face on object, extreme muscle definition, Chibi proportions.
```

## Examples of Usage
*   *Correct:* A yellow school bus driving down a quiet suburban street.
*   *Incorrect:* A smiling school bus waving hello. (No faces on objects).
*   *Correct:* Sam reading a book under a large oak tree.
*   *Incorrect:* Sam fighting a dragon with explosions. (Too violent and visually chaotic for the audience.)
