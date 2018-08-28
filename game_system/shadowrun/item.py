#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Item

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunItem(Item):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'

    mod_types = []
    cost_types = ['cost_money']

    def __str__(self):
        return "ShadowRunItem: {}".format(self.item_name)
