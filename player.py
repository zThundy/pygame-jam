import pygame
from pygame.locals import *

class Player:
    acceleration = 5

    position = pygame.Vector2()
    position.xy = 200, 200
    velocity = pygame.Vector2()
    velocity.xy = 3, 0
    rightSprite = pygame.image.load("./sprites/test.png")
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite

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
        # if right key is pressed down (d) add value to x coordinates
        if keys[K_RIGHT] or keys[K_d]:
            self.setPosition(self.getPosition()[0] + self.acceleration, self.getPosition()[1])
        # if up key is pressed down (w) remove value to y coordinates
        if keys[K_UP] or keys[K_w]:
            self.setPosition(self.getPosition()[0], self.getPosition()[1] - self.acceleration)
        # if down key is pressed down (s) add value to y coordinates
        if keys[K_DOWN] or keys[K_s]:
            self.setPosition(self.getPosition()[0], self.getPosition()[1] + self.acceleration)