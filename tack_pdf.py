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
    # Parse Arguments
    parser = argparse.ArgumentParser(description = "Scan and hash files on media, then push into the database.")
    parser.add_argument("-v", "--verbose", action = "store_true") # Use this for debug logging later
    parser.add_argument("--data_dir", help = "Specify the directory where the data JSON files exist.")
    parser.add_argument("char_file", help = "Path to the character to use for generating PDF.")
    args = parser.parse_args()

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
    gs_object_loader.load_from_directory(args.data_dir)

    # Create the character from the json file
    logging.debug("Creating a simple character from a file")
    charfile = game_system.CharacterFile()
    charfile.register_item_factory(gs_item_factory)
    charfile.register_equipment_factory(gs_equipment_factory)
    charfile.register_weapon_factory(gs_weapon_factory)
    char_ten = charfile.load_char(args.char_file)

    logging.debug("Creating PDF class")
    # FIXME: Make this work for all game_systems
    pdf_gen = game_system.adnd.ADNDPDFGen(char_ten)

    logging.debug("Outputing PDF file")
    pdf_gen.output_file("{}.pdf".format(os.path.splitext(args.char_file)[0]))

if __name__ == '__main__':
    main()
