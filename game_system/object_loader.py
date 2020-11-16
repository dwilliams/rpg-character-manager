#!/usr/bin/env python3

### IMPORTS ###
import json
import logging
import os

from game_system.exceptions import BadFactoryTypeException, InvalidGameSystemException, InvalidObjectTypeException
from game_system.factories.item_factory import ItemFactory
from game_system.factories.equipment_factory import EquipmentFactory
from game_system.factories.weapon_factory import WeaponFactory

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
        self.item_factory = None
        self.equipment_factory = None
        self.weapon_factory = None

    def register_item_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, ItemFactory):
            raise BadFactoryTypeException()
        self.item_factory = factory

    def register_equipment_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, EquipmentFactory):
            raise BadFactoryTypeException()
        self.equipment_factory = factory

    def register_weapon_factory(self, factory):
        self.logger.debug("Start - factory: %s", factory)
        if not isinstance(factory, WeaponFactory):
            raise BadFactoryTypeException()
        self.weapon_factory = factory

    def load_from_directory(self, path):
        self.logger.debug("Start - path: %s", path)
        self.logger.debug("abs_path: %s", os.path.abspath(path))
        # Walk the path for .json files, calling the load_from_file method for each one
        for root, dirs, files in os.walk(os.path.abspath(path)):
            self.logger.debug("root: %s, dirs: %s, files: %s", root, dirs, files)
            for tmp_file in files:
                self.load_from_file(os.path.join(root, tmp_file))

    def load_from_file(self, path):
        self.logger.debug("Start - path: %s", path)
        self.logger.debug("abs_path: %s", os.path.abspath(path))
        # Load JSON in to memory
        with open(os.path.abspath(path)) as tmp_file:
            tmp_data = json.load(tmp_file)
        # Walk list of objects from the json file, sending each to the proper factory
        for tmp_object in tmp_data:
            self.logger.debug("Object from JSON: %s", tmp_object)
            try:
                if tmp_object['object_type'] == "item":
                    self.item_factory.load_object_data(tmp_object)
                elif tmp_object['object_type'] == "equipment":
                    self.equipment_factory.load_object_data(tmp_object)
                elif tmp_object['object_type'] == "weapon":
                    self.weapon_factory.load_object_data(tmp_object)
            except InvalidObjectTypeException:
                self.logger.warning("Attempted to load bad object: %s", tmp_object)
            except InvalidGameSystemException:
                self.logger.warning("Attempted to load bad object: %s", tmp_object)
