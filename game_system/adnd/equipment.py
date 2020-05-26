#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Equipment

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDEquipment(Equipment):
    # pylint: disable=too-few-public-methods
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'adnd'

    mod_types = ['mod_strength', 'mod_dexterity', 'mod_constitution', 'mod_intelligence', 'mod_wisdom', 'mod_charisma']
    cost_types = ['cost_money']

    def __str__(self):
        return "ADNDEquipment: {}".format(self.item_name)
