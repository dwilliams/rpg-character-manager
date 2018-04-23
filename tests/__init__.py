#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

from tests import test_character, test_item

### GLOBALS ###

### FUNCTIONS ###
def generate_test_suite():
    logging.debug("generate_test_suite")
    test_suite = unittest.TestSuite()
    # Test Item
    test_suite.addTest(unittest.makeSuite(test_item.TestItemCreation))
    # Test Equipment
    # Test Character
    test_suite.addTest(unittest.makeSuite(test_character.TestCharacterCreation))
    test_suite.addTest(unittest.makeSuite(test_character.TestCharacterInventory))
    test_suite.addTest(unittest.makeSuite(test_character.TestCharacterInventoryWOverride))
    test_suite.addTest(unittest.makeSuite(test_character.TestCharacterEquipment))
    test_suite.addTest(unittest.makeSuite(test_character.TestCharacterLoadSave))
    return test_suite

### CLASSES ###

### MAIN ###
#def main():
#    my_test_suite = generate_test_suite()
#
#    runner = unittest.TextTestRunner()
#    runner.run(my_test_suite)

if __name__ == '__main__':
    pass
