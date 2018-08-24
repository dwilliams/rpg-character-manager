#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CharacterInvalidStatTypeException(Exception):
    pass

class GameSystemMismatchException(Exception):
    pass

class ItemNotEquipableException(Exception):
    pass

class ItemNotExistsException(Exception):
    pass

class ItemNotInInventoryException(Exception):
    pass

class NotCharacterException(Exception):
    pass

class BadFactoryTypeException(Exception):
    pass

class InvalidObjectTypeException(Exception):
    pass

class InvalidGameSystemException(Exception):
    pass

class InvalidItemAttributeException(Exception):
    pass
