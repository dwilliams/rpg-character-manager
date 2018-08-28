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
        self.assertEqual(item.get_name(), "Generic Item One")
        self.assertEqual(str(item), "Item: Generic Item One")

    def test_create_shadowrun(self):
        self.logger.debug("test_create_shadowrun")
        item = game_system.shadowrun.ShadowRunItem({"item_name": "Generic SR Item Two", "cost_money": 567})
        self.logger.debug("ShadowRunItem: %s", item)
        self.assertEqual(item.get_name(), "Generic SR Item Two")
        self.assertEqual(str(item), "ShadowRunItem: Generic SR Item Two")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
