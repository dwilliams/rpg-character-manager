#!/usr/bin/env python3

### IMPORTS ###
#import logging

import bisect

from game_system.exceptions import GameSystemMismatchException
from game_system.exceptions import ItemNotActiveException
from game_system.exceptions import InvalidCharacterStatTypeException
from game_system.exceptions import InvalidObjectTypeException
from game_system.exceptions import BadDataException

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
    special_stats_types = ['experience', 'comeliness']

    class_types = ['warrior', 'wizard', 'priest', 'rogue']

    # Class = string
    # Skills = ?

    def __init__(self, name=''):
        # Ensure the parent's __init__ is called
        super().__init__(name=name)

        # Initialize basic and special stats to creation defaults
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

    def __str__(self):
        return "ADND{}".format(super().__str__())

    def load_dict(self, char_dict, item_factory, equipment_factory, weapon_factory):
        self.logger.debug("Start - char_dict: %s", str(char_dict))
        super().load_dict(char_dict, item_factory, equipment_factory, weapon_factory)

        self.hit_dice = char_dict['data']['hit_dice'][0:10] # Should this be checked to make sure it's a list?

        self.thief_skills = char_dict['data']['thief_skills'] # Should this be checked to make sure it's the right data
                                                              # structure?  Really, should this be a class?

        self.logger.debug("End - None")

    def save_dict(self):
        self.logger.debug("Start - None")
        char_dict = super().save_dict()

        char_dict['data']['hit_dice'] = self.hit_dice

        char_dict['data']['thief_skills'] = self.thief_skills

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
        if stat_name == 'level':
            return self._get_level()
        # STR based stats
        elif stat_name == 'to_hit_adjust':
            tmp_stat = self.get_basic_stat('strength')
            self.logger.debug("stat strength: %d", tmp_stat)
            tmp_value = DATA_ABILITY['strength'][tmp_stat]['hit_probability']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        elif stat_name == 'damage_adjust':
            tmp_stat = self.get_basic_stat('strength')
            self.logger.debug("stat strength: %d", tmp_stat)
            tmp_value = DATA_ABILITY['strength'][tmp_stat]['damage_adjust']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        elif stat_name == 'open_doors':
            tmp_stat = self.get_basic_stat('strength')
            self.logger.debug("stat strength: %d", tmp_stat)
            tmp_value = DATA_ABILITY['strength'][tmp_stat]['open_doors']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        # DEX based stats
        elif stat_name == 'reaction_adjust':
            tmp_stat = self.get_basic_stat('dexterity')
            self.logger.debug("stat dexterity: %d", tmp_stat)
            tmp_value = DATA_ABILITY['dexterity'][tmp_stat]['reaction_adjust']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        elif stat_name == 'missile_adjust':
            tmp_stat = self.get_basic_stat('dexterity')
            self.logger.debug("stat dexterity: %d", tmp_stat)
            tmp_value = DATA_ABILITY['dexterity'][tmp_stat]['missile_attack_adjust']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        elif stat_name == 'defense_adjust':
            tmp_stat = self.get_basic_stat('dexterity')
            self.logger.debug("stat dexterity: %d", tmp_stat)
            tmp_value = DATA_ABILITY['dexterity'][tmp_stat]['defensive_adjust']
            self.logger.debug("stat value: %d", tmp_value)
            return tmp_value
        # CON based stats
        # INT based stats
        # WIS based stats
        # CHA based stats
        else:
            raise InvalidCharacterStatTypeException()

    def _get_level(self):
        self.logger.debug("Start - None")
        exp = self.get_special_stat('experience')
        self.logger.debug("Experience: %d", exp)
        tmp_exp_list = [DATA_LEVEL['rogue'][tmp_i]['experience'] for tmp_i in DATA_LEVEL['rogue'].keys()] # FIXME: Move to character class variable
        self.logger.debug("Experience TMP: %s", tmp_exp_list)
        pos = bisect.bisect_right(tmp_exp_list, exp)
        self.logger.debug("Bisect Position: %d", pos)
        return pos

    def get_thaco_for_weapon(self, weapon):
        self.logger.debug("Start - weapon: %s", weapon)
        # Get starting thac0 based on level
        tmp_thaco = DATA_LEVEL['rogue'][self._get_level()]['thac0'] # FIXME: Move to character class variable
        # Check for spec based modifiers
        tmp_thaco = tmp_thaco - self.get_calcd_stat('to_hit_adjust')
        # Check for weapon modifiers
        if weapon not in self.active_weapons:
            raise ItemNotActiveException
        tmp_thaco = tmp_thaco - weapon.get_stat('stat_to_hit_adjust')
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
        for tmp_i in self.hit_dice[0:(DATA_LEVEL['rogue'][self._get_level()]['hitdice'])]:
            tmp_result = tmp_result + tmp_i
        # FIXME: Don't forget to add the levelhp for levels above 10
        self.logger.debug("End - health: %s", tmp_result)
        return tmp_result

    def get_hit_dice(self):
        self.logger.debug("Start - None")
        tmp_result = "{} + {}".format(
            DATA_LEVEL['rogue'][self._get_level()]['hitdice'],
            DATA_LEVEL['rogue'][self._get_level()]['levelhp']
        )
        self.logger.debug("End - hit_dice_str: %s", tmp_result)
        return tmp_result

    def get_thief_skill(self, thief_skill, level = 0):
        self.logger.debug("Start - thief_skill: %s, level: %d", thief_skill, level)
        tmp_thief_skill = "thief_{}".format(thief_skill)
        tmp_level = int(self._get_level() if level == 0 else level)
        tmp_result = 0
        for i in self.thief_skills[thief_skill][0:tmp_level]:
            tmp_result = tmp_result + i # Adding percents
        self.logger.debug("Level add ups: %d", tmp_result)
        if tmp_thief_skill in DATA_ABILITY['dexterity'][self.get_basic_stat('dexterity')]:
            tmp_result = tmp_result + DATA_ABILITY['dexterity'][self.get_basic_stat('dexterity')][tmp_thief_skill]
        self.logger.debug("Stat Modifier add ups: %d", tmp_result)
        return tmp_result
