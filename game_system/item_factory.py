#!/usr/bin/env python3

### IMPORTS ###
import logging
import json

from game_system.exceptions import InvalidGameSystemException, InvalidObjectTypeException, ItemNotExistsException

from game_system.none import Item
from game_system.shadowrun import ShadowRunItem

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ItemFactory:
    creation_classes = {
        "none": Item,
        "shadowrun": ShadowRunItem
    }
    object_type = 'item'

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_dict = {}
        for tmp_key in self.creation_classes.keys():
            self.item_dict[tmp_key] = {}

    def load_object_data(self, data):
        self.logger.debug("Start - data: %s", data)
        # Check if correct type of object
        if not data['object_type'] == self.object_type:
            raise InvalidObjectTypeException()
        if data['game_system'] not in self.creation_classes.keys():
            raise InvalidGameSystemException()
        self.item_dict[data['game_system']][data['data']['item_name']] = data['data']

    # def _load_data_json(self, json_string):
        # self.logger.debug("json_string: %s", json_string)
        # tmp_data = json.loads(json_string)
        # self.logger.debug("tmp_data: %s", tmp_data)
        # self.item_dict = {}
        # for tmp_item in tmp_data:
            # self.item_dict[tmp_item['item_name']] = tmp_item
        # self.logger.debug("self.item_dict: %s", self.item_dict)

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

    def get_list_names(self):
        return self.item_dict.keys()
