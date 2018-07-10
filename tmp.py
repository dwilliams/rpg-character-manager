#!/usr/bin/env python3

### IMPORTS ###
import logging
import os

import game_system
import game_system.shadowrun

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    log_format = "%(asctime)s:%(levelname)s:%(name)s.%(funcName)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    sr_ef = game_system.shadowrun.ShadowRunEquipmentFactory()

    sr_e_1 = sr_ef.create("Muscle Augmentation - Level 1")
    sr_e_2 = sr_ef.create("Muscle Augmentation - Level 2")

if __name__ == '__main__':
    main()
