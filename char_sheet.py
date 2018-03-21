#!/usr/bin/env python3

### IMPORT ###
import logging
import pygame

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CMCharSheetOne:
    def __init__(self, width, height):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height)) # Make a surface to blit everything down.

        self.sections = [] # Sections of the sheet.  Add tuples with section objects and rects for placement.
                           # Placements are tuples with x, y locations

        self.sections.append((object(), (0, 0)))

    def draw(self):
        self.logger.debug("Starting drawing")

        for section in self.sections:
            self.logger.debug("Drawing section %s at placement %s", section[0], section[1])
            # Need to add isDirty logic here
            # section.draw stuff here
            # self.surface.blit stuff here too

        return self.surface

### MAIN ###
if __name__ == '__main__':
    pass
