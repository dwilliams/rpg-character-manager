#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    # pylint: disable=too-few-public-methods
    game_system = 'none'

    def __init__(self, data):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_name = 'Generic Item'
        if data is not None:
            self._morph(data)

    def _morph(self, data):
        # pylint: disable=unused-argument,no-self-use
        NotImplementedError()

    def __str__(self):
        return "Item: {}".format(self.item_name)

class ItemFactory:
    game_system = 'none'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_dict = {}
        self._load_data()

    def _load_data(self):
        raise NotImplementedError()

    def create(self, item_name):
        raise NotImplementedError()

    def get_list_names(self):
        return self.item_dict.keys()
