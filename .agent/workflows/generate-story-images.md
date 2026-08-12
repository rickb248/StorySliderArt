---
description: Workflow for generating story images (cover + comprehension answers)
---

# Generate Story Images Workflow

Use this workflow to generate all images needed for a story in the Story Slider app.

## Prerequisites
1. The story must exist in `/Users/ricky/workspace/StorySlider/StorySlider/Content/Level X/[Story Name]/`
2. Read the story's JSON file to understand the content and comprehension question
3. Read `.agent/workflows/story-illustration-quality-gates.md`
4. For approved production, read the story's child hook, delight engine, tone class, and signature visual beat from its review records

## Image Requirements Per Story
Each story needs **4 images**:
1. **Cover Image** (`story_[snake_case_title].png`) - Represents the story theme
2. **Correct Answer** (`comp_[snake_case_title]_[correctIndex].png`) - Illustrates the correct answer
3. **Distraction 1** (`comp_[snake_case_title]_[index].png`) - Illustrates an incorrect answer
4. **Distraction 2** (`comp_[snake_case_title]_[index].png`) - Illustrates another incorrect answer

## Step-by-Step Process

### Step 1: Read the Story JSON
Read the story JSON file (e.g., `the_rat.json`) to extract:
```json
{
    "title": "The Rat",
    "sentences": ["A rat.", "A rat ran.", ...],
    "comprehensionQuestion": {
        "question": "Who did the rat run to?",
        "answers": ["Sam", "Dan", "Pam"],
        "correctAnswerIndex": 2
    }
}
```

### Step 2: Inspect Existing Images
Before generating, locate any existing candidates:
```bash
# Check cover
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_[snake_case_title].imageset/*.png

# Check comprehension images
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_0.imageset/*.png
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_1.imageset/*.png
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_2.imageset/*.png
```
Open every candidate and compare it with the current story, character references, and quality
gates. Record `ACCEPT`, `REVISE`, or `REPLACE`. Skip generation only for an inspected
`ACCEPT`; a filename or file count alone is not evidence of quality.

### Step 3: Identify Characters
Check which characters from `StorySliderArt/Characters/` appear in the story.
For each character, read their `CHARACTER.md` to get their visual description.

**Animal characters (Pip, Rat, Cat, etc.):** Must be natural animals - no clothes, walking on four legs.

### Step 3.5: Calibrate the House Style
Open at least four anchors listed in `.agent/workflows/generate-art.md`: two approved Level 1-2
covers and two level cards. Use them to calibrate the white-field vignette composition, simplicity,
palette, contrast, outline weight, young proportions, and whitespace. Character reference images
control identity only; the approved anchors control composition and rendering. Do not use a
full-scene image as a composition anchor. When possible, attach the most relevant style anchor to
the generation request separately from character references. Never attach an anchor containing an
unrelated person, animal, or distinctive prop; use a neutral level-card/object anchor for
object-only answers so ImageGen cannot copy a benchmark subject into the story image.

Palette matching is blocking. Default to warm neutrals, muted blues/greens, dusty secondary
colors, gentle earth tones, restrained accents, and low-contrast relationships. If prose names
red, yellow, or orange, keep the object recognizable using a muted storybook version: brick,
cranberry, terracotta, mustard, ochre, butter, straw, clay, burnt orange, or muted apricot. Reject
large areas or repeated accents of bright red/yellow/orange and any candidate that reads hotter,
brighter, or more saturated than the Level 1-2 anchors at full size or card size.

### Step 4: Generate or Repair the Cover
Create a prompt following the `/generate-art` workflow:
```markdown
House style: StorySlider white-field vignette. Pure white extends uninterrupted to all four edges. Show one tight subject/action cluster, not a scenic illustration.
Story beat: [Child hook and signature visual beat].
Subject: [Main character(s)] [performing the single strongest written action]. [Character description from CHARACTER.md]. Show [specific expression, gaze, pose, or anticipation].
Palette: calming Level 1-2 palette with warm neutrals, muted blues/greens, dusty secondary colors, gentle earth tones, restrained accents, and low-contrast relationships. Preserve any named red/yellow/orange with a recognizable muted storybook variant; mute large colored objects and balance them with neutrals.
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, story-appropriate emotional energy, calm muted storybook palette, gentle low-contrast cel-shading, clean medium-to-thin dark-charcoal outlines, rounded young child proportions, large expressive eyes.
Format: 600px × 600px, 1:1 square, pure white background #FFFFFF connected to every edge, complete subject in frame, white breathing room on every side.
Composition: one cohesive vignette and one story moment. Use zero to two essential support cues, such as a contact shadow, small rug/grass/dirt patch, one log, or a tabletop fragment. The subject/action carries 70-85% of the visual attention. Ground through contact and overlap; do not construct an environment.
Negative: room interior, wall, window, corner, broad floor plane, bedroom, kitchen, dining room, cabinets, shelves, bed-and-furniture arrangement, horizon, landscape, scenic backdrop, background rectangle, colored panel, circle or blob backdrop, decorative frame, excessive props, montage, triptych, collage, storyboard, split scene, repeated character, multiple moments, wide establishing shot, panoramic view, tiny subject, generic standing pose, floating object, cropped essential action, cut off, heavy pitch-black outlines, harsh contrast, fire-engine red, lemon yellow, vivid orange, traffic-cone orange, candy-color saturation, multiple competing saturated warm colors, fully saturated primary color blocks, glossy rendering, tall or teen-like child proportions, realistic photo, 3d render, frightening, neon, messy lines.
```

Reject any cover that summarizes the story with multiple panels or multiple copies of a
character. Choose the single strongest action that represents the story instead. A picture
may amplify a written moment but must not add an essential plot fact absent from the prose.

### Step 5: Generate Comprehension Answer Images (from JSON)
Read the `answers` array from the story JSON. Generate one image per answer.

**Example** for `"answers": ["Sam", "Dan", "Pam"]` with `"correctAnswerIndex": 2`:
| Index | Answer | Image File | Notes |
|-------|--------|------------|-------|
| 0 | Sam | `comp_the_rat_0.png` | Incorrect |
| 1 | Dan | `comp_the_rat_1.png` | Incorrect |
| 2 | Pam | `comp_the_rat_2.png` | **Correct** |

Illustrate the literal answer choice in the context required by the question. Do not default
to a character standing alone when the answer is an action, outcome, location, or object.

**Prompt for each answer image:**
```markdown
Subject: [Literal answer choice as the question asks it], shown clearly in one action or state. [Description from CHARACTER.md if character exists].
Palette: calming Level 1-2 palette with warm neutrals, muted blues/greens, dusty secondary colors, gentle earth tones, restrained accents, and low-contrast relationships. Preserve any named red/yellow/orange with a recognizable muted storybook variant; mute large colored objects and balance them with neutrals.
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, clear emotional tone, calm muted storybook palette, gentle low-contrast cel-shading, clean medium-to-thin dark-charcoal outlines, rounded young child proportions.
Format: 600px × 600px, 1:1 square, pure white background #FFFFFF connected to every edge, complete subject in frame, white breathing room on every side.
Composition: one tight white-field vignette. Keep the literal answer large and immediately recognizable. Include only the characters, props, and zero to two support cues needed to make the answer clear.
Physical grounding: every prop must be held, contained, overlapped, shadowed, or resting on one small support fragment. Never add a room or broad floor plane merely for grounding.
Negative: room interior, wall, window, corner, broad floor plane, bedroom, kitchen, dining room, cabinets, shelves, horizon, landscape, scenic backdrop, background rectangle, colored panel, circle or blob backdrop, decorative frame, excessive props, montage, split scene, wide establishing shot, panoramic view, tiny subject, correctness cue, check mark, glow, badge, floating object, unsupported prop, cropped essential action, cut off, heavy pitch-black outlines, harsh contrast, fire-engine red, lemon yellow, vivid orange, traffic-cone orange, candy-color saturation, multiple competing saturated warm colors, fully saturated primary color blocks, glossy rendering, tall or teen-like child proportions, realistic photo, 3d render, frightening, neon.

```

### Step 6: Save Images to Assets
Copy generated images to the Story Slider app:
```bash
# Create imageset directories if needed
mkdir -p /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_[snake_case_title].imageset
mkdir -p /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_0.imageset
mkdir -p /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_1.imageset
mkdir -p /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_2.imageset

# Copy images
cp [generated_cover].png .../story_[snake_case_title].imageset/story_[snake_case_title].png
cp [generated_comp_0].png .../comp_[snake_case_title]_0.imageset/comp_[snake_case_title]_0.png
# ... repeat for indices 1 and 2
```

### Step 7: Create/Update Contents.json
Each `.imageset` folder needs a `Contents.json`:
```json
{
    "images": [
        { "filename": "[image_name].png", "idiom": "universal", "scale": "1x" },
        { "idiom": "universal", "scale": "2x" },
        { "idiom": "universal", "scale": "3x" }
    ],
    "info": { "author": "xcode", "version": 1 }
}
```

### Step 8: Document Prompts and QA
Create or update `StorySliderArt/Stories/[Story Name]/PROMPTS.md`. Record the exact prompt,
negative constraints, style anchors, character references, iteration, accepted filename, and
the six binary vignette/palette verdicts (`WHITE_FIELD`, `NO_SCENIC_BACKDROP`,
`TIGHT_FOCAL_CLUSTER`, `MINIMAL_CUES`, `CARD_SCALE_MATCH`, `CALM_PALETTE_MATCH`) for all four
images. Prompt history is required for approved production.

---

## Quick Reference: Snake Case Conversion
| Title | Snake Case |
|-------|------------|
| The Dig | `the_dig` |
| Sam and the Cat | `sam_and_the_cat` |
| My Dad | `my_dad` |

## Character Quick Reference
| Character | Type | Key Visual Traits |
|-----------|------|------------------|
| Sam | Boy | Brown messy hair, blue sweatshirt, brown pants |
| Kit | Girl | Brown bob, blue overalls, striped shirt |
| Pip | Pig | Pink, natural animal on four legs, expressive eyes |
| Rat | Rat | Grey/white fur, natural animal |
| Cat | Cat | [Check CHARACTER.md] |
| Dad | Adult | [Check CHARACTER.md] |
| Dan | Boy | [Check CHARACTER.md] |
| Man | Adult | [Check CHARACTER.md] |
