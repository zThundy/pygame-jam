from events import mouseClickEvent
import pygame, math, time

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
        SCREEN.blit(main_title, ((SCREEN.get_width()/2 - main_title.get_width()/2) + settings["x_off"], (SCREEN.get_height()/2 - main_title.get_height()/2) + + settings["y_off"]))