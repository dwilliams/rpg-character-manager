#!/usr/bin/env python3

### IMPORTS ###
import glob
import logging
import os
import sys
import unittest

#from tests import test_equipment, test_equipment_factory
#from tests import test_item, test_item_factory

#from tests.init_test_env import start_thread

### GLOBALS ###

### FUNCTIONS ###
# def generate_test_suite():
#     logging.debug("generate_test_suite")
#     test_suite = unittest.TestSuite()
#     # Test Item
#     test_suite.addTest(unittest.makeSuite(test_item.TestItemCreation))
#     # Test Item Factory
#     test_suite.addTest(unittest.makeSuite(test_item_factory.TestItemFactoryDataLoad))
#     test_suite.addTest(unittest.makeSuite(test_item_factory.TestItemFactoryItemCreation))
#     # Test Equipment
#     test_suite.addTest(unittest.makeSuite(test_equipment.TestEquipmentCreation))
#     test_suite.addTest(unittest.makeSuite(test_equipment.TestEquipmentStats))
#     # Test Equipment Factory
#     test_suite.addTest(unittest.makeSuite(test_equipment_factory.TestEquipmentFactoryDataLoad))
#     test_suite.addTest(unittest.makeSuite(test_equipment_factory.TestEquipmentFactoryEquipmentCreation))
#     # Test Character
#     #test_suite.addTest(unittest.makeSuite(test_character.TestCharacterCreation))
#     #test_suite.addTest(unittest.makeSuite(test_character.TestCharacterInventory))
#     #test_suite.addTest(unittest.makeSuite(test_character.TestCharacterInventoryWOverride))
#     #test_suite.addTest(unittest.makeSuite(test_character.TestCharacterEquipment))
#     #test_suite.addTest(unittest.makeSuite(test_character.TestCharacterLoadSave))
#     return test_suite

def build_test_suites(test_glob):
    test_files = glob.glob(test_glob)
    suites = []
    for tmp_test_file in test_files:
        tmp_test_file_replace = tmp_test_file.replace('/', '.')
        tmp_test_file_replace = tmp_test_file_replace.replace('\\', '.')
        tmp_mod_str = "tests.{}".format(tmp_test_file_replace[0:len(tmp_test_file_replace) - 3])
        suites.append(unittest.defaultTestLoader.loadTestsFromName(tmp_mod_str))
    return suites

def run_all_tests():
    # Start the test server on a new thread
    #start_thread()

    #===== Run all test modules========
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Get all python files that start with 'test_'
    #test_files = glob.glob('test_*.py')
    # Convert files found into module names
    #module_strings = ['tests.' + test_file[0:len(test_file) - 3] for test_file in test_files]
    # Make testing suites for each module
    #suites = [unittest.defaultTestLoader.loadTestsFromName(test_file) for test_file in
    #          module_strings]
    # Consolidate all suites into one
    suites = []
    suites.extend(build_test_suites("test_*.py"))
    suites.extend(build_test_suites("factories/test_*.py"))
    suites.extend(build_test_suites("none/test_*.py"))
    suites.extend(build_test_suites("adnd/test_*.py"))
    test_suite = unittest.TestSuite(suites)
    # Run the test suite containing all the tests from all the modules
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    if result.wasSuccessful():
        return True
    return False

### CLASSES ###

### MAIN ###
#def main():
#    my_test_suite = generate_test_suite()
#
#    runner = unittest.TextTestRunner()
#    runner.run(my_test_suite)

if __name__ == '__main__':
    if run_all_tests() is False:
        sys.exit(1)
    sys.exit(0)
