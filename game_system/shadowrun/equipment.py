#!/usr/bin/env python3

### IMPORTS ###
#import logging
import json

import pkg_resources

from game_system.exceptions import ItemNotExistsException

from game_system.equipment import Equipment, EquipmentFactory

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunEquipment(Equipment):
    # pylint: disable=too-few-public-methods
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'shadowrun'

    mod_types = ['mod_body', 'mod_quickness', 'mod_strength', 'mod_charisma', 'mod_intelligence', 'mod_willpower']
    cost_types = ['cost_money', 'cost_body', 'cost_essence']

    def _morph(self, data):
        # This should be a dictionary in the form:
        #{
        #  "item_name":"...",
        #  "mod_strength": #,
        #  ...
        #  "cost_money": #,
        #  ...
        #}
        self.item_name = data["item_name"]
        for tmp_mod in self.mod_types:
            if tmp_mod in data.keys():
                setattr(self, tmp_mod, data[tmp_mod])
                self.logger.debug("Set attribute %s to %s", tmp_mod, data[tmp_mod])
        for tmp_cost in self.cost_types:
            if tmp_cost in data.keys():
                setattr(self, tmp_cost, data[tmp_cost])
                self.logger.debug("Set attribute %s to %s", tmp_cost, data[tmp_cost])

    def __str__(self):
        return "ShadowRunEquipment: {}".format(self.item_name)

class ShadowRunEquipmentFactory(EquipmentFactory):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'
    resource_package = __name__
    resource_path = 'equipment.json'
    creation_class = ShadowRunEquipment

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()
    #    self._load_data()

    #def _load_data(self):
    #    self.logger.debug("resource_package: %s", self.resource_package)
    #    self.logger.debug("resource_path: %s", self.resource_path)
    #    json_string = pkg_resources.resource_string(self.resource_package, self.resource_path)
    #    self.logger.debug("json_string: %s", json_string)
    #    self._load_data_json(json_string)

    #def create(self, item_name):
    #    if item_name not in self.item_dict.keys():
    #        raise ItemNotExistsException()
    #    return self.creation_class(self.item_dict[item_name])
