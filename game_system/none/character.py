#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.none.equipment import Equipment
from game_system.none.item import Item
from game_system.none.weapon import Weapon

from game_system.exceptions import InvalidCharacterStatTypeException
from game_system.exceptions import GameSystemMismatchException
from game_system.exceptions import ItemNotEquipableException
from game_system.exceptions import ItemNotInInventoryException
from game_system.exceptions import NotCharacterException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Character:
    game_system = 'none'

    class_equipment = Equipment
    class_item = Item
    class_weapon = Weapon

    basic_stats_types = ['strength', 'charisma', 'intelligence', 'wisdom']
    special_stats_types = ['magic']

    def __init__(self, name = "New Character"):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Some basic values about the character
        self.name = name
        self.age = 1

        # Race
        # NOTE: Seeing as racial attributes in most game system have an effect on the character, this should be a set of
        #       classes, similar to equipment.  This will be added later.
        #self.race = race

        # Categories of things
        self.inventory = set()
        self.active_equipment = set()
        self.active_weapons = set()
        self.effects = set() # Effects from spells, etc.  Have burn down time (might be inf).

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

    def _check_item_type(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if not isinstance(item, self.class_item):
            raise GameSystemMismatchException()

    def load_dict(self, char_dict):
        self.logger.debug("Start - char_dict: %s", str(char_dict))

        # Check the object format and game_system
        if not char_dict['game_system'] == self.game_system:
            raise GameSystemMismatchException()
        if not char_dict['object_type'] == 'character':
            raise NotCharacterException()

        # Load the basic character stats
        self.name = char_dict['data']['name']

        for stats_type in self.basic_stats_types:
            if stats_type in char_dict['data']['basic_stats']:
                self.basic_stats[stats_type] = char_dict['data']['basic_stats'][stats_type]

        for stats_type in self.special_stats_types:
            if stats_type in char_dict['data']['special_stats']:
                self.special_stats[stats_type] = char_dict['data']['special_stats'][stats_type]

        # Load the inventory & equipment

    def save_dict(self):
        self.logger.debug("Start - None")
        char_dict = {}

        # Save the object format
        char_dict['game_system'] = self.game_system
        char_dict['object_type'] = 'character'
        char_dict['data'] = {}

        # Save the basic character format
        char_dict['data']['name'] = self.name

        char_dict['data']['basic_stats'] = {}
        for stats_type in self.basic_stats_types:
            char_dict['data']['basic_stats'][stats_type] = self.basic_stats[stats_type]

        char_dict['data']['special_stats'] = {}
        for stats_type in self.special_stats_types:
            char_dict['data']['special_stats'][stats_type] = self.special_stats[stats_type]

        # Save the inventory & equipment
        char_dict['data']['inventory'] = []
        for tmp_item in self.inventory:
            char_dict['data']['inventory'].append(tmp_item.get_name())

        char_dict['data']['equipped'] = []
        for tmp_item in self.equipped:
            char_dict['data']['equipped'].append(tmp_item.get_name())

        return char_dict

    def add_to_inventory(self, item):
        self.logger.debug("Start - item: %s", str(item))
        self._check_item_type(item)
        self.inventory.add(item)

    def remove_from_inventory(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if item not in self.inventory:
            raise ItemNotInInventoryException()
        if item in self.active_equipment:
            self.active_equipment.remove(item)
        if item in self.active_weapons:
            self.active_weapons.remove(item)
        self.inventory.remove(item)

    def equip_equipment(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if not isinstance(item, self.class_equipment):
            raise ItemNotEquipableException()
        if item not in self.inventory:
            raise ItemNotInInventoryException()
        self.active_equipment.add(item)

    def unequip_equipment(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if item in self.active_equipment:
            self.active_equipment.remove(item)

    def get_equipment(self):
        return self.active_equipment

    def equip_weapon(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if not isinstance(item, self.class_weapon):
            raise ItemNotEquipableException()
        if item not in self.inventory:
            raise ItemNotInInventoryException()
        self.active_weapons.add(item)

    def unequip_weapon(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if item in self.active_weapons:
            self.active_weapons.remove(item)

    def get_weapons(self):
        return self.active_weapons

    def get_basic_stat(self, stat_name):
        self.logger.debug("Start - stat_name: %s", str(stat_name))
        if stat_name not in self.basic_stats_types:
            raise InvalidCharacterStatTypeException()
        ## Calculate the total stat for the character
        # Grab the base stat for the character
        result = self.basic_stats[stat_name]
        self.logger.debug("base: %s", result)
        # Add mod_ stat_name for equipped items
        for tmp_item in self.equipped:
            result = result + tmp_item.get_mod("mod_{}".format(stat_name))
        self.logger.debug("base+equip: %s", result)
        # Add mod_ stat_name for temporaries (magic spells, etc)
        for tmp_effect in self.effects:
            result = result + tmp_effect.get_mod("mod_{}".format(stat_name))
        self.logger.debug("base+equip+effect: %s", result)
        return result

    def get_special_stat(self, stat_name):
        self.logger.debug("Start - stat_name: %s", str(stat_name))
        if stat_name not in self.special_stats_types:
            raise InvalidCharacterStatTypeException()
        ## Calculate the total stat for the character
        # Grab the base stat for the character
        result = self.special_stats[stat_name]
        self.logger.debug("base: %s", result)
        # Add mod_ stat_name for equipped items
        for tmp_item in self.equipped:
            result = result + tmp_item.get_mod("mod_{}".format(stat_name))
        self.logger.debug("base+equip: %s", result)
        # Add mod_ stat_name for temporaries (magic spells, etc)
        for tmp_effect in self.effects:
            result = result + tmp_effect.get_mod("mod_{}".format(stat_name))
        self.logger.debug("base+equip+effect: %s", result)
        return result

    def get_calcd_stat(self, stat_name):
        self.logger.debug("Start - stat_name: %s", str(stat_name))
        raise InvalidCharacterStatTypeException()
