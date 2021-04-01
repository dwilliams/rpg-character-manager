#!/usr/bin/env python3

### IMPORTS ###
from game_system.none import Equipment

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ADNDEquipment(Equipment):
    # pylint: disable=too-few-public-methods
    game_system = 'adnd'

    mod_types = [
        # Basic Stats
        'mod_strength',
        'mod_dexterity',
        'mod_constitution',
        'mod_intelligence',
        'mod_wisdom',
        'mod_charisma',
        # Strength
        'mod_hit_probability',
        'mod_damage_adjust',
        'mod_weight_allowance',
        'mod_max_press',
        'mod_open_doors',
        'mod_open_doors_locked_magic',
        'mod_bend_bars_lift_gates',
        # Dexterity
        'mod_reaction_adjust',
        'mod_missile_attack_adjust',
        'mod_defensive_adjust',
        'mod_thief_pick_pockets',
        'mod_thief_open_locks',
        'mod_thief_find_remove_traps',
        'mod_thief_move_silently',
        'mod_thief_hide_shadows',
        # Constitution
        'mod_hit_point_adjust',
        'mod_hit_point_adjust_warrior',
        'mod_system_shock',
        'mod_resurrection_survival',
        'mod_poison_save',
        'mod_regeneration',
        # Intelligence
        'mod_num_languages',
        'mod_spell_level',
        'mod_learn_spell_chance',
        'mod_max_spells_per_level',
        'mod_spell_immunity',
        # Wisdom
        'mod_magic_defense',
        'mod_bonus_spells',
        'mod_spell_failure_chance',
        'mod_spell_immunity',
        # Charisma
        'mod_max_num_henchmen',
        'mod_loyalty_base',
        'mod_reaction_adjust'
    ]
    cost_types = ['cost_money']

    def __str__(self):
        return "ADNDEquipment: {}".format(self.item_name)
