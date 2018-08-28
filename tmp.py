#!/usr/bin/env python3

### IMPORTS ###
import logging
import os

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    # Initialize the Game System Factories
    gs_item_factory = game_system.ItemFactory()
    gs_equipment_factory = game_system.EquipmentFactory()
    gs_object_loader = game_system.ObjectLoader()
    gs_object_loader.register_item_factory(gs_item_factory)
    gs_object_loader.register_equipment_factory(gs_equipment_factory)
    gs_object_loader.load_from_directory("./data")

    # Create an object from the factory
    item_one = gs_item_factory.create("none", "Generic Item One")

    # Check the item
    logging.info("item cost: %d", item_one.get_cost('cost_money'))

    # Create a character
    char_one = game_system.none.Character()
    char_one.name = "Test Char One"
    char_one.add_to_inventory(item_one)

    # Check the character
    logging.info("character: %s", char_one)

    # Print the character save output
    logging.debug("character save: %s", char_one.save_dict())

if __name__ == '__main__':
    main()
