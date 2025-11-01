def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, physical_damage, ki_damage, health, speed, gold
    """
    # Base stats by class
    if character_class == "Warrior":
        physical_damage = 15
        ki_damage = 5
        health = 120
        speed = 10
    elif character_class == "Mage":
        physical_damage = 5
        ki_damage = 15
        health = 80
        speed = 12
    elif character_class == "Rogue":
        physical_damage = 10
        ki_damage = 8
        health = 90
        speed = 20
    elif character_class == "Cleric":
        physical_damage = 8
        ki_damage = 12
        health = 110
        speed = 14
    else:
        physical_damage = 0
        ki_damage = 0
        health = 0
        speed = 0

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "physical_damage": physical_damage,
        "ki_damage": ki_damage,
        "health": health,
        "speed": speed,
        "gold": 100
    }
    return character


def save_character(character, filename):
    """
    Saves character to text file in specific format
    """
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Physical Damage: {character['physical_damage']}\n")
        file.write(f"Ki Damage: {character['ki_damage']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Speed: {character['speed']}\n")
        file.write(f"Gold: {character['gold']}\n")


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful
    """
    character = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                key, value = parts
                # match keys to dictionary format
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
    return character


def display_character(character):
    """
    Prints formatted character sheet
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Physical Damage: {character['physical_damage']}")
    print(f"Ki Damage: {character['ki_damage']}")
    print(f"Health: {character['health']}")
    print(f"Speed: {character['speed']}")
    print(f"Gold: {character['gold']}")
