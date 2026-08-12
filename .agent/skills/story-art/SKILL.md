---
name: story-art
description: Generate and review playful K-2 StorySlider illustrations, including story covers and comprehension-choice images. Use for new art, regeneration, visual QA, prompt writing, or style repair. Enforce the approved white-field vignette house style, calming Level 1-2 palette, level-card calibration, one dominant story beat, young rounded characters, continuity, card-scale clarity, and physically supported props.
---

# Story Art Generation Skill

Use this skill whenever you need to generate or describe art for the Story Slider project.

## Instructions
1.  **Read the Complete Workflow**: Read `.agent/workflows/generate-art.md`, `.agent/workflows/generate-story-images.md`, and `.agent/workflows/story-illustration-quality-gates.md` completely before generation or review.
2.  **Lock the House Style**: Create a playful **StorySlider white-field vignette**, not a scenic illustration. Keep pure white connected to all four canvas edges. Show one tight subject/action cluster with only essential props and, when needed, one small support cue such as a contact shadow, rug patch, grass patch, dirt patch, log, or tabletop fragment. Reject rooms, walls, windows, corners, broad floor planes, landscapes, and rectangular or colored backdrops.
3.  **Calibrate Visually**: Before prompting, inspect the required approved Level 1-2 cover and level-card anchors named in `generate-art.md`. Match their composition and whitespace as well as their restrained saturation, gentle contrast, soft line weight, and rounded K-2 proportions. Character references control identity; house-style anchors control composition and rendering. When attaching an anchor to ImageGen, never use one containing a person or animal absent from the target; use a neutral level-card or object anchor for object-only images to prevent subject contamination.
4.  **Lock the Calm Palette**: Default to warm neutrals, muted blues/greens, dusty secondary colors, gentle earth tones, and low-contrast relationships. Reject large areas or repeated accents of fire-engine red, lemon yellow, vivid orange, candy/neon primaries, or multiple competing high-saturation warm colors. When prose names red, yellow, or orange, preserve recognition with a calm storybook variant—brick/cranberry/terracotta; mustard/ochre/butter/straw; clay/burnt orange/muted apricot—and balance large colored objects with neutrals. Create playfulness through pose, expression, silhouette, scale, and action, not color intensity.
5.  **Balance Energy and Clarity**: Visuals may be funny, surprising, cozy, or serious as the story requires, but must remain clear and emotionally safe for children in grades K-2.
6.  **No Decorative Object Faces**: Keep ordinary objects realistic. Give an object a face or agency only when the approved prose explicitly establishes it as a living fantasy character; never add anthropomorphism merely to make an image whimsical.
7.  **Preserve Identity**: Check the `Characters/` directory before generating recurring characters and include actual reference images when supported. Do not let a full-scene character reference override the white-field vignette composition.
8.  **One Moment Per Cover**: Depict one clear moment and one unified focal cluster. Never use a montage, triptych, collage, storyboard, split scene, repeated character, or sequence of events in one cover.
9.  **Readable at Card Size**: Let the primary subject/action carry roughly 70-85% of the visual attention while preserving white breathing room on every side. Avoid establishing shots and decorative setting details.
10. **Ground Without Building a Scene**: Use a held prop, contact shadow, or one essential support fragment. “Grounded” never means furnishing a room or adding a full floor plane.
11. **Express the Story's Hook**: Build covers around the approved signature visual beat. Use a clear focal action, readable pose and expression, and one story-specific detail. Do not settle for a generic character standing beside a prop.
12. **Apply the Vignette and Palette Gates First**: Reject a candidate before other QA if it reads as “a room or landscape containing characters” instead of “the character, object, relationship, or action,” or if it reads noticeably hotter, brighter, or more saturated than the Level 1-2 anchors.
13. **Inspect Before Reuse**: An existing file is a candidate, not an approval. Recheck it against the current story, required style anchors, character references, and quality gates before accepting or skipping generation.

## Invocation
The user can invoke this skill by:
*   Asking to "Generate art" or "Create a story image."
*   Referencing this skill explicitly.
*   Using the `/generate-art` workflow.
