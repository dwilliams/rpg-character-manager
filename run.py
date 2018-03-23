#!/usr/bin/env python3

### IMPORT ###
import logging
import pygame

import char_sheet

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Init Logging
    logging.basicConfig(level=logging.DEBUG)

    # Init Engine
    logging.debug("Initializing Engine")
    pygame.init()
    pygame.font.init()

    # Init Values
    logging.debug("Initializing Values")
    screen_size = screen_width, screen_height = 850 // 2, 1100 // 2
    frame_rate = 30
    stop_event_loop = False
    color_background = pygame.Color('blue')

    # Setup screen, et. al.
    logging.debug("Setting up Engine Components")
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    frame_clock = pygame.time.Clock()

    # Setup assets
    logging.debug("Setting up Assets")
    font_default_fps = pygame.font.Font(None, 20)

    ### Test Asset ###
    cmcharsheetone = char_sheet.CMCharSheet()

    # Event Loop
    logging.debug("Starting Event Loop")
    while not stop_event_loop:
        # Process events
        logging.debug("Processing Events")
        for event in pygame.event.get():
            logging.debug("Event Type: %s (%d)", pygame.event.event_name(event.type), event.type)
            if event.type == pygame.QUIT:
                stop_event_loop = True
            if event.type == pygame.VIDEORESIZE:
                screen_size = screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

        # Do more stuff, e.g. draw
        text = "FPS: {}".format(frame_clock.get_fps())
        #text_width, text_height = font_default_fps.size(text)
        surface_fps = font_default_fps.render(text, True, pygame.Color('red'), color_background)

        ### Test Asset ###
        cm_surface = cmcharsheetone.draw(screen_width, screen_height - 20)

        # Fill, Blit, and Flip the screen
        logging.debug("Filling, Blitting, and Flipping")
        screen.fill(color_background)

        # // makes integer division in python3
        screen.blit(surface_fps, (10, screen_height - 20))
        screen.blit(cm_surface, (0, 0))

        pygame.display.flip()

        # Tick the frame_clock to help control the frame rate
        logging.debug("Frame Rate Control - raw_time: %d, time: %d", frame_clock.get_rawtime(), frame_clock.get_time())
        frame_clock.tick(frame_rate)

    # Teardown

if __name__ == '__main__':
    main()
