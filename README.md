COMP 163 - Project 1: Simple Character Creator

Overview

This project implements a basic role-playing game (RPG) character creation system in Python. It allows users to create new characters, calculate stats based on class and level, level up existing characters, and persist character data to a text file for saving and loading.

The goal is to demonstrate fundamental Python concepts, including:

Dictionary usage for data structures.

Conditional logic (if/elif/else).

Function definition and modular code structure.

Basic file input/output (I/O) operations.

Game Concept

This project is set in the high-fantasy world of Aethelred, a realm recovering from a cataclysmic event known as the Sundering. Player characters start as nascent members of one of four major guilds—each specializing in a different form of combat or utility. The core loop involves creating a character and tracking their growth as they prepare to venture out into the shattered lands.

Design Choices: Stat Formulas

The stat formulas in the calculate_stats function were designed to ensure that each class possesses a distinct and non-overlapping identity, particularly concerning their primary attributes:

Warrior: Features the highest base Health and Strength scaling (+15 Health, +6 Strength per level) to establish a clear "tank" and melee focus. Magic is negligible.

Mage: Has the highest base Magic and Magic scaling (+6 Magic per level) but the lowest base Health and Strength, enforcing a "glass cannon" role.

Cleric & Rogue: Offer more balanced growth, ensuring intermediate roles (utility/support) while maintaining competitive scaling in their focused areas (Cleric with Health/Magic, Rogue with Strength/Health for durability/damage).

This approach satisfies the requirement for statistically different class distributions at any given level.

Features

The script provides the following core functionalities:

create_character(name, character_class): Creates a new Level 1 character dictionary with base stats and 100 Gold.

calculate_stats(character_class, level): Determines a character's Strength, Magic, and Health based on their class and current level.

level_up(character): Increments the character's level by 1 and recalculates their stats.

save_character(character, filename): Writes the character dictionary data to a specified text file in a clear, readable format.

load_character(filename): Reads character data from a text file and reconstructs the character dictionary.

display_character(character): Prints a formatted character sheet to the console.

Bonus Creative Features

The primary unique feature of this project is the robust file handling for persistence which adheres to strict environmental constraints.

Import-Free File Handling: The save_character and load_character functions utilize native Python try...except blocks with with open(...) to handle file I/O errors (like FileNotFoundError or general IOError) without requiring imports from the os module. This makes the code exceptionally resilient in restricted execution environments.

Data Integrity: The load_character function includes safety measures to ensure all loaded numeric values are correctly converted back to integers using int(), preventing runtime errors from type mismatches.

AI Usage

AI assistance was utilized collaboratively in the development of this project:

ChatGPT (GPT-5): Assisted with refining the initial draft of the function logic, ensuring proper dictionary formatting, and generating detailed Python docstrings.

Google Gemini: Provided assistance in debugging and refactoring the file handling logic, replacing path checks with more robust, idiomatic Python try...except file I/O error handling.

Usage: How to Run

To test and run this script:

Ensure you have a Python environment (Python 3.6+) ready.

Save the provided code as character_creator.py.

Run the script directly from your terminal:

python character_creator.py


The main block (if __name__ == "__main__":) demonstrates the creation, leveling, saving, and loading process:

A character named "Aria" (Mage) is created.

Aria is leveled up from Level 1 to Level 2.

Aria's data is saved to aria.txt in the current working directory.

The data is loaded back from aria.txt and displayed.

Character Classes and Stat Distribution

The available classes are designed with distinct stat priorities:

Class

Primary Stat Focus

Base Strength (Lvl 1)

Base Magic (Lvl 1)

Base Health (Lvl 1)

Warrior

Strength, High Health

18

2

165

Mage

High Magic, Low Health

3

26

75

Rogue

Balanced Agility/Magic

10

9

96

Cleric

Balanced Health/Magic

8

14

108

Note: The numbers above reflect the initial stat calculation at Level 1 (Base + 1 * multiplier).

Character File Format

Characters are saved in a simple key-value text format, with each property on a new line:

Character Name: Aria
Class: Mage
Level: 2
Strength: 4
Magic: 32
Health: 75
Gold: 100
