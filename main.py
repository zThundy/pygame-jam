import sys, pygame, time, math, random
from pygame.locals import *

from events import *
from level import Board, Player, Level
from utils import *
from options import Options, Sounds

from interactions import *

size = width, height = 1920, 1080
SETTINGS_TITLE = "Settings"
GAME_NAME = "Er tecnico"
GAME_TITLE = "Python Gamejam"
GAME_SUBTITLE = "Un gioco brutto fatto da poppity"

MAIN_THEME_STARTED = False

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
    global MAIN_THEME_STARTED

    titleScreen = True
    SCREEN.fill((0, 0, 0))

    if not MAIN_THEME_STARTED:
        MAIN_THEME_STARTED = True
        SOUNDS.playMusic("./sounds/main_theme.mp3", True)

    count = 0
    first_button_sprite = ""
    second_button_sprite = ""
    third_button_sprite = ""

    while titleScreen:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()

        # get mouse position to check if player is clicking on button
        mouseX, mouseY = pygame.mouse.get_pos()
        
        # draw game title
        FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
        main_title = FONT.render(GAME_NAME, True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 200) + math.sin(time.time()*8)*8))
        
        if count > 200:
            if count == 201:
                SOUNDS.playSound("./sounds/button_show_sound.wav")
            second_button_sprite = pygame.image.load("./sprites/buttons/play.png")
            SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, second_button_sprite.get_width(), second_button_sprite.get_height()):
                second_button_sprite = pygame.image.load("./sprites/buttons/play_dark.png")
                SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    pygame.time.delay(1000)
                    SOUNDS.stopMusic()
                    titleScreen = False

        if count > 250:
            if count == 251:
                SOUNDS.playSound("./sounds/button_show_sound.wav")
            first_button_sprite = pygame.image.load("./sprites/buttons/settings.png")
            SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, first_button_sprite.get_width(), first_button_sprite.get_height()):
                first_button_sprite = pygame.image.load("./sprites/buttons/settings_dark.png")
                SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    titleScreen = False
                    showSettingsScreen()
        
        if count > 300:
            if count == 301:
                SOUNDS.playSound("./sounds/button_show_sound.wav")
                canClick = True
            third_button_sprite = pygame.image.load("./sprites/buttons/exit.png")
            SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, third_button_sprite.get_width(), third_button_sprite.get_height()):
                third_button_sprite = pygame.image.load("./sprites/buttons/exit_dark.png")
                SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    SOUNDS.playSound("./sounds/button_press_sound.wav")
                    pygame.time.delay(1000)
                    pygame.quit()
                    sys.exit()

        # update display
        pygame.display.update()
        # limit the number of fps to prevent
        # problems :)
        CLOCK.tick(60)

        if not canClick:
            count += 1
        else:
            count = 400

    gameThread()


def showSettingsScreen():
    # access to global variables
    global SCREEN
    global FONT
    global OPTIONS
    global MAIN_THEME_STARTED

    while True:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()

        # get mouse position to check if player is clicking on button
        mouseX, mouseY = pygame.mouse.get_pos()

        # draw settings page title
        FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
        main_title = FONT.render(SETTINGS_TITLE, True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 400) + math.sin(time.time()*8)*8))

        # fullscreen option
        FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
        main_title = FONT.render("Fullscreen", True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - 50, SCREEN.get_height()/2 - (main_title.get_height()/2 + 200)))

        if OPTIONS.getValue("fullscreen"):
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 180), main_title.get_height()/2, main_title.get_height()/2))
        else:
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 180), main_title.get_height()/2, main_title.get_height()/2), 3)
        
        if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 180), main_title.get_height()/2, main_title.get_height()/2):
            if mouseClickEvent():
                OPTIONS.setValue("fullscreen", not OPTIONS.getValue("fullscreen"))
                SOUNDS.playSound("./sounds/button_press_settings_sound.wav")
                pygame.display.toggle_fullscreen()

        # vsync option
        FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
        main_title = FONT.render("VSync", True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - 50, SCREEN.get_height()/2 - (main_title.get_height()/2 + 150)))

        if OPTIONS.getValue("vsync"):
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 130), main_title.get_height()/2, main_title.get_height()/2))
        else:
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 130), main_title.get_height()/2, main_title.get_height()/2), 3)

        if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 130), main_title.get_height()/2, main_title.get_height()/2):
            if mouseClickEvent():
                OPTIONS.setValue("vsync", not OPTIONS.getValue("vsync"))
                SOUNDS.playSound("./sounds/button_press_settings_sound.wav")

        # music option
        FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
        main_title = FONT.render("Music", True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - 50, SCREEN.get_height()/2 - (main_title.get_height()/2 + 100)))

        if OPTIONS.getValue("music"):
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 80), main_title.get_height()/2, main_title.get_height()/2))
        else:
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 80), main_title.get_height()/2, main_title.get_height()/2), 3)

        if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 80), main_title.get_height()/2, main_title.get_height()/2):
            if mouseClickEvent():
                OPTIONS.setValue("music", not OPTIONS.getValue("music"))
                SOUNDS.playSound("./sounds/button_press_settings_sound.wav")
                if MAIN_THEME_STARTED:
                    MAIN_THEME_STARTED = False
                    SOUNDS.stopMusic()

        # sounds option
        FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
        main_title = FONT.render("Sounds", True, MAIN_COLOR)
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - 50, SCREEN.get_height()/2 - (main_title.get_height()/2 + 50)))

        if OPTIONS.getValue("sound"):
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 30), main_title.get_height()/2, main_title.get_height()/2))
        else:
            pygame.draw.rect(SCREEN, MAIN_COLOR, (SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 30), main_title.get_height()/2, main_title.get_height()/2), 3)

        if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - 100, SCREEN.get_height()/2 - (main_title.get_height()/2 + 30), main_title.get_height()/2, main_title.get_height()/2):
            if mouseClickEvent():
                OPTIONS.setValue("sound", not OPTIONS.getValue("sound"))
                SOUNDS.playSound("./sounds/button_press_settings_sound.wav")

        # render back to main screen button
        back_button_sprite = pygame.image.load("./sprites/buttons/back.png")
        SCREEN.blit(back_button_sprite, ((SCREEN.get_width()/2 - back_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - back_button_sprite.get_height()/2) + 100))
        if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - back_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - back_button_sprite.get_height()/2) + 100, back_button_sprite.get_width(), back_button_sprite.get_height()):
            back_button_sprite = pygame.image.load("./sprites/buttons/back_dark.png")
            SCREEN.blit(back_button_sprite, ((SCREEN.get_width()/2 - back_button_sprite.get_width()/2) - 300, (SCREEN.get_height()/2 - back_button_sprite.get_height()/2) + 100))
            if mouseClickEvent():
                SOUNDS.playSound("./sounds/button_press_sound.wav")
                showTitleScreen(True)
                break

        # render apply button
        apply_button_sprite = pygame.image.load("./sprites/buttons/apply.png")
        SCREEN.blit(apply_button_sprite, ((SCREEN.get_width()/2 - apply_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - apply_button_sprite.get_height()/2) + 100))
        if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - apply_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - apply_button_sprite.get_height()/2) + 100, apply_button_sprite.get_width(), apply_button_sprite.get_height()):
            apply_button_sprite = pygame.image.load("./sprites/buttons/apply_dark.png")
            SCREEN.blit(apply_button_sprite, ((SCREEN.get_width()/2 - apply_button_sprite.get_width()/2) + 300, (SCREEN.get_height()/2 - apply_button_sprite.get_height()/2) + 100))
            if mouseClickEvent():
                SOUNDS.playSound("./sounds/button_press_sound.wav")
                showTitleScreen(True)
                break

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

    SOUNDS.playMusic("./sounds/game_theme.mp3", True)

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
    # pygame.display.set_icon("./sprites/test.png")

    # show splash screen png
    showSplashScreen()

    # show title screen after splash screen
    showTitleScreen()

    gameThread()

if __name__ == "__main__":
    main()