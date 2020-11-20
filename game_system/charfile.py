#!/usr/bin/env python3

### IMPORTS ###
import json
import logging
import os

from game_system.exceptions import BadFactoryTypeException, GameSystemMismatchException, NotCharacterException

from game_system.factories.item_factory import ItemFactory
from game_system.factories.equipment_factory import EquipmentFactory
from game_system.factories.weapon_factory import WeaponFactory

from game_system.none import Character
from game_system.shadowrun import ShadowRunCharacter
from game_system.adnd import ADNDCharacter

### GLOBALS ###
SUPPORTED_GAME_SYSTEMS = ['shadowrun', 'adnd']

### FUNCTIONS ###
def get_blank_char_of_game_system(game_system):
    char = None
    if game_system == 'shadowrun':
        char = ShadowRunCharacter()
    elif game_system == 'adnd':
        char = ADNDCharacter()
    return char

### CLASSES ###
class CharacterFile:
    """
    This class handles the conversion of the Character object and other associated data into or from a JSON string saved
    into a file.
    """
    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        self.item_factory = None
        self.equipment_factory = None
        self.weapon_factory = None

    def register_item_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, ItemFactory):
            raise BadFactoryTypeException()
        self.item_factory = factory

    def register_equipment_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, EquipmentFactory):
            raise BadFactoryTypeException()
        self.equipment_factory = factory

    def register_weapon_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, WeaponFactory):
            raise BadFactoryTypeException()
        self.weapon_factory = factory

    def load_char(self, filepath):
        # Read the file
        with open(os.path.abspath(filepath), 'r') as filehandle:
            to_load_json = filehandle.read()
        self.logger.debug("JSON: \n%s", to_load_json)

        # Load the JSON into a dict
        to_load_dict = json.loads(to_load_json)

        # Check the game_system type
        if to_load_dict['game_system'] not in SUPPORTED_GAME_SYSTEMS:
            raise GameSystemMismatchException()

        # Convert the dict into a Character using the correct game_system type
        character = get_blank_char_of_game_system(to_load_dict['game_system'])
        character.load_dict(to_load_dict, self.item_factory, self.equipment_factory, self.weapon_factory)

        return character

    def save_char(self, character, filepath):
        to_save_dict = {}

        # Check to make sure the passed in character is derived from the game_system Character
        if not isinstance(character, Character):
            raise NotCharacterException()

        # Grab the character dictionary
        to_save_dict = character.save_dict()

        # Convert the dictionary to JSON
        to_save_json = json.dumps(to_save_dict)

        # Write to the file
        with open(os.path.abspath(filepath), 'w') as filehandle:
            filehandle.write(to_save_json)
