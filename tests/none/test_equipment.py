#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestEquipmentCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_none(self):
        self.logger.debug("test_create_none")
        equipment = game_system.none.Equipment({"item_name": "Generic Equipment One", "cost_money": 111, "mod_strength": 1, "mod_charisma": 1, "mod_intelligence": 1, "mod_wisdom": 1})
        self.logger.debug("Equipment: %s", equipment)
        self.assertEqual(equipment.get_name(), "Generic Equipment One")
        self.assertEqual(str(equipment), "Equipment: Generic Equipment One")

    #def test_create_shadowrun(self):
    #    self.logger.debug("test_create_shadowrun")
    #    equipment = game_system.shadowrun.ShadowRunEquipment({"item_name": "Generic SR Equipment Two", "mod_quickness": 1, "mod_strength": 1, "cost_body": 0.8, "cost_money": 45000})
    #    self.logger.debug("ShadowRunEquipment: %s", equipment)
    #    self.assertEqual(equipment.get_name(), "Generic SR Equipment Two")
    #    self.assertEqual(str(equipment), "ShadowRunEquipment: Generic SR Equipment Two")

class TestEquipmentStats(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.eq_none_data = {"item_name": "Generic Equipment One", "cost_money": 111, "mod_strength": 1, "mod_charisma": 1, "mod_intelligence": 1, "mod_wisdom": 1}
        self.eq_none = game_system.none.Equipment(self.eq_none_data)
        #self.eq_shadowrun_data = {"item_name": "Generic SR Equipment Two", "mod_quickness": 1, "mod_strength": 1, "cost_body": 0.8, "cost_money": 45000}
        #self.eq_shadowrun = game_system.shadowrun.ShadowRunEquipment(self.eq_shadowrun_data)

    def test_costs_none(self):
        self.logger.debug("test_costs_none")
        for tmp_cost in game_system.none.Equipment.cost_types:
            if tmp_cost in self.eq_none_data:
                self.logger.debug("tmp_cost: %s, equip value: %s, data value: %s", tmp_cost, self.eq_none.get_cost(tmp_cost), self.eq_none_data[tmp_cost])
                self.assertEqual(self.eq_none.get_cost(tmp_cost), self.eq_none_data[tmp_cost])
            else:
                self.logger.debug("tmp_cost: %s, equip value: %s, 0", tmp_cost, self.eq_none.get_cost(tmp_cost))
                self.assertEqual(self.eq_none.get_cost(tmp_cost), 0)

    def test_bad_cost_none(self):
        self.logger.debug("test_bad_cost_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.eq_none.get_cost("bad_cost")

    #def test_costs_shadowrun(self):
    #    self.logger.debug("test_costs_shadowrun")
    #    for tmp_cost in game_system.shadowrun.ShadowRunEquipment.cost_types:
    #        if tmp_cost in self.eq_shadowrun_data:
    #            self.logger.debug("tmp_cost: %s, equip value: %s, data value: %s", tmp_cost, self.eq_shadowrun.get_cost(tmp_cost), self.eq_shadowrun_data[tmp_cost])
    #            self.assertEqual(self.eq_shadowrun.get_cost(tmp_cost), self.eq_shadowrun_data[tmp_cost])
    #        else:
    #            self.logger.debug("tmp_cost: %s, equip value: %s, 0", tmp_cost, self.eq_shadowrun.get_cost(tmp_cost))
    #            self.assertEqual(self.eq_shadowrun.get_cost(tmp_cost), 0)
    #    self.logger.debug("testing a bad cost")
    #    with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
    #        self.eq_shadowrun.get_cost("bad_cost")

    def test_mods_none(self):
        self.logger.debug("test_mods_none")
        for tmp_mod in game_system.none.Equipment.mod_types:
            if tmp_mod in self.eq_none_data:
                self.logger.debug("tmp_mod: %s, equip value: %s, data value: %s", tmp_mod, self.eq_none.get_mod(tmp_mod), self.eq_none_data[tmp_mod])
                self.assertEqual(self.eq_none.get_mod(tmp_mod), self.eq_none_data[tmp_mod])
            else:
                self.logger.debug("tmp_mod: %s, equip value: %s, 0", tmp_mod, self.eq_none.get_mod(tmp_mod))
                self.assertEqual(self.eq_none.get_mod(tmp_mod), 0)

    def test_bad_mod_none(self):
        self.logger.debug("test_bad_mod_none")
        with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
            self.eq_none.get_mod("bad_mod")

    #def test_mods_shadowrun(self):
    #    self.logger.debug("test_mods_shadowrun")
    #    for tmp_mod in game_system.shadowrun.ShadowRunEquipment.mod_types:
    #        if tmp_mod in self.eq_shadowrun_data:
    #            self.logger.debug("tmp_mod: %s, equip value: %s, data value: %s", tmp_mod, self.eq_shadowrun.get_mod(tmp_mod), self.eq_shadowrun_data[tmp_mod])
    #            self.assertEqual(self.eq_shadowrun.get_mod(tmp_mod), self.eq_shadowrun_data[tmp_mod])
    #        else:
    #            self.logger.debug("tmp_mod: %s, equip value: %s, 0", tmp_mod, self.eq_shadowrun.get_mod(tmp_mod))
    #            self.assertEqual(self.eq_shadowrun.get_mod(tmp_mod), 0)
    #    self.logger.debug("testing a bad mod")
    #    with self.assertRaises(game_system.exceptions.InvalidItemAttributeException):
    #        self.eq_shadowrun.get_mod("bad_mod")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
