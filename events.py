import pygame, sys
from pygame.locals import *

from player import Player
player = Player()

def checkForQuitEvent():
    for event in pygame.event.get():
        # questo controllo dell'evento serve a terminare il
        # programma se l'utente preme la X di windows
        if event.type == QUIT:
            pygame.quit()
            sys.exit()