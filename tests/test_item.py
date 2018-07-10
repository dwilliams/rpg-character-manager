#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestItemCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Test item data for the item class
        self.item_data = {
            "item_name": "Test Item One"
        }

    def test_create_none(self):
        self.logger.debug("test_create_none")
        item = game_system.Item(None)
        self.logger.debug("Item: %s", item)
        self.assertEqual(item.item_name, 'Generic Item')

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
