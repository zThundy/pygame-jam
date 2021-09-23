import sys, pygame, time, math, random
from pygame.locals import *

from events import *
from level import Board, Player, Level
from utils import *
from options import Options, Sounds

from title_screen import *
from settings_screen import *

from interactions import *

size = width, height = 1920, 1080
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

        # ovverwrite prev font element to have bigger dimension
        FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
        main_title = FONT.render(first_string, True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 150)))
        
        FONT = pygame.font.Font("./fonts/game_over.ttf", 150)
        main_subtitle = FONT.render(second_stirng, True, MAIN_COLOR)
        SCREEN.blit(main_subtitle, (SCREEN.get_width()/2 - main_subtitle.get_width()/2, main_title.get_height() + SCREEN.get_height()/2 - (main_subtitle.get_height()/2 + 150)))

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

        if len(first_string) == len(GAME_TITLE) and len(second_stirng) == len(GAME_SUBTITLE):  
            pygame.time.delay(2500)
            break


def showTitleScreen(canClick = False):
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
        pygame.quit()
        sys.exit()

    while titleScreen:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()
        
        # draw game title
        FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
        main_title = FONT.render(GAME_NAME, True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 200) + math.sin(time.time()*8)*8))
        
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
        showTitleScreen(True)
        settings_screen = False
    def cb_button_2():
        global settings_screen
        showTitleScreen(True)
        settings_screen = False

    while settings_screen:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()

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
            s = pygame.Surface(size, SRCALPHA)
            s.fill((0, 0, 0, 200))
            SCREEN.blit(s, (0, 0))

            # draw settings page title
            FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
            main_title = FONT.render("Game Over", True, MAIN_COLOR)
            SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 200) + math.sin(time.time()*8)*8))

            # render retray gameover button
            retry_button_sprite = pygame.image.load("./sprites/buttons/back.png")
            SCREEN.blit(retry_button_sprite, ((SCREEN.get_width()/2 - retry_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - retry_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - retry_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - retry_button_sprite.get_height()/2) + 100, retry_button_sprite.get_width(), retry_button_sprite.get_height()):
                retry_button_sprite = pygame.image.load("./sprites/buttons/back_dark.png")
                SCREEN.blit(retry_button_sprite, ((SCREEN.get_width()/2 - retry_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - retry_button_sprite.get_height()/2) + 100))
                if mouseClickEvent():
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    showTitleScreen()
                    break

            # render apply button
            exit_button_sprite = pygame.image.load("./sprites/buttons/exit.png")
            SCREEN.blit(exit_button_sprite, ((SCREEN.get_width()/2 - exit_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - exit_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - exit_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - exit_button_sprite.get_height()/2) + 100, exit_button_sprite.get_width(), exit_button_sprite.get_height()):
                exit_button_sprite = pygame.image.load("./sprites/buttons/exit_dark.png")
                SCREEN.blit(exit_button_sprite, ((SCREEN.get_width()/2 - exit_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - exit_button_sprite.get_height()/2) + 100))
                if mouseClickEvent():
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    pygame.time.delay(1000)
                    pygame.quit()
                    sys.exit()
        else:
            # check timer and draw on screen
            seconds = (pygame.time.get_ticks() - start_ticks)/1000
            remaining_seconds = time.strftime('%M:%S', time.gmtime(math.floor(max_seconds - seconds)))

            pygame.draw.rect(SCREEN, (230, 230, 230), (SCREEN.get_width()/2 - 200, 20, 400, 70), 0, 20)
            FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
            main_title = FONT.render("Time remaining: " + str(remaining_seconds), True, (0, 0, 0))
            SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, 20))

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

    # access to global variables
    global SCREEN

    # define screen dimensions and flags
    SCREEN = pygame.display.set_mode(size)
    pygame.display.set_caption(GAME_NAME)

    # fill both fake and real screen with black background
    SCREEN.fill((0, 0, 0))
    picture = pygame.image.load("./sprites/personaggio.ico")
    pygame.display.set_icon(picture)

    # show splash screen png
    showSplashScreen()

    # show title screen after splash screen
    showTitleScreen()

    gameThread()

if __name__ == "__main__":
    main()