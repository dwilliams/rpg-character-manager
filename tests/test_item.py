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

    def test_create(self):
        self.logger.debug("test_create")
        item = game_system.Item()
        self.logger.debug("Item: %s", item)
        self.assertEqual(item.item_name, 'Generic Item')

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
