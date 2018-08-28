#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###
TEST_ITEM_LIST = [
  {"game_system": "shadowrun", "object_type": "item", "data": {"item_name": "Generic SR Item Two", "cost_money": 567}}
]

### FUNCTIONS ###

### CLASSES ###
class TestItemCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_none(self):
        self.logger.debug("test_create_none")
        item = game_system.none.Item({"item_name": "Generic Item One", "cost_money": 111})
        self.logger.debug("Item: %s", item)
        self.assertEqual(item.item_name, "Generic Item One")

    #def test_create_data(self):
    #    self.logger.debug("test_create_data")
    #    item = game_system.Item(self.item_data)
    #    self.logger.debug("Item: %s", item)
    #    self.assertEqual(item.item_name, "Test Item One")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
