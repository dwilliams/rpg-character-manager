#!/usr/bin/env python3

### IMPORTS ###
import logging

from character import Character

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ShadowRunCharacter(Character):
    game_system = 'shadow_run'

    def __init__(self, name = '', age = ''):
        # Ensure the parent's __init__ is called
        super().__init__(name = name, age = age)

    def __str__(self):
        return "ShadowRun{}".format(super().__str__())

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
