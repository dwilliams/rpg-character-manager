#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.equipment import Equipment

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunEquipment(Equipment):
    # FIXME: How are modifiers to the character handled?  Currently thinking of adding modifier_?? methods that the
    #        character class can call when calculating the attribute.  An example would be:
    #            def mod_strength(self):
    #                return 4
    #        This would be used to add 4 to the character's strength.  The values could be added to class or __init__,
    #        allowing value overrides and base class functions for access.
    game_system = 'shadowrun'
    item_name = 'Generic Equipment'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

    def __str__(self):
        return "ShadowRun{}".format(super().__str__())

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
