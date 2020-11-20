#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import math
import os

import game_system
import game_system.adnd

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    # Load Objects and Prime Factories
    gs_item_factory = game_system.factories.ItemFactory()
    gs_equipment_factory = game_system.factories.EquipmentFactory()
    gs_weapon_factory = game_system.factories.WeaponFactory()
    gs_object_loader = game_system.ObjectLoader()
    gs_object_loader.register_item_factory(gs_item_factory)
    gs_object_loader.register_equipment_factory(gs_equipment_factory)
    gs_object_loader.register_weapon_factory(gs_weapon_factory)
    gs_object_loader.load_from_directory("data_ignore") # FIXME: Convert to argparse?

    # Create the character from the json file
    logging.debug("Creating a simple character from a file")
    charfile = game_system.CharacterFile()
    charfile.register_item_factory(gs_item_factory)
    charfile.register_equipment_factory(gs_equipment_factory)
    charfile.register_weapon_factory(gs_weapon_factory)
    #char_ten = game_system.adnd.ADNDCharacter()
    char_ten = charfile.load_char('tack_pdf_char2.json')

    logging.debug("Creating PDF class")
    pdf_gen = game_system.adnd.ADNDPDFGen(char_ten)

    logging.debug("Outputing PDF file")
    pdf_gen.output_file('test.pdf')

if __name__ == '__main__':
    main()
