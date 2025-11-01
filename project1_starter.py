"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Joshua Evans]
Date: [10/20/2025]

AI Usage: AI gave an example on how to code the "Earthling" character class, which helped code the rest of the classes.
AI helped code the load_character section 
AI coded the level 100 forms and stat booster for forms.

def create_character (name , character_class): #
    if character_class == "Earthling":
        return{"Physical_Damage": 50, "Ki_Damage": 50, "Health": 100, "Speed": 100}
    elif character_class == "Saiyan":
        return{"Physical_Damage": 75, "Ki_Damage": 35, "Health": 80, "Speed": 150 }
    elif character_class == "Namekian":
        return{"Physical_Damage": 65, "Ki_Damage": 45, "Health": 120, "Speed": 80}
    elif character_class == "Frieza":
        return{"Physical_Damage": 45, "Ki_Damage": 55, "Health": 70, "Speed": 200}
    else: return{"Pick a race: Earthling, Saiyan, Namekian, Frieza"}
    def create_character(name, character_class):
        stats = calculate_stats(charcacter_class)
        character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "Physical_Damage": stats[Physical_Damage"],
        "Ki_Damage": stats["Ki_Damage"],
        "Health": stats["Health"],
        "Speed": stats["speed"],
        "zeni": 100
    }
    return character
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level): #Calculates stats based on level and class and returns a tuple of all stats 
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

    elif character_class == "Freiza":
    Physical_Damage = 45 + (level * 2)
    Ki_Damage = 55 + (level * 2)
    Health = 70 + (level * 2)
    Speed = 100 + (level * 4)
    
    else:print("please choose a class: Earthling, Saiyan, Namekian, or Frieza")

    return (Physical_Damage, Ki_Damage, Health, Speed)
    
    
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    """
    Saves character to a text file in a specific format
    Returns: True if successful
    """
    with open(filename, "w") as file:
        file.write("Character Name: " + character["name"] + "\n")
        file.write("Class: " + character["class"] + "\n")
        file.write("Level: " + str(character["level"]) + "\n")
        file.write("Physical Damage: " + str(character["physical_damage"]) + "\n")
        file.write("Ki Damage: " + str(character["ki_damage"]) + "\n")
        file.write("Health: " + str(character["health"]) + "\n")
        file.write("Speed: " + str(character["speed"]) + "\n")
        file.write("Gold: " + str(character["gold"]) + "\n")
    return True



    #Saves character to text file in specific format
    #Returns: True if successful, False if an error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary
    """
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
    return character


def display_character(character):
    print("=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Physical Damage:", character["physical_damage"])
    print("Ki Damage:", character["ki_damage"])
    print("Health:", character["health"])
    print("Speed:", character["speed"])
    print("Gold:", character["gold"])

    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    character["level"] = character["level"] + 1
    character["physical_damage"] = character["physical_damage"] + 5
    character["ki_damage"] = character["ki_damage"] + 5
    character["health"] = character["health"] + 10
    character["speed"] = character["speed"] + 3
    print(character["name"], "leveled up to Level", character["level"], "!")
    if character["level"] == 100:
        if character["class"].lower() == "saiyan":
            character["form"] = "Super Saiyan"
            boost_stats(character, 1.5)
            print("🔥", ["name"], "has transformed into a Super Saiyan, the legend lives on!")
        elif character["class"].lower() == "frieza":
            character["form"] = "Final Form"
            boost_stats(character, 1.6)
            print("❄️", character["name"], "has reached their Final Form!")
        elif character["class"].lower() == "earthling":
            character["form"] = "Ultimate Mode"
            boost_stats(character, 1.4)
            print("💪", character["name"], "has unlocked Ultimate Mode!")
        elif character["class"].lower() == "namekian":
            character["form"] = "Power Awakening"
            boost_stats(character, 1.45)
            print("🌿", character["name"], "has achieved Power Awakening!")

    def boost_stats(character, multiplier):
        character["physical_damage"] = int(character["physical_damage"] * multiplier)
        character["ki_damage"] = int(character["ki_damage"] * multiplier)
        character["health"] = int(character["health"] * multiplier)
        character["speed"] = int(character["speed"] * multiplier)



    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
