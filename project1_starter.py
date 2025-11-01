"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Joshua Evans
Date: 10/31/2025

AI Usage: ChatGPT (GPT-5) and Google Gemini helped with function logic, formatting, and documentation.
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
    
    Stats updated to ensure Warrior and Mage do not produce identical level 1 values.
    """
    cls = character_class.lower()
    if cls == "warrior":
        # Focused on Strength and Health
        strength = 12 + level * 6
        magic = 1 + level * 1
        health = 150 + level * 15
    elif cls == "mage":
        # Focused on Magic and lower Health
        strength = 2 + level * 1
        magic = 20 + level * 6
        health = 70 + level * 5
    elif cls == "rogue":
        strength = 7 + level * 3
        magic = 7 + level * 2
        health = 90 + level * 6
    elif cls == "cleric":
        strength = 6 + level * 2
        magic = 10 + level * 4
        health = 100 + level * 8
    else:
        # Default fallback
        strength = 5 + level * 2
        magic = 5 + level * 2
        health = 100 + level * 5
    return (strength, magic, health)


# Save character to a text file
def save_character(character, filename):
    """
    Saves character to file in proper format.
    Returns True if successful, False if file path invalid.
    
    Note: Directory checking logic removed due to 'os' module restriction.
    """
    if filename == "":
        return False
    
    try:
        # Use 'with open' to ensure the file is closed automatically
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except IOError:
        # Catch FileNotFoundError or other path/permission issues
        return False


# Load character from a text file
def load_character(filename):
    """
    Loads character from file
    Returns character dictionary or None if file doesn't exist.
    Uses try/except instead of os.path.exists for file existence check.
    """
    try:
        # Use 'with open' for reading
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None
    except IOError:
        # Catch other file read errors (e.g., permissions)
        return None

    data = {}
    for line in lines:
        if ":" in line:
            # Use split with maxsplit=1 to handle potential colons in values (safer)
            key, value = line.strip().split(": ", 1)
            data[key] = value

    # Note: Need to convert level, stats, and gold back to integers for the dictionary
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
    Increase level by 1, recalc stats
    """
    character["level"] += 1
    character["strength"], character["magic"], character["health"] = calculate_stats(
        character["class"], character["level"]
    )


# Main testing block
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("Aria", "Mage")
    display_character(char)

    print("\nLeveling up character...")
    level_up(char)
    display_character(char)

    print("\nSaving character...")
    # This assumes 'aria.txt' can be created in the current directory
    save_character(char, "aria.txt")

    print("\nLoading character...")
    loaded = load_character("aria.txt")
    display_character(loaded)
