#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestWeaponCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_none(self):
        self.logger.debug("test_create_none")
        weapon = game_system.none.Weapon({"item_name": "Generic Weapon One", "cost_money": {"value": 123}, "stat_damage": 1})
        self.logger.debug("Weapon: %s", weapon)
        self.assertEqual(weapon.get_name(), "Generic Weapon One")
        self.assertEqual(str(weapon), "Weapon: Generic Weapon One")

class TestWeaponStats(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.wpn_none_data = {"item_name": "Generic Weapon One", "cost_money": {"value": 123}, "stat_damage": 1}
        self.wpn_none = game_system.none.Weapon(self.wpn_none_data)

    def test_costs_none(self):
        self.logger.debug("test_costs_none")
        for tmp_cost in game_system.none.Weapon.cost_types:
            if tmp_cost in self.wpn_none_data:
                self.logger.debug("tmp_cost: %s, weapon value: %s, data value: %s", tmp_cost, self.wpn_none.get_cost(tmp_cost).get_value(), self.wpn_none_data[tmp_cost]['value'])
                self.assertEqual(self.wpn_none.get_cost(tmp_cost).get_value(), self.wpn_none_data[tmp_cost]['value'])
            else:
                self.logger.debug("tmp_cost: %s, weapon value: %s, 0", tmp_cost, self.wpn_none.get_cost(tmp_cost).get_value())
                self.assertEqual(self.wpn_none.get_cost(tmp_cost).get_value(), 0)

    def test_bad_cost_none(self):
        self.logger.debug("test_bad_cost_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_none.get_cost("bad_cost")

    def test_mods_none(self):
        self.logger.debug("test_mods_none")
        for tmp_mod in game_system.none.Weapon.mod_types:
            if tmp_mod in self.wpn_none_data:
                self.logger.debug("tmp_mod: %s, weapon value: %s, data value: %s", tmp_mod, self.wpn_none.get_mod(tmp_mod).get_value(), self.wpn_none_data[tmp_mod]['value'])
                self.assertEqual(self.wpn_none.get_mod(tmp_mod).get_value(), self.wpn_none_data[tmp_mod]['value'])
            else:
                self.logger.debug("tmp_mod: %s, weapon value: %s, 0", tmp_mod, self.wpn_none.get_mod(tmp_mod).get_value())
                self.assertEqual(self.wpn_none.get_mod(tmp_mod).get_value(), 0)

    def test_bad_mod_none(self):
        self.logger.debug("test_bad_mod_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_none.get_mod("bad_mod")

    def test_stats_none(self):
        self.logger.debug("test_stats_none")
        for tmp_stat in game_system.none.Weapon.stat_types:
            if tmp_stat in self.wpn_none_data:
                self.logger.debug("tmp_stat: %s, weapon value: %s, data value: %s", tmp_stat, self.wpn_none.get_stat(tmp_stat), self.wpn_none_data[tmp_stat])
                self.assertEqual(self.wpn_none.get_stat(tmp_stat), self.wpn_none_data[tmp_stat])
            else:
                self.logger.debug("tmp_stat: %s, weapon value: %s, 0", tmp_stat, self.wpn_none.get_stat(tmp_stat))
                self.assertEqual(self.wpn_none.get_stat(tmp_stat), 0)

    def test_bad_stat_none(self):
        self.logger.debug("test_bad_stat_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_none.get_stat("bad_stat")
