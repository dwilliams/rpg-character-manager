#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    # pylint: disable=too-few-public-methods
    game_system = 'none'
    item_name = 'Generic Item'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

    def __str__(self):
        return "Item: {}".format(self.item_name)
