COMP 163 - Project 1: Simple Character Creator

Overview

This project implements a basic role-playing game (RPG) character creation system in Python. It allows users to create new characters, calculate stats based on class and level, level up existing characters, and persist character data to a text file for saving and loading.

The goal is to demonstrate fundamental Python concepts, including:

Dictionary usage for data structures.

Conditional logic (if/elif/else).

Function definition and modular code structure.

Basic file input/output (I/O) operations.

Features

The script provides the following core functionalities:

create_character(name, character_class): Creates a new Level 1 character dictionary with base stats and 100 Gold.

calculate_stats(character_class, level): Determines a character's Strength, Magic, and Health based on their class and current level.

level_up(character): Increments the character's level by 1 and recalculates their stats.

save_character(character, filename): Writes the character dictionary data to a specified text file in a clear, readable format.

load_character(filename): Reads character data from a text file and reconstructs the character dictionary.

display_character(character): Prints a formatted character sheet to the console.

Usage

To use this script:

Ensure you have a Python environment ready.

Run the script directly from your terminal:

python character_creator.py


The main block (if __name__ == "__main__":) demonstrates the creation, leveling, saving, and loading process:

A character named "Aria" (Mage) is created.

Aria is leveled up from Level 1 to Level 2.

Aria's data is saved to aria.txt.

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
