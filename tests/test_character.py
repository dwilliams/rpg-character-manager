#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import character

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
        char = character.Character()
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, '')
        self.assertEqual(char.age, '')

    def test_create_with_name_value(self):
        self.logger.debug("test_create_with_name_value")
        char = character.Character(name='One')
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, 'One')
        self.assertEqual(char.age, '')

    def test_create_with_age_value(self):
        self.logger.debug("test_create_with_age_value")
        char = character.Character(age='1')
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, '')
        self.assertEqual(char.age, '1')

    def test_create_with_name_and_age_values(self):
        self.logger.debug("test_create_with_name_and_age_values")
        char = character.Character(name='Two', age='2')
        self.logger.debug("Character: %s", char)
        self.assertEqual(char.name, 'Two')
        self.assertEqual(char.age, '2')

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
