#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    game_system = 'none'
    item_name = 'Generic Item'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

    def __str__(self):
        return "Item: {}".format(self.item_name)

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
