import pygame, random

class Level:
    screen_dimensions = width, height = 0, 0
    screen = None

    blockSize = 120
    grid = {}

    cornerSprite = pygame.image.load("./sprites/rooms/Muro_angolare.png")
    windowSprite = pygame.image.load("./sprites/rooms/Muro_con_finestra.png")
    doorSprite = pygame.image.load("./sprites/rooms/Muro_con_porta.png")
    normalSprite = pygame.image.load("./sprites/rooms/Muro_intero.png")

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN

    def generateGrid(self):
        for x in range(0, self.screen_dimensions[0], self.blockSize):
            for y in range(0, self.screen_dimensions[1], self.blockSize):
                num = random.randint(0, 100)
                choosenSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                if num > 80:
                    choosenSprite = pygame.transform.scale(self.windowSprite, (self.blockSize, self.blockSize))
                # drawing of straight walls
                if (y == 0 and x != 0) and (x < (self.screen_dimensions[0] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    self.grid[(x, y)] = choosenSprite
                if (y != 0 and x == 0):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    self.grid[(x, y)] = choosenSprite
                if (x == (self.screen_dimensions[0] - self.blockSize) and y < (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    self.grid[(x, y)] = choosenSprite
                if (x < (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    self.grid[(x, y)] = choosenSprite

                # drawing of corners
                if (x == 0 and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    self.grid[(x, y)] = choosenSprite
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    self.grid[(x, y)] = choosenSprite
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    self.grid[(x, y)] = choosenSprite
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    self.grid[(x, y)] = choosenSprite

                # drawing of door
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)/2):
                    choosenSprite = pygame.transform.scale(self.doorSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    self.grid[(x, y)] = choosenSprite

    def generateWalls(self):
        for tile in self.grid:
            current_tile = self.grid[tile]
            self.screen.blit(current_tile, (tile[0], tile[1]))
