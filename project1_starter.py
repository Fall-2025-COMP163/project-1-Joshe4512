"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Joshua Evans
Date: 10/31/2025

AI Usage: AI helped with the development of the leveling system and the transformations for when characters reach level 100
AI explained Functions and files to further help development
AI used CHAT GPT and GOOGLE GEMINI
"""

# Function to create a new character
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, physical_damage, ki_damage, health, speed, gold
    """
    level = 1  # All new characters start at level 1

    # Calculate base stats
    physical_damage, ki_damage, health, speed = calculate_stats(character_class, level)

    # Base gold for all characters
    gold = 100

    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "physical_damage": physical_damage,
        "ki_damage": ki_damage,
        "health": health,
        "speed": speed,
        "gold": gold,
        "form": ""  # Will store transformations like Super Saiyan
    }

    return character


# Function to calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (physical_damage, ki_damage, health, speed)
    """
    if character_class.lower() == "earthling":
        physical_damage = 50 + (level * 3)
        ki_damage = 50 + (level * 3)
        health = 100 + (level * 3)
        speed = 100 + (level * 3)
    elif character_class.lower() == "saiyan":
        physical_damage = 75 + (level * 4)
        ki_damage = 35 + (level * 2)
        health = 80 + (level * 2)
        speed = 150 + (level * 3)
    elif character_class.lower() == "namekian":
        physical_damage = 65 + (level * 2)
        ki_damage = 45 + (level * 2)
        health = 125 + (level * 4)
        speed = 80 + (level * 2)
    elif character_class.lower() == "frieza":
        physical_damage = 45 + (level * 2)
        ki_damage = 55 + (level * 2)
        health = 70 + (level * 2)
        speed = 100 + (level * 4)
    else:
        physical_damage = 10
        ki_damage = 10
        health = 100
        speed = 50

    return (physical_damage, ki_damage, health, speed)


# Function to save a character to a text file
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
    if filename == "":
        return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Physical Damage: {character['physical_damage']}\n")
    file.write(f"Ki Damage: {character['ki_damage']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Speed: {character['speed']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.write(f"Form: {character['form']}\n")
    file.close()
    return True


# Function to load a character from a text file
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    import os
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    data = {}
    for line in lines:
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            data[key] = value

    character = {
        "name": data.get("Character Name", ""),
        "class": data.get("Class", ""),
        "level": int(data.get("Level", 1)),
        "physical_damage": int(data.get("Physical Damage", 0)),
        "ki_damage": int(data.get("Ki Damage", 0)),
        "health": int(data.get("Health", 0)),
        "speed": int(data.get("Speed", 0)),
        "gold": int(data.get("Gold", 0)),
        "form": data.get("Form", "")
    }

    return character


# Function to display a character sheet
def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Physical Damage: {character['physical_damage']}")
    print(f"Ki Damage: {character['ki_damage']}")
    print(f"Health: {character['health']}")
    print(f"Speed: {character['speed']}")
    print(f"Gold: {character['gold']}")
    if character["form"] != "":
        print(f"Form: {character['form']}")


# Function to level up a character and recalculate stats
def level_up(character):
    character["level"] += 1
    pd, kd, hp, spd = calculate_stats(character["class"], character["level"])
    character["physical_damage"] = pd
    character["ki_damage"] = kd
    character["health"] = hp
    character["speed"] = spd

    # Unlock ultimate forms at level 100
    if character["level"] == 100:
        if character["class"].lower() == "saiyan":
            character["form"] = "Super Saiyan"
            boost_stats(character, 1.5)
        elif character["class"].lower() == "frieza":
            character["form"] = "Final Form"
            boost_stats(character, 1.6)
        elif character["class"].lower() == "earthling":
            character["form"] = "Ultimate Mode"
            boost_stats(character, 1.4)
        elif character["class"].lower() == "namekian":
            character["form"] = "Power Awakening"
            boost_stats(character, 1.45)


# Helper function to boost stats for transformations
def boost_stats(character, multiplier):
    character["physical_damage"] = int(character["physical_damage"] * multiplier)
    character["ki_damage"] = int(character["ki_damage"] * multiplier)
    character["health"] = int(character["health"] * multiplier)
    character["speed"] = int(character["speed"] * multiplier)


# Main program for testing
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    char = create_character("Goku", "Saiyan")
    display_character(char)

    print("\nLeveling up to 100...")
    for _ in range(99):
        level_up(char)
    display_character(char)

    print("\nSaving character...")
    save_character(char, "goku.txt")

    print("\nLoading character...")
    loaded_char = load_character("goku.txt")
    display_character(loaded_char)
