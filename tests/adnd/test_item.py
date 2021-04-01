#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestADNDItemCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_adnd(self):
        self.logger.debug("test_create_none")
        item = game_system.adnd.ADNDItem({"item_name": "Generic ADND Item One", "cost_money": {"value": 111}})
        self.logger.debug("ADNDItem: %s", item)
        self.assertEqual(item.get_name(), "Generic ADND Item One")
        self.assertEqual(str(item), "ADNDItem: Generic ADND Item One")

class TestADNDItemStats(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.item_adnd_data = {"item_name": "Generic ADND Item One", "cost_money": {"value": 303}}
        self.item_adnd = game_system.adnd.ADNDItem(self.item_adnd_data)

    def test_costs_none(self):
        self.logger.debug("test_costs_none")
        for tmp_cost in game_system.none.Item.cost_types:
            if tmp_cost in self.item_adnd_data:
                self.logger.debug("tmp_cost: %s, equip value: %s, data value: %s", tmp_cost, self.item_adnd.get_cost(tmp_cost).get_value(), self.item_adnd_data[tmp_cost]['value'])
                self.assertEqual(self.item_adnd.get_cost(tmp_cost).get_value(), self.item_adnd_data[tmp_cost]['value'])
            else:
                self.logger.debug("tmp_cost: %s, equip value: %s, 0", tmp_cost, self.item_adnd.get_cost(tmp_cost).get_value())
                self.assertEqual(self.item_adnd.get_cost(tmp_cost).get_value(), 0)

    def test_bad_cost_none(self):
        self.logger.debug("test_bad_cost_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.item_adnd.get_cost("bad_cost")

    def test_mods_none(self):
        self.logger.debug("test_mods_none")
        for tmp_mod in game_system.none.Item.mod_types:
            if tmp_mod in self.item_adnd_data:
                self.logger.debug("tmp_mod: %s, equip value: %s, data value: %s", tmp_mod, self.item_adnd.get_mod(tmp_mod).get_value(), self.item_adnd_data[tmp_mod]['value'])
                self.assertEqual(self.item_adnd.get_mod(tmp_mod).get_value(), self.item_adnd_data[tmp_mod]['value'])
            else:
                self.logger.debug("tmp_mod: %s, equip value: %s, 0", tmp_mod, self.item_adnd.get_mod(tmp_mod).get_value())
                self.assertEqual(self.item_adnd.get_mod(tmp_mod).get_value(), 0)

    def test_bad_mod_none(self):
        self.logger.debug("test_bad_mod_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.item_adnd.get_mod("bad_mod")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
