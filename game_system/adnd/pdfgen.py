#!/usr/bin/env python3

### IMPORTS ###
from fpdf import FPDF

from game_system.adnd.character import ADNDCharacter

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDPDF(FPDF):
    def __init__(self, name, orientation = 'P', unit = 'in', format = 'Letter'):
        super().__init__(orientation = orientation, unit = unit, format = format)
        self.alias_nb_pages()
        self.set_font('Arial', '', 16)
        self.char_name = name

    def header(self):
        self.set_font('Arial', '', 10)
        self.cell(0, 0.25, "{} - Advanced Dungeons and Dragons".format(self.char_name), 'B', 0, 'C')
        self.ln(0.5)

    def footer(self):
        self.set_y(-0.5)
        self.set_font('Arial', '', 10)
        self.cell(0, 0.25, "{} of {nb}".format(self.page_no(), nb = "{nb}"), 'T', 0, 'R')

class ADNDPDFGen:
    def __init__(self, char):
        self.character = char
        self.pdf_class = ADNDPDF(self.character.name)
        # We're going to be bad and do the work here so it's only done once.
        self._generate_pdf()

    def output_file(self, filename):
        self.pdf_class.output(name = filename, dest = 'F')

    def output_string(self):
        return self.pdf_class.output(dest = 'S').encode('latin-1')

    def _generate_pdf(self):
        self._generate_page_char()
        self._generate_page_skills()
        self._generate_page_thaco()
        self._generate_page_inventory()

    def _generate_page_char(self):
        self.pdf_class.add_page()

        # Name Block
        self.pdf_class.set_xy(0.75, 1.0)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(0.5, 0, "Name:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 14)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.name), 0, 1, 'L')

        # Basic Stat Block
        self.pdf_class.set_xy(0.75, 1.0)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(5.5, 0, "Level:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 14)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(self.character.get_calcd_stat('level')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 1.20)
        self.pdf_class.set_font('Arial', '', 10)
        self.pdf_class.cell(5.5, 0, "Experience:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 8)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(self.character.get_special_stat('experience')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 1.5)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(5.5, 0, "Hit Points:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 14)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(self.character.get_special_stat('hitpoints')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 1.70)
        self.pdf_class.set_font('Arial', '', 10)
        self.pdf_class.cell(5.5, 0, "Hit Dice:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 8)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(0), 0, 1, 'L')
        
        self.pdf_class.set_xy(0.75, 2.0)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(5.5, 0, "Armor Class:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 14)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(0), 0, 1, 'L')

        # STR Block
        self.pdf_class.set_xy(0.75, 3.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "STR:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('strength')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 3.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "To Hit Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('to_hit_adjust')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 3.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Damage Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('damage_adjust')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 3.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Open Doors:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('open_doors')), 0, 1, 'L')

        # DEX Block
        self.pdf_class.set_xy(3.5, 3.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "DEX:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('dexterity')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 3.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Reaction Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('reaction_adjust')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 3.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Missile Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('missile_adjust')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 3.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Defense Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_calcd_stat('defense_adjust')), 0, 1, 'L')

        # CON Block
        self.pdf_class.set_xy(6.25, 3.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "CON:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('constitution')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 3.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Hit Point Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('constitution')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 3.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "System Shock:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('constitution')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 3.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Res Survival:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('constitution')), 0, 1, 'L')

        # INT Block
        self.pdf_class.set_xy(0.75, 5.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "INT:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('intelligence')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 5.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Max Spell Lvl:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('intelligence')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 5.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "% to Learn:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('intelligence')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 5.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Spells / Lvl:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('intelligence')), 0, 1, 'L')

        # WIS Block
        self.pdf_class.set_xy(3.5, 5.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "WIS:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('wisdom')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 5.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "MD Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('wisdom')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 5.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Bonus Spells:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('wisdom')), 0, 1, 'L')

        self.pdf_class.set_xy(3.5, 5.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "% Fail:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('wisdom')), 0, 1, 'L')

        # CHA Block
        self.pdf_class.set_xy(6.25, 5.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(0.5, 0, "CHA:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('charisma')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 5.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Max Henchmen:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('charisma')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 5.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Loyalty Base:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('charisma')), 0, 1, 'L')

        self.pdf_class.set_xy(6.25, 5.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "Reaction Adj:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(self.character.get_basic_stat('charisma')), 0, 1, 'L')

        # Saving Throws Block
        self.pdf_class.set_xy(0.75, 7.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1.5, 0, "Saving Throws:", 0, 0, 'L')
        #self.pdf_class.set_font('Arial', 'U', 10)
        #self.pdf_class.cell(1, 0, "{0: ^16}".format(self.character.get_basic_stat('intelligence')), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 7.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "PPDM:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 7.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "RSW:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 7.75)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "PP:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 8.0)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "BW:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 8.25)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "SPELL:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 8.5)
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.cell(1, 0, "MR:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 10)
        self.pdf_class.cell(1.5, 0, "{0: ^6}".format(0), 0, 1, 'L')

    def _generate_page_skills(self):
        pass

    def _generate_page_thaco(self):
        pass

    def _generate_page_inventory(self):
        pass