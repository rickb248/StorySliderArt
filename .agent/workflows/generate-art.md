---
description: Used to generate consistent art.
---

# Story Slider Art Generation Guidelines

This document serves as the source of truth for generating images for the Story Slider project. The target audience is children in grades K-2 (ages 5-8).

## Core Art Style Definition

The art style is designed to be **calm, clear, and easily processable** for young children. It avoids overstimulation and ambiguity.

**Key Characteristics:**
*   **Medium/Technique:** Soft vector illustration. It should look digital but organic, not mechanical.
*   **Line Work:** Clear black outlines defining shapes. Use thin but distinct black strokes to separate colors and define the character's form. Avoid lineless or fuzzy edges.
*   **Color Palette:** Calm, soothing colors.
    *   Use: Pastels, soft earth tones, muted primaries.
    *   Avoid: Neon colors, jarring contrasts, overly saturated "electric" hues.
*   **Shading & Lighting:** Simple shading.
    *   Use: Flat shading or soft, subtle gradients to show form.
    *   Avoid: Harsh cast shadows, complex realistic lighting, dramatic noir lighting.
*   **Realism Level:** Semi-realistic / Stylized Realism.
    *   Proportions should be generally realistic (not super-deformed or abstract).
    *   **No Anthropomorphism:** Inanimate objects (buses, trees, clouds) do **NOT** have faces or human traits.
    *   Characters should feel friendly and approachable.
*   **Composition & Format:**
    *   **Aspect Ratio:** Always maintain an **11:10** aspect ratio.
    *   **Background:** Always use a solid white background (**#FFFFFF**).
    *   **Whitespace:** Minimize whitespace; the subject should fill the frame as much as possible while maintaining the aspect ratio and a clean look.

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

When creating prompts for image generation models, follow this structure:

```markdown
**Subject:** [Character Name] doing [Action] in [Setting].
**Style Modifiers:** soft vector illustration, children's book style, K-2 audience, calm atmosphere, pastel colors, clear lines, simple shading, flat design style.
**Format:** 11:10 aspect ratio, solid white background #FFFFFF, minimal whitespace, subject fills frame.
**Negative Prompts:** realistic photo, 3d render, shiny, complex details, scary, dark, night, neon, messy lines, sketch, face on object.
```

## Examples of Usage
*   *Correct:* A yellow school bus driving down a quiet suburban street.
*   *Incorrect:* A smiling school bus waving hello. (No faces on objects).
*   *Correct:* Sam reading a book under a large oak tree.
*   *Incorrect:* Sam fighting a dragon with explosions. (Too violent/chaotic, keep it calm).
