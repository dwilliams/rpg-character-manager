#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###
TEST_EQUIPMENT_LIST = [
  {"game_system": "none", "object_type": "equipment", "data": {"item_name": "Generic Equipment One", "cost_money": 111, "mod_strength": 1, "mod_charisma": 1, "mod_intelligence": 1, "mod_wisdom": 1}},
  {"game_system": "none", "object_type": "equipment", "data": {"item_name": "Generic Equipment Two", "cost_money": 234, "mod_strength": 2}},
  {"game_system": "shadowrun", "object_type": "equipment", "data": {"item_name": "Generic SR Equipment Two", "mod_quickness": 1, "mod_strength": 1, "cost_body": 0.8, "cost_money": 45000}}
]

### FUNCTIONS ###

### CLASSES ###
class TestEquipmentFactoryDataLoad(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.test_equipment_names = {'none': [], 'shadowrun': []}
        for test_equipment_data in TEST_EQUIPMENT_LIST:
            self.test_equipment_names[test_equipment_data['game_system']].append(test_equipment_data['data']['item_name'])

    def test_create_factory_and_load_data(self):
        self.logger.debug("test_create_factory_and_load_data")
        equipment_factory = game_system.EquipmentFactory()
        for test_equipment_data in TEST_EQUIPMENT_LIST:
            equipment_factory.load_object_data(test_equipment_data)
        for tmp_game_system in self.test_equipment_names:
            tmp_names = equipment_factory.get_list_names(tmp_game_system)
            self.assertListEqual(tmp_names, self.test_equipment_names[tmp_game_system])

class TestEquipmentFactoryEquipmentCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.equipment_factory = game_system.EquipmentFactory()
        for test_equipment_data in TEST_EQUIPMENT_LIST:
            self.equipment_factory.load_object_data(test_equipment_data)

    def test_create_none(self):
        self.logger.debug("test_create_none")
        equipment = self.equipment_factory.create('none', "Generic Equipment One")
        self.logger.debug("Equipment: %s", equipment)
        self.assertIsInstance(equipment, game_system.none.Equipment)
        self.assertEqual(equipment.item_name, "Generic Equipment One")

    def test_create_shadowrun(self):
        self.logger.debug("test_create_shadowrun")
        equipment = self.equipment_factory.create('shadowrun', "Generic SR Equipment Two")
        self.logger.debug("Equipment: %s", equipment)
        self.assertIsInstance(equipment, game_system.shadowrun.ShadowRunEquipment)
        self.assertEqual(equipment.item_name, "Generic SR Equipment Two")

    def test_create_bad(self):
        self.logger.debug("test_create_bad")
        with self.assertRaises(game_system.exceptions.InvalidGameSystemException):
            equipment = self.equipment_factory.create('bad', "Generic Equipment One")

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
