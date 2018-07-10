#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.equipment import Equipment

from game_system.exceptions import CharacterInvalidStatTypeException
from game_system.exceptions import ItemNotEquipableException
from game_system.exceptions import ItemNotInInventoryException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Character:
    game_system = 'none'

    basic_stats_types = ['strength', 'charisma', 'intelligence', 'wisdom']
    special_stats_types = ['magic']

    def __init__(self, name=''):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Some basic values about the character
        self.name = name
        #self.age = age

        # Race
        # NOTE: Seeing as racial attributes in most game system have an effect on the character, this should be a set of
        #       classes, similar to equipment.  This will be added later.
        #self.race = race

        # Categories of things
        self.inventory = set()
        self.equipped = set()
        self.effects = set() # Spells, etc.  Have burn down time (might be inf).

        # Stats dictionaries
        self.basic_stats = {}
        self.special_stats = {}

        # Initialize basic and special stats to creation defaults
        for stats_type in self.basic_stats_types:
            self.basic_stats[stats_type] = 0
        for stats_type in self.special_stats_types:
            self.special_stats[stats_type] = 0

    def __str__(self):
        return "Character: {}".format(self.name)

    def load_dict(self, char_dict):
        self.logger.debug("Arguments: char_dict: %s", str(char_dict))
        raise NotImplementedError()

    def save_dict(self):
        self.logger.debug("Arguments: None")
        raise NotImplementedError()

    def add_to_inventory(self, item):
        self.logger.debug("Arguments: item: %s", str(item))
        self._check_item_type(item)
        self.inventory.add(item)

    def remove_from_inventory(self, item):
        self.logger.debug("Arguments: item: %s", str(item))
        if item in self.inventory:
            if item in self.equipped:
                self.equipped.remove(item)
            self.inventory.remove(item)

    def equip_item(self, item):
        self.logger.debug("Arguments: item: %s", str(item))
        if not isinstance(item, Equipment):
            raise ItemNotEquipableException()
        if item not in self.inventory:
            raise ItemNotInInventoryException()
        self.equipped.add(item)

    def unequip_item(self, item):
        self.logger.debug("Arguments: item: %s", str(item))
        if item in self.equipped:
            self.equipped.remove(item)

    def _check_item_type(self, item):
        self.logger.debug("Arguments: item: %s", str(item))
        # This function should be implented for each game_system to check to make sure the items being added to the
        # inventory are of the correct type for the game_system.  If the item is of the wrong type, a
        # 'GameSystemMismatchException' should be raised.
        raise NotImplementedError()

    def get_basic_stat(self, stat_name):
        self.logger.debug("Arguments: stat_name: %s", str(stat_name))
        if stat_name not in self.basic_stats_types:
            raise CharacterInvalidStatTypeException()
        # Calculate the total strength for the character
        result = self.basic_stats[stat_name]
        self.logger.debug("base: %s", result)
        # Add mod_ stat_name for equipped items
        for tmp_item in self.equipped:
            result = result + getattr(tmp_item, "mod_{}".format(stat_name), 0)
        self.logger.debug("base+equip: %s", result)
        # Add mod_ stat_name for temporaries (magic spells, etc)
        for tmp_effect in self.effects:
            result = result + getattr(tmp_effect, "mod_{}".format(stat_name), 0)
        self.logger.debug("base+equip+effect: %s", result)
        return result
