import sys, pygame, time, math, random
from pygame.locals import *

from events import *
from level import Board, Player, Level
from utils import *
from options import Options, Sounds

from title_screen import *

from interactions import *

GAME_NAME = "Er tecnico"
GAME_TITLE = "Python Gamejam"
GAME_SUBTITLE = "Un gioco brutto fatto da zThundy__"

MAIN_COLOR = (50, 255, 50)

# constant variable
SCREEN = 0
FONT = 0
OPTIONS = Options()
SOUNDS = Sounds()
CLOCK = pygame.time.Clock()

def showSplashScreen():
    # access to global variables
    global SCREEN
    global FONT

    first_string = ""
    second_stirng = ""

    # 4 secondi di attesa
    while True:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        if random.randint(0, 100) > 85:
            if len(first_string) != len(GAME_TITLE):
                first_string += GAME_TITLE[len(first_string)]
                SOUNDS.playSound("./sounds/keyboard/" + str(random.randint(1, 10)) + ".wav")
            elif len(second_stirng) != len(GAME_SUBTITLE):
                second_stirng += GAME_SUBTITLE[len(second_stirng)]
                SOUNDS.playSound("./sounds/keyboard/" + str(random.randint(1, 10)) + ".wav")

        # draw first string
        drawText(SCREEN, MAIN_COLOR, { "text": first_string, "size": 250, "x_off": 0, "y_off": -200, "jump": False })
        # draw second string
        drawText(SCREEN, MAIN_COLOR, { "text": second_stirng, "size": 150, "x_off": 0, "y_off": -50, "jump": False })

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

        if len(first_string) == len(GAME_TITLE) and len(second_stirng) == len(GAME_SUBTITLE):  
            time.sleep(2)
            break

def showTitleScreen():
    # access to global variables
    global SCREEN
    global FONT

    SCREEN.fill((0, 0, 0))
    titleScreen = True

    SOUNDS.playMusic("./sounds/main_theme.mp3", True, False)

    def button_1_press():
        global titleScreen
        titleScreen = False
        showSettingsScreen()
    def button_2_press():
        global titleScreen
        titleScreen = False
        SOUNDS.stopMusic()
        gameThread()
    def button_3_press():
        global titleScreen
        titleScreen = False
        pygame.time.delay(500)
        pygame.quit()
        sys.exit()

    while titleScreen:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))
        # check events.py to see the executed code
        checkForQuitEvent()
        
        # draw game title
        drawText(SCREEN, MAIN_COLOR, { "text": GAME_NAME, "size": 250, "x_off": 0, "y_off": -200, "jump": True })
        # draw main button animation
        drawMainButtons(SCREEN, SOUNDS, button_1_press, button_2_press, button_3_press)

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

def showSettingsScreen():
    # access to global variables
    global SCREEN
    global FONT
    global OPTIONS

    settings_screen = True

    def cb_01():
        pygame.display.toggle_fullscreen()
    def cb_03():
        SOUNDS.stopMusic()

    def cb_button_1():
        global settings_screen
        showTitleScreen()
        settings_screen = False
    def cb_button_2():
        global settings_screen
        showTitleScreen()
        settings_screen = False

    while settings_screen:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))
        # check events.py to see the executed code
        checkForQuitEvent()

        # draw settings title
        drawText(SCREEN, MAIN_COLOR, { "text": "Settings", "size": 250, "x_off": 0, "y_off": -350, "jump": True })

        # fullscreen button
        drawSettingsButtonAndText(SCREEN, MAIN_COLOR, OPTIONS, SOUNDS, { "text": "Fullscreen", "value": "fullscreen", "image_off_x": -50, "image_off_y": 200, "rect_off_x": -100, "rect_off_y": 180, "cb": cb_01 })
        # vsync button
        drawSettingsButtonAndText(SCREEN, MAIN_COLOR, OPTIONS, SOUNDS, { "text": "VSync", "value": "vsync", "image_off_x": -50, "image_off_y": 150, "rect_off_x": -100, "rect_off_y": 130 })
        # music button
        drawSettingsButtonAndText(SCREEN, MAIN_COLOR, OPTIONS, SOUNDS, { "text": "Music", "value": "music", "image_off_x": -50, "image_off_y": 100, "rect_off_x": -100, "rect_off_y": 80, "cb": cb_03 })
        # sounds button
        drawSettingsButtonAndText(SCREEN, MAIN_COLOR, OPTIONS, SOUNDS, { "text": "Sounds", "value": "sound", "image_off_x": -50, "image_off_y": 50, "rect_off_x": -100, "rect_off_y": 30 })
        # render back to main screen button
        drawButton(SCREEN, SOUNDS, { "image_off_x": -300, "image_off_y": 100, "name": "back", "cb": cb_button_1 })
        # render apply button
        drawButton(SCREEN, SOUNDS, { "image_off_x": 300, "image_off_y": 100, "name": "apply", "cb": cb_button_2 })

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

def gameThread():
    # access to global variables
    global SCREEN
    global FONT

    player = Player(SCREEN)
    board = Board(SCREEN)
    level = Level(SCREEN)

    game_over = False
    start_ticks = pygame.time.get_ticks()
    max_seconds = 240

    SOUNDS.playMusic("./sounds/game_theme.mp3", True, True)

    # this function ready the level generator
    # and creates a grid of elements with their images inside
    board.generateGrid()
    # generate current level
    level.generateLevel()

    def cb_button_1():
        showTitleScreen()
    def cb_button_2():
        pygame.quit()
        sys.exit()

    while True:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((255, 255, 255))
        # check events.py to see the executed code
        checkForQuitEvent()
        # get mouse position to check if player is clicking on button
        mouseX, mouseY = pygame.mouse.get_pos()
        # draw grid
        board.generateWalls()
        
        if game_over:
            s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
            s.fill((0, 0, 0, 200))
            SCREEN.blit(s, (0, 0))
            # draw game over title
            drawText(SCREEN, MAIN_COLOR, { "text": "Game Over", "size": 250, "x_off": 0, "y_off": -200, "jump": True })
            # render retray gameover button
            drawButton(SCREEN, SOUNDS, { "image_off_x": -300, "image_off_y": 100, "name": "back", "cb": cb_button_1 })
            # render apply button
            drawButton(SCREEN, SOUNDS, { "image_off_x": -300, "image_off_y": 100, "name": "back", "cb": cb_button_2 })
        else:
            # check timer and draw on screen
            seconds = (pygame.time.get_ticks() - start_ticks)/1000
            remaining_seconds = time.strftime('%M:%S', time.gmtime(math.floor(max_seconds - seconds)))

            pygame.draw.rect(SCREEN, (230, 230, 230), (SCREEN.get_width()/2 - 200, 20, 400, 70), 0, 20)
            # draw time remaining text
            drawText(SCREEN, (0, 0, 0), { "text": "Time remaining: " + str(remaining_seconds), "size": 100, "x_off": 0, "y_off": -490, "jump": False })

            # check if user interact with something
            interaction = player.checkInteraction(mouseX, mouseY, SOUNDS)
            if not interaction:
                # check if user press a movement key and move the player
                player.checkPlayerMovements()
            
            if math.floor(max_seconds - seconds) <= 0:
                game_over = True

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

def main():
    pygame.init()
    global SCREEN
    # get display info
    infoObject = pygame.display.Info()

    # define screen dimensions and flags
    _screen = pygame.display.set_mode((0, 0))
    pygame.display.set_caption(GAME_NAME)
    SCREEN = pygame.Surface((1920, 1080))
    pygame.transform.scale(_screen, (infoObject.current_w, infoObject.current_h))
    print(SCREEN)
    SCREEN = _screen
    SCREEN.fill((0, 0, 0))

    picture = pygame.image.load("./sprites/personaggio.ico")
    pygame.display.set_icon(picture)

    # this is used only on startup
    # -------------------------- #
    # show splash screen png
    # showSplashScreen()
    # show title screen after splash screen
    showTitleScreen()
    # start the gameplay
    gameThread()

if __name__ == "__main__":
    main()