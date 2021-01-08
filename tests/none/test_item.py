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

class TestItemStats(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.item_none_data = {"item_name": "Generic Item One", "cost_money": 303}
        self.item_none = game_system.none.Item(self.item_none_data)

    def test_costs_none(self):
        self.logger.debug("test_costs_none")
        for tmp_cost in game_system.none.Item.cost_types:
            if tmp_cost in self.item_none_data:
                self.logger.debug("tmp_cost: %s, equip value: %s, data value: %s", tmp_cost, self.item_none.get_cost(tmp_cost), self.item_none_data[tmp_cost])
                self.assertEqual(self.item_none.get_cost(tmp_cost), self.item_none_data[tmp_cost])
            else:
                self.logger.debug("tmp_cost: %s, equip value: %s, 0", tmp_cost, self.item_none.get_cost(tmp_cost))
                self.assertEqual(self.item_none.get_cost(tmp_cost), 0)

    def test_bad_cost_none(self):
        self.logger.debug("test_bad_cost_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.item_none.get_cost("bad_cost")

    def test_mods_none(self):
        self.logger.debug("test_mods_none")
        for tmp_mod in game_system.none.Item.mod_types:
            if tmp_mod in self.item_none_data:
                self.logger.debug("tmp_mod: %s, equip value: %s, data value: %s", tmp_mod, self.item_none.get_mod(tmp_mod), self.item_none_data[tmp_mod])
                self.assertEqual(self.item_none.get_mod(tmp_mod), self.item_none_data[tmp_mod])
            else:
                self.logger.debug("tmp_mod: %s, equip value: %s, 0", tmp_mod, self.item_none.get_mod(tmp_mod))
                self.assertEqual(self.item_none.get_mod(tmp_mod), 0)

    def test_bad_mod_none(self):
        self.logger.debug("test_bad_mod_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.item_none.get_mod("bad_mod")
