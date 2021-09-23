import pygame
from pygame.locals import *
from events import *
from utils import *

CLOCK = pygame.time.Clock()

coords = {
    "1": (55, 150),
    "2": (213, 150),
    "3": (355, 150),
    "4": (55, 245),
    "5": (213, 245),
    "6": (355, 245),
    "7": (55, 340),
    "8": (213, 340),
    "9": (355, 340),

    "0": (213, 435),
    "ok": (213, 515),
}

number_string = ""
secret_code = "7355608"
def keyPadInteraction(SCREEN, mouseX, mouseY, sounds):
    global number_string

    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/tasti.png")
    image = pygame.transform.scale(image, (512, 600))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))

    # pygame.draw.rect(s, (255, 0, 0), (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2, image.get_width(), image.get_height()), 1)
    for index in coords:
        # pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + coords[index][0], (SCREEN.get_height()/2 - image.get_height()/2) + coords[index][1], 100, 75), 1)
        if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + coords[index][0], (SCREEN.get_height()/2 - image.get_height()/2) + coords[index][1], 100, 75):
            if mouseClickEvent():
                sounds.playSound("./sounds/tasks/click.wav")
                if len(number_string) < 15 and index != "ok":
                    number_string += index
                else:
                    if number_string == secret_code:
                        sounds.playSound("./sounds/tasks/correct_task.wav")
                        number_string = ""
                    else:
                        sounds.playSound("./sounds/tasks/wrong_task.wav")
                        number_string = ""

    FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
    main_title = FONT.render(number_string, True, (0, 0, 0))
    s.blit(main_title, ((SCREEN.get_width()/2 - image.get_width()/2) + 100, (SCREEN.get_height()/2 - image.get_height()/2) + 45))

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)

def boardInteraction(SCREEN, mouseX, mouseY, sounds):
    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/post_it.png")
    image = pygame.transform.scale(image, (256, 256))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))
    
    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)
