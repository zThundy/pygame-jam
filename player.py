import pygame

class Player:
    position = pygame.Vector2()
    position.xy = 100, 100
    velocity = pygame.Vector2()
    velocity.xy = 3, 0
    acceleration = 0.1
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