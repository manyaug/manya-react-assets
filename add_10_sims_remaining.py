import json
import os

base_path = r"d:\manya_garage\MANYA-ASSETS\manya-react-assets\content\english\holidays"

# Add to quest_05 and quest_06
quests_config = {
    "quest_05_detail_order": {
        "num": "05",
        "concept": "Order of Adjectives",
        "engines": ["MORPH_GAME", "GARDEN_GUARD", "SENTENCE_BLOCKS", "WORDGRID_ENGINE"]
    },
    "quest_06_village_arrival": {
        "num": "06",
        "concept": "Participles",
        "engines": ["MORPH_GAME", "GARDEN_GUARD", "SENTENCE_BLOCKS", "WORDGRID_ENGINE"]
    }
}

characters = ["Manya", "Polly", "Kiki"]

for quest_folder, config in quests_config.items():
    quest_path = os.path.join(base_path, quest_folder)
    quest_num = config["num"]
    
    # Find existing SIM files
    existing_sims = []
    if os.path.exists(quest_path):
        for file in os.listdir(quest_path):
            if file.startswith(f"SIM-ENG7-T1-{quest_num}-"):
                num = int(file.split("-")[-1].replace(".json", ""))
                existing_sims.append(num)
    
    if existing_sims:
        max_num = max(existing_sims)
    else:
        max_num = 0
    
    # Create 10 more SIM files
    for i in range(1, 11):
        new_num = max_num + i
        char_idx = (new_num - 1) % 3
        engine = config["engines"][(new_num - 1) % len(config["engines"])]
        
        sim_file = {
            "qid": f"SIM-ENG7-T1-{quest_num}-{new_num:04d}",
            "engine_type": engine,
            "subtopic": quest_folder,
            "data": {
                "character": characters[char_idx],
                "title": f"{config['concept']} Challenge #{new_num}"
            }
        }
        
        # Add engine-specific data
        if engine == "MORPH_GAME":
            sim_file["data"]["queries"] = [
                {"before": "example before", "after": "example after", "changeType": config["concept"]}
            ]
        elif engine == "GARDEN_GUARD":
            sim_file["data"]["winScore"] = 250
            sim_file["data"]["queries"] = [
                {"text": "example text", "error": "wrong", "correct": "right"}
            ]
        elif engine == "SENTENCE_BLOCKS":
            sim_file["data"]["slots"] = [
                {"id": "s1", "expected": "word1"},
                {"id": "s2", "expected": "word2"}
            ]
            sim_file["data"]["distractors"] = ["distractor1", "distractor2"]
        elif engine == "WORDGRID_ENGINE":
            sim_file["data"]["size"] = 8
            sim_file["data"]["words"] = ["WORD1", "WORD2", "WORD3"]
        
        # Write file
        file_path = os.path.join(quest_path, f"SIM-ENG7-T1-{quest_num}-{new_num:04d}.json")
        with open(file_path, 'w') as f:
            json.dump(sim_file, f, indent=4)
    
    print(f"✓ quest_{quest_num}: Added 10 SIM files (now {max_num + 10} total)")

print("\n✅ All 10 additional SIM files added to quest_05 and quest_06!")
