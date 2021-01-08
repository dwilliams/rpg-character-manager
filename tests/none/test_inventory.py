#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestInventory(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test inventory
        self.inventory = game_system.Inventory(
            'none',
            game_system.none.Item,
            game_system.none.Equipment,
            game_system.none.Weapon
        )

    def test_add_item(self):
        self.logger.debug("test_add_item")
        item2 = game_system.none.Item()
        self.inventory.add_item(item2)
        self.assertIn(item2, self.inventory.get_items())
        self.assertEqual(len(self.inventory.get_items_by_name(item2.item_name)), 1)

    def test_add_two_item(self):
        self.logger.debug("test_add_item_two_item")
        item1 = game_system.none.Item()
        item2 = game_system.none.Item()
        self.inventory.add_item(item1)
        self.assertIn(item1, self.inventory.get_items())
        self.inventory.add_item(item2)
        self.assertIn(item2, self.inventory.get_items())
        self.assertEqual(len(self.inventory.get_items_by_name(item1.item_name)), 2)
        self.assertEqual(len(self.inventory.get_items_by_name(item2.item_name)), 2)

    def test_add_item_already_in_inventory(self):
        self.logger.debug("test_add_item_already_in_inventory")
        item2 = game_system.none.Item()
        self.inventory.add_item(item2)
        self.assertIn(item2, self.inventory.get_items())
        self.inventory.add_item(item2)
        self.assertEqual(len(self.inventory.get_items_by_name(item2.item_name)), 1)

    def test_add_item_wrong_object_type(self):
        self.logger.debug("test_add_item_wrong_object_type")
        char1 = game_system.none.Character()
        with self.assertRaises(game_system.exceptions.InvalidObjectTypeException):
            self.inventory.add_item(char1)

    def test_add_item_wrong_gamesystem(self):
        self.logger.debug("test_add_item_wrong_gamesystem")
        item4 = game_system.adnd.ADNDItem()
        with self.assertRaises(game_system.exceptions.GameSystemMismatchException):
            self.inventory.add_item(item4)

    def test_get_item_names(self):
        self.logger.debug("test_add_item_two_item")
        item1 = game_system.none.Item()
        item2 = game_system.none.Item()
        item3 = game_system.none.Item()
        item3.item_name = "Test name two"
        self.inventory.add_item(item1)
        self.inventory.add_item(item2)
        self.inventory.add_item(item3)
        item_names = self.inventory.get_item_names()
        self.assertEqual(len(item_names), 2)
        self.assertIn(item1.item_name, item_names)
        self.assertIn(item2.item_name, item_names)
        self.assertIn(item3.item_name, item_names)

    def test_remove_item(self):
        self.logger.debug("test_remove_item")
        item3 = game_system.none.Item()
        self.inventory.add_item(item3)
        self.assertIn(item3, self.inventory.get_items())
        self.inventory.remove_item(item3)
        self.assertNotIn(item3, self.inventory.get_items())
        self.assertEqual(len(self.inventory.get_items_by_name(item3.item_name)), 0)

    def test_remove_item_not_in_inventory(self):
        self.logger.debug("test_remove_item")
        item3 = game_system.none.Item(None)
        self.assertNotIn(item3, self.inventory.get_items())
        with self.assertRaises(game_system.exceptions.ItemNotInInventoryException):
            self.inventory.remove_item(item3)
        self.assertNotIn(item3, self.inventory.get_items())
        self.assertEqual(len(self.inventory.get_items_by_name(item3.item_name)), 0)

class TestInventoryEquipment(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test inventory
        self.inventory = game_system.Inventory(
            'none',
            game_system.none.Item,
            game_system.none.Equipment,
            game_system.none.Weapon
        )

    def test_equip_item(self):
        self.logger.debug("test_equip_item")
        equip1 = game_system.none.Equipment()
        self.inventory.add_item(equip1)
        self.assertIn(equip1, self.inventory.get_items())
        self.inventory.equip_equipment(equip1)
        self.assertIn(equip1, self.inventory.get_equipment())

    def test_equip_item_already_equipped(self):
        self.logger.debug("test_equip_item_already_equipped")
        equip1 = game_system.none.Equipment()
        self.inventory.add_item(equip1)
        self.assertIn(equip1, self.inventory.get_items())
        self.inventory.equip_equipment(equip1)
        self.assertIn(equip1, self.inventory.get_equipment())
        self.inventory.equip_equipment(equip1)
        self.assertEqual(len(self.inventory.get_items_by_name(equip1.item_name)), 1)
        self.assertEqual(len(self.inventory.get_equipment()), 1)

    def test_equip_item_not_in_inventory(self):
        self.logger.debug("test_equip_item_not_in_inventory")
        equip1 = game_system.none.Equipment()
        with self.assertRaises(game_system.exceptions.ItemNotInInventoryException):
            self.inventory.equip_equipment(equip1)
        self.assertNotIn(equip1, self.inventory.get_items())

    def test_equip_item_not_equippable(self):
        self.logger.debug("test_equip_item_not_equippable")
        equip1 = game_system.none.Item()
        with self.assertRaises(game_system.exceptions.ItemNotEquipableException):
            self.inventory.equip_equipment(equip1)

    def test_unequip_item(self):
        self.logger.debug("test_unequip_item")
        equip1 = game_system.none.Equipment()
        self.inventory.add_item(equip1)
        self.assertIn(equip1, self.inventory.get_items())
        self.inventory.equip_equipment(equip1)
        self.assertIn(equip1, self.inventory.get_equipment())
        self.inventory.unequip_equipment(equip1)
        self.assertNotIn(equip1, self.inventory.get_equipment())

    def test_unequip_item_not_equipped(self):
        self.logger.debug("test_unequip_item_not_equipped")
        equip1 = game_system.none.Equipment()
        self.inventory.add_item(equip1)
        self.assertIn(equip1, self.inventory.get_items())
        self.inventory.unequip_equipment(equip1)
        self.assertNotIn(equip1, self.inventory.get_equipment())

    def test_unequip_item_not_in_inventory(self):
        self.logger.debug("test_unequip_item_not_in_inventory")
        equip1 = game_system.none.Equipment()
        self.inventory.unequip_equipment(equip1)
        self.assertNotIn(equip1, self.inventory.get_items())
        self.assertNotIn(equip1, self.inventory.get_equipment())

    def test_remove_equipped_item(self):
        self.logger.debug("test_remove_equipped_item")
        equip1 = game_system.none.Equipment()
        self.inventory.add_item(equip1)
        self.assertIn(equip1, self.inventory.get_items())
        self.inventory.equip_equipment(equip1)
        self.assertIn(equip1, self.inventory.get_equipment())
        self.inventory.remove_item(equip1)
        self.assertNotIn(equip1, self.inventory.get_equipment())
        self.assertNotIn(equip1, self.inventory.get_items())

class TestInventoryWeapon(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        # Create test inventory
        self.inventory = game_system.Inventory(
            'none',
            game_system.none.Item,
            game_system.none.Equipment,
            game_system.none.Weapon
        )

    def test_equip_weapon(self):
        self.logger.debug("test_equip_weapon")
        wpn1 = game_system.none.Weapon()
        self.inventory.add_item(wpn1)
        self.assertIn(wpn1, self.inventory.get_items())
        self.inventory.equip_weapon(wpn1)
        self.assertIn(wpn1, self.inventory.get_weapons())

    def test_equip_weapon_already_equipped(self):
        self.logger.debug("test_equip_weapon_already_equipped")
        wpn1 = game_system.none.Weapon()
        self.inventory.add_item(wpn1)
        self.assertIn(wpn1, self.inventory.get_items())
        self.inventory.equip_weapon(wpn1)
        self.assertIn(wpn1, self.inventory.get_weapons())
        self.inventory.equip_weapon(wpn1)
        self.assertEqual(len(self.inventory.get_items_by_name(wpn1.item_name)), 1)
        self.assertEqual(len(self.inventory.get_weapons()), 1)

    def test_equip_weapon_not_in_inventory(self):
        self.logger.debug("test_equip_weapon_not_in_inventory")
        wpn1 = game_system.none.Weapon()
        with self.assertRaises(game_system.exceptions.ItemNotInInventoryException):
            self.inventory.equip_weapon(wpn1)
        self.assertNotIn(wpn1, self.inventory.get_items())

    def test_equip_weapon_not_equippable(self):
        self.logger.debug("test_equip_weapon_not_equippable")
        wpn1 = game_system.none.Item()
        with self.assertRaises(game_system.exceptions.ItemNotEquipableException):
            self.inventory.equip_weapon(wpn1)

    def test_unequip_weapon(self):
        self.logger.debug("test_unequip_weapon")
        wpn1 = game_system.none.Weapon()
        self.inventory.add_item(wpn1)
        self.assertIn(wpn1, self.inventory.get_items())
        self.inventory.equip_weapon(wpn1)
        self.assertIn(wpn1, self.inventory.get_weapons())
        self.inventory.unequip_weapon(wpn1)
        self.assertNotIn(wpn1, self.inventory.get_weapons())

    def test_unequip_weapon_not_equipped(self):
        self.logger.debug("test_unequip_weapon_not_equipped")
        wpn1 = game_system.none.Weapon()
        self.inventory.add_item(wpn1)
        self.assertIn(wpn1, self.inventory.get_items())
        self.inventory.unequip_weapon(wpn1)
        self.assertNotIn(wpn1, self.inventory.get_weapons())

    def test_unequip_weapon_not_in_inventory(self):
        self.logger.debug("test_unequip_weapon_not_in_inventory")
        wpn1 = game_system.none.Weapon()
        self.inventory.unequip_weapon(wpn1)
        self.assertNotIn(wpn1, self.inventory.get_items())
        self.assertNotIn(wpn1, self.inventory.get_weapons())

    def test_remove_equipped_weapon(self):
        self.logger.debug("test_remove_equipped_weapon")
        wpn1 = game_system.none.Weapon()
        self.inventory.add_item(wpn1)
        self.assertIn(wpn1, self.inventory.get_items())
        self.inventory.equip_weapon(wpn1)
        self.assertIn(wpn1, self.inventory.get_weapons())
        self.inventory.remove_item(wpn1)
        self.assertNotIn(wpn1, self.inventory.get_weapons())
        self.assertNotIn(wpn1, self.inventory.get_items())

class TestInventoryLoadSave(unittest.TestCase):
    '''
    The load and save format assumes the items are being built using the
    factories and that the unique id of the item "types" is the name of the
    item.

    Inventory data structure is a list of the names of the items in each of the
    sets.  The inventory is allowed to have duplicates, but the active equipment
    and active weapons are not currently allowed to have duplicates.

    example:
    data = {
      "inventory": ["item one", "item two", "item three", "item one", "equip one", "equip two", "wpn one"],
      "active_equipment": ["equip one", "equip two"],
      "active_weapons": ["wpn one"]
    }
    '''
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

        self.test_item_data = [
            { "game_system": "none", "object_type": "item", "data": {"item_name": "item one"}},
            { "game_system": "none", "object_type": "item", "data": {"item_name": "item two"}},
            { "game_system": "none", "object_type": "item", "data": {"item_name": "item three"}}
        ]
        self.test_equip_data = [
            { "game_system": "none", "object_type": "equipment", "data": {"item_name": "equip one"}},
            { "game_system": "none", "object_type": "equipment", "data": {"item_name": "equip two"}},
            { "game_system": "none", "object_type": "equipment", "data": {"item_name": "equip three"}}
        ]
        self.test_wpn_data = [
            { "game_system": "none", "object_type": "weapon", "data": {"item_name": "wpn one"}}
        ]

        self.dict_keys = ['inventory', 'active_equipment', 'active_weapons']
        self.test_data = {
            "inventory": [
                "item one", "item two", "item three", "item one", "equip one", "equip two", "equip three", "wpn one"
            ],
            "active_equipment": ["equip one", "equip two"],
            "active_weapons": ["wpn one"]
        }

        # Create test inventory and supporting objects
        self.item_factory = game_system.factories.ItemFactory()
        for item in self.test_item_data:
            self.item_factory.load_object_data(item)
        self.equipment_factory = game_system.factories.EquipmentFactory()
        for item in self.test_equip_data:
            self.equipment_factory.load_object_data(item)
        self.weapon_factory = game_system.factories.WeaponFactory()
        for item in self.test_wpn_data:
            self.weapon_factory.load_object_data(item)

        self.inventory = game_system.Inventory(
            'none',
            game_system.none.Item,
            game_system.none.Equipment,
            game_system.none.Weapon
        )

    def test_load(self):
        self.logger.debug("test_load")

        # Verify empty inventory
        self.assertEqual(self.inventory.get_items(), [])

        # Load the test data
        self.inventory.load_dict(self.test_data, self.item_factory, self.equipment_factory, self.weapon_factory)

        # Check the items
        self.assertEqual(len(self.inventory.get_item_names()), 7)
        self.assertEqual(len(self.inventory.get_items_by_name('item one')), 2)
        self.assertEqual(len(self.inventory.get_items_by_name('item two')), 1)
        self.assertEqual(len(self.inventory.get_items_by_name('item three')), 1)
        self.assertEqual(len(self.inventory.get_items_by_name('equip one')), 1)
        self.assertEqual(len(self.inventory.get_items_by_name('equip two')), 1)
        self.assertEqual(len(self.inventory.get_items_by_name('equip three')), 1)
        self.assertEqual(len(self.inventory.get_items_by_name('wpn one')), 1)
        self.assertEqual(len(self.inventory.get_equipment_names()), 2)
        self.assertEqual(len(self.inventory.get_weapon_names()), 1)

    def test_save(self):
        self.logger.debug("test_save")

        # Verify empty inventory
        self.assertEqual(self.inventory.get_items(), [])

        # Load items, equipment, weapons into the inventory and equip
        self.inventory.add_item(self.item_factory.create('none', 'item one'))
        self.inventory.add_item(self.item_factory.create('none', 'item two'))
        self.inventory.add_item(self.item_factory.create('none', 'item three'))
        self.inventory.add_item(self.item_factory.create('none', 'item one'))
        self.inventory.add_item(self.equipment_factory.create('none', 'equip three'))

        tmp_item = self.equipment_factory.create('none', 'equip one')
        self.inventory.add_item(tmp_item)
        self.inventory.equip_equipment(tmp_item)

        tmp_item = self.equipment_factory.create('none', 'equip two')
        self.inventory.add_item(tmp_item)
        self.inventory.equip_equipment(tmp_item)

        tmp_item = self.weapon_factory.create('none', 'wpn one')
        self.inventory.add_item(tmp_item)
        self.inventory.equip_weapon(tmp_item)

        tmp_result = self.inventory.save_dict()

        # Check the output
        self.assertEqual(sorted(tmp_result.keys()), sorted(self.dict_keys))
        for tmp_key in self.dict_keys:
            self.assertEqual(sorted(tmp_result[tmp_key]), sorted(self.test_data[tmp_key]))
