import pygame, sys
from pygame.locals import *

input_key = 0
last_input = 0
def checkLastInput(input_type):
    global input_key
    global last_input
    keys = pygame.key.get_pressed()

    if input_type == input_key and last_input != keys[input_type] and last_input == 1:
        last_input = 0
        return True
    input_key = input_type
    if keys[input_type]:
        last_input = keys[input_type]
    return False

def checkForQuitEvent(cb = False):
    # questo controllo dell'evento serve a terminare il
    # programma se l'utente preme la X di windows
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if checkLastInput(K_ESCAPE):
        if not cb:
            pygame.quit()
            sys.exit()
        else:
            cb()

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