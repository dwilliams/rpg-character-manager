#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import os

import game_system
import game_system.shadowrun

### GLOBALS ###

### FUNCTIONS ###
def create_char(game_sys, char_name, filename):
    # Create a character for the desired system
    if game_sys == 'shadowrun':
        character = game_system.shadowrun.ShadowRunCharacter(char_name)

    # Save the character to the file
    charfile = game_system.CharacterFile(filename)
    charfile.save_char(character)

def load_char(filename):
    # Load the character from the file
    charfile = game_system.CharacterFile(filename)
    return charfile.load_char()

def save_char(character, filename):
    # Save the character to the file
    charfile = game_system.CharacterFile(filename)
    charfile.save_char(character)

def print_char(char):
    print("Game System: {}".format(char.game_system))
    print("Name: {}".format(char.name))
    # Add a template here for printing the character data nicely

def add_item_to_char(char, item_class_name):
    # Gotta find a better way to handle this than adding each item by class, but that'll likely be in the GUI...
    # https://stackoverflow.com/a/452981
    parts = item_class_name.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    # 'm' now has the item class 'type' and is instantiable

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    # Parse Arguments
    parser = argparse.ArgumentParser(description="CLI for manipulating RPG characters.")
    subparsers = parser.add_subparsers(
        dest="operation",
        help="Action help, Action to be performed on the RPG character.")

    ## Operation Arguments for Create
    parser_create = subparsers.add_parser("create", help="Create the RPG character.")
    parser_create.add_argument(
        "game_system",
        help="The RPG system to use for the character.",
        choices=['shadowrun'],
        default='shadowrun')
    parser_create.add_argument("char_name", help="The name of the character.")

    ## Operation Arguments for Print
    parser_print = subparsers.add_parser("print", help="Print the RPG character to the console.")

    ## Operation Arguments for AddItem
    parser_add_item = subparsers.add_parser("add_item", help="Add item to the RPG character.")
    parser_add_item.add_argument(
        "item_class_name",
        help="The python class name (import name) of the item to add to the inventory.")
    parser_add_item.add_argument(
        "--equip",
        help="Flag to equip the item.",
        action="store_const",
        const=True,
        default=False)

    ## Global Arguments
    parser.add_argument("filename", help="Path to the RPG character file to be manipulated.")
    args = parser.parse_args()

    # If not the create operation, load the json file
    if args.operation is not "create":
        with open(os.path.abspath(args.filename)) as f:
            char_json = f.read()

    # Call the correct operation with the needed arguments
    if args.operation == 'create':
        create_char(args.game_system, args.char_name, args.filename)
    else:
        char = load_char(args.filename)
        if args.operation == 'print':
            print_char(char)
        elif args.operation == 'add_item':
            add_item_to_char(char, args.item_class_name)
            save_char(char, args.filename)

if __name__ == '__main__':
    main()
