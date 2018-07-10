#!/usr/bin/env python3

### IMPORTS ###
#import logging

from game_system import Item, ItemFactory

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunItem(Item):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()

    def __str__(self):
        return "ShadowRunItem: ".format(self.item_name)

class ShadowRunItemFactory(Item):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()

    def create(self, item_name):
        # Figure out how to create the item
        return ShadowRunItem()
