import pygame, sys
from pygame.locals import *

from player import Player
player = Player()

def checkForQuitEvent():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # questo controllo dell'evento serve a terminare il
        # programma se l'utente preme la X di windows
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

def mouseClickEvent():
    for event in pygame.event.get():
        # with this we check if the player press the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True
        return False