---
description: Used to generate consistent art.
---

# Story Slider Art Generation Guidelines

This document serves as the source of truth for generating images for the Story Slider project. The target audience is children in grades K-2 (ages 5-8).

## Core Art Style Definition

The art style is **Modern Storybook Anime**. It is designed to be **calm, clear, and high-quality**, featuring anime-influenced character designs with a crisp vector look.

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
    *   Avoid: Complex gradients, realistic textures, or dramatic lighting.
*   **Realism Level:** Stylized Anime Realism.
    *   **No Anthropomorphism:** Inanimate objects (buses, trees, clouds) do **NOT** have faces or human traits.
*   **Composition & Format:**
    *   **Image Size:** Always generate images at **600px × 600px** (square).
    *   **Aspect Ratio:** Always maintain an **11:10** aspect ratio (the 600×600 square satisfies this).
    *   **Background:** Always use a solid white background (**#FFFFFF**).
    *   **Whitespace & Composition:** The subject must be **completely in view** and centered. Ensure there is visible whitespace (breathing room) on all sides of the subject. 
    *   **No Crops:** Portions of the characters or objects (feet, ears, tails, wheels) must **NEVER** go off-screen.
    *   **Full Body:** Always provide a full body/full object view unless specifically asked otherwise.

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
**Style Modifiers:** digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear black outlines, simple cel-shading, large expressive eyes, friendly expression.
**Format:** 600px × 600px, 11:10 aspect ratio, solid white background #FFFFFF, minimal whitespace, subject fills frame.
**Negative Prompts:** lineless, fuzzy, 3d render, realistic photo, shiny, complex textures, scary, dark, night, neon, messy lines, sketch, face on object, extreme muscle definition, Chibi proportions.
```

## Examples of Usage
*   *Correct:* A yellow school bus driving down a quiet suburban street.
*   *Incorrect:* A smiling school bus waving hello. (No faces on objects).
*   *Correct:* Sam reading a book under a large oak tree.
*   *Incorrect:* Sam fighting a dragon with explosions. (Too violent/chaotic, keep it calm).
