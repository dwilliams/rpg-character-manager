#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.none.equipment import Equipment
from game_system.none.item import Item
from game_system.none.weapon import Weapon

from game_system.exceptions import GameSystemMismatchException
from game_system.exceptions import ItemNotEquipableException
from game_system.exceptions import ItemNotInInventoryException
from game_system.exceptions import InvalidObjectTypeException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Inventory:
    def __init__(self, game_system, class_item, class_equipment, class_weapon):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.game_system = game_system
        self.class_item = class_item
        self.class_equipment = class_equipment
        self.class_weapon = class_weapon

        # Categories of things
        self.inventory = set()
        self.active_equipment = set()
        self.active_weapons = set()

    def load_dict(self, inv_dict, item_factory, equipment_factory, weapon_factory):
        # FIXME: Figure out how to load the data safely and efficiently
        for tmp_item_name in inv_dict['inventory']:
            if tmp_item_name in item_factory.get_list_names(self.game_system):
                self.add_item(item_factory.create(self.game_system, tmp_item_name))
            elif tmp_item_name in equipment_factory.get_list_names(self.game_system):
                tmp_equipment = equipment_factory.create(self.game_system, tmp_item_name)
                self.add_item(tmp_equipment)
                if tmp_item_name in inv_dict['active_equipment']:
                    self.equip_equipment(tmp_equipment)
            elif tmp_item_name in weapon_factory.get_list_names(self.game_system):
                tmp_weapon = weapon_factory.create(self.game_system, tmp_item_name)
                self.add_item(tmp_weapon)
                if tmp_item_name in inv_dict['active_weapons']:
                    self.equip_weapon(tmp_weapon)

    def save_dict(self):
        tmp_result = {}
        tmp_result['inventory'] = [item.item_name for item in self.inventory]
        tmp_result['active_equipment'] = [item.item_name for item in self.active_equipment]
        tmp_result['active_weapons'] = [item.item_name for item in self.active_weapons]
        return tmp_result

    # Items Methods
    def add_item(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if not isinstance(item, (self.class_item, self.class_equipment, self.class_weapon)):
            raise InvalidObjectTypeException()
        if item.game_system != self.class_item.game_system:
            raise GameSystemMismatchException()
        self.inventory.add(item)

    def remove_item(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if item not in self.inventory:
            raise ItemNotInInventoryException()
        if item in self.active_equipment:
            self.active_equipment.remove(item)
        if item in self.active_weapons:
            self.active_weapons.remove(item)
        self.inventory.remove(item)

    def get_items(self):
        self.logger.debug("Start")
        return list(self.inventory)

    def get_item_names(self):
        self.logger.debug("Start")
        self.logger.debug("Inventory Size: %d", len(self.inventory))
        tmp_result = [] # Prefer returning lists instead of sets.
        for item in self.inventory:
            # This de-duplicates the names
            if item.item_name not in tmp_result:
                tmp_result.append(item.item_name)
        self.logger.debug("Result Size: %d", len(tmp_result))
        return tmp_result

    def get_items_by_name(self, item_name):
        self.logger.debug("Start - item_name: %s", item_name)
        tmp_result = []
        for item in self.inventory:
            if item.item_name == item_name:
                tmp_result.append(item)
        self.logger.debug("Result Size: %d", len(tmp_result))
        return tmp_result

    # Equipment Methods
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
        self.logger.debug("Start")
        return list(self.active_equipment)

    def get_equipment_names(self):
        self.logger.debug("Start")
        self.logger.debug("Active Equipment Size: %d", len(self.active_equipment))
        tmp_result = []
        for item in self.active_equipment:
            # This de-duplicates the names
            if item.item_name not in tmp_result:
                tmp_result.append(item.item_name)
        self.logger.debug("Result Size: %d", len(tmp_result))
        return tmp_result

    # Weapon Methods
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
        self.logger.debug("Start")
        return list(self.active_weapons)

    def get_weapon_names(self):
        self.logger.debug("Start")
        self.logger.debug("Active Weapons Size: %d", len(self.active_weapons))
        tmp_result = []
        for item in self.active_weapons:
            # This de-duplicates the names
            if item.item_name not in tmp_result:
                tmp_result.append(item.item_name)
        self.logger.debug("Result Size: %d", len(tmp_result))
        return tmp_result