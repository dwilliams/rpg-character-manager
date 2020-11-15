#!/usr/bin/env python3

### IMPORTS ###
from game_system.none.item import Item

from game_system.exceptions import InvalidItemAttributeException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Weapon(Item):
    # pylint: disable=too-few-public-methods
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'none'

    mod_types = []
    cost_types = ['cost_money']
    stat_types = ['stat_damage']

    def __init__(self, data=None):
        # Ensure the parent's __init__ is called
        super().__init__(None)
        self.item_name = 'Generic Weapon'
        for tmp_stat in self.stat_types:
            setattr(self, tmp_stat, 0)
        if data is not None:
            self._morph(data)

    def __str__(self):
        return "Weapon: {}".format(self.item_name)

    def _morph(self, data):
        self.logger.debug("Start - data: %s", data)
        # Ensure the parent's _morph is called
        super()._morph(data)
        # Handle types unique to weapons
        for tmp_stat in self.stat_types:
            if tmp_stat in data.keys():
                setattr(self, tmp_stat, data[tmp_stat])
                self.logger.debug("Set attribute %s to %s", tmp_stat, data[tmp_stat])

    def get_stat(self, stat_type):
        self.logger.debug("Start - stat_type: %s", stat_type)
        if stat_type not in self.stat_types:
            raise InvalidItemAttributeException()
        self.logger.debug("Return: %s", getattr(self, stat_type, 0))
        return getattr(self, stat_type, 0)
