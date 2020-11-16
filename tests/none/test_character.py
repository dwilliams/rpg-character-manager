#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestCharacterCreation(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_without_values(self):
        self.logger.debug("test_create_without_values")
        char = game_system.none.Character()
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, "New Character")
        #self.assertEqual(char.age, '')

    def test_create_with_name_value(self):
        self.logger.debug("test_create_with_name_value")
        char = game_system.none.Character(name='One')
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, 'One')
        #self.assertEqual(char.age, '')

    #def test_create_with_age_value(self):
    #    self.logger.debug("test_create_with_age_value")
    #    char = game_system.Character(age='1')
    #    self.logger.debug("Character: %s", char)
    #    self.assertEqual(char.name, '')
    #    self.assertEqual(char.age, '1')

    #def test_create_with_name_and_age_values(self):
    #    self.logger.debug("test_create_with_name_and_age_values")
    #    char = game_system.Character(name='Two', age='2')
    #    self.logger.debug("Character: %s", char)
    #    self.assertEqual(char.name, 'Two')
    #    self.assertEqual(char.age, '2')

class TestCharacterInventory(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test character
        self.char = game_system.none.Character(name='Two')

    def test_add_to_inventory(self):
        self.logger.debug("test_add_to_inventory")
        item2 = game_system.none.Item(None)
        self.char.add_to_inventory(item2)
        self.assertIn(item2, self.char.inventory)

    def test_add_to_inventory_already_in_inventory(self):
        self.logger.debug("test_add_to_inventory_already_in_inventory")
        item2 = game_system.none.Item(None)
        self.char.add_to_inventory(item2)
        self.assertIn(item2, self.char.inventory)
        self.char.add_to_inventory(item2)
        #self.assertEqual(self.char.inventory.count(item2), 1)
        # Need to figure out how to test the set functionality without .count().

    def test_remove_from_inventory(self):
        self.logger.debug("test_remove_from_inventory")
        item3 = game_system.none.Item(None)
        self.char.add_to_inventory(item3)
        self.assertIn(item3, self.char.inventory)
        self.char.remove_from_inventory(item3)
        self.assertNotIn(item3, self.char.inventory)

    def test_remove_from_inventory_not_in_inventory(self):
        self.logger.debug("test_remove_from_inventory")
        item3 = game_system.none.Item(None)
        self.assertNotIn(item3, self.char.inventory)
        with self.assertRaises(game_system.exceptions.ItemNotInInventoryException):
            self.char.remove_from_inventory(item3)
        self.assertNotIn(item3, self.char.inventory)

class TestCharacterEquipment(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test character
        self.char = game_system.none.Character(name='Three')

    def test_equip_item(self):
        self.logger.debug("test_equip_item")
        item4 = game_system.none.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_equipment(item4)
        self.assertIn(item4, self.char.active_equipment)

    def test_equip_item_already_equipped(self):
        self.logger.debug("test_equip_item_already_equipped")
        item4 = game_system.none.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_equipment(item4)
        self.assertIn(item4, self.char.active_equipment)
        self.char.equip_equipment(item4)
        #self.assertEqual(self.char.equipped.count(item4), 1)
        # Need to figure out how to test the set functionality without .count().

    def test_equip_item_not_in_inventory(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item4 = game_system.none.Equipment()
        with self.assertRaises(game_system.exceptions.ItemNotInInventoryException):
            self.char.equip_equipment(item4)
        self.assertNotIn(item4, self.char.inventory)

    def test_equip_item_not_equippable(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item3 = game_system.none.Item(None)
        with self.assertRaises(game_system.exceptions.ItemNotEquipableException):
            self.char.equip_equipment(item3)
        #self.assertNotIn(item3, self.char.inventory) # should make sure this isn't in the inventory or active_equipment
        # Should also do this with an Item in the inventory

    def test_unequip_item(self):
        self.logger.debug("test_unequip_item")
        item4 = game_system.none.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_equipment(item4)
        self.assertIn(item4, self.char.active_equipment)
        self.char.unequip_equipment(item4)
        self.assertNotIn(item4, self.char.active_equipment)

    def test_unequip_item_not_equipped(self):
        self.logger.debug("test_unequip_item")
        item4 = game_system.none.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.unequip_equipment(item4)
        self.assertNotIn(item4, self.char.active_equipment)

    def test_unequip_item_not_in_inventory(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item4 = game_system.none.Equipment()
        self.char.unequip_equipment(item4)
        self.assertNotIn(item4, self.char.inventory)
        self.assertNotIn(item4, self.char.active_equipment)

#FIXME: Implemented the core of the load and save character methods, so need to write tests for them.
#class TestCharacterLoadSave(unittest.TestCase):
#    def setUp(self):
#        # Setup logging for the class
#        self.logger = logging.getLogger(type(self).__name__)
#        self.logger.debug("setUp")
#
#        # Create test character
#        self.char = game_system.none.Character(name='One')
#
#    def test_load(self):
#        self.logger.debug("test_load")
#        with self.assertRaises(NotImplementedError):
#            self.char.load_dict(char_dict = {})
#
#    def test_save(self):
#        self.logger.debug("test_save")
#        with self.assertRaises(NotImplementedError):
#            self.char.save_dict()
