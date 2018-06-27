#!/usr/bin/env python3

### IMPORT ###
import logging
import pygame

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CMCharSheet:
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        self.width = 0
        self.height = 0
        self.surface = None

        self.sections = [] # Sections of the sheet.  Add tuples with section objects and rects for placement.
                           # Placements are tuples with x, y locations

        self.sections.append((CharSheetField(), (0, 0)))

    def draw(self, width, height):
        self.logger.debug("Starting drawing")

        if self.width != width or self.height != height:
            self.width = width
            self.height = height
            self.surface = pygame.Surface((self.width, self.height))

        for section in self.sections:
            self.logger.debug("Drawing section %s at placement %s", section[0], section[1])
            # Need to add isDirty logic here
            # section.draw stuff here
            # self.surface.blit stuff here too
            tmp_surface = section[0].draw(width, height)
            self.surface.blit(tmp_surface, section[1])

        return self.surface

class CharSheetField:
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        self.width = 0
        self.height = 0
        self.surface = None
        
        self.label = "Label"
        self.value = "Value"
        self.color_background = pygame.Color('white')
        self.color_border = pygame.Color('black')
        self.color_thickness = 1
        self.isDirty = True

    def draw(self, width, height):
        self.logger.debug("Starting drawing")

        if self.width != width or self.height != height:
            self.width = width
            self.height = height
            self.isDirty = True
            self.surface = pygame.Surface((self.width, self.height))

        if self.isDirty:
            self.surface.fill(self.color_background)
            pygame.draw.rect(self.surface, self.color_border, pygame.Rect(0, 0, self.width, self.height), self.color_thickness)
            #self.isDirty = False

        return self.surface

    def update(self, value):
        self.value = value
        self.isDirty = True

    def mark_dirty(self):
        self.isDirty = True

### MAIN ###
if __name__ == '__main__':
    pass
