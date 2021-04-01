#!/usr/bin/env python3

### IMPORTS ###
#import logging

import bisect

from game_system.exceptions import GameSystemMismatchException
from game_system.exceptions import ItemNotActiveException
from game_system.exceptions import InvalidCharacterStatTypeException
from game_system.exceptions import InvalidObjectTypeException
from game_system.exceptions import BadDataException

from game_system.modifierdata import ModifierDataCombiner

from game_system.none.character import Character

from game_system.adnd.equipment import ADNDEquipment
from game_system.adnd.item import ADNDItem
from game_system.adnd.weapon import ADNDWeapon

from game_system.adnd.data_ability import DATA_ABILITY
from game_system.adnd.data_level import DATA_LEVEL

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDCharacter(Character):
    game_system = 'adnd'

    class_equipment = ADNDEquipment
    class_item = ADNDItem
    class_weapon = ADNDWeapon

    basic_stats_types = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    special_stats_types = ['comeliness']

    # FIXME: Should probably make this a series of python classes so character
    #        classes like 'thief' and 'bard' can expand on 'rogue'.
    class_types = ['warrior', 'wizard', 'priest', 'rogue']

    weapon_penalties = {
        'rogue': 3,
        'warrior': 2,
        'wizard': 5,
        'priest': 3
    }

    # Class = string

    def __init__(self, name=''):
        # Ensure the parent's __init__ is called
        super().__init__(name=name)

        # Initialize basic and special stats to creation defaults
        self.experience = [0]
        self.hit_dice = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Should be 10 hit dice max for character in ADND

        # Skills
        self.thief_skills = {
            'pick_pockets': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'open_locks': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'find_remove_traps': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'move_silently': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'hide_shadows': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'detect_noise': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'climb_walls': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'read_languages': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }

        self.weapon_proficienies = []
        self.nonweapon_proficienies = []

    def __str__(self):
        return "ADND{}".format(super().__str__())

    def load_dict(self, char_dict, item_factory, equipment_factory, weapon_factory):
        self.logger.debug("Start - char_dict: %s", str(char_dict))
        super().load_dict(char_dict, item_factory, equipment_factory, weapon_factory)

        self.experience = char_dict['data']['experience']
        self.hit_dice = char_dict['data']['hit_dice'][0:10] # Should this be checked to make sure it's a list?

        self.thief_skills = char_dict['data']['thief_skills'] # Should this be checked to make sure it's the right data
                                                              # structure?  Really, should this be a class?

        self.weapon_proficienies = char_dict['data']['weapon_proficienies']
        self.nonweapon_proficienies = char_dict['data']['nonweapon_proficienies']

        self.logger.debug("End - None")

    def save_dict(self):
        self.logger.debug("Start - None")
        char_dict = super().save_dict()

        char_dict['data']['experience'] = self.experience
        char_dict['data']['hit_dice'] = self.hit_dice

        char_dict['data']['thief_skills'] = self.thief_skills

        char_dict['data']['weapon_proficienies'] = self.weapon_proficienies
        char_dict['data']['nonweapon_proficienies'] = self.nonweapon_proficienies

        self.logger.debug("End - char_dict: %s", char_dict)
        return char_dict

    def _check_item_type(self, item):
        self.logger.debug("Start - item: %s", str(item))
        if item.game_system != self.game_system:
            raise GameSystemMismatchException()
        if not isinstance(item, (ADNDItem, ADNDEquipment, ADNDWeapon)):
            raise InvalidObjectTypeException()

    def get_calcd_stat(self, stat_name):
        self.logger.debug("Start - stat_name: %s", str(stat_name))
        tmp_value = 0
        # STR based stats
        if stat_name in DATA_ABILITY['strength']['1']:
            tmp_stat = self.get_basic_calcd_stat('strength')
            self.logger.debug("stat strength: %s", tmp_stat)
            tmp_value = DATA_ABILITY['strength'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        # DEX based stats
        elif stat_name in DATA_ABILITY['dexterity']['1']:
            tmp_stat = self.get_basic_calcd_stat('dexterity')
            self.logger.debug("stat dexterity: %s", tmp_stat)
            tmp_value = DATA_ABILITY['dexterity'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        # CON based stats
        elif stat_name in DATA_ABILITY['constitution']['1']:
            tmp_stat = self.get_basic_calcd_stat('constitution')
            self.logger.debug("stat constitution: %s", tmp_stat)
            tmp_value = DATA_ABILITY['constitution'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        # INT based stats
        elif stat_name in DATA_ABILITY['intelligence']['1']:
            tmp_stat = self.get_basic_calcd_stat('intelligence')
            self.logger.debug("stat intelligence: %s", tmp_stat)
            tmp_value = DATA_ABILITY['intelligence'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        # WIS based stats
        elif stat_name in DATA_ABILITY['wisdom']['1']:
            tmp_stat = self.get_basic_calcd_stat('wisdom')
            self.logger.debug("stat wisdom: %s", tmp_stat)
            tmp_value = DATA_ABILITY['wisdom'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        # CHA based stats
        elif stat_name in DATA_ABILITY['charisma']['1']:
            tmp_stat = self.get_basic_calcd_stat('charisma')
            self.logger.debug("stat charisma: %s", tmp_stat)
            tmp_value = DATA_ABILITY['charisma'][tmp_stat][stat_name]
            self.logger.debug("stat value: %s", tmp_value)
            #return tmp_value
        else:
            raise InvalidCharacterStatTypeException()
        self.logger.debug("End - tmp_value: %s", tmp_value)
        return tmp_value

    def get_experience(self):
        self.logger.debug("Start - None")
        exp_list = self.experience
        exp = 0
        for i in exp_list:
            exp = exp + int(i)
        self.logger.debug("Experience: %d", exp)
        return exp

    def get_level(self):
        self.logger.debug("Start - None")
        exp = self.get_experience()
        self.logger.debug("Experience: %d", exp)
        tmp_exp_list = [DATA_LEVEL['rogue'][tmp_i]['experience'] for tmp_i in DATA_LEVEL['rogue'].keys()] # FIXME: Move to character class variable
        self.logger.debug("Experience TMP: %s", tmp_exp_list)
        pos = bisect.bisect_right(tmp_exp_list, exp)
        self.logger.debug("Bisect Position: %d", pos)
        return pos

    def get_thaco_base(self):
        self.logger.debug("Start - None")
        # Get starting thac0 based on level
        tmp_thaco = DATA_LEVEL['rogue'][self.get_level()]['thac0'] # FIXME: Move to character class variable
        self.logger.debug("End - thac0: %s", tmp_thaco)
        return tmp_thaco


    def get_thaco_with_equipment(self):
        self.logger.debug("Start - None")
        tmp_thaco = self.get_thaco_base()
        # Check for spec based modifiers
        tmp_thaco = tmp_thaco - self.get_calcd_stat('hit_probability')
        # Check for modifications due to equipment
        tmp_mdc = ModifierDataCombiner()
        for tmp_item in self.inventory.get_equipment():
            tmp_mdc.add_item(tmp_item.get_mod('mod_hit_probability')) # FIXME: Should there be a mod for hit_probability
        self.logger.debug("number of items: %d", len(tmp_mdc.items_to_combine))
        tmp_thaco = tmp_thaco - tmp_mdc.resolve(0)
        self.logger.debug("End - thac0: %s", tmp_thaco)
        return tmp_thaco

    def get_thaco_for_weapon(self, weapon):
        self.logger.debug("Start - weapon: %s", weapon)
        # FIXME: Make this work for ranged weapons (e.g. dex instead of str
        tmp_thaco = self.get_thaco_with_equipment()
        # Check for weapon modifiers
        if weapon not in self.inventory.get_weapons():
            raise ItemNotActiveException
        tmp_thaco = tmp_thaco - weapon.get_stat('stat_to_hit_adjust')
        self.logger.debug("after weapon to hit - tmp_thaco: %s", tmp_thaco)
        # Check for weapon proficiencies
        if not weapon.get_stat('stat_proficiency_type') in self.weapon_proficienies:
            self.logger.debug("weapon proficiency not found: %s", weapon.get_stat('stat_proficiency_type'))
            tmp_thaco = tmp_thaco + self.weapon_penalties['rogue'] # FIXME: Make penalty based on subclass
        if "specialize_{}".format(weapon.get_stat('stat_proficiency_type')) in self.weapon_proficienies:
            # For melee weapons
            tmp_thaco = tmp_thaco - 1
        self.logger.debug("End - thac0: %s", tmp_thaco)
        return tmp_thaco

    def get_thaco_for_weapon_offhand(self, weapon):
        self.logger.debug("Start - weapon: %s", weapon)
        tmp_thaco = self.get_thaco_for_weapon(weapon)
        # Check for offhand proficiencies
        # FIXME: Figure out how to handle dex vs penalty
        # FIXME: Figure out what "two weapon fighting" does for this
        tmp_thaco = tmp_thaco + 2 # Just using this for now
        self.logger.debug("End - thac0: %s", tmp_thaco)
        return tmp_thaco

    def add_hit_dice(self, index, roll):
        self.logger.debug("Start - index: %s, roll: %s", index, roll)
        if index > 10: # len(self.hit_dice) which should always be 10 for ADND, using index starting at 1
            raise BadDataException()
        self.hit_dice[index - 1] = roll # FIXME: Should eventually add checks for max roll based on class.
        self.logger.debug("End - None")

    def get_health(self):
        self.logger.debug("Start - None")
        # Add up all hit_dice rolls for level
        tmp_result = 0
        for tmp_i in self.hit_dice[0:(DATA_LEVEL['rogue'][self.get_level()]['hitdice'])]:
            tmp_result = tmp_result + tmp_i
        # FIXME: Don't forget to add the levelhp for levels above 10
        self.logger.debug("End - health: %s", tmp_result)
        return tmp_result

    def get_hit_dice(self):
        self.logger.debug("Start - None")
        tmp_result = "{} + {}".format(
            DATA_LEVEL['rogue'][self.get_level()]['hitdice'],
            DATA_LEVEL['rogue'][self.get_level()]['levelhp']
        )
        self.logger.debug("End - hit_dice_str: %s", tmp_result)
        return tmp_result

    def get_saving_throw(self, type):
        self.logger.debug("Start - Type: %s", type)
        tmp_result = 20
        if type in DATA_LEVEL['rogue'][self.get_level()]['saving_throws']:
            tmp_result = DATA_LEVEL['rogue'][self.get_level()]['saving_throws'][type]
        self.logger.debug("End - Value: %s", tmp_result)
        return tmp_result

    def get_thief_skill(self, thief_skill, level = 0):
        self.logger.debug("Start - thief_skill: %s, level: %d", thief_skill, level)
        base_thief_skills = {
            "pick_pockets": 15,
            "open_locks": 10,
            "find_remove_traps": 5,
            "move_silently": 10,
            "hide_shadows": 5,
            "detect_noise": 15,
            "climb_walls": 60,
            "read_languages": 0
        }
        tmp_thief_skill = "thief_{}".format(thief_skill)
        tmp_level = int(self.get_level() if level == 0 else level)
        tmp_result = base_thief_skills[thief_skill]
        for i in self.thief_skills[thief_skill][0:tmp_level]:
            tmp_result = tmp_result + i # Adding percents
        self.logger.debug("Level add ups: %d", tmp_result)
        if tmp_thief_skill in DATA_ABILITY['dexterity'][self.get_basic_calcd_stat('dexterity')]:
            tmp_result = tmp_result + DATA_ABILITY['dexterity'][self.get_basic_calcd_stat('dexterity')][tmp_thief_skill]
        self.logger.debug("Stat Modifier add ups: %d", tmp_result)
        return tmp_result
