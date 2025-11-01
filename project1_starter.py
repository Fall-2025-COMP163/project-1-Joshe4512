# DBZ Character Creator

# Create a new character
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns a dictionary with keys: name, class, level, strength, magic, health, gold
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
        "gold": gold,
        "form": "Base"
    }

    return character

# Calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Returns (strength, magic, health) for the given class and level.
    Each class has distinct base stats and growth per level.
    """
    if character_class.lower() == "earthling":
        strength = 10 + level * 3
        magic = 10 + level * 2
        health = 100 + level * 5
    elif character_class.lower() == "saiyan":
        strength = 15 + level * 4
        magic = 5 + level * 1
        health = 90 + level * 3
    elif character_class.lower() == "namekian":
        strength = 12 + level * 2
        magic = 12 + level * 3
        health = 120 + level * 4
    elif character_class.lower() == "frieza":
        strength = 8 + level * 2
        magic = 15 + level * 4
        health = 80 + level * 3
    else:
        strength = 5 + level * 2
        magic = 5 + level * 2
        health = 100 + level * 3

    return (strength, magic, health)

# Save character to file
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
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.write(f"Form: {character['form']}\n")

    return True

# Load character from file
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
        "strength": int(data.get("Strength", 0)),
        "magic": int(data.get("Magic", 0)),
        "health": int(data.get("Health", 0)),
        "gold": int(data.get("Gold", 0)),
        "form": data.get("Form", "Base")
    }

    return character

# Display character
def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print(f"Form: {character['form']}")

# Level up character and handle transformations
def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    # Level 100 transformations
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

# Helper to boost stats
def boost_stats(character, multiplier):
    character["strength"] = int(character["strength"] * multiplier)
    character["magic"] = int(character["magic"] * multiplier)
    character["health"] = int(character["health"] * multiplier)
