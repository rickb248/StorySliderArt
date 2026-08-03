---
name: story-art
description: Generate and review calm, K-2 appropriate modern storybook anime illustrations for StorySlider, including story covers and comprehension-choice images with character continuity, card-scale readability, single-scene composition, and physically grounded props.
---

# Story Art Generation Skill

Use this skill whenever you need to generate or describe art for the Story Slider project.

## Instructions
1.  **Read the Style Guidelines**: Refer to `.agent/workflows/generate-art.md` for the core art style definition.
2.  **Maintain Calmness**: All visuals must be calm, clear, and easy for children in grades K-2 to process.
3.  **No Faces on Objects**: Stick to realism for inanimate objects (buses, trees, etc.).
4.  **Consistency**: Check the `Characters/` directory for character references before generating new images of Sam or other characters.
5.  **One Moment Per Cover**: A story cover must depict one unified scene and one clear moment. Never use a montage, triptych, collage, storyboard, split scene, repeated character, or sequence of events in one cover.
6.  **Readable at Card Size**: Keep the main character/action cluster large enough to read in the app's small story cards. Avoid wide or panoramic scenes that shrink characters; normally let the primary subjects occupy roughly 65–80% of the square while preserving the required white margin.
7.  **Ground Every Prop**: Objects must visibly obey gravity. Support them with a hand, table, floor, container, or another story-appropriate surface; reject floating or ambiguously suspended pans, bags, food, tools, and other props.

## Invocation
The user can invoke this skill by:
*   Asking to "Generate art" or "Create a story image."
*   Referencing this skill explicitly.
*   Using the `/generate-art` workflow.
