#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Weapon

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDWeapon(Weapon):
    # pylint: disable=too-few-public-methods
    game_system = 'adnd'

    # FIXME: How should magical plusses be handled?  Should it be split among stats, modifiers, or be a new stat?
    mod_types = []
    cost_types = ['cost_money']
    stat_types = [
        'stat_weight',
        'stat_type',
        'stat_size',
        'stat_speed',
        'stat_damage_sm',
        'stat_damage_l',
        'stat_range',
        'stat_to_hit_adjust',
        'stat_proficiency_type'
    ]


    def __str__(self):
        return "ADNDWeapon: {}".format(self.item_name)
