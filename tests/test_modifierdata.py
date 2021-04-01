#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import game_system

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestModifierData(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_default(self):
        self.logger.debug("test_create_default")
        tmp_mod_data = game_system.modifierdata.ModifierData()
        self.logger.debug("ModifierData: %s", tmp_mod_data)
        self.assertIsNone(tmp_mod_data.get_value())
        self.assertEqual(tmp_mod_data.get_combine_method(), game_system.modifierdata.CombineMethod.OVERWRITE)
        self.assertEqual(str(tmp_mod_data), "ModifierData: [OVERWRITE] None")

    def test_create_str(self):
        self.logger.debug("test_create_str")
        tmp_mod_data = game_system.modifierdata.ModifierData("something")
        self.logger.debug("ModifierData: %s", tmp_mod_data)
        self.assertEqual(tmp_mod_data.get_value(), "something")
        self.assertEqual(tmp_mod_data.get_combine_method(), game_system.modifierdata.CombineMethod.OVERWRITE)
        self.assertEqual(str(tmp_mod_data), "ModifierData: [OVERWRITE] something")

    def test_create_int_add(self):
        self.logger.debug("test_create_int_add")
        tmp_mod_data = game_system.modifierdata.ModifierData(19, game_system.modifierdata.CombineMethod.ADD)
        self.logger.debug("ModifierData: %s", tmp_mod_data)
        self.assertEqual(tmp_mod_data.get_value(), 19)
        self.assertEqual(tmp_mod_data.get_combine_method(), game_system.modifierdata.CombineMethod.ADD)
        self.assertEqual(str(tmp_mod_data), "ModifierData: [ADD] 19")


class TestModifierDataCombiner(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_create_none(self):
        self.logger.debug("test_create_none")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        self.assertEqual(str(tmp_mod_data_com), "ModifierDataCombiner: 0")

    def test_add_modifierdata(self):
        self.logger.debug("test_add_modifierdata")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(1))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        self.assertEqual(len(tmp_mod_data_com.items_to_combine), 1)
        self.assertEqual(str(tmp_mod_data_com), "ModifierDataCombiner: 1")

    def test_add_bad_data(self):
        self.logger.debug("test_add_bad_data")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        with self.assertRaises(game_system.exceptions.InvalidObjectTypeException):
            tmp_mod_data_com.add_item(object())

    def test_resolve_ints_adds(self):
        self.logger.debug("test_resolve_ints_adds")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(1, game_system.modifierdata.CombineMethod.ADD))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(2, game_system.modifierdata.CombineMethod.ADD))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve(3)
        self.assertIsInstance(tmp_result, int)
        self.assertEqual(tmp_result, 6)

    def test_resolve_ints_overwrite_over(self):
        self.logger.debug("test_resolve_ints_overwrite_over")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(7, game_system.modifierdata.CombineMethod.OVERWRITE))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(2, game_system.modifierdata.CombineMethod.OVERWRITE))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve(3)
        self.assertIsInstance(tmp_result, int)
        self.assertEqual(tmp_result, 7)

    def test_resolve_ints_overwrite_under(self):
        self.logger.debug("test_resolve_ints_overwrite_under")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(1, game_system.modifierdata.CombineMethod.OVERWRITE))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(2, game_system.modifierdata.CombineMethod.OVERWRITE))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve(3)
        self.assertIsInstance(tmp_result, int)
        self.assertEqual(tmp_result, 3)

    def test_resolve_ints_adds_overwrite_over(self):
        self.logger.debug("test_resolve_ints_adds_overwrite_over")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(1, game_system.modifierdata.CombineMethod.ADD))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(9, game_system.modifierdata.CombineMethod.OVERWRITE))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(2, game_system.modifierdata.CombineMethod.ADD))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve(3)
        self.assertIsInstance(tmp_result, int)
        self.assertEqual(tmp_result, 9)

    def test_resolve_ints_adds_overwrite_under(self):
        self.logger.debug("test_resolve_ints_adds_overwrite_under")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(1, game_system.modifierdata.CombineMethod.ADD))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(3, game_system.modifierdata.CombineMethod.OVERWRITE))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData(2, game_system.modifierdata.CombineMethod.ADD))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve(3)
        self.assertIsInstance(tmp_result, int)
        self.assertEqual(tmp_result, 6)

    def test_resolve_strs_adds(self):
        self.logger.debug("test_resolve_strs_adds")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData("seven", game_system.modifierdata.CombineMethod.ADD))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData("two", game_system.modifierdata.CombineMethod.ADD))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve("one")
        self.assertIsInstance(tmp_result, str)
        self.assertEqual(tmp_result, "one")

    def test_resolve_strs_overwrite(self):
        self.logger.debug("test_resolve_strs_overwrite")
        tmp_mod_data_com = game_system.modifierdata.ModifierDataCombiner()
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData("seven", game_system.modifierdata.CombineMethod.OVERWRITE))
        tmp_mod_data_com.add_item(game_system.modifierdata.ModifierData("two", game_system.modifierdata.CombineMethod.OVERWRITE))
        self.logger.debug("ModifierDataCombiner: %s", tmp_mod_data_com)
        tmp_result = tmp_mod_data_com.resolve("one")
        self.assertIsInstance(tmp_result, str)
        self.assertEqual(tmp_result, "two")
