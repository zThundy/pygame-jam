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
        
    keys = pygame.key.get_pressed()
    # if left key is pressed down (a) remove value from x coordinates
    if keys[K_LEFT]:
        player.setPosition(player.getPosition()[0] - 1, player.getPosition()[1])
    # if right key is pressed down (d) add value to x coordinates
    if keys[K_RIGHT]:
        player.setPosition(player.getPosition()[0] + 1, player.getPosition()[1])
    # if up key is pressed down (w) remove value to y coordinates
    if keys[K_UP]:
        player.setPosition(player.getPosition()[0], player.getPosition()[1] - 1)
    # if down key is pressed down (s) add value to y coordinates
    if keys[K_DOWN]:
        player.setPosition(player.getPosition()[0], player.getPosition()[1] + 1)

    return player.getPosition()