#!/usr/bin/env python3

### IMPORTS ###
from game_system.none.item import Item

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Equipment(Item):
    # pylint: disable=too-few-public-methods
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'none'

    mod_types = ['mod_strength', 'mod_charisma', 'mod_intelligence', 'mod_wisdom']
    cost_types = ['cost_money']

    def __init__(self, data=None):
        # Ensure the parent's __init__ is called
        super().__init__(None)
        self.item_name = 'Generic Equipment'
        if data is not None:
            self._morph(data)

    def __str__(self):
        return "Equipment: {}".format(self.item_name)
