import pygame
from pygame.locals import *

# to change screen dimensions
# pygame.display.set_mode((1600, 900))

def setFullScreen(screen, size, set):
    if set:
        return pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode(size, 0)