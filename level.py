import pygame

class Level:
    screen_dimensions = width, height = 0, 0
    screen = None
    tiles = {}

    blockSize = 120

    cornerSprite = pygame.image.load("./sprites/rooms/Muro_angolare.png")
    windowSprite = pygame.image.load("./sprites/rooms/Muro_con_finestra.png")
    doorSprite = pygame.image.load("./sprites/rooms/Muro_con_porta.png")
    normalSprite = pygame.image.load("./sprites/rooms/Muro_intero.png")

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN

    def setTileAtPosition(self, tile, x, y):
        self.tiles[pygame.Vector2(x, y)] = tile

    def isTilePresent(self, x, y):
        return self.tiles[pygame.Vector2(x, y)] != None

    def generateWalls(self):
        cornerSprite = None
        normalSprite = None

        for x in range(0, self.screen_dimensions[0], self.blockSize):
            for y in range(0, self.screen_dimensions[1], self.blockSize):
                # drawing of straight walls
                if (y == 0 and x != 0) and (x < (self.screen_dimensions[0] - self.blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                    normalSprite = pygame.transform.rotate(normalSprite, 180)
                    self.screen.blit(normalSprite, (x, y))
                if (y != 0 and x == 0):
                    normalSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                    normalSprite = pygame.transform.rotate(normalSprite, 270)
                    self.screen.blit(normalSprite, (x, y))
                if (x == (self.screen_dimensions[0] - self.blockSize) and y < (self.screen_dimensions[1] - self.blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                    normalSprite = pygame.transform.rotate(normalSprite, 90)
                    self.screen.blit(normalSprite, (x, y))
                if (x < (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                    normalSprite = pygame.transform.rotate(normalSprite, 0)
                    self.screen.blit(normalSprite, (x, y))

                # drawing of corners
                if (x == 0 and y == 0):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 180)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == 0):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 90)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 0)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 270)
                    self.screen.blit(cornerSprite, (x, y))
