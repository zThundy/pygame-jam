import pygame

class Level:
    screen_dimensions = width, height = 0, 0
    screen = None
    tiles = {}

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
        blockSize = 64 # Set the size of the grid block

        cornerSprite = None
        normalSprite = None

        for x in range(0, self.screen_dimensions[0], blockSize):
            for y in range(0, self.screen_dimensions[1], blockSize):
                # drawing of straight walls
                if (y == 0 and x != 0) and (x < (self.screen_dimensions[0] - blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (64, 64))
                    normalSprite = pygame.transform.rotate(normalSprite, 180)
                    self.screen.blit(normalSprite, (x, y))
                if (y != 0 and x == 0):
                    normalSprite = pygame.transform.scale(self.normalSprite, (64, 64))
                    normalSprite = pygame.transform.rotate(normalSprite, 270)
                    self.screen.blit(normalSprite, (x, y))
                if (x == (self.screen_dimensions[0] - blockSize) and y < (self.screen_dimensions[1] - blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (64, 64))
                    normalSprite = pygame.transform.rotate(normalSprite, 90)
                    self.screen.blit(normalSprite, (x, y))
                if (x < (self.screen_dimensions[0] - blockSize) and y == (self.screen_dimensions[1] - blockSize)):
                    normalSprite = pygame.transform.scale(self.normalSprite, (64, 64))
                    normalSprite = pygame.transform.rotate(normalSprite, 0)
                    self.screen.blit(normalSprite, (x, y))

                # drawing of corners
                if (x == 0 and y == 0):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (64, 64))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 180)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == (self.screen_dimensions[0] - blockSize) and y == 0):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (64, 64))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 90)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == (self.screen_dimensions[0] - blockSize) and y == (self.screen_dimensions[1] - blockSize)):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (64, 64))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 0)
                    self.screen.blit(cornerSprite, (x, y))
                if (x == 0 and y == (self.screen_dimensions[1] - blockSize)):
                    cornerSprite = pygame.transform.scale(self.cornerSprite, (64, 64))
                    cornerSprite = pygame.transform.rotate(cornerSprite, 270)
                    self.screen.blit(cornerSprite, (x, y))
