#!/usr/bin/env python3

### IMPORTS ###
import argparse
import logging
import math
import os

import game_system
import game_system.adnd

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDCharacterTMP:
    def __init__(self):
        self.name = 'Ten Tin'
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.health = 10

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
    #char_one = SRCharacter()
    #char_one.quickness = 10
    #char_one.intelligence = 8
    #char_one.willpower = 6
    #char_one.stun = 3
    #char_one.damage = 7

    # Display Character
    #logging.debug("Char: \n%s", char_one.format_to_text())

    logging.debug("Creating a simple character from a file")
    charfile = game_system.CharacterFile('tack_pdf_char.json')
    #char_ten = game_system.adnd.ADNDCharacter()
    char_ten = charfile.load_char()

    logging.debug("Creating PDF class")
    pdf_gen = game_system.adnd.ADNDPDFGen(char_ten)

    logging.debug("Outputing PDF file")
    pdf_gen.output_file('test.pdf')

if __name__ == '__main__':
    main()
