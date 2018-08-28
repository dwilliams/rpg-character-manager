#!/usr/bin/env python3

### IMPORTS ###
from game_system.item_factory import ItemFactory

from game_system.none import Equipment
from game_system.shadowrun import ShadowRunEquipment

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class EquipmentFactory(ItemFactory):
    creation_classes = {
        "none": Equipment,
        "shadowrun": ShadowRunEquipment
    }
    object_type = 'equipment'
