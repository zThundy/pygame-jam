import pygame
from pygame.locals import *

CLOCK = pygame.time.Clock()

def keyPadInteraction(SCREEN):
    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/tasti.png")
    image = pygame.transform.scale(image, (512, 600))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))

    FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
    main_title = FONT.render("Sounds", True, (0, 0, 0))
    SCREEN.blit(main_title, ((SCREEN.get_width()/2 - image.get_width()/2) + 55, (SCREEN.get_height()/2 - image.get_height()/2) + 150))

    pygame.draw.rect(s, (255, 0, 0), (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2, image.get_width(), image.get_height()), 1)
    # number 1
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 55, (SCREEN.get_height()/2 - image.get_height()/2) + 150, 100, 75), 1)
    # number 2
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 213, (SCREEN.get_height()/2 - image.get_height()/2) + 150, 100, 75), 1)
    # number 3
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 355, (SCREEN.get_height()/2 - image.get_height()/2) + 150, 100, 75), 1)
    # number 4
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 55, (SCREEN.get_height()/2 - image.get_height()/2) + 245, 100, 75), 1)
    # number 5
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 213, (SCREEN.get_height()/2 - image.get_height()/2) + 245, 100, 75), 1)
    # number 6
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 355, (SCREEN.get_height()/2 - image.get_height()/2) + 245, 100, 75), 1)
    # number 7
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 55, (SCREEN.get_height()/2 - image.get_height()/2) + 340, 100, 75), 1)
    # number 8
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 213, (SCREEN.get_height()/2 - image.get_height()/2) + 340, 100, 75), 1)
    # number 9
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 355, (SCREEN.get_height()/2 - image.get_height()/2) + 340, 100, 75), 1)
    # number 0
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 213, (SCREEN.get_height()/2 - image.get_height()/2) + 435, 100, 75), 1)
    # number ok
    pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 213, (SCREEN.get_height()/2 - image.get_height()/2) + 515, 100, 75), 1)

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)