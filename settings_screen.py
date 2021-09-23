import pygame, math, time
from utils import *

def drawSettingsTitle(SCREEN, MAIN_COLOR):
    # draw settings page title
    FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
    main_title = FONT.render("Settings", True, MAIN_COLOR)
    SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 400) + math.sin(time.time()*8)*8))

def drawSettingsButtonAndText(SCREEN, MAIN_COLOR, OPTIONS, SOUNDS, settings = False):
    if not settings:
        settings = {
            "text": "NO_LABEL_DEFINED",
            "value": "no_value",
            "image_off_x": -50,
            "image_off_y": 200,
            "rect_off_x": -100,
            "rect_off_y": 180,
            "cb": None
        }

    # get mouse position to check if player is clicking on button
    mouseX, mouseY = pygame.mouse.get_pos()

    # fullscreen option
    FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
    main_title = FONT.render(settings["text"], True, MAIN_COLOR)
    SCREEN.blit(main_title, (SCREEN.get_width()/2 + settings["image_off_x"], SCREEN.get_height()/2 - (main_title.get_height()/2 + settings["image_off_y"])))

    if OPTIONS.getValue(settings["value"]):
        pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 + settings["rect_off_x"], SCREEN.get_height()/2 - (main_title.get_height()/2 + settings["rect_off_y"]), main_title.get_height()/2, main_title.get_height()/2))
    else:
        pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 + settings["rect_off_x"], SCREEN.get_height()/2 - (main_title.get_height()/2 + settings["rect_off_y"]), main_title.get_height()/2, main_title.get_height()/2), 3)
    
    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 + settings["rect_off_x"], SCREEN.get_height()/2 - (main_title.get_height()/2 + settings["rect_off_y"]), main_title.get_height()/2, main_title.get_height()/2):
        OPTIONS.setValue(settings["value"], not OPTIONS.getValue(settings["value"]))
        SOUNDS.playSound("./sounds/button_press_settings_sound.wav")
        if "cb" in settings:
            settings["cb"]()

def drawButton(SCREEN, SOUNDS, settings = False):
    if not settings:
        settings = {
            "image_off_x": -300,
            "image_off_y": 100,
            "name": "no_name"
        }
    # get mouse position to check if player is clicking on button
    mouseX, mouseY = pygame.mouse.get_pos()

    # render back to main screen button
    button = pygame.image.load("./sprites/buttons/" + settings["name"] + ".png")
    SCREEN.blit(button, ((SCREEN.get_width()/2 - button.get_width()/2) + settings["image_off_x"], (SCREEN.get_height()/2 - button.get_height()/2) + settings["image_off_y"]))
    if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - button.get_width()/2) + settings["image_off_x"], (SCREEN.get_height()/2 - button.get_height()/2) + settings["image_off_y"], button.get_width(), button.get_height()):
        button = pygame.image.load("./sprites/buttons/" + settings["name"] + "_dark.png")
        SCREEN.blit(button, ((SCREEN.get_width()/2 - button.get_width()/2) + settings["image_off_x"], (SCREEN.get_height()/2 - button.get_height()/2) + settings["image_off_y"]))
        if mouseClickEvent():
            SOUNDS.playSound("./sounds/button_press_sound.wav")
            if "cb" in settings:
                settings["cb"]()