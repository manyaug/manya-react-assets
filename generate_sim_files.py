import json
import os

base_path = r"d:\manya_garage\MANYA-ASSETS\manya-react-assets\content\english\holidays"

# Define quest data
quests_data = {
    "quest_05_detail_order": {
        "num": "05",
        "concept": "Order of Adjectives",
        "recap": "recap_adjective_order"
    },
    "quest_06_village_arrival": {
        "num": "06",
        "concept": "Participles",
        "recap": "recap_participles"
    },
    "quest_09_village_life": {
        "num": "09",
        "concept": "Adverbs",
        "recap": "recap_adverbs"
    },
    "quest_10_comprehension": {
        "num": "10",
        "concept": "Reading Comprehension",
        "recap": "recap_reading"
    }
}

# SIM file templates for each quest
sim_templates = {
    "quest_05_detail_order": [
        {"engine": "MORPH_GAME", "title": "Opinion before Size", "example": ("small nice blue flowers", "nice small blue flowers")},
        {"engine": "GARDEN_GUARD", "title": "Adjective Fix", "errors": [("beautiful small", "small beautiful"), ("green lovely", "lovely green")]},
        {"engine": "SENTENCE_BLOCKS", "title": "Order Blocks", "blocks": ["elegant", "old", "wooden", "chairs"]},
        {"engine": "MORPH_GAME", "title": "Color Order", "example": ("blue small car", "small blue car")},
        {"engine": "GARDEN_GUARD", "title": "Material Order", "errors": [("plastic round", "round plastic"), ("metal big", "big metal")]},
        {"engine": "WORDGRID_ENGINE", "title": "Adjective Hunt", "words": ["BEAUTIFUL", "SMALL", "RED", "WOODEN"]},
        {"engine": "MORPH_GAME", "title": "Size and Age", "example": ("ancient big temple", "big ancient temple")},
        {"engine": "SENTENCE_BLOCKS", "title": "Build Sentence", "blocks": ["lovely", "round", "silver", "ball"]},
        {"engine": "GARDEN_GUARD", "title": "Fix Opinion", "errors": [("expensive lovely", "lovely expensive"), ("ugly big", "big ugly")]},
        {"engine": "MORPH_GAME", "title": "Mixed Adjectives", "example": ("bright wonderful yellow light", "wonderful bright yellow light")},
        {"engine": "WORDGRID_ENGINE", "title": "Size Words", "words": ["HUGE", "TINY", "ENORMOUS", "LITTLE"]},
        {"engine": "SENTENCE_BLOCKS", "title": "Decorate Hall", "blocks": ["magnificent", "tall", "golden", "decorations"]},
    ],
    "quest_06_village_arrival": [
        {"engine": "MORPH_GAME", "title": "Present Participle", "example": ("broken arm", "breaking arm")},
        {"engine": "GARDEN_GUARD", "title": "Participle Use", "errors": [("boring movie", "bore movie"), ("excited girl", "excite girl")]},
        {"engine": "SENTENCE_BLOCKS", "title": "Participle Order", "blocks": ["running", "dog", "wagging", "tail"]},
        {"engine": "MORPH_GAME", "title": "Past Participle", "example": ("paint house", "painted house")},
        {"engine": "GARDEN_GUARD", "title": "Action Form", "errors": [("laugh children", "laughing children"), ("dance girls", "dancing girls")]},
        {"engine": "WORDGRID_ENGINE", "title": "Participle Hunt", "words": ["RUNNING", "PAINTED", "BROKEN", "FLYING"]},
        {"engine": "MORPH_GAME", "title": "Describing Action", "example": ("bored students", "boring students")},
        {"engine": "SENTENCE_BLOCKS", "title": "Farm Scene", "blocks": ["working", "farmers", "harvesting", "crops"]},
        {"engine": "GARDEN_GUARD", "title": "Verb to Participle", "errors": [("confuse rules", "confusing rules"), ("amaze facts", "amazing facts")]},
        {"engine": "MORPH_GAME", "title": "Perfect Participles", "example": ("arrive early, he rested", "having arrived early, he rested")},
        {"engine": "WORDGRID_ENGINE", "title": "Action Words", "words": ["HELPING", "WORKING", "ARRIVING", "LEAVING"]},
        {"engine": "SENTENCE_BLOCKS", "title": "Village Activity", "blocks": ["children", "playing", "happily", "laughing"]},
    ],
    "quest_09_village_life": [
        {"engine": "MORPH_GAME", "title": "Adverb Formation", "example": ("quick runner", "quick runs quickly")},
        {"engine": "GARDEN_GUARD", "title": "Adverb Placement", "errors": [("quickly she ran", "she ran quickly"), ("carefully he worked", "he worked carefully")]},
        {"engine": "SENTENCE_BLOCKS", "title": "Manner Adverbs", "blocks": ["spoke", "softly", "and", "kindly"]},
        {"engine": "MORPH_GAME", "title": "Frequency Adverbs", "example": ("always she comes", "she always comes")},
        {"engine": "GARDEN_GUARD", "title": "Adverb Errors", "errors": [("bad he did", "he did badly"), ("good she sings", "she sings well")]},
        {"engine": "WORDGRID_ENGINE", "title": "Adverb Hunt", "words": ["QUICKLY", "SLOWLY", "HAPPILY", "CAREFULLY"]},
        {"engine": "MORPH_GAME", "title": "Time Adverbs", "example": ("comes tomorrow she", "she comes tomorrow")},
        {"engine": "SENTENCE_BLOCKS", "title": "Manner Description", "blocks": ["danced", "gracefully", "and", "elegantly"]},
        {"engine": "GARDEN_GUARD", "title": "Fix Position", "errors": [("loudly he sang", "he sang loudly"), ("gently they worked", "they worked gently")]},
        {"engine": "MORPH_GAME", "title": "Degree Adverbs", "example": ("very careful", "very carefully")},
        {"engine": "WORDGRID_ENGINE", "title": "Frequency Words", "words": ["ALWAYS", "NEVER", "OFTEN", "RARELY"]},
        {"engine": "SENTENCE_BLOCKS", "title": "Daily Life", "blocks": ["works", "diligently", "every", "day"]},
    ],
    "quest_10_comprehension": [
        {"engine": "DEEP_READER", "title": "Market Story", "passage": "The village market was busy..."},
        {"engine": "DEEP_READER", "title": "Festival Day", "passage": "The annual festival brings joy..."},
        {"engine": "DEEP_READER", "title": "Farm Life", "passage": "Life on the farm starts early..."},
        {"engine": "DEEP_READER", "title": "School Holidays", "passage": "When school breaks for holidays..."},
        {"engine": "DEEP_READER", "title": "Weather Change", "passage": "The rainy season has arrived..."},
        {"engine": "DEEP_READER", "title": "Family Gathering", "passage": "All cousins came to visit..."},
        {"engine": "DEEP_READER", "title": "Journey Home", "passage": "The journey back to the village..."},
        {"engine": "DEEP_READER", "title": "Night Stories", "passage": "Grandma told stories every night..."},
        {"engine": "DEEP_READER", "title": "Morning Routine", "passage": "Every morning starts with chores..."},
        {"engine": "DEEP_READER", "title": "Evening Meals", "passage": "Dinner brings everyone together..."},
        {"engine": "DEEP_READER", "title": "Harvest Time", "passage": "It's time to gather the crops..."},
        {"engine": "DEEP_READER", "title": "Friends Meeting", "passage": "We met our friends at the well..."},
    ]
}

# Create SIM files
for quest_folder, quest_info in quests_data.items():
    quest_path = os.path.join(base_path, quest_folder)
    quest_num = quest_info["num"]
    templates = sim_templates.get(quest_folder, [])
    
    characters = ["Manya", "Polly", "Kiki"]
    char_idx = 0
    
    for i, template in enumerate(templates, 1):
        sim_file = {
            "qid": f"SIM-ENG7-T1-{quest_num}-{i:04d}",
            "engine_type": template["engine"],
            "subtopic": quest_folder,
            "data": {
                "character": characters[char_idx % 3],
                "title": template["title"]
            }
        }
        
        # Add engine-specific data
        if template["engine"] == "MORPH_GAME" and "example" in template:
            sim_file["data"]["queries"] = [{"before": template["example"][0], "after": template["example"][1], "changeType": quest_info["concept"]}]
        elif template["engine"] == "GARDEN_GUARD" and "errors" in template:
            sim_file["data"]["winScore"] = 250
            sim_file["data"]["queries"] = [{"text": err[0], "error": err[0].split()[0], "correct": err[1].split()[0]} for err in template["errors"]]
        elif template["engine"] == "SENTENCE_BLOCKS" and "blocks" in template:
            sim_file["data"]["slots"] = [{"id": f"s{j}", "expected": block} for j, block in enumerate(template["blocks"], 1)]
            sim_file["data"]["distractors"] = ["wrong", "text"]
        elif template["engine"] == "WORDGRID_ENGINE" and "words" in template:
            sim_file["data"]["size"] = 8
            sim_file["data"]["words"] = template["words"]
        elif template["engine"] == "DEEP_READER" and "passage" in template:
            sim_file["data"]["passage"] = f"<h2>{template['title']}</h2><p>{template['passage']}</p>"
            sim_file["data"]["questions"] = [{"text": "What is the main idea?", "options": ["A", "B", "C"], "answer": "A"}]
        
        # Write file
        file_path = os.path.join(quest_path, f"SIM-ENG7-T1-{quest_num}-{i:04d}.json")
        with open(file_path, 'w') as f:
            json.dump(sim_file, f, indent=4)
        
        char_idx += 1
    
    print(f"✓ Created {len(templates)} SIM files for {quest_folder}")

print("\n✅ All SIM files generated successfully!")
