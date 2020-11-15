#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Weapon

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDWeapon(Weapon):
    # pylint: disable=too-few-public-methods
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'adnd'

    mod_types = []
    cost_types = ['cost_money']
    stat_types = ['stat_weight', 'stat_type', 'stat_size', 'stat_speed', 'stat_damage_sm', 'stat_damage_l', 'stat_range']

    def __str__(self):
        return "ADNDWeapon: {}".format(self.item_name)
