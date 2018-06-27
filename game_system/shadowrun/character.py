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

    basic_stats_types = ['body', 'quickness', 'strength', 'charisma', 'intelligence', 'wisdom']
    special_stats_types = ['essence', 'magic']

    def __init__(self, name = ''):
        # Ensure the parent's __init__ is called
        super().__init__(name = name)

        # Initialize basic and special stats to creation defaults
        self.special_stats['essence'] = 6

    def __str__(self):
        return "ShadowRun{}".format(super().__str__())

    def load_dict(self, char_dict):
        if not char_dict['game_system'] == self.game_system:
            raise GameSystemMismatchException()

        # Load the basic character stats
        self.name = char_dict['name']

        # Load the inventory & equipment

    def save_dict(self):
        to_save_dict = {}

        # Save the basic character stats
        to_save_dict['game_system'] = self.game_system
        to_save_dict['name'] = self.name
        
        # Save the inventory & equipment
        
        return to_save_dict

    def _check_item_type(self, item):
        if not isinstance(item, ShadowRunItem):
            raise GameSystemMismatchException()

    def _get_basic_stat_game_system_specials(self, stat_name):
        # Override this for special modifiers for game systems (e.g. biowares in ShadowRun)
        # Add strength for biowares
        # Add strength for cyberwares
        return 0

### MAIN ###
def main():
    pass

if __name__ == '__main__':
    main()
