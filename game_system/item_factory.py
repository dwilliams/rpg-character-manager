#!/usr/bin/env python3

### IMPORTS ###
import logging
import json

from game_system.exceptions import ItemNotExistsException

from game_system.none import Item
from game_system.shadowrun import ShadowRunItem

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ItemFactory:
    #game_system = 'none'
    #resource_package = __name__
    #resource_path = None
    creation_classes = {
        "none": Item,
        "shadowrun": ShadowRunItem
    }

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_dict = {
            "none": {},
            "shadowrun": {},
        }

    def load_object_data(self, data):
        self.logger.debug("load_object_data start - data: %s", data)

    # def _load_data_json(self, json_string):
        # self.logger.debug("json_string: %s", json_string)
        # tmp_data = json.loads(json_string)
        # self.logger.debug("tmp_data: %s", tmp_data)
        # self.item_dict = {}
        # for tmp_item in tmp_data:
            # self.item_dict[tmp_item['item_name']] = tmp_item
        # self.logger.debug("self.item_dict: %s", self.item_dict)

    def create(self, item_name):
        if item_name not in self.item_dict.keys():
            raise ItemNotExistsException()
        return self.creation_class(self.item_dict[item_name])

    def get_list_names(self):
        return self.item_dict.keys()
