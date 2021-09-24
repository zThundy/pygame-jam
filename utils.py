from events import mouseClickEvent
import pygame, math, time
from utils import *

# this function helps to check if an element is colliding with another one
def checkCollisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)

def checkCollisionAndMouseClick(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    if checkCollisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
        if mouseClickEvent():
            return True
    return False

def drawText(SCREEN, MAIN_COLOR, settings = False):
    if not settings:
        settings = {
            "text": "NO_TEXT_GIVEN",
            "size": 250,
            "x_off": 0,
            "y_off": 150,
            "jump": False
        }
    # ovverwrite prev font element to have bigger dimension
    text = pygame.font.Font("./fonts/game_over.ttf", settings["size"])
    main_title = text.render(settings["text"], True, MAIN_COLOR)
    if "jump" in settings and settings["jump"]:
        SCREEN.blit(main_title, ((SCREEN.get_width()/2 - main_title.get_width()/2) + settings["x_off"], ((SCREEN.get_height()/2 - main_title.get_height()/2) + settings["y_off"]) + math.sin(time.time()*8)*8))
    else:
        SCREEN.blit(main_title, ((SCREEN.get_width()/2 - main_title.get_width()/2) + settings["x_off"], (SCREEN.get_height()/2 - main_title.get_height()/2) + settings["y_off"]))

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