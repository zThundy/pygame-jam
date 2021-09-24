import pygame, sys
from pygame.locals import *

def checkForQuitEvent(settings = False):
    if not settings:
        settings = { "cb": False, "in_game": False }
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # questo controllo dell'evento serve a terminare il
        # programma se l'utente preme la X di windows
        if event.type == QUIT:
            if not settings["in_game"]:
                pygame.quit()
                sys.exit()
            else:
                if settings["cb"]:
                    settings["cb"]()
    if keys[K_ESCAPE]:
        if not settings["in_game"]:
            pygame.quit()
            sys.exit()
        else:
            if settings["cb"]:
                settings["cb"]()

old_state = (0, 0, 0)
def mouseClickEvent():
    global old_state
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if old_state != pygame.mouse.get_pressed():
            old_state = pygame.mouse.get_pressed()
            return True
    if old_state == (1, 0, 0) and pygame.mouse.get_pressed() == (0, 0, 0):
        old_state = pygame.mouse.get_pressed()
    return False

def isInteractionPressed():
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] or keys[K_e]:
        return True
    return False

# threading could be handy later
# def keyPadInteraction(SCREEN):
#     global keypad_opened
#     if not keypad_opened:
#         t = threading.Thread(target = _keyPadInteraction, args = (SCREEN,))
#         t.start()