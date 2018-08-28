#!/usr/bin/env python3

### IMPORTS ###
import json
import logging
import os

from game_system.exceptions import GameSystemMismatchException, NotCharacterException

from game_system.none import Character
from game_system.shadowrun import ShadowRunCharacter

### GLOBALS ###
SUPPORTED_GAME_SYSTEMS = ['shadowrun']

### FUNCTIONS ###
def get_blank_char_of_game_system(game_system):
    char = None
    if game_system == 'shadowrun':
        char = ShadowRunCharacter()
    return char

### CLASSES ###
class CharacterFile:
    """
    This class handles the convertion of the Character object and other associated data into or from a JSON string saved
    into a file.
    """
    def __init__(self, charfilepath):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Save the file path
        self.filepath = os.path.abspath(charfilepath)

    def load_char(self):
        # Read the file
        with open(self.filepath, 'r') as filehandle:
            to_load_json = filehandle.read()

        # Load the JSON into a dict
        to_load_dict = json.loads(to_load_json)

        # Check the game_system type
        if to_load_dict['game_system'] not in SUPPORTED_GAME_SYSTEMS:
            raise GameSystemMismatchException()

        # Convert the dict into a Character using the correct game_system type
        character = get_blank_char_of_game_system(to_load_dict['game_system'])
        character.load_dict(to_load_dict)

        return character

    def save_char(self, character):
        to_save_dict = {}

        # Check to make sure the passed in character is derived from the game_system Character
        if not isinstance(character, Character):
            raise NotCharacterException()

        # Grab the character dictionary
        to_save_dict = character.save_dict()

        # Convert the dictionary to JSON
        to_save_json = json.dumps(to_save_dict)

        # Write to the file
        with open(self.filepath, 'w') as filehandle:
            filehandle.write(to_save_json)
