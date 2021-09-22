import pygame, random
from pygame.locals import *
from utils import *

class Level:
    screen_dimensions = width, height = 0, 0
    screen = None

    blockSize = 120
    grid = {}

    cornerSprite = pygame.image.load("./sprites/rooms/muro_angolare.png")
    windowSprite = pygame.image.load("./sprites/rooms/muro_con_finestra.png")
    doorSprite = pygame.image.load("./sprites/rooms/muro_con_porta.png")
    normalSprite = pygame.image.load("./sprites/rooms/muro_intero.png")
    floorSprite = pygame.image.load("./sprites/rooms/pavimento.png")

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN

    def generateGrid(self):
        for x in range(0, self.screen_dimensions[0], self.blockSize):
            for y in range(0, self.screen_dimensions[1], self.blockSize):
                found = False
                num = random.randint(0, 100)
                choosenSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                if num > 80:
                    choosenSprite = pygame.transform.scale(self.windowSprite, (self.blockSize, self.blockSize))
                # drawing of straight walls
                if (y == 0 and x != 0) and (x < (self.screen_dimensions[0] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (y != 0 and x == 0):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y < (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (x < (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    self.grid[(x, y)] = choosenSprite
                    found = True

                # drawing of corners
                if (x == 0 and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    self.grid[(x, y)] = choosenSprite
                    found = True
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    self.grid[(x, y)] = choosenSprite
                    found = True

                # drawing of door
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)/2):
                    choosenSprite = pygame.transform.scale(self.doorSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    self.grid[(x, y)] = choosenSprite
                    found = True

                if not found:
                    choosenSprite = pygame.transform.scale(self.floorSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    self.grid[(x, y)] = choosenSprite

    def generateWalls(self):
        for tile in self.grid:
            current_tile = self.grid[tile]
            self.screen.blit(current_tile, (tile[0], tile[1]))

class Player(Level):
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
        self.position = pygame.Vector2(120, self.screen_dimensions[1]/2 - 60)

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
            if not self.checkObjectCollisions(0, 0, -10, 0):
                self.moving = True
                self.setPosition(self.getPosition()[0] - self.acceleration, self.getPosition()[1])
                self.currentSprite = self.leftSprite
        # if right key is pressed down (d) add value to x coordinates
        if keys[K_RIGHT] or keys[K_d]:
            if not self.checkObjectCollisions(10, 0, 0, 0):
                self.moving = True
                self.setPosition(self.getPosition()[0] + self.acceleration, self.getPosition()[1])
                self.currentSprite = self.rightSprite
        # if up key is pressed down (w) remove value to y coordinates
        if keys[K_UP] or keys[K_w]:
            if not self.checkObjectCollisions(0, 0, 0, -10):
                self.moving = True
                self.setPosition(self.getPosition()[0], self.getPosition()[1] - self.acceleration)
        # if down key is pressed down (s) add value to y coordinates
        if keys[K_DOWN] or keys[K_s]:
            if not self.checkObjectCollisions(0, 10, 0, 0):
                self.moving = True
                self.setPosition(self.getPosition()[0], self.getPosition()[1] + self.acceleration)
        self.screen.blit(self.currentSprite, self.position)
        if not (keys[K_LEFT] or keys[K_a]) and not (keys[K_RIGHT] or keys[K_d]) and not (keys[K_UP] or keys[K_w]) and not (keys[K_DOWN] or keys[K_s]):
            self.moving = False
        self.movePlayerLegs()

    def checkObjectCollisions(self, x_off, y_off, x_off_2, y_off_2):
        for tile in self.grid:
            current_tile = self.grid[tile]
            if checkCollisions(self.position[0] + x_off_2, self.position[1] + y_off_2, self.currentSprite.get_width() + x_off, self.currentSprite.get_height() + y_off, tile[0], tile[1], current_tile.get_width(), current_tile.get_height()):
                return True
        return False

