# Level 3 R4 white-field and calm-palette art status

**Approved revision:** `Level 3 — Review R4 — Active`
**Production state:** **COMPLETE — 40/40 white-field, calm-palette masters accepted.**
**Calm-palette repair:** 35 offending masters regenerated; 5 already-compliant masters retained byte-identically.
**Targeted Red Bag follow-up:** cover and choice 2 revised so the required red bag uses deep dusty cranberry while the required red bus uses lighter muted terracotta/brick. Choice 2's malformed zippered case was replaced with a conventional open tote with believable rim, handles, containment, and color separation.
**App import:** completed by the coordinator after art handoff. All 40 StorySlider app PNGs SHA-256 match these masters, exactly 35 changed and 5 remained byte-identical, the R4 source hashes remain locked, `xcodebuild test` passed 17/17, and the iPhone 17 simulator build passed.

## Source lock reverified

| Slot | Approved source JSON | SHA-256 |
| ---: | --- | --- |
| 1 | `01_the_rag_in_the_sun.json` | `546bc8457eac514037bfb20e658265afb28833f0490df93219cb50643912e79d` |
| 2 | `02_a_bed_for_the_pig.json` | `803906d796a5ef057933ae2da92a599fa99d75ecc0db0409c0b1b5d36104b898` |
| 3 | `03_the_tub_jet.json` | `3edc8f3d3802ec2f2a8c9e012461db15350465346c7dbed84a509f01f8f0a106` |
| 4 | `04_the_hot_ham.json` | `c5f028a773ca76398a476ed625e5e5aa835c026dbbaf7c199dd0f449c48f2bd0` |
| 5 | `05_the_big_red_hat.json` | `343c030390930d34351f72d0a5d931df41e25085284e81e2fb8435a3ea6c21b5` |
| 6 | `06_hum_and_tap.json` | `fd6f8af333b68edf74808815d8f63be7f853b1c331144ea44e86f4d54b863397` |
| 7 | `07_dad_came_in.json` | `0e84d1ec01fbf5071da66c5983663bf21c1d34d5e32a109637f94a4f04dec146` |
| 8 | `08_ben_and_his_pug.json` | `577c71570ba59bc83b846f620746a9765b4950c420351cc8618efd4254e62c1d` |
| 9 | `09_the_red_bag.json` | `295decf28e053f4c8c22e8263d75101cbda2d5382777c899e8ebe5b1818281b9` |
| 10 | `10_the_pug_and_the_rag.json` | `5b43bdc098ed6cdcbb54dda9cd145d085ab31e5dc1c8a2999d234affa715e5f0` |

The source ledger is `/Users/ricky/workspace/StorySlider/Reference/StoryDrafts/Level 3/Review R4/COLLECTION_LEDGER.json`.

## House-style QA

The contact sheet at `Stories/LEVEL_3_R4_CALM_PALETTE_CONTACT_SHEET.png` places the full final set beside the inspected anchors: `story_pip_the_pig.png`, `story_the_log.png`, `level_1_card.png`, and `level_2_card.png`. Character references were used for identity only. For object-only targets, no person/animal/distinctive-prop anchor was attached; no accepted target contains copied unrelated anchor content.

Every master below is nonempty **600×600 PNG**, was inspected full-size and at card scale, and has this binary verdict: `WHITE_FIELD=PASS; NO_SCENIC_BACKDROP=PASS; TIGHT_FOCAL_CLUSTER=PASS; MINIMAL_CUES=PASS; CARD_SCALE_MATCH=PASS; CALM_PALETTE_MATCH=PASS`.

Across the 35 repaired images, the measured high-saturation warm-pixel share fell **68.5%** and mean nonwhite saturation fell **33.1%**. Literal story reds remain legible as brick, cranberry, terracotta, or dusty rose; yellows use ochre, mustard, straw, or sand; orange is limited to subdued brown-copper and baked earth tones.

## Accepted 40-master inventory

| # | Story | Master path | Literal visual QA / references |
| ---: | --- | --- | --- |
| 1 | The Rag in the Sun | `Stories/The Rag in the Sun/story_the_rag_in_the_sun.png` | Jen puts dry gray rug into beige bag; `Characters/Jen/jen_reference_sheet.png`. |
| 2 | The Rag in the Sun | `Stories/The Rag in the Sun/comp_the_rag_in_the_sun_0.png` | Wet gray rug in hot sun. |
| 3 | The Rag in the Sun | `Stories/The Rag in the Sun/comp_the_rag_in_the_sun_1.png` | Wet gray rug on red bed. |
| 4 | The Rag in the Sun | `Stories/The Rag in the Sun/comp_the_rag_in_the_sun_2.png` | Wet gray rug in big mug. |
| 5 | A Bed for the Pig | `Stories/A Bed for the Pig/story_a_bed_for_the_pig.png` | Jen/pink pig/red bed; Jen and Pip references. |
| 6 | A Bed for the Pig | `Stories/A Bed for the Pig/comp_a_bed_for_the_pig_0.png` | Red bed on mat. |
| 7 | A Bed for the Pig | `Stories/A Bed for the Pig/comp_a_bed_for_the_pig_1.png` | Red bed in pen. |
| 8 | A Bed for the Pig | `Stories/A Bed for the Pig/comp_a_bed_for_the_pig_2.png` | Red bed in tub. |
| 9 | The Tub Jet | `Stories/The Tub Jet/story_the_tub_jet.png` | Ken pretends jet while real red tub remains grounded; `Characters/Ken/ken_reference_sheet.png`. |
| 10 | The Tub Jet | `Stories/The Tub Jet/comp_the_tub_jet_0.png` | Ken on big bed. |
| 11 | The Tub Jet | `Stories/The Tub Jet/comp_the_tub_jet_1.png` | Ken in red bus. |
| 12 | The Tub Jet | `Stories/The Tub Jet/comp_the_tub_jet_2.png` | Ken in red tub. |
| 13 | The Hot Ham | `Stories/The Hot Ham/story_the_hot_ham.png` | Clean-shaven Dad plate/Ben small ham bite; Ben and BenDad refs. |
| 14 | The Hot Ham | `Stories/The Hot Ham/comp_the_hot_ham_0.png` | Ben bites ham. |
| 15 | The Hot Ham | `Stories/The Hot Ham/comp_the_hot_ham_1.png` | Ben bites palm-sized red bread roll. |
| 16 | The Hot Ham | `Stories/The Hot Ham/comp_the_hot_ham_2.png` | Ben bites small halved purple fig. |
| 17 | The Big Red Hat | `Stories/The Big Red Hat/story_the_big_red_hat.png` | Clean-shaven Dad wears enormous red hat; Ben and BenDad refs. |
| 18 | The Big Red Hat | `Stories/The Big Red Hat/comp_the_big_red_hat_0.png` | Dad sits on red bed. |
| 19 | The Big Red Hat | `Stories/The Big Red Hat/comp_the_big_red_hat_1.png` | Dad puts on big red hat. |
| 20 | The Big Red Hat | `Stories/The Big Red Hat/comp_the_big_red_hat_2.png` | Dad puts red cap in bag. |
| 21 | Hum and Tap | `Stories/Hum and Tap/story_hum_and_tap.png` | Sam/Ted hum on log; Ted taps leg; Sam/Ted refs. |
| 22 | Hum and Tap | `Stories/Hum and Tap/comp_hum_and_tap_0.png` | Ted taps big mug. |
| 23 | Hum and Tap | `Stories/Hum and Tap/comp_hum_and_tap_1.png` | Ted taps red rug. |
| 24 | Hum and Tap | `Stories/Hum and Tap/comp_hum_and_tap_2.png` | Ted taps his leg. |
| 25 | Dad Came In | `Stories/Dad Came In/story_dad_came_in.png` | Ned warmly hugs Dad on Dad’s lap; Ned/NedDad refs. |
| 26 | Dad Came In | `Stories/Dad Came In/comp_dad_came_in_0.png` | Ned on Dad’s lap. |
| 27 | Dad Came In | `Stories/Dad Came In/comp_dad_came_in_1.png` | Ned on red bed. |
| 28 | Dad Came In | `Stories/Dad Came In/comp_dad_came_in_2.png` | Ned in big tub. |
| 29 | Ben and His Pug | `Stories/Ben and His Pug/story_ben_and_his_pug.png` | Ben/pug/one ladybug; Ben, BenPug, Bug refs. |
| 30 | Ben and His Pug | `Stories/Ben and His Pug/comp_ben_and_his_pug_0.png` | One bug moves to Ben. |
| 31 | Ben and His Pug | `Stories/Ben and His Pug/comp_ben_and_his_pug_1.png` | One bug on pug. |
| 32 | Ben and His Pug | `Stories/Ben and His Pug/comp_ben_and_his_pug_2.png` | One bug on distinct rug. |
| 33 | The Red Bag | `Stories/The Red Bag/story_the_red_bag.png` | Jen/Mom reveal big red bus; Jen/JenMom refs. |
| 34 | The Red Bag | `Stories/The Red Bag/comp_the_red_bag_0.png` | Red mug in bag. |
| 35 | The Red Bag | `Stories/The Red Bag/comp_the_red_bag_1.png` | Wet rag in bag. |
| 36 | The Red Bag | `Stories/The Red Bag/comp_the_red_bag_2.png` | Big red bus in bag. |
| 37 | The Pug and the Rag | `Stories/The Pug and the Rag/story_the_pug_and_the_rag.png` | Ben and one fawn pug tug red rag; Ben/BenPug refs. |
| 38 | The Pug and the Rag | `Stories/The Pug and the Rag/comp_the_pug_and_the_rag_0.png` | One pug holds red cap. |
| 39 | The Pug and the Rag | `Stories/The Pug and the Rag/comp_the_pug_and_the_rag_1.png` | One pug holds one bread bun. |
| 40 | The Pug and the Rag | `Stories/The Pug and the Rag/comp_the_pug_and_the_rag_2.png` | One pug holds one red rag. |

## Preservation and corrections

- Calm-palette superseded masters: `Rejected/level_3_r4_pre_calm_palette_2026-08-11/` (35 files, story-relative paths preserved).
- Targeted Red Bag superseded masters: `Rejected/level_3_r4_targeted_red_bag_repair_2026-08-11/The Red Bag/` (cover and choice 2).
- Prior masters: `Rejected/level_3_r3_superseded_2026-08-10/` and `Rejected/level_3_r4_pre_whitefield_vignette_2026-08-10/`.
- White-field revisions, including the Ben-and-His-Pug multi-bug/cap-log failures and the Pug-and-Rag duplicated-pug failures: `Rejected/level_3_r4_whitefield_revisions_2026-08-10/` plus story-local rejection folders where created in earlier R4 corrections. The two Ben-and-His-Pug failures are retained as `Ben and His Pug/comp_ben_and_his_pug_0_rejected_multiple_bugs_cap_log.png` and `Ben and His Pug/comp_ben_and_his_pug_2_rejected_no_distinct_rug_cap_log.png`.
- The final Pug-and-Rag replacements are the coordinator-approved `exec-1b762f6c-dd90-4397-b05e-9b8c40970200.png` (bun) and `exec-12a546de-1624-4658-bb2e-acfa02f8903f.png` (rag); the superseded `exec-e342856d…` and `exec-0990247f…` candidates are archived, never masters.

**Unresolved issues:** none.
**Completion:** all source hashes, filenames, dimensions, nonempty files, individual semantics, choice parity, cross-set character continuity, calm-palette compliance, 40/40 art/app SHA-256 parity, 35/5 changed/preserved split, 17/17 tests, and iPhone 17 simulator build verified after final installation.
