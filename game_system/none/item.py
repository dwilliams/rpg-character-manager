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
        raise NotImplementedError()

    def __str__(self):
        return "Item: {}".format(self.item_name)
