#!/usr/bin/env python3

### IMPORTS ###
#import logging

from game_system.exceptions import GameSystemMismatchException
from game_system.none.character import Character

#from game_system.adnd.item import ADNDItem

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDCharacter(Character):
    game_system = 'adnd'

    basic_stats_types = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    special_stats_types = []

    def __init__(self, name=''):
        # Ensure the parent's __init__ is called
        super().__init__(name=name)

        # Initialize basic and special stats to creation defaults

    def __str__(self):
        return "ADND{}".format(super().__str__())

    def load_dict(self, char_dict):
        self.logger.debug("Start - char_dict: %s", str(char_dict))
        super().load_dict(char_dict)

    def save_dict(self):
        self.logger.debug("Start - None")
        char_dict = super().save_dict()
        return char_dict

    def _check_item_type(self, item):
        self.logger.debug("Start - item: %s", str(item))
        #if not isinstance(item, ADNDItem):
        if item.game_system != self.game_system:
            raise GameSystemMismatchException()
