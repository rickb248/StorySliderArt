---
description: Workflow for generating story images (cover + comprehension answers)
---

# Generate Story Images Workflow

Use this workflow to generate all images needed for a story in the Story Slider app.

## Prerequisites
1. The story must exist in `/Users/ricky/workspace/StorySlider/StorySlider/Content/Level X/[Story Name]/`
2. Read the story's JSON file to understand the content and comprehension question

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

### Step 2: Check for Existing Images (SKIP LOGIC)
Before generating, check if images already exist:
```bash
# Check cover
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/story_[snake_case_title].imageset/*.png

# Check comprehension images
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_0.imageset/*.png
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_1.imageset/*.png
ls /Users/ricky/workspace/StorySlider/StorySlider/Assets.xcassets/comp_[snake_case_title]_2.imageset/*.png
```
**If an image exists, SKIP generation for that image.**

### Step 3: Identify Characters
Check which characters from `StorySliderArt/Characters/` appear in the story.
For each character, read their `CHARACTER.md` to get their visual description.

**Animal characters (Pip, Rat, Cat, etc.):** Must be natural animals - no clothes, walking on four legs.

### Step 4: Generate Cover Image (if not exists)
Create a prompt following the `/generate-art` workflow:
```markdown
Subject: [Main character(s)] [doing action from story]. [Character description from CHARACTER.md].
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear thin black outlines, simple cel-shading.
Format: 600px × 600px, 11:10 aspect ratio, solid white background #FFFFFF, centered full view.
Negative: cropped, cut off, realistic photo, 3d render, scary, dark, neon, messy lines.
```

### Step 5: Generate Comprehension Answer Images (from JSON)
Read the `answers` array from the story JSON. Generate one image per answer.

**Example** for `"answers": ["Sam", "Dan", "Pam"]` with `"correctAnswerIndex": 2`:
| Index | Answer | Image File | Notes |
|-------|--------|------------|-------|
| 0 | Sam | `comp_the_rat_0.png` | Incorrect |
| 1 | Dan | `comp_the_rat_1.png` | Incorrect |
| 2 | Pam | `comp_the_rat_2.png` | **Correct** |

**Prompt for each answer image:**
```markdown
Subject: [Answer] standing/posed clearly. [Description from CHARACTER.md if character exists].
Style: digital vector illustration, modern storybook anime style, high quality, K-2 audience, calm atmosphere, clean vibrant colors, clear thin black outlines, simple cel-shading.
Format: 600px × 600px, 11:10 aspect ratio, solid white background #FFFFFF, centered full view.
Negative: cropped, cut off, realistic photo, 3d render, scary, dark, neon.

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

### Step 8: Document Prompts (Optional)
Add successful prompts to `StorySliderArt/Stories/[Story Name]/PROMPTS.md` for future reference.

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

