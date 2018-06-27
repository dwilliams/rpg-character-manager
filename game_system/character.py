#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.equipment import Equipment

from game_system.exceptions import ItemNotEquipableException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Character:
    game_system = 'none'

    basic_stats_types = ['strength', 'charisma', 'intelligence', 'wisdom']
    special_stats_types = ['magic']

    def __init__(self, name = '', age = ''):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Some basic values about the character
        self.name = name
        self.age = age
        #self.race = race # FIXME: Should this be a string or a set of classes that can affect stats?

        # Categories of things
        # FIXME: Should these be objects or basic data structures for storing items and equipment?
        self.inventory = []
        self.equipped = []

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
        raise NotImplementedError()

    def save_dict(self):
        raise NotImplementedError()

    def add_to_inventory(self, item):
        self._check_item_type(item)
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.equipped:
            # FIXME: Should this raise an exception or just remove from equipped?
            self.equipped.remove(item)
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_item(self, item):
        if not isinstance(item, Equipment):
            raise ItemNotEquipableException()
        # FIXME: Should this raise exceptions for all invalid attempts (e.g. if item not in inventory)?
        if item in self.inventory and item not in self.equipped:
            self.equipped.append(item)

    def unequip_item(self, item):
        if item in self.equipped:
            self.equipped.remove(item)

    def _check_item_type(self, item):
        # This function should be implented for each game_system to check to make sure the items being added to the
        # inventory are of the correct type for the game_system.  If the item is of the wrong type, a
        # 'GameSystemMismatchException' should be raised.
        raise NotImplementedError()

    def get_basic_stat(self, stat_name):
        if stat_name not in self.basic_stats_types:
            raise CharacterInvalidStatTypeException()
        # Calculate the total strength for the character
        result = self.basic_stats[stat_name]
        # Add strength for equipped items
        # ??
        # Add stat for game system specials
        result = result + self._get_basic_stat_game_system_specials(stat_name)
        # Add strength for temporaries (magic spells, etc)
        # ??
        return result

    def _get_basic_stat_game_system_specials(self, stat_name):
        # Override this for special modifiers for game systems (e.g. biowares in ShadowRun)
        return 0

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
