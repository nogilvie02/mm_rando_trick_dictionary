# database.py

trackable_items = ["an Ocarina", "a Bow", "Fire Arrows", "Ice Arrows", "Light Arrows", "a Deed/Moon's Tear/Room Key/Letter/Pendant", 
                   "Bombs", "Bombchus", "Deku Sticks", "Deku Nuts", "Magic Beans", 
                   "a Powder Keg", "the Lens of Truth", "the Hookshot", "the Great Fairy's Sword", 
                   "a Bottle", "a Shield", "a Sword", 
                   "Deku Mask", "Goron Mask", "Zora Mask", "Fierce Deity Mask", 
                   "Postman's Hat", "Blast Mask", "Bremen/Kamaro's Mask", 
                   "any following mask: All-Night/Stone/Great Fairy's/Keaton/Bunny/Don Gero/Scents/Romani/Circus Leader's/Kafei's/Couple's/Truth/Gibdo/Garo/Captain's"
                   ]


trick_database = {
    "Action Swap (Inverted Deku Stick)": {
        "items_needed": [["a Bow", "Deku Sticks"], 
                         ["Fire Arrows", "Deku Sticks"], 
                         ["Ice Arrows", "Deku Sticks"], 
                         ["Light Arrows", "Deku Sticks"], 
                         ["the Hookshot", "Deku Sticks"]
                         ] 
    },
    "Action Swap (Flaming Arrow)": {
        "items_needed": [["a Bow", "Deku Sticks"]
                         ]
    },
    "Bomb Hover": {
        "items_needed": [["Bombs", "a Shield", "a Sword"], 
                         ["Bombchus", "a Shield", "a Sword"], 
                         ["Blast Mask", "a Shield", "a Sword"], 
                         ["Bombs", "a Shield", "Deku Sticks"], 
                         ["Bombchus", "a Shield", "Deku Sticks"], 
                         ["Blast Mask", "a Shield", "Deku Sticks"], 
                         ["Bombs", "a Shield", "the Great Fairy's Sword"], 
                         ["Bombchus", "a Shield", "the Great Fairy's Sword"], 
                         ["Blast Mask", "a Shield", "the Great Fairy's Sword"]
                         ]
    },
    "Bottle Duplication": {
        "items_needed": [["a Bottle", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Bottle", "Postman's Hat"], 
                         ["a Bottle", "any following mask: All-Night/Stone/Great Fairy's/Keaton/Bunny/Don Gero/Scents/Romani/Circus Leader's/Kafei's/Couple's/Truth/Gibdo/Garo/Captain's"], 
                         ["a Bottle", "Bremen/Kamaro's Mask"], 
                         ["a Bottle", "Blast Mask"], 
                         ["a Bottle", "Deku Sticks"], 
                         ["a Bottle", "Deku Nuts"], 
                         ["a Bottle", "Bombs"], 
                         ["a Bottle", "Magic Beans"], 
                         ["a Bottle", "the Lens of Truth"], 
                         ["a Bottle", "a Powder Keg", "Goron Mask"]
                         ]
    },
    "Bow Extension": {
        "items_needed": [["a Bow"]
                         ]
    },
    "Equip Swap": {
        "items_needed": [["an Ocarina"], 
                         ["a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["Postman's Hat"], 
                         ["Deku Mask"]
                         ]
    },
    "HESS": {
        "items_needed": [["Bombs"]
                         ]
    },
    "Gainer": {
        "items_needed": [[]
                         ]
    },
    "Goron Damage Boost": {
        "items_needed": [["Goron Mask"]
                         ]
    },
    "Hookshot Clip": {
        "items_needed": [["the Hookshot"]
                         ]
    },
    "ISG Anywhere": {
        "items_needed": [["a Shield", "a Sword", "Bombs"], 
                         ["a Shield", "Deku Sticks", "Bombs"], 
                         ["a Shield", "the Great Fairy's Sword", "Bombs"], 
                         ["a Shield", "Deku Sticks", "Bremen/Kamaro's Mask"], 
                         ["a Shield", "the Great Fairy's Sword", "Bremen/Kamaro's Mask"]
                         ]
    },
    "Situational ISG (may need sign or rock or pot)": {
        "items_needed": [["a Shield", "a Sword"], 
                         ["a Shield", "Deku Sticks"], 
                         ["a Shield", "the Great Fairy's Sword"]
                         ]
    },
    "Long (Bomb Recoil) Jump": {
        "items_needed": [["Bombs"]
                         ]
    },
    "Megaflip": {
        "items_needed": [["Bombs"], 
                         ["Bombchus", "a Shield"]
                         ]
    },
    "Ocarina/Cutscene Dive": {
        "items_needed": [["an Ocarina"], 
                         ["a Shield", "a Sword", "Bombs", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Shield", "Deku Sticks", "Bombs", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Shield", "the Great Fairy's Sword", "Bombs", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Shield", "Deku Sticks", "Bremen/Kamaro's Mask", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Shield", "the Great Fairy's Sword", "Bremen/Kamaro's Mask", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Shield", "a Sword", "Bombs", "a Bottle"], 
                         ["a Shield", "Deku Sticks", "Bombs", "a Bottle"], 
                         ["a Shield", "the Great Fairy's Sword", "Bombs", "a Bottle"], 
                         ["a Shield", "Deku Sticks", "Bremen/Kamaro's Mask", "a Bottle"], 
                         ["a Shield", "the Great Fairy's Sword", "Bremen/Kamaro's Mask", "a Bottle"]
                         ]
    },
    "Ocarina Items": {
        "items_needed": [["Bombs", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["Bombs", "a Bottle"], 
                         ["Bombs", "Deku Mask"], 
                         ["Bombs", "Goron Mask"], 
                         ["Bombs", "Zora Mask"], 
                         ["Bombs", "Fierce Deity Mask"], 
                         ["Bombs", "Magic Beans"], 
                         ["a Bottle", "a Bow"], 
                         ["a Bottle", "Fire Arrows"], 
                         ["a Bottle", "Ice Arrows"], 
                         ["a Bottle", "Light Arrows"], 
                         ["a Bottle", "Bombs"], 
                         ["a Bottle, Bombchus"], 
                         ["a Bottle", "Deku Sticks"], 
                         ["a Bottle", "the Hookshot"], 
                         ["a Bottle", "the Great Fairy's Sword"], 
                         ["a Bottle", "Deku Mask"], 
                         ["a Bottle", "Goron Mask"], 
                         ["a Bottle", "Zora Mask"], 
                         ["a Bottle", "a Sword"]
                         ]
    },
    "Recoil Flip": {
        "items_needed": [["Bombs", "a Shield"], 
                         ["Bombchus", "a Shield"], 
                         ["Blast Mask", "a Shield"]
                         ]
    },
    "Remote Hookshot/Hookslide": {
        "items_needed": [["the Hookshot", "a Bottle"]
                         ]
    },
    "Slash Extension": {
        "items_needed": [["a Sword"], 
                         ["Deku Sticks"], 
                         ["the Great Fairy's Sword"], 
                         ["Fierce Deity Mask"]
                         ]
    },
    "Song Storage": {
        "items_needed": [["an Ocarina"]
                         ]
    },
    "Superslide": {
        "items_needed": [["a Shield", "Bombs"], 
                         ["a Shield", "Bombchus"]
                         ]
    },
    "Timestop": {
        "items_needed": [["Bombs", "a Shield", "an Ocarina"], 
                         ["Bombs", "a Shield", "Deku Mask"], 
                         ["Bombs", "a Shield", "Goron Mask"], 
                         ["Bombs", "a Shield", "Zora Mask"], 
                         ["Bombs", "a Shield", "Fierce Deity Mask"], 
                         ["Bombs", "a Shield", "a Deed/Moon's Tear/Room Key/Letter/Pendant"], 
                         ["a Bottle", "a Shield"]]
    },
    "Weirdshot": {
        "items_needed": [["Bombs", "the Hookshot", "a Shield"]
                         ]
    },
    "Zora Clipping": {
        "items_needed": [["Zora Mask"]
                         ]
    }
}