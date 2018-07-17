#!/usr/bin/env python3

### IMPORTS ###
import logging
import json
import pkg_resources

from game_system.exceptions import ItemNotExistsException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Item:
    # pylint: disable=too-few-public-methods
    game_system = 'none'

    def __init__(self, data):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_name = 'Generic Item'
        if data is not None:
            self._morph(data)

    def _morph(self, data):
        # pylint: disable=unused-argument,no-self-use
        raise NotImplementedError()

    def __str__(self):
        return "Item: {}".format(self.item_name)

class ItemFactory:
    game_system = 'none'
    resource_package = __name__
    resource_path = None
    creation_class = Item

    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")
        self.item_dict = {}
        self._load_data()

    def _load_data(self):
        self.logger.debug("resource_package: %s", self.resource_package)
        self.logger.debug("resource_path: %s", self.resource_path)
        if self.resource_path is not None:
            json_string = pkg_resources.resource_string(self.resource_package, self.resource_path)
            self.logger.debug("json_string: %s", json_string)
            self._load_data_json(json_string)

    def _load_data_json(self, json_string):
        self.logger.debug("json_string: %s", json_string)
        tmp_data = json.loads(json_string)
        self.logger.debug("tmp_data: %s", tmp_data)
        self.item_dict = {}
        for tmp_item in tmp_data:
            self.item_dict[tmp_item['item_name']] = tmp_item
        self.logger.debug("self.item_dict: %s", self.item_dict)

    def create(self, item_name):
        if item_name not in self.item_dict.keys():
            raise ItemNotExistsException()
        return self.creation_class(self.item_dict[item_name])

    def get_list_names(self):
        return self.item_dict.keys()
