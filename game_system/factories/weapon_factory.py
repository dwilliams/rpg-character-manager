#!/usr/bin/env python3

### IMPORTS ###
from game_system.factories.item_factory import ItemFactory

from game_system.none import Weapon
from game_system.adnd import ADNDWeapon
from game_system.shadowrun import ShadowRunWeapon

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class WeaponFactory(ItemFactory):
    creation_classes = {
        "none": Weapon,
        "adnd": ADNDWeapon,
        "shadowrun": ShadowRunWeapon
    }
    object_type = 'weapon'