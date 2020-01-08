# Integrated modules
import sys, os

# Installed modules
import pygame

# Local files
from myutils import colors, consts, options

# Set up Pygame window
pygame.init()
win = pygame.display.set_mode(consts.WN_RES)
pygame.display.set_caption(consts.WN_TITLE)

# Other setups

# Mainloop

running = 1
clock = pygame.time.Clock()
FPS = consts.WN_FPS

while running:
    clock.tick_busy_loop(FPS)
    deltaTime = clock.get_time()
    if running == 1:
        deltaTime = 0
        running = 2
    elif running == 2:
        WN_FPS = min(1 / (2 / consts.WN_FPS - deltaTime), 240)  # Hold FPS stable

    # Events
    events = pygame.event.get()
    keyStrokes = pygame.key.get_pressed()

    # Update
    for e in events:
        if e.type == pygame.QUIT:
            running = False
            break

    # Draw
    win.fill(colors.rgb("#fff"))
    pygame.display.flip()

# Quit

pygame.quit()
