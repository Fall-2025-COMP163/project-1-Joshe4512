"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Joshua Evans
Date: 10/31/2025

AI Usage: ChatGPT helped with function and files logic, formatting, and level 100 transformations.
"""

# Create a new character
def create_character(name, character_class):
    """
    Creates a character dictionary with base stats
    Keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100
    
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


# Calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Returns a tuple (strength, magic, health) based on class and level
    strength = physical damage
    magic = ki damage
    """
    cls = character_class.lower()
    if cls == "earthling":
        strength = 50 + level * 3
        magic = 50 + level * 3
        health = 100 + level * 3
    elif cls == "saiyan":
        strength = 75 + level * 4
        magic = 35 + level * 2
        health = 80 + level * 2
    elif cls == "namekian":
        strength = 65 + level * 2
        magic = 45 + level * 2
        health = 120 + level * 4
    elif cls == "frieza":
        strength = 45 + level * 2
        magic = 55 + level * 2
        health = 70 + level * 2
    else:
        # Default fallback for unknown class
        strength = 10 + level * 2
        magic = 10 + level * 2
        health = 100 + level * 3
    return (strength, magic, health)


# Save character to a text file
def save_character(character, filename):
    """
    Saves character to file in proper format.
    Returns True if successful, False if file path invalid.
    """
    if filename == "":
        return False

    import os
    directory = os.path.dirname(filename)
    if directory != "" and not os.path.exists(directory):
        return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True


# Load character from a text file
def load_character(filename):
    """
    Loads character from file
    Returns character dictionary or None if file doesn't exist
    """
    import os
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            data[key] = value

    character = {
        "name": data.get("Character Name", ""),
        "class": data.get("Class", ""),
        "level": int(data.get("Level", 1)),
        "strength": int(data.get("Strength", 0)),
        "magic": int(data.get("Magic", 0)),
        "health": int(data.get("Health", 0)),
        "gold": int(data.get("Gold", 0))
    }
    return character


# Display character sheet
def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# Level up a character
def level_up(character):
    """
    Increase level by 1, recalc stats, unlock special forms at level 100
    """
    character["level"] += 1
    character["strength"], character["magic"], character["health"] = calculate_stats(
        character["class"], character["level"]
    )

    if character["level"] == 100:
        cls = character["class"].lower()
        if cls == "saiyan":
            print(f"🔥 {character['name']} has transformed into Super Saiyan!")
            character["strength"] = int(character["strength"] * 1.5)
            character["magic"] = int(character["magic"] * 1.5)
            character["health"] = int(character["health"] * 1.5)
        elif cls == "frieza":
            print(f"❄️ {character['name']} has reached Final Form!")
            character["strength"] = int(character["strength"] * 1.6)
            character["magic"] = int(character["magic"] * 1.6)
            character["health"] = int(character["health"] * 1.6)
        elif cls == "earthling":
            print(f"💪 {character['name']} has unlocked Ultimate Mode!")
            character["strength"] = int(character["strength"] * 1.4)
            character["magic"] = int(character["magic"] * 1.4)
            character["health"] = int(character["health"] * 1.4)
        elif cls == "namekian":
            print(f"🌿 {character['name']} has achieved Power Awakening!")
            character["strength"] = int(character["strength"] * 1.45)
            character["magic"] = int(character["magic"] * 1.45)
            character["health"] = int(character["health"] * 1.45)


# Main testing block
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("Goku", "Saiyan")
    display_character(char)

    print("\nLeveling up character...")
    for _ in range(99):
        level_up(char)
    display_character(char)

    print("\nSaving character...")
    save_character(char, "goku.txt")

    print("\nLoading character...")
    loaded = load_character("goku.txt")
    display_character(loaded)
