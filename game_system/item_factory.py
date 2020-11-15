#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.exceptions import InvalidGameSystemException, InvalidObjectTypeException, ItemNotExistsException

from game_system.none import Item
from game_system.adnd import ADNDItem
from game_system.shadowrun import ShadowRunItem

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ItemFactory:
    creation_classes = {
        "none": Item,
        "adnd": ADNDItem,
        "shadowrun": ShadowRunItem
    }
    object_type = 'item'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_dict = {}
        for tmp_key in self.creation_classes:
            self.item_dict[tmp_key] = {}

    def load_object_data(self, data):
        self.logger.debug("Start - data: %s", data)
        # Check if correct type of object
        if not data['object_type'] == self.object_type:
            raise InvalidObjectTypeException()
        if data['game_system'] not in self.creation_classes.keys():
            raise InvalidGameSystemException()
        self.logger.debug("game_system: %s, item_name: %s", data['game_system'], data['data']['item_name'])
        self.item_dict[data['game_system']][data['data']['item_name']] = data['data']

    def create(self, game_system, item_name):
        self.logger.debug("Start - game_system: %s, item_name: %s", game_system, item_name)
        # Make sure game_system is in list of available game systems
        if game_system not in self.creation_classes.keys():
            raise InvalidGameSystemException()
        # Make sure item name is in list of available items
        if item_name not in self.item_dict[game_system].keys():
            raise ItemNotExistsException()
        # Create and return the item object
        return self.creation_classes[game_system](self.item_dict[game_system][item_name])

    def get_list_names(self, game_system):
        self.logger.debug("Start - game_system: %s", game_system)
        # Make sure game_system is in list of available game systems
        if game_system not in self.creation_classes.keys():
            raise InvalidGameSystemException()
        self.logger.debug("item_dict keys: %s", self.item_dict.keys())
        self.logger.debug("item_dict[%s] keys: %s", game_system, self.item_dict[game_system].keys())
        return list(self.item_dict[game_system].keys())
