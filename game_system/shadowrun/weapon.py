#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Weapon

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunWeapon(Weapon):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'

    mod_types = []
    cost_types = ['cost_money']

    def __str__(self):
        return "ShadowRunWeapon: {}".format(self.item_name)
