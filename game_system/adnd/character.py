#!/usr/bin/env python3

### IMPORTS ###
#import logging

import bisect

from game_system.exceptions import GameSystemMismatchException
from game_system.exceptions import InvalidCharacterStatTypeException

from game_system.none.character import Character

from game_system.adnd.data_ability import DATA_ABILITY

### GLOBALS ###


LEVELING_DATA = {
    'rogue': {
        0: {
            'level': 1,
            'hitdice': 1,
            'levelhp': 0
        },
        1250: {
            'level': 2,
            'hitdice': 2,
            'levelhp': 0
        },
        2500: {
            'level': 3,
            'hitdice': 3,
            'levelhp': 0
        },
        5000: {
            'level': 4,
            'hitdice': 4,
            'levelhp': 0
        },
        10000: {
            'level': 5,
            'hitdice': 5,
            'levelhp': 0
        },
        20000: {
            'level': 6,
            'hitdice': 6,
            'levelhp': 0
        },
        40000: {
            'level': 7,
            'hitdice': 7,
            'levelhp': 0
        },
        70000: {
            'level': 8,
            'hitdice': 8,
            'levelhp': 0
        },
        110000: {
            'level': 9,
            'hitdice': 9,
            'levelhp': 0
        },
        160000: {
            'level': 10,
            'hitdice': 10,
            'levelhp': 0
        },
        220000: {
            'level': 11,
            'hitdice': 10,
            'levelhp': 2
        },
        440000: {
            'level': 12,
            'hitdice': 10,
            'levelhp': 4
        },
        660000: {
            'level': 13,
            'hitdice': 10,
            'levelhp': 6
        },
        880000: {
            'level': 14,
            'hitdice': 10,
            'levelhp': 8
        },
        1100000: {
            'level': 15,
            'hitdice': 10,
            'levelhp': 10
        },
        1320000: {
            'level': 16,
            'hitdice': 10,
            'levelhp': 12
        },
        1540000: {
            'level': 17,
            'hitdice': 10,
            'levelhp': 14
        },
        1760000: {
            'level': 18,
            'hitdice': 10,
            'levelhp': 16
        },
        1980000: {
            'level': 19,
            'hitdice': 10,
            'levelhp': 18
        },
        2200000: {
            'level': 20,
            'hitdice': 10,
            'levelhp': 20
        }
    },
    'warrior': {
    },
    'wizard': {
    },
    'priest': {
    }
}

### FUNCTIONS ###

### CLASSES ###
class ADNDCharacter(Character):
    game_system = 'adnd'

    basic_stats_types = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    special_stats_types = ['hitpoints', 'experience', 'comeliness']

    class_types = ['warrior', 'wizard', 'priest', 'rogue']

    # Class = string
    # Skills = ?

    def __init__(self, name=''):
        # Ensure the parent's __init__ is called
        super().__init__(name=name)

        # Initialize basic and special stats to creation defaults
        self.special_stats['health'] = 6

    def __str__(self):
        return "ADND{}".format(super().__str__())

    def load_dict(self, char_dict):
        self.logger.debug("Start - char_dict: %s", str(char_dict))
        super().load_dict(char_dict)

    def save_dict(self):
        self.logger.debug("Start - None")
        char_dict = super().save_dict()
        return char_dict

    def _check_item_type(self, item):
        self.logger.debug("Start - item: %s", str(item))
        #if not isinstance(item, ADNDItem):
        if item.game_system != self.game_system:
            raise GameSystemMismatchException()

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
        exp_list = list(LEVELING_DATA['rogue'].keys())
        self.logger.debug("Experience: %s", exp_list)
        pos = bisect.bisect_right(exp_list, exp)
        self.logger.debug("Bisect Position: %d", pos)
        return LEVELING_DATA['rogue'][exp_list[pos-1]]['level']
