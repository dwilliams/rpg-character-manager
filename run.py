#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging

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
    
    parser_create = subparsers.add_parser("create", help="Create the RPG character.")
    parser_create.add_argument("--game_system", help="The RPG system to use for the character.", choices=['shadowrun'], default='shadowrun')
    parser_create.add_argument("filename", help="Path to the RPG character file to be manipulated.")
    
    parser_print = subparsers.add_parser("print", help="Print the RPG character to the console.")
    parser_print.add_argument("filename", help="Path to the RPG character file to be manipulated.")
    
    args = parser.parse_args()
    
    # Debug Stuff
    print(args)

if __name__ == '__main__':
    main()
