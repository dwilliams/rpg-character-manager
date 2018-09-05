#!/usr/bin/env python3

### IMPORTS ###
import logging
import math
import os

import jinja2

### GLOBALS ###

### FUNCTIONS ###
def load_template(name):
    path = os.path.join('./', name)
    with open(os.path.abspath(path), 'r') as tmp_file:
        return jinja2.Template(tmp_file.read())

### CLASSES ###
class SRCharacter:
    def __init__(self):
        self.name = 'One'
        self.body = 1
        self.quickness = 1
        self.strength = 1
        self.charisma = 1
        self.intelligence = 1
        self.willpower = 1
        self.stun = 0
        self.damage = 0

    @property
    def dice_combat(self):
        return math.floor((self.quickness + self.intelligence + self.willpower) / 2)

    @property
    def dice_magic(self):
        return 0

    @property
    def dice_rigger(self):
        return 0

    @property
    def dice_initiative(self):
        return 1

    @property
    def reaction(self):
        return math.floor((self.quickness + self.intelligence) / 2)

    @property
    def armor_impact(self):
        return 0

    @property
    def armor_balistic(self):
        return 0

    def format_to_text(self):
        # Jinja Template
        tmp_template = load_template('tack.text.jinja')
        return tmp_template.render(char=self)

### MAIN ###
def main():
    # Init Logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    # Create Character
    char_one = SRCharacter()
    char_one.quickness = 10
    char_one.intelligence = 8
    char_one.willpower = 6
    char_one.stun = 3
    char_one.damage = 7

    # Display Character
    logging.debug("Char: \n%s", char_one.format_to_text())

if __name__ == '__main__':
    main()
