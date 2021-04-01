#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.exceptions import InvalidItemAttributeException
from game_system.modifierdata import ModifierData, CombineMethod

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    game_system = 'none'

    mod_types = []
    cost_types = ['cost_money']

    def __init__(self, data = None):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_name = 'Generic Item'
        for tmp_mod in self.mod_types:
            setattr(self, tmp_mod, ModifierData(0, CombineMethod.ADD))
        for tmp_cost in self.cost_types:
            setattr(self, tmp_cost, ModifierData(0, CombineMethod.ADD))
        if data is not None:
            self._morph(data)

    def __str__(self):
        return "Item: {}".format(self.item_name)

    def _morph(self, data):
        self.logger.debug("Start - data: %s", data)
        for tmp_mod in self.mod_types:
            if tmp_mod in data.keys():
                tmp_md = ModifierData(data[tmp_mod]['value'])
                if 'combine_method' in data[tmp_mod]:
                    tmp_md.set_combine_method_str(data[tmp_mod]['combine_method'])
                setattr(self, tmp_mod, tmp_md)
                self.logger.debug("Set attribute %s to %s", tmp_mod, tmp_md)
        self.item_name = data['item_name']
        for tmp_cost in self.cost_types:
            if tmp_cost in data.keys():
                tmp_md = ModifierData(data[tmp_cost]['value'])
                if 'combine_method' in data[tmp_cost]:
                    tmp_md.set_combine_method_str(data[tmp_cost]['combine_method'])
                setattr(self, tmp_cost, tmp_md)
                self.logger.debug("Set attribute %s to %s", tmp_cost, tmp_md)

    def get_name(self):
        self.logger.debug('Start - None')
        return self.item_name

    def get_mod(self, mod_type):
        self.logger.debug("Start - mod_type: %s", mod_type)
        if mod_type not in self.mod_types:
            raise InvalidItemAttributeException()
        tmp_md = getattr(self, mod_type, ModifierData(0))
        self.logger.debug("Return: %s", tmp_md)
        return tmp_md

    def get_cost(self, cost_type):
        self.logger.debug("Start - cost_type: %s", cost_type)
        if cost_type not in self.cost_types:
            raise InvalidItemAttributeException()
        tmp_md = getattr(self, cost_type, ModifierData(0))
        self.logger.debug("Return: %s", tmp_md)
        return tmp_md
