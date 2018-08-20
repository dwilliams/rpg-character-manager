#!/usr/bin/env python3

### IMPORTS ###
import json
import logging
import os

from game_system.exceptions import BadFactoryTypeException
from game_system.item import ItemFactory
from game_system.equipment import ItemEquipment

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ObjectLoader:
    """
    This class loads game objects from data files into the proper factories for use by the game system.
    """
    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Save the file path
        self.filepath = None
        self.itemFactory = None
        self.equipmentFactory = None # FIXME: Do I use separate Item and Equipment factories, or an equipable flag?

    def register_item_factory(self, factory):
        self.logger.debug("register_item_factory start - factory: %s", factory)
        if not isinstance(factory, ItemFactory):
            raise BadFactoryTypeException()
        self.itemFactory = factory

    def register_equipement_factory(self, factory):
        self.logger.debug("register_equipement_factory start - factory: %s", factory)
        if not isinstance(factory, EquipmentFactory):
            raise BadFactoryTypeException()
        self.equipmentFactory = factory

    def load_from_directory(self, path):
        self.logger.debug("load_from_directory start - path: %s", path)
        # Walk the path for .json files, calling the load_from_file method for each one

    def load_from_file(self, path):
        self.logger.debug("load_from_file start - path: %s", path)
        # Check for .json extension
        # Load JSON in to memory
        # Walk list of objects, sending each to the proper factory
