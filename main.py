# Simple pygame program

# Import and initialize the pygame library
import pygame as pg

pg.init()

# Import other dependencies
import numpy as np

# Import all user made function and classes
from Entity import *

# Global variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the drawing window and time
SCREEN = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
CLOCK = pg.time.Clock()

# player
player = Entity([0, 0], [0, 0], [5, 5])

# Run until the user asks to quit
running = True
dt = 0  # First step delta time is zero
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background with white
    SCREEN.fill((255, 255, 255))

    # Update
    player.update(dt)

    # Draw
    player.draw(SCREEN)

    # Flip the display
    pg.display.flip()

    # Maintain FPS
    dt = CLOCK.tick(60)
    print(dt)

# Done! Time to quit.
pg.quit()
