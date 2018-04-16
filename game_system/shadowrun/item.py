#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system import Item

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunItem(Item):
    game_system = 'shadowrun'
    item_name = 'Generic Item'

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
