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
        self.assertEqual(equipment.item_name, "Generic Equipment One")

    def test_create_shadowrun(self):
        self.logger.debug("test_create_shadowrun")
        equipment = game_system.shadowrun.ShadowRunEquipment({"item_name": "Generic SR Equipment Two", "mod_quickness": 1, "mod_strength": 1, "cost_body": 0.8, "cost_money": 45000})
        self.logger.debug("ShadowRunEquipment: %s", equipment)
        self.assertEqual(equipment.item_name, "Generic SR Equipment Two")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
