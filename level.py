import pygame, random
from pygame.locals import *
from utils import *
from events import *
from interactions import *

class Board:
    screen_dimensions = width, height = 0, 0
    screen = None
    bacheca = False

    blockSize = 120
    grid = {}

    cornerSprite = pygame.image.load("./sprites/rooms/muro_angolare.png")
    windowSprite = pygame.image.load("./sprites/rooms/muro_con_finestra.png")
    doorSprite = pygame.image.load("./sprites/rooms/muro_con_porta.png")
    normalSprite = pygame.image.load("./sprites/rooms/muro_intero.png")
    floorSprite = pygame.image.load("./sprites/rooms/pavimento.png")
    boardSprite = pygame.image.load("./sprites/rooms/Muro_con_bacheca.png")

    def __init__(self, SCREEN):
        self.screen_dimensions = (SCREEN.get_width(), SCREEN.get_height())
        self.screen = SCREEN

    def generateGrid(self):
        for x in range(0, self.screen_dimensions[0], self.blockSize):
            for y in range(0, self.screen_dimensions[1], self.blockSize):
                # create the grid element index with the tuple
                # ready to be filled
                self.grid[(x, y)] = {}
                temp_element = {}

                # this will be used to check if the
                # tile will be a floor tile or not
                found = False
                choosenSprite = pygame.transform.scale(self.normalSprite, (self.blockSize, self.blockSize))
                if random.randint(0, 100) > 80:
                    choosenSprite = pygame.transform.scale(self.windowSprite, (self.blockSize, self.blockSize))

                # drawing of corners
                if (x == 0 and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == 0):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.scale(self.cornerSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                
                if not self.bacheca and not found:
                    self.bacheca = True
                    choosenSprite = pygame.transform.scale(self.boardSprite, (self.blockSize, self.blockSize))
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    temp_element["interaction"] = boardInteraction
                    found = True

                # drawing of straight walls
                if (y == 0 and x != 0) and (x < (self.screen_dimensions[0] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 180)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (y != 0 and x == 0):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 270)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (x == (self.screen_dimensions[0] - self.blockSize) and y < (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True
                if (x < (self.screen_dimensions[0] - self.blockSize) and y == (self.screen_dimensions[1] - self.blockSize)):
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    found = True

                # drawing of door
                if (x == 0 and y == (self.screen_dimensions[1] - self.blockSize)/2):
                    choosenSprite = pygame.transform.scale(self.doorSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 90)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = True
                    temp_element["coords"] = (x, y)
                    temp_element["interaction"] = keyPadInteraction
                    found = True

                if not found:
                    choosenSprite = pygame.transform.scale(self.floorSprite, (self.blockSize, self.blockSize))
                    choosenSprite = pygame.transform.rotate(choosenSprite, 0)
                    temp_element["sprite"] = choosenSprite
                    temp_element["collision"] = False
                    temp_element["coords"] = (x, y)
                self.grid[(x, y)][str(len(self.grid[(x, y)]))] = temp_element

    def generateLevelObjects(self, x, y, sprite, collision = True, interaction = None, resize = True, offset = (0, 0)):
        if offset[0] > 0 or offset[1] > 0:
            x += offset[0]
            y += offset[1]
            self.grid[(x, y)] = {}

        temp_element = {}
        if resize:
            temp_element["sprite"] = pygame.transform.scale(sprite, (self.blockSize, self.blockSize))
        else:
            temp_element["sprite"] = sprite
        temp_element["collision"] = collision
        temp_element["coords"] = (x, y)
        if interaction:
            temp_element["interaction"] = interaction
        self.grid[(x, y)][str(len(self.grid[(x, y)]))] = temp_element

    def generateWalls(self):
        for _, coords in enumerate(self.grid):
            for index in self.grid[coords]:
                current_tile = self.grid[coords][str(index)]["sprite"]
                self.screen.blit(current_tile, (coords[0], coords[1]))

class Level(Board):
    level_number = 0

    def generateLevel(self):
        if self.level_number == 0:
            # here we add the single objects on the screen
            self.generateLevelObjects(960, 120, pygame.image.load("./sprites/rooms/room_elements/tavolo.png"), False, None, False, (15, 30))
            self.generateLevelObjects(960, 120, pygame.image.load("./sprites/rooms/room_elements/computer_spento.png"), True, computerInteractions, False, (25, 10))
            self.generateLevelObjects(600, 600, pygame.image.load("./sprites/rooms/room_elements/server_rack.png"), True)
            self.generateLevelObjects(960, 840, pygame.image.load("./sprites/rooms/room_elements/server_rack.png"), True)

class Player(Board):
    saved_interaction = False
    acceleration = 5

    screen_dimensions = width, height = 0, 0
    screen = 0

    # player position vector
    position = pygame.Vector2()
    position.xy = 0, 0
    # general player sprite
    rightSprite = pygame.image.load("./sprites/user/personaggio.png")
    rightSprite = pygame.transform.scale(rightSprite, (64, 110))
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
            if not self.checkObjectCollisions(0, 0, -10, 0)[0]:
                self.moving = True
                self.setPosition(self.getPosition()[0] - self.acceleration, self.getPosition()[1])
                self.currentSprite = self.leftSprite
        # if right key is pressed down (d) add value to x coordinates
        if keys[K_RIGHT] or keys[K_d]:
            if not self.checkObjectCollisions(10, 0, 0, 0)[0]:
                self.moving = True
                self.setPosition(self.getPosition()[0] + self.acceleration, self.getPosition()[1])
                self.currentSprite = self.rightSprite
        # if up key is pressed down (w) remove value to y coordinates
        if keys[K_UP] or keys[K_w]:
            if not self.checkObjectCollisions(0, 0, 0, -10)[0]:
                self.moving = True
                self.setPosition(self.getPosition()[0], self.getPosition()[1] - self.acceleration)
        # if down key is pressed down (s) add value to y coordinates
        if keys[K_DOWN] or keys[K_s]:
            if not self.checkObjectCollisions(0, 10, 0, 0)[0]:
                self.moving = True
                self.setPosition(self.getPosition()[0], self.getPosition()[1] + self.acceleration)
        self.drawPlayer()
        if not (keys[K_LEFT] or keys[K_a]) and not (keys[K_RIGHT] or keys[K_d]) and not (keys[K_UP] or keys[K_w]) and not (keys[K_DOWN] or keys[K_s]):
            self.moving = False
        self.movePlayerLegs()
    
    def drawPlayer(self):
        self.screen.blit(self.currentSprite, self.position)

    def checkObjectCollisions(self, x_off, y_off, x_off_2, y_off_2):
        for _, coords in enumerate(self.grid):
            for index in self.grid[coords]:
                current_tile = self.grid[coords][str(index)]
                if current_tile["collision"] and checkCollisions(self.position[0] + x_off_2, self.position[1] + y_off_2, self.currentSprite.get_width() + x_off, self.currentSprite.get_height() + y_off, current_tile["coords"][0], current_tile["coords"][1], current_tile["sprite"].get_width(), current_tile["sprite"].get_height()):
                    return (True, current_tile)
        return (False, False)

    def checkInteraction(self):
        if isInteractionPressed():
            (isColliding, obj) = self.checkObjectCollisions(15, 15, -15, -15)
            if isColliding and "interaction" in obj:
                self.saved_interaction = obj["interaction"]

        if self.saved_interaction:
            keys = pygame.key.get_pressed()
            if keys[K_BACKSPACE] or keys[K_DELETE]:
                self.saved_interaction = False
        return self.saved_interaction

