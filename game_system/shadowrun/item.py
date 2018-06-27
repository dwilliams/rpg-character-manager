#!/usr/bin/env python3

### IMPORTS ###
#import logging

from game_system import Item

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunItem(Item):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'
    item_name = 'Generic Item'

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()

    def __str__(self):
        return "ShadowRun{}".format(super().__str__())
