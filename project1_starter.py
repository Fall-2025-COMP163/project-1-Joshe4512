"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Joshua Evans
Date: 10/20/2025

AI Usage: AI gave an example on how to code the "Earthling" character class, which helped code the rest of the classes.
AI helped code the load_character section.
AI coded the level 100 forms and stat booster for forms.
AI helped troubleshoot issues with code and fixed typos and indentation errors.
"""

# ==============================
# CHARACTER CREATION
# ==============================

def calculate_stats(character_class, level):
    """Calculates stats based on level and class and returns a tuple of all stats."""
    if character_class == "Earthling":
        Physical_Damage = 50 + (level * 3)
        Ki_Damage = 50 + (level * 3)
        Health = 100 + (level * 3)
        Speed = 100 + (level * 3)

    elif character_class == "Saiyan":
        Physical_Damage = 75 + (level * 4)
        Ki_Damage = 35 + (level * 2)
        Health = 80 + (level * 2)
        Speed = 150 + (level * 3)

    elif character_class == "Namekian":
        Physical_Damage = 65 + (level * 2)
        Ki_Damage = 45 + (level * 2)
        Health = 125 + (level * 4)
        Speed = 80 + (level * 2)

    elif character_class == "Frieza":
        Physical_Damage = 45 + (level * 2)
        Ki_Damage = 55 + (level * 2)
        Health = 70 + (level * 2)
        Speed = 100 + (level * 4)

    else:
        print("Please choose a valid class: Earthling, Saiyan, Namekian, or Frieza.")
        Physical_Damage = Ki_Damage = Health = Speed = 0

    return (Physical_Damage, Ki_Damage, Health, Speed)


def create_character(name, character_class):
    """Creates a new character dictionary with calculated stats."""
    level = 1
    stats = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "physical_damage": stats[0],
        "ki_damage": stats[1],
        "health": stats[2],
        "speed": stats[3],
        "gold": 100,
        "form": "Base"
    }
    return character

# ==============================
# FILE OPERATIONS
# ==============================

def save_character(character, filename):
    """Saves character to a text file in a specific format."""
    with open(filename, "w") as file:
        file.write("Character Name: " + character["name"] + "\n")
        file.write("Class: " + character["class"] + "\n")
        file.write("Level: " + str(character["level"]) + "\n")
        file.write("Physical Damage: " + str(character["physical_damage"]) + "\n")
        file.write("Ki Damage: " + str(character["ki_damage"]) + "\n")
        file.write("Health: " + str(character["health"]) + "\n")
        file.write("Speed: " + str(character["speed"]) + "\n")
        file.write("Gold: " + str(character["gold"]) + "\n")
        file.write("Form: " + character["form"] + "\n")
    return True


def load_character(filename):
    """Loads character from text file and returns a character dictionary."""
    character = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Physical Damage":
                    character["physical_damage"] = int(value)
                elif key == "Ki Damage":
                    character["ki_damage"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Speed":
                    character["speed"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)
                elif key == "Form":
                    character["form"] = value
    return character

# ==============================
# DISPLAY AND LEVEL UP
# ==============================

def display_character(character):
    """Prints formatted character sheet."""
    print("=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Physical Damage:", character["physical_damage"])
    print("Ki Damage:", character["ki_damage"])
    print("Health:", character["health"])
    print("Speed:", character["speed"])
    print("Gold:", character["gold"])
    print("Form:", character["form"])


def boost_stats(character, multiplier):
    """Boosts stats when transformation unlocks."""
    character["physical_damage"] = int(character["physical_damage"] * multiplier)
    character["ki_damage"] = int(character["ki_damage"] * multiplier)
    character["health"] = int(character["health"] * multiplier)
    character["speed"] = int(character["speed"] * multiplier)


def level_up(character):
    """Increases level and recalculates stats, unlocking transformations at 100."""
    character["level"] = character["level"] + 1
    character["physical_damage"] += 5
    character["ki_damage"] += 5
    character["health"] += 10
    character["speed"] += 3
    print(character["name"], "leveled up to Level", character["level"], "!")

    # Unlock special transformations
    if character["level"] == 100:
        race = character["class"].lower()
        if race == "saiyan":
            character["form"] = "Super Saiyan"
            boost_stats(character, 1.5)
            print("🔥", character["name"], "has transformed into a Super Saiyan!")
        elif race == "frieza":
            character["form"] = "Final Form"
            boost_stats(character, 1.6)
            print("❄️", character["name"], "has reached their Final Form!")
        elif race == "earthling":
            character["form"] = "Ultimate Mode"
            boost_stats(character, 1.4)
            print("💪", character["name"], "has unlocked Ultimate Mode!")
        elif race == "namekian":
            character["form"] = "Power Awakening"
            boost_stats(character, 1.45)
            print("🌿", character["name"], "has achieved Power Awakening!")

# ==============================
# TEST AREA
# ==============================

if __name__ == "__main__":
    char = create_character("Karo", "Saiyan")
    display_character(char)
    level_up(char)
    save_character(char, "test_char.txt")
    loaded = load_character("test_char.txt")
    display_character(loaded)
