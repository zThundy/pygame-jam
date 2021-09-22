import pygame
from pygame.locals import *

class Player:
    acceleration = 5

    screen_dimensions = width, height = 0, 0
    screen = 0

    position = pygame.Vector2()
    position.xy = 50, 50
    velocity = pygame.Vector2()
    velocity.xy = 3, 0
    rightSprite = pygame.image.load("./sprites/user/personaggio.png")
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN

    def setPosition(self, x, y):
        self.position.xy = x, y

    def getCurrentSprite(self):
        return self.currentSprite

    def getVelocity(self):
        return self.velocity

    def getPosition(self):
        return self.position.xy

    def checkPlayerMovements(self):
        keys = pygame.key.get_pressed()
        # if left key is pressed down (a) remove value from x coordinates
        if keys[K_LEFT] or keys[K_a]:
            self.setPosition(self.getPosition()[0] - self.acceleration, self.getPosition()[1])
            self.currentSprite = self.leftSprite
        # if right key is pressed down (d) add value to x coordinates
        if keys[K_RIGHT] or keys[K_d]:
            self.setPosition(self.getPosition()[0] + self.acceleration, self.getPosition()[1])
            self.currentSprite = self.rightSprite
        # if up key is pressed down (w) remove value to y coordinates
        if keys[K_UP] or keys[K_w]:
            self.setPosition(self.getPosition()[0], self.getPosition()[1] - self.acceleration)
        # if down key is pressed down (s) add value to y coordinates
        if keys[K_DOWN] or keys[K_s]:
            self.setPosition(self.getPosition()[0], self.getPosition()[1] + self.acceleration)