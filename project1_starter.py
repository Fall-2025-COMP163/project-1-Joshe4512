Name: Joshua Evans
Date: 10/31/2025

AI Usage: ChatGPT helped with function logic, formatting, troubleshooting, and implementation for level 100 forms.
AI Usage: GPT-5 helped with mapping DBZ stats to autograder-friendly keys and implementing transformations.
"""

# Function to create a new character
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    Returns dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    # Compute stats
    level = 1  # All new characters start at level 1
    
    # Calculate base stats based on class and level
    strength, magic, health = calculate_stats(character_class, level)
    return {
    
    # Base gold for all characters
    gold = 100

    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
        "gold": gold
    }

    return character

# Function to calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Returns (strength, magic, health) based on character_class and level
    """
    cls = character_class.lower()
    
    if cls == "earthling":
        strength = 50 + (level * 3)
        magic = 50 + (level * 3)
@@ -38,53 +51,52 @@ def calculate_stats(character_class, level):
    elif cls == "namekian":
        strength = 65 + (level * 2)
        magic = 45 + (level * 2)
        health = 120 + (level * 4)
        health = 125 + (level * 4)
    elif cls == "frieza":
        strength = 45 + (level * 2)
        magic = 55 + (level * 2)
        health = 70 + (level * 2)
    else:
        strength = 10 + (level * 2)
        magic = 10 + (level * 2)
        health = 100 + (level * 2)
        # fallback
        strength = 10 + level
        magic = 10 + level
        health = 100 + level
    
    return (strength, magic, health)

# Function to save a character to a file
# Function to save a character to a text file
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

# Function to load a character from a file
# Function to load a character from a text file
def load_character(filename):
    import os
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    
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
@@ -94,10 +106,10 @@ def load_character(filename):
        "health": int(data.get("Health", 0)),
        "gold": int(data.get("Gold", 0))
    }

    
    return character

# Function to display a character sheet
# Function to display a character
def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
@@ -112,24 +124,38 @@ def display_character(character):
def level_up(character):
    character["level"] += 1
    character["strength"], character["magic"], character["health"] = calculate_stats(character["class"], character["level"])

    # Level 100 special forms
    
    # Level 100 transformations
    if character["level"] == 100:
        cls = character["class"].lower()
        if cls == "saiyan":
            character["form"] = "Super Saiyan"
            boost_stats(character, 1.5)
            print(f"{character['name']} has transformed into a Super Saiyan!")
            print(f"🔥 {character['name']} has transformed into a Super Saiyan!")
        elif cls == "frieza":
            character["form"] = "Final Form"
            boost_stats(character, 1.6)
            print(f"{character['name']} has reached their Final Form!")
            print(f"❄️ {character['name']} has reached Final Form!")
        elif cls == "earthling":
            character["form"] = "Ultimate Mode"
            boost_stats(character, 1.4)
            print(f"{character['name']} has unlocked Ultimate Mode!")
            print(f"💪 {character['name']} has unlocked Ultimate Mode!")
        elif cls == "namekian":
            character["form"] = "Power Awakening"
            boost_stats(character, 1.45)
            print(f"{character['name']} has achieved Power Awakening!")
            print(f"🌿 {character['name']} has achieved Power Awakening!")

# Helper function to boost stats on transformations
def boost_stats(character, multiplier):
    character["strength"] = int(character["strength"] * multiplier)
    character["magic"] = int(character["magic"] * multiplier)
    character["health"] = int(character["health"] * multiplier)

# --- Main program for testing ---
if __name__ == "__main__":
    hero = create_character("Goku", "Saiyan")
    display_character(hero)
    print("\nLeveling up...")
    for _ in range(99):
        level_up(hero)
    display_character(hero)
