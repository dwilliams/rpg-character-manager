#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import character

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestCharacterCreation(unittest.TestCase)
    def test_create_without_values(self):
        char = character.Character()
        self.assertEqual(char.name, '')
        self.assertEqual(char.age, '')

    def test_create_with_name_value(self):
        char = character.Character(name='One')
        self.assertEqual(char.name, 'One')
        self.assertEqual(char.age, '')

    def test_create_with_age_value(self):
        char = character.Character(age='1')
        self.assertEqual(char.name, '')
        self.assertEqual(char.age, '1')

    def test_create_with_name_and_age_values(self):
        char = character.Character(name='Two', age='2')
        self.assertEqual(char.name, 'Two')
        self.assertEqual(char.age, '2')

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
