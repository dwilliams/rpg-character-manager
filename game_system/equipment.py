#!/usr/bin/env python3

### IMPORTS ###
#import logging

from game_system.item import Item, ItemFactory

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
        for tmp_mod in self.mod_types:
            setattr(self, tmp_mod, 0)
        for tmp_cost in self.cost_types:
            setattr(self, tmp_cost, 0)
        if data is not None:
            self._morph(data)

    def _morph(self, data):
        raise NotImplementedError()

    def __str__(self):
        return "Equipment: {}".format(self.item_name)

class EquipmentFactory(ItemFactory):
    # pylint: disable=abstract-method
    pass
    #game_system = 'none'

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()

    #def _load_data(self):
    #    raise NotImplementedError()

    #def create(self, item_name):
    #    raise NotImplementedError()

    #def get_list_names(self):
    #    raise NotImplementedError()
