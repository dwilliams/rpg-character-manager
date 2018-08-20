#!/usr/bin/env python3

### IMPORTS ###
#import logging
import json

import pkg_resources

from game_system.exceptions import ItemNotExistsException

from game_system.none import Item

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunItem(Item):
    # pylint: disable=too-few-public-methods
    game_system = 'shadowrun'

    #def __init__(self):
    #    # Ensure the parent's __init__ is called
    #    super().__init__()

    def __str__(self):
        return "ShadowRunItem: {}".format(self.item_name)

# class ShadowRunItemFactory(ItemFactory):
    # # pylint: disable=too-few-public-methods
    # game_system = 'shadowrun'
# 
    # #def __init__(self):
    # #    # Ensure the parent's __init__ is called
    # #    super().__init__()
# 
    # def _load_data(self):
        # resource_package = __name__
        # resource_path = 'items.json' #'/'.join(('shadowrun','items.json'))
        # self.logger.debug("resource_package: %s", resource_package)
        # self.logger.debug("resource_path: %s", resource_path)
        # json_string = pkg_resources.resource_string(resource_package, resource_path)
        # self.logger.debug("json_string: %s", json_string)
        # tmp_data = json.loads(json_string)
        # self.logger.debug("tmp_data: %s", tmp_data)
        # self.item_dict = {}
        # for tmp_item in tmp_data:
            # self.item_dict[tmp_item['item_name']] = tmp_item
        # self.logger.debug("self.item_dict: %s", self.item_dict)
# 
    # def create(self, item_name):
        # if item_name not in self.item_dict.keys():
            # raise ItemNotExistsException()
        # return ShadowRunItem(self.item_dict[item_name])
