#!/usr/bin/env python3

### IMPORTS ###
import enum
import logging

from game_system.exceptions import InvalidObjectTypeException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CombineMethod(enum.Enum):
    OVERWRITE = "overwrite"
    ADD = "add"

class ModifierData:
    def __init__(self, value = None, combine_method = CombineMethod.OVERWRITE):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing - value: %s, combine_method: %s", value, combine_method.name)
        # Variables
        self.value = value # Should this be an enum?
        self.method = combine_method # or 'overload' # Should this be an enum?

    def __str__(self):
        return "ModifierData: [{}] {}".format(self.method.name, self.value)

    def get_value(self):
        self.logger.debug("Start - None")
        return self.value

    def get_combine_method(self):
        self.logger.debug("Start - None")
        return self.method

    def set_combine_method_str(self, method):
        self.logger.debug("Start - method: %s", method)
        self.method = CombineMethod(method)

class ModifierDataCombiner:
    def __init__(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing - None")
        # Variables
        self.items_to_combine = []

    def __str__(self):
        return "ModifierDataCombiner: {}".format(len(self.items_to_combine))

    def add_item(self, item):
        self.logger.debug("Start - item: %s", str(item))
        # Check to make sure the item is a ModifierData
        if not isinstance(item, ModifierData):
            raise InvalidObjectTypeException
        self.items_to_combine.append(item)

    def resolve(self, base):
        self.logger.debug("Start - base: %s", base)
        tmp_value = base
        # Integer type modifier:
        if isinstance(tmp_value, int):
            # Add all of the "add" items
            for item in self.items_to_combine:
                if item.get_combine_method() == CombineMethod.ADD:
                    tmp_value = tmp_value + int(item.get_value())
            # Check each overwrite to see if it's larger than the total of the adds
            for item in self.items_to_combine:
                if item.get_combine_method() == CombineMethod.OVERWRITE:
                    if int(item.get_value()) > tmp_value:
                        tmp_value = int(item.get_value())
        # String type modifier:
        else:
            # Check each overwrite...
            #   Can't really compare strings, so just used the last one in the list
            for item in self.items_to_combine:
                if item.get_combine_method() == CombineMethod.OVERWRITE:
                    tmp_value = item.get_value()
        return tmp_value
