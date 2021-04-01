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

    def test_create_adnd(self):
        self.logger.debug("test_create_adnd")
        weapon = game_system.adnd.ADNDWeapon({"item_name": "Generic ADND Weapon One", "cost_money": {"value": 123}, "stat_damage": 1})
        self.logger.debug("ADNDWeapon: %s", weapon)
        self.assertEqual(weapon.get_name(), "Generic ADND Weapon One")
        self.assertEqual(str(weapon), "ADNDWeapon: Generic ADND Weapon One")

class TestWeaponStats(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.wpn_adnd_data = {
            "item_name": "Generic ADND Weapon One",
            "cost_money": {"value": 123},
            "stat_weight": 1,
            "stat_type": 'P',
            "stat_size": 'S',
            "stat_speed": 2,
            "stat_damage_sm": "1D4",
            "stat_damage_l": "1D3",
            "stat_range": "Melee"
        }
        self.wpn_adnd = game_system.adnd.ADNDWeapon(self.wpn_adnd_data)

    def test_costs_adnd(self):
        self.logger.debug("test_costs_adnd")
        for tmp_cost in game_system.adnd.ADNDWeapon.cost_types:
            if tmp_cost in self.wpn_adnd_data:
                self.logger.debug("tmp_cost: %s, weapon value: %s, data value: %s", tmp_cost, self.wpn_adnd.get_cost(tmp_cost).get_value(), self.wpn_adnd_data[tmp_cost]['value'])
                self.assertEqual(self.wpn_adnd.get_cost(tmp_cost).get_value(), self.wpn_adnd_data[tmp_cost]['value'])
            else:
                self.logger.debug("tmp_cost: %s, weapon value: %s, 0", tmp_cost, self.wpn_adnd.get_cost(tmp_cost).get_value())
                self.assertEqual(self.wpn_adnd.get_cost(tmp_cost).get_value(), 0)

    def test_bad_cost_adnd(self):
        self.logger.debug("test_bad_cost_adnd")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_adnd.get_cost("bad_cost")

    def test_mods_adnd(self):
        self.logger.debug("test_mods_adnd")
        for tmp_mod in game_system.adnd.ADNDWeapon.mod_types:
            if tmp_mod in self.wpn_adnd_data:
                self.logger.debug("tmp_mod: %s, weapon value: %s, data value: %s", tmp_mod, self.wpn_adnd.get_mod(tmp_mod).get_value(), self.wpn_adnd_data[tmp_mod]['value'])
                self.assertEqual(self.wpn_adnd.get_mod(tmp_mod).get_value(), self.wpn_adnd_data[tmp_mod]['value'])
            else:
                self.logger.debug("tmp_mod: %s, weapon value: %s, 0", tmp_mod, self.wpn_adnd.get_mod(tmp_mod).get_value())
                self.assertEqual(self.wpn_adnd.get_mod(tmp_mod).get_value(), 0)

    def test_bad_mod_adnd(self):
        self.logger.debug("test_bad_mod_adnd")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_adnd.get_mod("bad_mod")

    def test_stats_adnd(self):
        self.logger.debug("test_stats_adnd")
        for tmp_stat in game_system.adnd.ADNDWeapon.stat_types:
            if tmp_stat in self.wpn_adnd_data:
                self.logger.debug("tmp_stat: %s, weapon value: %s, data value: %s", tmp_stat, self.wpn_adnd.get_stat(tmp_stat), self.wpn_adnd_data[tmp_stat])
                self.assertEqual(self.wpn_adnd.get_stat(tmp_stat), self.wpn_adnd_data[tmp_stat])
            else:
                self.logger.debug("tmp_stat: %s, weapon value: %s, 0", tmp_stat, self.wpn_adnd.get_stat(tmp_stat))
                self.assertEqual(self.wpn_adnd.get_stat(tmp_stat), 0)

    def test_bad_stat_adnd(self):
        self.logger.debug("test_bad_stat_adnd")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.wpn_adnd.get_stat("bad_stat")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
