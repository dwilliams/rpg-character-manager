#!/usr/bin/env python3

# pylint: disable=too-few-public-methods

### IMPORTS ###
#import logging

from game_system.shadowrun.bioware import ShadowRunBioware

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class MuscleAugmentationLevelOne(ShadowRunBioware):
    game_system = 'shadowrun'
    item_name = 'Muscle Augmentation - Level 1'

    mod_quickness = 1
    mod_strength = 1
    body_cost = 0.8
    money_cost = 45000

class MuscleAugmentationLevelTwo(ShadowRunBioware):
    game_system = 'shadowrun'
    item_name = 'Muscle Augmentation - Level 2'

    mod_quickness = 2
    mod_strength = 2
    body_cost = 1.6
    money_cost = 90000
