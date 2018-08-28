#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.exceptions import InvalidItemAttributeException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    game_system = 'none'

    mod_types = []
    cost_types = ['cost_money']

    def __init__(self, data):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_name = 'Generic Item'
        for tmp_mod in self.mod_types:
            setattr(self, tmp_mod, 0)
        for tmp_cost in self.cost_types:
            setattr(self, tmp_cost, 0)
        if data is not None:
            self._morph(data)

    def __str__(self):
        return "Item: {}".format(self.item_name)

    def _morph(self, data):
        self.logger.debug("Start - data: %s", data)
        for tmp_mod in self.mod_types:
            if tmp_mod in data.keys():
                setattr(self, tmp_mod, data[tmp_mod])
                self.logger.debug("Set attribute %s to %s", tmp_mod, data[tmp_mod])
        self.item_name = data['item_name']
        for tmp_cost in self.cost_types:
            if tmp_cost in data.keys():
                setattr(self, tmp_cost, data[tmp_cost])
                self.logger.debug("Set attribute %s to %s", tmp_cost, data[tmp_cost])

    def get_mod(self, mod_type):
        self.logger.debug("Start - mod_type: %s", mod_type)
        if mod_type not in self.mod_types:
            raise InvalidItemAttributeException()
        self.logger.debug("Return: %d", getattr(self, mod_type, 0))
        return getattr(self, mod_type, 0)

    def get_cost(self, cost_type):
        self.logger.debug("Start - cost_type: %s", cost_type)
        if cost_type not in self.cost_types:
            raise InvalidItemAttributeException()
        self.logger.debug("Return: %d", getattr(self, cost_type, 0))
        return getattr(self, cost_type, 0)
