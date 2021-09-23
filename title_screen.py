import pygame, sys
from utils import *

can_click = False
first_button_sprite = ""
second_button_sprite = ""
third_button_sprite = ""
count = 0

def drawMainButtons(SCREEN, SOUNDS, cb_1, cb_2, cb_3):
    global can_click
    global first_button_sprite
    global second_button_sprite
    global third_button_sprite
    global count
    
    # get mouse position to check if player is clicking on button
    mouseX, mouseY = pygame.mouse.get_pos()

    if count > 150:
        if count == 151:
            SOUNDS.playSound("./sounds/button_show_sound.wav")
        second_button_sprite = pygame.image.load("./sprites/buttons/play.png")
        SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
        if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, second_button_sprite.get_width(), second_button_sprite.get_height()):
            second_button_sprite = pygame.image.load("./sprites/buttons/play_dark.png")
            SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if (mouseClickEvent() and can_click):
                SOUNDS.playSound("./sounds/button_press_sound.wav")
                cb_2()

        if count > 200:
            if count == 201:
                SOUNDS.playSound("./sounds/button_show_sound.wav")
            first_button_sprite = pygame.image.load("./sprites/buttons/settings.png")
            SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, first_button_sprite.get_width(), first_button_sprite.get_height()):
                first_button_sprite = pygame.image.load("./sprites/buttons/settings_dark.png")
                SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and can_click):
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    cb_1()
        
        if count > 250:
            if count == 251:
                SOUNDS.playSound("./sounds/button_show_sound.wav")
                can_click = True
            third_button_sprite = pygame.image.load("./sprites/buttons/exit.png")
            SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, third_button_sprite.get_width(), third_button_sprite.get_height()):
                third_button_sprite = pygame.image.load("./sprites/buttons/exit_dark.png")
                SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and can_click):
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    cb_3()
    
    if not can_click:
        count += 1
    else:
        count = 400