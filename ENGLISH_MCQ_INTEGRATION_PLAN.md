# English MCQ Integration Plan

## Overview
Integrate 436 raw MCQ questions + 1,009 rephrased variations from `eng-p7-question-bank.xlsx` into the quest structure.

---

## Current Asset Structure (UPDATED ✓)

### 1. **Asset Folders** (assets/english/chap-1-holidays/)
```
quest_1_holiday_kickoff/           → images for vocabulary quest
quest_2_going_to_mastery/          → (empty - to be populated)
quest_3_question_tags_mastery/     → (empty - to be populated)
quest_4_reported_speech_mastery/   → (empty - to be populated)
quest_5_detail_order/              → (empty - to be populated)
quest_6_village_arrival/           → (empty - to be populated)
quest_7_past_regrets/              → (empty - to be populated)
quest_8_voice_mastery/             → (empty - to be populated)
quest_9_village_life/              → (empty - to be populated)
quest_10_comprehension/            → (empty - to be populated)
```

### 2. **Content Files** (content/english/holidays/)
Each quest folder contains:
- `0X_[quest_name].json` - Main study/story file with CHAT + GAME engines
- `recap_[quest_name].json` - Summary with rules
- `SIM-ENG7-T1-0X-XXXX.json` - Individual practice MCQ files (15-16 per quest)

---

## Excel Structure Mapping

### Raw Sheet (436 base questions)
```
q_id: PQ-ENG7-T1-00001
sub-topic: quest_01_holiday_kickoff
question_text: When does the school term ________ for the holidays?
option_a/b/c/d: [4 options]
correct_answer: Option_B
detailed_solution: Explanation text
hint: Student hint
tags: JSON array ["P7","English","Vocabulary","Phrasal Verbs"]
```

### Rephrased Sheet (1,009 variations)
- 3 variations per base question
- Same structure, different wording
- Formula-based q_id with version suffix (-V1, -V2, -V3)

---

## Proposed Integration Strategy

### **Option A: Hybrid Approach (RECOMMENDED)**

#### Phase 1: Create MCQ JSON Files
For each quest, create game-based MCQ files from Excel:

```json
{
  "qid": "ENG7-T1-01-MCQ-0001",
  "engine_type": "MCQ_MASTER",
  "subtopic": "quest_01_holiday_kickoff",
  "data": {
    "question": "When does the school term ________ for the holidays?",
    "options": [
      {"label": "A", "text": "break out"},
      {"label": "B", "text": "break off"},
      {"label": "C", "text": "break in"},
      {"label": "D", "text": "break up"}
    ],
    "correct": "B",
    "solution": "The correct phrasal verb for schools closing for holidays is 'break off'.",
    "hint": "Think of a two-word phrase that means to separate or stop for a while.",
    "tags": ["Phrasal Verbs", "Vocabulary", "Easy"],
    "difficulty": "E"
  }
}
```

#### Phase 2: Game Integration Points
Each quest can include multiple game engines:

1. **WORDGRID_ENGINE** (Existing)
   - Extract key vocabulary from MCQ question text
   - Create word search games

2. **MCQ_MASTER** (New)
   - Direct MCQ questions from Excel
   - ~15-20 questions per quest based on difficulty

3. **HARVEST_GAME** (Existing)
   - Sort correct vs incorrect sentence constructions
   - Use solution examples from Excel

4. **DRAG_DROP_ENGINE** (Potential)
   - Match grammatical concepts to examples
   - Reorder words/phrases based on grammar rules

---

## Distribution Plan by Quest

| Quest | Concept | Excel Questions | Game Type | Assets Needed |
|-------|---------|-----------------|-----------|---------------|
| quest_01 | Vocabulary | ~40-50 | WordGrid + MCQ | Images already there |
| quest_02 | Be Going To | ~35-45 | Story + MCQ | Character dialogue images |
| quest_03 | Question Tags | ~30-40 | Dialogue + MCQ | Chat character images |
| quest_04 | Reported Speech | ~35-45 | Conversation + MCQ | Chat images |
| quest_05 | Adjectives Order | ~25-35 | Grammar + MCQ | Diagram/chart images |
| quest_06 | Participles | ~30-40 | Analysis + MCQ | Sentence structure images |
| quest_07 | Conditionals | ~28-38 | Logic Puzzle + MCQ | Scenario images |
| quest_08 | Passive Voice | ~35-45 | Active/Passive + MCQ | Transformation images |
| quest_09 | Adverbs | ~32-42 | Drag/Drop + MCQ | Placement guide images |
| quest_10 | Comprehension | ~25-35 | Reading + MCQ | Passage text |

**Total: ~300-410 questions to integrate** (from Raw sheet)

---

## JSON File Naming Convention

```
SIM-ENG7-T1-0[quest]-[0001-0050].json    → Individual MCQ files
GAME-ENG7-T1-0[quest]-[01-05].json       → Game/engine files
RECAP-ENG7-T1-0[quest].json              → Summary files
```

---

## Proposed Folder Structure (assets)

```
assets/english/chap-1-holidays/
├── quest_1_holiday_kickoff/
│   ├── holiday_chat_1.webp
│   ├── holiday_chat_2.webp
│   ├── holiday_chat_3.webp
│   └── [more images]
├── quest_2_going_to_mastery/
│   ├── future_chat_1.webp
│   ├── future_chat_2.webp
│   └── [scenario images]
├── quest_3_question_tags_mastery/
│   ├── question_tags_1.webp
│   └── [dialogue images]
└── [7 more quest folders with images]
```

---

## Implementation Checklist

### ✓ Done
- [x] Fixed curriculum-master.json folder names
- [x] Created 10 quest folders in assets/english/chap-1-holidays/
- [x] Copied existing images to quest_1_holiday_kickoff

### To Do
- [ ] Create Python script to extract Excel data → MCQ JSON files
- [ ] Generate MCQ files for all 10 quests
- [ ] Create game/engine wrapper files for each quest
- [ ] Add character images/animations for each quest
- [ ] Update content files to reference MCQ JSON files
- [ ] Test MCQ engine integration
- [ ] Create difficulty distribution report
- [ ] Validate all question IDs and linking

---

## Recommended Tools & Scripts

### Python Script: Excel → JSON Converter
```python
# pseudocode
def convert_excel_to_json():
    # Read Excel
    # Group by sub-topic
    # For each question:
    #   - Create MCQ_MASTER JSON
    #   - Store with proper naming
    #   - Link to quest folder
```

### Benefits
1. **Fast Processing**: Convert 1,000+ questions automatically
2. **Consistent Format**: Ensures all JSONs follow same structure
3. **Easy Updates**: Re-run script if Excel changes
4. **Quality Control**: Validate all fields before saving

---

## Next Steps

1. **Confirm game engine types** you want to use (MCQ_MASTER, WORDGRID, HARVEST, etc.)
2. **Create sample MCQ JSON** for quest_02 as proof of concept
3. **Generate script** to batch convert Excel → JSON
4. **Gather/create images** for each quest (characters, scenarios, diagrams)
5. **Update main quest JSON files** (01_holiday_kickoff.json, etc.) to include MCQ game steps

---

## Questions to Clarify

1. Should we use **Raw sheet** (436 questions) or **Rephrased sheet** (1,009 questions) or **both**?
2. How many questions per quest? Should we distribute evenly or by difficulty?
3. Do you have character illustrations for each quest's narrative?
4. Should MCQs appear as:
   - Separate practice files (like current SIM-ENG7-T1-XX-XXXX.json)?
   - Or integrated into main quest flow in 0X_quest_name.json?

---

## Summary of Changes

✅ **Asset Structure**: 10 quest folders created  
✅ **Curriculum**: Fixed folder names & titles  
✅ **Excel Mapping**: Ready to extract questions by sub-topic  
🔄 **Next**: Create conversion script & sample JSON files
