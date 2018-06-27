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

def print_char(char):
    print("Game System: {}".format(char.game_system))
    print("Name: {}".format(char.name))

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Parse Arguments
    parser = argparse.ArgumentParser(description="CLI for manipulating RPG characters.")
    subparsers = parser.add_subparsers(dest="operation", help="Action help, Action to be performed on the RPG character.")
    
    ## Operation Arguments for Create
    parser_create = subparsers.add_parser("create", help="Create the RPG character.")
    parser_create.add_argument("game_system", help="The RPG system to use for the character.", choices=['shadowrun'], default='shadowrun')
    parser_create.add_argument("char_name", help="The name of the character.")
    
    ## Operation Arguments for Print
    parser_print = subparsers.add_parser("print", help="Print the RPG character to the console.")
    
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
    elif args.operation == 'print':
        print_char(load_char(args.filename))
    
    # Debug Stuff
    logging.debug("Args: %s", str(args))
    logging.debug("char_json: %s", char_json)

if __name__ == '__main__':
    main()
