# Name: Joshua Evans 
# Date: 10/20/25
# COMP 163
def create_character(name, character_class):
    #"""Creates a new character dictionary."""
    # Base stats for each class
    if character_class == "Earthling":
        physical_damage = 50
        ki_damage = 50
        health = 100
        speed = 100
    elif character_class == "Saiyan":
        physical_damage = 75
        ki_damage = 35
        health = 80
        speed = 150
    elif character_class == "Namekian":
        physical_damage = 65
        ki_damage = 45
        health = 125
        speed = 80
    elif character_class == "Frieza":
        physical_damage = 45
        ki_damage = 55
        health = 70
        speed = 100
    else:
        physical_damage = 0
        ki_damage = 0
        health = 0
        speed = 0

    # Create character dictionary
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
    """Saves the character dictionary to a file."""
    with open(filename, "w") as file:
        for key in character:
            file.write(f"{key}:{character[key]}\n")


def load_character(filename):
    """Loads character data from a file and returns a dictionary."""
    character = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(":")
            if key in ["level", "physical_damage", "ki_damage", "health", "speed", "gold"]:
                character[key] = int(value)
            else:
                character[key] = value
    return character


def display_character(character):
    """Prints all character information."""
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Physical Damage: {character['physical_damage']}")
    print(f"Ki Damage: {character['ki_damage']}")
    print(f"Health: {character['health']}")
    print(f"Speed: {character['speed']}")
    print(f"Gold: {character['gold']}")
