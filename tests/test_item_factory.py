#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###
TEST_ITEM_LIST = [
  {"game_system": "none", "object_type": "item", "data": {"item_name": "Generic Item One", "cost_money": 111}},
  {"game_system": "none", "object_type": "item", "data": {"item_name": "Generic Item Two", "cost_money": 234}},
  {"game_system": "shadowrun", "object_type": "item", "data": {"item_name": "Generic SR Item Two", "cost_money": 567}}
]

### FUNCTIONS ###

### CLASSES ###
class TestItemFactoryDataLoad(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.test_item_names = {'none': [], 'shadowrun': []}
        for test_item_data in TEST_ITEM_LIST:
            self.test_item_names[test_item_data['game_system']].append(test_item_data['data']['item_name'])

    def test_create_factory_and_load_data(self):
        self.logger.debug("test_create_factory_and_load_data")
        item_factory = game_system.ItemFactory()
        for test_item_data in TEST_ITEM_LIST:
            item_factory.load_object_data(test_item_data)
        for tmp_game_system in self.test_item_names:
            tmp_names = item_factory.get_list_names(tmp_game_system)
            self.assertListEqual(tmp_names, self.test_item_names[tmp_game_system])

class TestItemFactoryItemCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.item_factory = game_system.ItemFactory()
        for test_item_data in TEST_ITEM_LIST:
            self.item_factory.load_object_data(test_item_data)

    def test_create_none(self):
        self.logger.debug("test_create_none")
        item = self.item_factory.create('none', "Generic Item One")
        self.logger.debug("Item: %s", item)
        self.assertIsInstance(item, game_system.none.Item)
        self.assertEqual(item.item_name, "Generic Item One")

    def test_create_shadowrun(self):
        self.logger.debug("test_create_shadowrun")
        item = self.item_factory.create('shadowrun', "Generic SR Item Two")
        self.logger.debug("Item: %s", item)
        self.assertIsInstance(item, game_system.shadowrun.ShadowRunItem)
        self.assertEqual(item.item_name, "Generic SR Item Two")

    def test_create_bad(self):
        self.logger.debug("test_create_bad")
        with self.assertRaises(game_system.exceptions.InvalidGameSystemException):
            item = self.item_factory.create('bad', "Generic Item One")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
