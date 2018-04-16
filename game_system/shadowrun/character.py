#!/usr/bin/env python3

### IMPORTS ###
import logging

from game_system.exceptions import GameSystemMismatchException
from game_system.character import Character

from game_system.shadowrun.item import ShadowRunItem

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunCharacter(Character):
    game_system = 'shadowrun'

    def __init__(self, name = '', age = ''):
        # Ensure the parent's __init__ is called
        super().__init__(name = name, age = age)

    def __str__(self):
        return "ShadowRun{}".format(super().__str__())

    def load_json(self, json_string):
        pass

    def save_json(self):
        return ''

    def _check_item_type(self, item):
        if not isinstance(item, ShadowRunItem):
            raise GameSystemMismatchException()

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
