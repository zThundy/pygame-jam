import pygame
from pygame.locals import *

class Player:
    acceleration = 5

    screen_dimensions = width, height = 0, 0
    screen = 0

    # player position vector
    position = pygame.Vector2()
    position.xy = 0, 0
    # general player sprite
    rightSprite = pygame.image.load("./sprites/user/personaggio.png")
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite
    # player legs sprites
    right_leg_sprite = pygame.image.load("./sprites/user/gamba_sinistra.png")
    left_leg_sprite = pygame.image.load("./sprites/user/gamba_destra.png")
    leg_counter = 0
    leg_switched = False
    moving = False

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN
        self.position = pygame.Vector2(10, self.screen_dimensions[1]/2 - 60)

    def setPosition(self, x, y):
        self.position.xy = x, y

    def getPosition(self):
        return self.position.xy

    def movePlayerLegs(self):
        if not self.moving:
            self.screen.blit(self.left_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) - 16, (self.position[1] + self.currentSprite.get_height()) - 25))
            self.screen.blit(self.right_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) + 5, (self.position[1] + self.currentSprite.get_height()) - 25))
            return
        if self.leg_counter <= 30 and not self.leg_switched:
            self.screen.blit(self.left_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) - 16, (self.position[1] + self.currentSprite.get_height()) - 25))
            self.screen.blit(self.right_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) + 5, (self.position[1] + self.currentSprite.get_height()) - 20))
            self.leg_counter += 1
            if self.leg_counter == 30:
                self.leg_switched = True
        elif self.leg_counter >= 0 and self.leg_switched:
            self.screen.blit(self.left_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) - 16, (self.position[1] + self.currentSprite.get_height()) - 20))
            self.screen.blit(self.right_leg_sprite, ((self.position[0] + self.currentSprite.get_width()/2) + 5, (self.position[1] + self.currentSprite.get_height()) - 25))
            self.leg_counter -= 1
            if self.leg_counter == 0:
                self.leg_switched = False



    def checkPlayerMovements(self):
        keys = pygame.key.get_pressed()
        # if left key is pressed down (a) remove value from x coordinates
        if keys[K_LEFT] or keys[K_a]:
            self.moving = True
            self.setPosition(self.getPosition()[0] - self.acceleration, self.getPosition()[1])
            self.currentSprite = self.leftSprite
        # if right key is pressed down (d) add value to x coordinates
        if keys[K_RIGHT] or keys[K_d]:
            self.moving = True
            self.setPosition(self.getPosition()[0] + self.acceleration, self.getPosition()[1])
            self.currentSprite = self.rightSprite
        # if up key is pressed down (w) remove value to y coordinates
        if keys[K_UP] or keys[K_w]:
            self.moving = True
            self.setPosition(self.getPosition()[0], self.getPosition()[1] - self.acceleration)
        # if down key is pressed down (s) add value to y coordinates
        if keys[K_DOWN] or keys[K_s]:
            self.moving = True
            self.setPosition(self.getPosition()[0], self.getPosition()[1] + self.acceleration)
        self.screen.blit(self.currentSprite, self.position)
        if not (keys[K_LEFT] or keys[K_a]) and not (keys[K_RIGHT] or keys[K_d]) and not (keys[K_UP] or keys[K_w]) and not (keys[K_DOWN] or keys[K_s]):
            self.moving = False
        self.movePlayerLegs()