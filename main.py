import sys, pygame, time, math, random
from pygame.locals import *

from player import Player
from events import *
from level import Level
from display import *
from utils import *

size = width, height = 1920, 1080
GAME_NAME = "Er tecnico"
GAME_TITLE = "Python Gamejam"
GAME_SUBTITLE = "Un gioco brutto fatto da poppity"

# constant variable
SCREEN = 0
FONT = 0

def showSplashScreen():
    # access to global variables
    global SCREEN
    global FONT

    display_splash_screen = 0
    first_string = ""
    second_stirng = ""

    # 4 secondi di attesa
    while display_splash_screen <= 5000:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()

        if display_splash_screen % random.randint(10, 20) == 1:
            if len(first_string) != len(GAME_TITLE):
                first_string += GAME_TITLE[len(first_string)]
                audio_keyboard = pygame.mixer.Sound("./sounds/keyboard/" + str(random.randint(1, 10)) + ".wav")
                pygame.mixer.Sound.play(audio_keyboard)
            elif len(second_stirng) != len(GAME_SUBTITLE):
                second_stirng += GAME_SUBTITLE[len(second_stirng)]
                audio_keyboard = pygame.mixer.Sound("./sounds/keyboard/" + str(random.randint(1, 10)) + ".wav")
                pygame.mixer.Sound.play(audio_keyboard)

        # ovverwrite prev font element to have bigger dimension
        FONT = pygame.font.Font("./fonts/game_over.ttf", 250)
        main_title = FONT.render(first_string, True, (50, 255, 50))
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 150)))
        
        FONT = pygame.font.Font("./fonts/game_over.ttf", 150)
        main_subtitle = FONT.render(second_stirng, True, (50, 255, 50))
        SCREEN.blit(main_subtitle, (SCREEN.get_width()/2 - main_subtitle.get_width()/2, main_title.get_height() + SCREEN.get_height()/2 - (main_subtitle.get_height()/2 + 150)))

        # update display
        pygame.display.update()
        # wait for 10 seconds
        pygame.time.delay(10)

        if len(first_string) == len(GAME_TITLE) and len(second_stirng) == len(GAME_SUBTITLE):  
            pygame.time.delay(2500)
            break
        
        # increment this counter to show the screen for a little bit more
        display_splash_screen += 1


def showTitleScreen():
    # access to global variables
    global SCREEN
    global FONT

    titleScreen = True
    SCREEN.fill((0, 0, 0))
    pygame.time.delay(2000)

    pygame.mixer.music.load("./sounds/main_theme.mp3")
    pygame.mixer.music.play(-1)

    count = 0
    canClick = False
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
        main_title = FONT.render(GAME_NAME, True, (50, 255, 50))
        SCREEN.blit(main_title, (SCREEN.get_width()/2 - main_title.get_width()/2, SCREEN.get_height()/2 - (main_title.get_height()/2 + 200) + math.sin(time.time()*8)*8))

        if count > 250:
            if count == 251:
                button_sound = pygame.mixer.Sound("./sounds/button_show_sound.wav")
                pygame.mixer.Sound.play(button_sound)
            first_button_sprite = pygame.image.load("./sprites/buttons/settings.png")
            SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, first_button_sprite.get_width(), first_button_sprite.get_height()):
                first_button_sprite = pygame.image.load("./sprites/buttons/settings_dark.png")
                SCREEN.blit(first_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) - 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    button_sound = pygame.mixer.Sound("./sounds/button_press_sound.wav")
                    pygame.mixer.Sound.play(button_sound)
                    print("settings")
        
        if count > 200:
            if count == 201:
                button_sound = pygame.mixer.Sound("./sounds/button_show_sound.wav")
                pygame.mixer.Sound.play(button_sound)
            second_button_sprite = pygame.image.load("./sprites/buttons/play.png")
            SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, second_button_sprite.get_width(), second_button_sprite.get_height()):
                second_button_sprite = pygame.image.load("./sprites/buttons/play_dark.png")
                SCREEN.blit(second_button_sprite, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    button_sound = pygame.mixer.Sound("./sounds/button_press_sound.wav")
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(1000)
                    pygame.mixer.music.stop()
                    titleScreen = False
        
        if count > 300:
            if count == 301:
                button_sound = pygame.mixer.Sound("./sounds/button_show_sound.wav")
                pygame.mixer.Sound.play(button_sound)
                canClick = True
            third_button_sprite = pygame.image.load("./sprites/buttons/exit.png")
            SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
            if checkCollisions(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100, third_button_sprite.get_width(), third_button_sprite.get_height()):
                third_button_sprite = pygame.image.load("./sprites/buttons/exit_dark.png")
                SCREEN.blit(third_button_sprite, ((SCREEN.get_width()/2 - second_button_sprite.get_width()/2) + 400, (SCREEN.get_height()/2 - second_button_sprite.get_height()/2) + 100))
                if (mouseClickEvent() and canClick):
                    button_sound = pygame.mixer.Sound("./sounds/button_press_sound.wav")
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(1000)
                    pygame.quit()
                    sys.exit()

        # update display
        pygame.display.update()
        # wait for 10 seconds
        pygame.time.delay(10)

        if not canClick:
            count += 1
        else:
            count = 400


def gameThread():
    # access to global variables
    global SCREEN
    global FONT

    player = Player(SCREEN)
    level = Level(SCREEN)

    pygame.mixer.music.load("./sounds/game_theme.mp3")
    pygame.mixer.music.play()

    # this function ready the level generator
    # and creates a grid of elements with their images inside
    level.generateGrid()

    while True:
        # fill every time the screen with black color to reset
        # every element on the screen
        SCREEN.fill((0, 0, 0))

        # check events.py to see the executed code
        checkForQuitEvent()

        # check if user press a movement key and move the player
        player.checkPlayerMovements()

        # draw grid
        level.generateWalls()

        # draw entity on screen
        SCREEN.blit(player.getCurrentSprite(), player.getPosition())

        # update display
        pygame.display.update()
        # wait for 10 seconds
        pygame.time.delay(10)


def main():
    pygame.init()

    # access to global variables
    global SCREEN

    # define screen dimensions and flags
    SCREEN = pygame.display.set_mode(size)
    SCREEN = setFullScreen(SCREEN, size, False)
    pygame.display.set_caption(GAME_NAME)

    # fill both fake and real screen with black background
    SCREEN.fill((0, 0, 0))
    # pygame.display.set_icon("./sprites/test.png")

    # show splash screen png
    # showSplashScreen()

    # show title screen after splash screen
    # showTitleScreen()

    # start the game if the showTitleScreen thread is broken
    gameThread()

if __name__ == "__main__":
    main()