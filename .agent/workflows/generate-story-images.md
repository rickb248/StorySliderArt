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

### Step 4: Generate or Repair the Cover
Create a prompt following the `/generate-art` workflow:
```markdown
Story beat: [Child hook and signature visual beat].
Subject: [Main character(s)] [performing the single strongest written action]. [Character description from CHARACTER.md]. Show [specific expression, gaze, pose, or anticipation].
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, story-appropriate emotional energy, clean vibrant colors, clear thin black outlines, simple cel-shading.
Format: 600px × 600px, 1:1 square, solid white background #FFFFFF, intentional full or close framing.
Composition: one unified scene and one story moment only. Keep the main character/action cluster large and readable at app-card size—normally about 65–80% of the square—without cropping or losing the white margin.
Negative: montage, triptych, collage, storyboard, split scene, repeated character, multiple moments, wide establishing shot, panoramic view, tiny subject, generic standing pose, floating object, cropped essential action, cut off, realistic photo, 3d render, frightening, neon, messy lines.
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
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, clear emotional tone, clean vibrant colors, clear thin black outlines, simple cel-shading.
Format: 600px × 600px, 1:1 square, solid white background #FFFFFF, intentional full or close framing.
Composition: keep the answer subject large and immediately recognizable at app-card size. Show one moment in a close, uncluttered composition.
Physical grounding: every prop must be visibly held or resting on a plausible support such as a table, floor, or container. Reject floating or ambiguously airborne objects.
Negative: montage, split scene, wide establishing shot, panoramic view, tiny subject, correctness cue, check mark, glow, badge, floating object, unsupported prop, cropped essential action, cut off, realistic photo, 3d render, frightening, neon.

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
negative constraints, character references, iteration, accepted filename, and final quality
verdict for all four images. Prompt history is required for approved production.

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
