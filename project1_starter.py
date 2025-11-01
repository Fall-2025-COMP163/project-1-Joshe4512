"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Joshua Evans
Date: 10/31/2025

AI Usage: ChatGPT (GPT-5) helped with function implementation logic, formatting, and documentation.
"""

# Function to calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Returns (Physical_Damage, Ki_Damage, Health, Speed)
    Each class has distinct base stats and growth per level.
    """
    c = character_class.lower()
    if c == "earthling":
        physical = 50 + level * 3
        ki       = 50 + level * 3
        health   = 100 + level * 4
        speed    = 100 + level * 2
    elif c == "saiyan":
        physical = 75 + level * 4
        ki       = 35 + level * 2
        health   = 80 + level * 3
        speed    = 150 + level * 3
    elif c == "namekian":
        physical = 65 + level * 3
        ki       = 45 + level * 3
        health   = 125 + level * 4
        speed    = 80 + level * 2
    elif c == "frieza":
        physical = 45 + level * 3
        ki       = 55 + level * 3
        health   = 70 + level * 3
        speed    = 200 + level * 2
    else:
        physical = 10 + level * 2
        ki       = 10 + level * 2
        health   = 50 + level * 2
        speed    = 10 + level * 2

    return (physical, ki, health, speed)


# Function to create a new character
def create_character(name, character_class):
    level = 1
    physical, ki, health, speed = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "physical_damage": physical,
        "ki_damage": ki,
        "health": health,
        "speed": speed,
        "gold": 100,
        "form": "Base"
    }
    return character


# Function to save a character
def save_character(character, filename):
    if filename == "":
        return False
    import os
    directory = os.path.dirname(filename)
    if directory != "" and not os.path.exists(directory):
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Physical Damage: {character['physical_damage']}\n")
        file.write(f"Ki Damage: {character['ki_damage']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Speed: {character['speed']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.write(f"Form: {character['form']}\n")
    return True


# Function to load a character
def load_character(filename):
    import os
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        if ":" in line:
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
        "form": data.get("Form", "Base")
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
    print(f"Form: {character['form']}")


# Function to boost stats for forms
def boost_stats(character, multiplier):
    character["physical_damage"] = int(character["physical_damage"] * multiplier)
    character["ki_damage"] = int(character["ki_damage"] * multiplier)
    character["health"] = int(character["health"] * multiplier)
    character["speed"] = int(character["speed"] * multiplier)


# Function to level up a character
def level_up(character):
    character["level"] += 1
    physical, ki, health, speed = calculate_stats(character["class"], character["level"])
    character["physical_damage"] = physical
    character["ki_damage"] = ki
    character["health"] = health
    character["speed"] = speed

    # Level 100 forms
    if character["level"] == 100:
        c = character["class"].lower()
        if c == "saiyan":
            character["form"] = "Super Saiyan"
            boost_stats(character, 1.5)
        elif c == "frieza":
            character["form"] = "Final Form"
            boost_stats(character, 1.6)
        elif c == "earthling":
            character["form"] = "Ultimate Mode"
            boost_stats(character, 1.4)
        elif c == "namekian":
            character["form"] = "Power Awakening"
            boost_stats(character, 1.45)


# Example test
if __name__ == "__main__":
    char = create_character("Goku", "Saiyan")
    display_character(char)
    level_up(char)
    display_character(char)
    save_character(char, "goku.txt")
    loaded = load_character("goku.txt")
    display_character(loaded)
