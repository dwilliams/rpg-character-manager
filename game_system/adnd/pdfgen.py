#!/usr/bin/env python3

### IMPORTS ###
from fpdf import FPDF

from game_system.adnd.character import ADNDCharacter

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDPDF(FPDF):
    def __init__(self, char_name, orientation = 'P', unit = 'in', format = 'Letter'):
        super().__init__(orientation = orientation, unit = unit, format = format)
        self.alias_nb_pages()
        self.set_font('Arial', '', 16)
        self.char_name = char_name
        self.set_title("{} - ADND".format(self.char_name))

    def header(self):
        self.set_font('Arial', '', 10)
        self.cell(0, 0.25, "Advanced Dungeons and Dragons", 'B', 0, 'C')
        self.ln(0.5)

    def footer(self):
        self.set_font('Arial', '', 10)
        self.set_y(-0.5)
        self.cell(0, 0.25, "{} of {nb}".format(self.page_no(), nb = "{nb}"), 'T', 0, 'R')
        self.set_y(-0.5)
        self.cell(0, 0.25, "{}".format(self.char_name), '0', 0, 'L')

class ADNDPDFGen:
    def __init__(self, char):
        self.character = char
        self.pdf_class = None
        # We're going to be bad and do the work here so it's only done once.
        self._generate_pdf()

    def output_file(self, filename):
        self.pdf_class.output(name = filename, dest = 'F')

    def output_string(self):
        return self.pdf_class.output(dest = 'S').encode('latin-1')

    def _generate_pdf(self):
        self.pdf_class = ADNDPDF(self.character.name)
        self._generate_page_char()
        self._generate_page_skills()
        self._generate_page_thaco()
        self._generate_inventory()

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
        self.pdf_class.cell(6, 0, "{0: ^16}".format(self.character.get_health()), 0, 1, 'L')

        self.pdf_class.set_xy(0.75, 1.70)
        self.pdf_class.set_font('Arial', '', 10)
        self.pdf_class.cell(5.5, 0, "Hit Dice:", 0, 0, 'R')
        self.pdf_class.set_font('Arial', 'U', 8)
        self.pdf_class.cell(6, 0, "{0: ^16}".format(self.character.get_hit_dice()), 0, 1, 'L')

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
        self.pdf_class.add_page()

        skill_count = 7
        page_count = int(skill_count / 33) # 33 rows
        # Figure out how to go to page 2?
        #row_count = 33
        column_count = 10

        # Page Title Block
        self.pdf_class.set_xy(0.5, 0.8)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(0.5, 0, "Thief Skills", 0, 0, 'L')

        # Page Layout
        self.pdf_class.line(0.75, 1.5, 2.75 + (0.5 * column_count), 1.5)
        row_count = 8 # Only 8 thief skills
        for i in range(row_count):
            self.pdf_class.line(0.75, 1.75 + (0.25 * i), 2.75 + (0.5 * column_count), 1.75 + (0.25 * i))

        self.pdf_class.line(0.75, 1.5, 0.75, 1.5 + (0.25 * row_count))
        self.pdf_class.line(2.75, 1.5, 2.75, 1.5 + (0.25 * row_count))
        for i in range(column_count):
            self.pdf_class.line(3.25 + (0.5 * i), 1.5, 3.25 + (0.5 * i), 1.5 + (0.25 * row_count))

        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.set_xy(0.45, 1.25)
        self.pdf_class.cell(1.25, 0.25, "Skill Name:", 0, 2, 'R')
        self.pdf_class.set_xy(1.45, 1.25)
        self.pdf_class.cell(1.25, 0.25, "Level:", 0, 2, 'R')
        for i in range(column_count):
            self.pdf_class.set_xy(2.75 + (i * 0.5), 1.25)
            if int(self.character.get_calcd_stat('level')) > 10:
                self.pdf_class.cell(0.5, 0.25, str(int(self.character.get_calcd_stat('level')) - i), 0, 2, 'C')
            else:
                self.pdf_class.cell(0.5, 0.25, str(column_count - i), 0, 2, 'C')

        # Character Skill Data
        self.pdf_class.set_xy(1.45, 1.5)
        self.pdf_class.cell(1.25, 0.25, "Pick Pockets", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Open Locks", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Find or Remove Traps", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Move Silently", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Hide in Shadows", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Detect Noise", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Climb Walls", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Read Languages", 0, 2, 'R')
        for i in range(column_count):
            self.pdf_class.set_xy(2.75 + (i * 0.5), 1.55)
            tmp_level = column_count - i
            if int(self.character.get_calcd_stat('level')) > 10:
                tmp_level = int(self.character.get_calcd_stat('level')) - i
            if tmp_level < int(self.character.get_calcd_stat('level')) + 1:
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('pick_pockets', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('open_locks', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('find_remove_traps', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('move_silently', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('hide_shadows', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('detect_noise', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('climb_walls', tmp_level)), 0, 2, 'C')
                self.pdf_class.cell(0.5, 0.25, "{}%".format(self.character.get_thief_skill('read_languages', tmp_level)), 0, 2, 'C')

    def _generate_page_thaco(self):
        self.pdf_class.add_page()

        # Page Title Block
        self.pdf_class.set_xy(0.5, 0.8)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(0.5, 0, "THAC0", 0, 0, 'L')

        # Page Layout
        self.pdf_class.line(1.75, 1.25, 7.75, 1.25)
        self.pdf_class.line(1.75, 1.5, 7.75, 1.5)
        self.pdf_class.line(1.75, 1.75, 7.75, 1.75)
        self.pdf_class.line(1.75, 2.0, 7.75, 2.0)
        self.pdf_class.line(1.75, 2.25, 7.75, 2.25)
        self.pdf_class.line(1.75, 2.5, 7.75, 2.5)
        self.pdf_class.line(1.75, 2.75, 7.75, 2.75)
        self.pdf_class.line(1.75, 3.0, 7.75, 3.0)
        self.pdf_class.line(1.75, 3.25, 7.75, 3.25)
        self.pdf_class.line(1.75, 3.5, 7.75, 3.5)

        self.pdf_class.line(0.75, 4.0, 7.75, 4.0)
        self.pdf_class.line(0.75, 4.25, 7.75, 4.25)
        self.pdf_class.line(0.75, 4.5, 7.75, 4.5)
        self.pdf_class.line(0.75, 4.75, 7.75, 4.75)
        self.pdf_class.line(0.75, 5.0, 7.75, 5.0)
        self.pdf_class.line(0.75, 5.25, 7.75, 5.25)
        self.pdf_class.line(0.75, 5.5, 7.75, 5.5)
        self.pdf_class.line(0.75, 5.75, 7.75, 5.75)
        self.pdf_class.line(0.75, 6.0, 7.75, 6.0)
        self.pdf_class.line(0.75, 6.25, 7.75, 6.25)
        self.pdf_class.line(0.75, 6.5, 7.75, 6.5)
        self.pdf_class.line(0.75, 6.75, 7.75, 6.75)
        self.pdf_class.line(0.75, 7.0, 7.75, 7.0)
        self.pdf_class.line(0.75, 7.25, 7.75, 7.25)
        self.pdf_class.line(0.75, 7.5, 7.75, 7.5)
        self.pdf_class.line(0.75, 7.75, 7.75, 7.75)
        self.pdf_class.line(0.75, 8.0, 7.75, 8.0)
        self.pdf_class.line(0.75, 8.25, 7.75, 8.25)
        self.pdf_class.line(0.75, 8.5, 7.75, 8.5)
        self.pdf_class.line(0.75, 8.75, 7.75, 8.75)
        self.pdf_class.line(0.75, 9.0, 7.75, 9.0)
        self.pdf_class.line(0.75, 9.25, 7.75, 9.25)

        self.pdf_class.line(0.75, 4.0, 0.75, 9.25)
        self.pdf_class.line(1.75, 1.25, 1.75, 9.25)
        self.pdf_class.line(3.25, 1.25, 3.25, 9.25)
        self.pdf_class.line(4.75, 1.25, 4.75, 9.25)
        self.pdf_class.line(6.25, 1.25, 6.25, 9.25)
        self.pdf_class.line(7.75, 1.25, 7.75, 9.25)

        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.set_xy(0.45, 1.25)
        self.pdf_class.cell(1.25, 0.25, "Weapon", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Weight", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Type", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Size", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Speed", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Damage S/M", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Damage L", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Attacks", 0, 2, 'R')
        self.pdf_class.cell(1.25, 0.25, "Range", 0, 2, 'R')

        self.pdf_class.set_xy(0.75, 3.75)
        self.pdf_class.cell(1.0, 0.25, "AC", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "10", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "9", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "8", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "7", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "6", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "5", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "4", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "3", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "2", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "1", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "0", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-1", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-2", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-3", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-4", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-5", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-6", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-7", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-8", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-9", 0, 2, 'C')
        self.pdf_class.cell(1.0, 0.25, "-10", 0, 2, 'C')

        # Weapons & THAC0
        # FIXME: Figure out how to do a second page
        tmp_wpns_list = list(self.character.active_weapons)
        tmp_num_wpns = len(tmp_wpns_list) if len(self.character.active_weapons) < 4 else 4 # Figure out how to go to page 2
        for tmp_i in range(tmp_num_wpns):
            # Grab and fill in Name and Stats from weapon
            # Grab THAC0 and fill in chart
            tmp_x_offset = 1.75 + (tmp_i * 1.5)
            tmp_thaco = self.character.get_thaco_for_weapon(tmp_wpns_list[tmp_i])
            self.pdf_class.set_font('Arial', '', 12)
            self.pdf_class.set_xy(tmp_x_offset, 1.25)
            self.pdf_class.cell(1.5, 0.25, tmp_wpns_list[tmp_i].item_name, 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, str(tmp_wpns_list[tmp_i].get_stat('stat_weight')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, str(tmp_wpns_list[tmp_i].get_stat('stat_type')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, str(tmp_wpns_list[tmp_i].get_stat('stat_size')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, str(tmp_wpns_list[tmp_i].get_stat('stat_speed')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{} + {}".format(tmp_wpns_list[tmp_i].get_stat('stat_damage_sm'), self.character.get_calcd_stat('damage_adjust')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{} + {}".format(tmp_wpns_list[tmp_i].get_stat('stat_damage_l'), self.character.get_calcd_stat('damage_adjust')), 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "?", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, str(tmp_wpns_list[tmp_i].get_stat('stat_range')), 0, 2, 'C')

            self.pdf_class.set_xy(tmp_x_offset, 4.0)
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 10) if tmp_thaco > 11 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 9) if tmp_thaco > 10 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 8) if tmp_thaco > 9 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 7) if tmp_thaco > 8 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 6) if tmp_thaco > 7 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 5) if tmp_thaco > 6 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 4) if tmp_thaco > 5 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 3) if tmp_thaco > 4 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 2) if tmp_thaco > 3 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco - 1) if tmp_thaco > 2 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco) if tmp_thaco > 1 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 1) if tmp_thaco < 20 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 2) if tmp_thaco < 19 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 3) if tmp_thaco < 18 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 4) if tmp_thaco < 17 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 5) if tmp_thaco < 16 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 6) if tmp_thaco < 15 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 7) if tmp_thaco < 14 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 8) if tmp_thaco < 13 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 9) if tmp_thaco < 12 else "", 0, 2, 'C')
            self.pdf_class.cell(1.5, 0.25, "{}".format(tmp_thaco + 10) if tmp_thaco < 11 else "", 0, 2, 'C')

    def _generate_inventory(self):
        tmp_items_list = list(self.character.inventory)
        inv_count = len(tmp_items_list)
        page_count = int(inv_count / 33) + 1 # 33 rows

        for i in range(page_count):
            page_inv_start = i * 33
            self._generate_page_inventory(tmp_items_list[page_inv_start:]) # Sublist without earlier items
        # Blank Page if needed
        if inv_count % 33 > 22:
            self._generate_page_inventory([])

    def _generate_page_inventory(self, inv_sublist):
        self.pdf_class.add_page()

        row_count = 33
        num_items = len(inv_sublist) if len(inv_sublist) < 34 else 33

        # Page Title Block
        self.pdf_class.set_xy(0.5, 0.8)
        self.pdf_class.set_font('Arial', '', 16)
        self.pdf_class.cell(0.5, 0, "Inventory", 0, 0, 'L')

        # Page Layout
        # 0.75 to 7.75: 7, (7 - 0.5) / 2: 3.25
        self.pdf_class.line(0.75, 1.5, 7.75, 1.5)
        for i in range(row_count):
            self.pdf_class.line(0.75, 1.75 + (0.25 * i), 7.75, 1.75 + (0.25 * i))
        self.pdf_class.line(0.75, 1.5, 0.75, 1.5 + (0.25 * row_count))
        self.pdf_class.line(1.25, 1.5, 1.25, 1.5 + (0.25 * row_count))
        self.pdf_class.line(6.75, 1.5, 6.75, 1.5 + (0.25 * row_count))
        self.pdf_class.line(7.75, 1.5, 7.75, 1.5 + (0.25 * row_count))
        # Column Headers
        self.pdf_class.set_font('Arial', '', 12)
        self.pdf_class.set_xy(0.75, 1.25)
        self.pdf_class.cell(0.5, 0.25, "QTY", 0, 2, 'C')
        self.pdf_class.set_xy(1.25, 1.25)
        self.pdf_class.cell(5.5, 0.25, "Name", 0, 2, 'C')
        self.pdf_class.set_xy(6.75, 1.25)
        self.pdf_class.cell(1.0, 0.25, "Value", 0, 2, 'C')

        # Draw character inventory data
        # Left column, then right column
        # FIXME: Handle quantities
        self.pdf_class.set_font('Arial', '', 12)
        for i in range(num_items):
            self.pdf_class.set_xy(0.75, 1.5 + (0.25 * i))
            self.pdf_class.cell(0.5, 0.25, "1", 0, 2, 'C') # QTY
            self.pdf_class.set_xy(1.25, 1.5 + (0.25 * i))
            self.pdf_class.cell(5.5, 0.25, inv_sublist[i].item_name, 0, 2, 'L') # NAME
            self.pdf_class.set_xy(6.75, 1.5 + (0.25 * i))
            self.pdf_class.cell(1.0, 0.25, inv_sublist[i].get_cost('cost_money'), 0, 2, 'R') # VALUE
