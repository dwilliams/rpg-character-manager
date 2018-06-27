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
        char = game_system.Character()
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, '')
        #self.assertEqual(char.age, '')

    def test_create_with_name_value(self):
        self.logger.debug("test_create_with_name_value")
        char = game_system.Character(name='One')
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
        self.char = game_system.Character(name='One')

    def test_add_to_inventory(self):
        self.logger.debug("test_add_to_inventory")
        item1 = game_system.Item()
        with self.assertRaises(NotImplementedError):
            self.char.add_to_inventory(item1)

class TestCharacterInventoryWOverride(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test character
        self.char = game_system.Character(name='Two')
        # NOTE: This is overriding the character class item check method to allow the rest of the functionality to be
        #       tested.
        self.char._check_item_type = self._check_item_type

    def test_add_to_inventory(self):
        self.logger.debug("test_add_to_inventory")
        item2 = game_system.Item()
        self.char.add_to_inventory(item2)
        self.assertIn(item2, self.char.inventory)

    def test_add_to_inventory_already_in_inventory(self):
        self.logger.debug("test_add_to_inventory_already_in_inventory")
        item2 = game_system.Item()
        self.char.add_to_inventory(item2)
        self.assertIn(item2, self.char.inventory)
        self.char.add_to_inventory(item2)
        self.assertEqual(self.char.inventory.count(item2), 1)

    def test_remove_from_inventory(self):
        self.logger.debug("test_remove_from_inventory")
        item3 = game_system.Item()
        self.char.add_to_inventory(item3)
        self.assertIn(item3, self.char.inventory)
        self.char.remove_from_inventory(item3)
        self.assertNotIn(item3, self.char.inventory)

    def test_remove_from_inventory_not_in_inventory(self):
        self.logger.debug("test_remove_from_inventory")
        item3 = game_system.Item()
        self.assertNotIn(item3, self.char.inventory)
        self.char.remove_from_inventory(item3)
        self.assertNotIn(item3, self.char.inventory)

    def _check_item_type(self, item):
        if not isinstance(item, game_system.Item):
            raise game_system.GameSystemMismatchException()

class TestCharacterEquipment(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test character
        self.char = game_system.Character(name='Three')
        # NOTE: This is overriding the character class item check method to allow the rest of the functionality to be
        #       tested.
        self.char._check_item_type = self._check_item_type

    def test_equip_item(self):
        self.logger.debug("test_equip_item")
        item4 = game_system.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_item(item4)
        self.assertIn(item4, self.char.equipped)

    def test_equip_item_already_equipped(self):
        self.logger.debug("test_equip_item_already_equipped")
        item4 = game_system.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_item(item4)
        self.assertIn(item4, self.char.equipped)
        self.char.equip_item(item4)
        self.assertEqual(self.char.equipped.count(item4), 1)

    def test_equip_item_not_in_inventory(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item4 = game_system.Equipment()
        self.char.equip_item(item4)
        self.assertNotIn(item4, self.char.inventory)
        self.assertNotIn(item4, self.char.equipped)

    def test_equip_item_not_equippable(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item3 = game_system.Item()
        with self.assertRaises(game_system.ItemNotEquipableException):
            self.char.equip_item(item3)

    def test_unequip_item(self):
        self.logger.debug("test_unequip_item")
        item4 = game_system.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.equip_item(item4)
        self.assertIn(item4, self.char.equipped)
        self.char.unequip_item(item4)
        self.assertNotIn(item4, self.char.equipped)

    def test_unequip_item_not_equipped(self):
        self.logger.debug("test_unequip_item")
        item4 = game_system.Equipment()
        self.char.add_to_inventory(item4)
        self.assertIn(item4, self.char.inventory)
        self.char.unequip_item(item4)
        self.assertNotIn(item4, self.char.equipped)

    def test_unequip_item_not_in_inventory(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        item4 = game_system.Equipment()
        self.char.unequip_item(item4)
        self.assertNotIn(item4, self.char.inventory)
        self.assertNotIn(item4, self.char.equipped)

    def _check_item_type(self, item):
        if not isinstance(item, game_system.Item):
            raise game_system.GameSystemMismatchException()

class TestCharacterLoadSave(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test character
        self.char = game_system.Character(name='One')

    def test_load(self):
        self.logger.debug("test_load")
        with self.assertRaises(NotImplementedError):
            self.char.load_json(json_string = "{}")

    def test_save(self):
        self.logger.debug("test_save")
        with self.assertRaises(NotImplementedError):
            self.char.save_json()

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
