#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import os

### GLOBALS ###

### FUNCTIONS ###

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
    parser_create.add_argument("--game_system", help="The RPG system to use for the character.", choices=['shadowrun'], default='shadowrun')
    
    ## Operation Arguments for Print
    parser_print = subparsers.add_parser("print", help="Print the RPG character to the console.")
    
    ## Global Arguments
    parser.add_argument("filename", help="Path to the RPG character file to be manipulated.")
    args = parser.parse_args()
    
    # If not the create operation, load the json file
    if args.operation is not "create":
        with open(os.path.abspath(args.filename)) as f:
            char_json = f.read()
    
    # Debug Stuff
    logging.debug("Args: %s", str(args))
    logging.debug("char_json: %s", char_json)

if __name__ == '__main__':
    main()
