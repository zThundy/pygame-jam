import sys, pygame, time, math, random
from pygame.locals import *

from player import Player
from events import *

size = width, height = 960, 540
GAME_NAME = "Er tecnico"
GAME_SUBTITLE = "Un gioco brutto fatto da poppity"

# constant variable
SCREEN = None
FONT = None

def showSplashScreen():
    display_splash_screen = 0
    first_string = ""
    second_stirng = ""

    # 4 secondi di attesa
    while display_splash_screen <= 5000:
        SCREEN.fill((0, 0, 0))
        display_splash_screen += 1

        # check events.py to see the executed code
        checkForQuitEvent()

        if display_splash_screen % random.randint(10, 30) == 1:
            if len(first_string) != len(GAME_NAME):
                first_string += GAME_NAME[len(first_string)]
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

        if len(first_string) == len(GAME_NAME) and len(second_stirng) == len(GAME_SUBTITLE):  
            pygame.time.delay(2500)
            break


def showTitleScreen():
    player = Player()
    while True:
        SCREEN.fill((0, 0, 0))
        # check events.py to see the executed code
        checkForQuitEvent()
        # check if user press a movement key and move the player
        player.checkPlayerMovements()

        # draw entity on screen
        SCREEN.blit(player.getCurrentSprite(), player.getPosition())
        
        # update display
        pygame.display.update()
        # wait for 10 seconds
        pygame.time.delay(10)


def main():
    pygame.init()

    # access global variables
    global SCREEN
    global FONT

    # define screen dimensions and flags
    SCREEN = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(GAME_NAME)
    # pygame.display.set_icon("./sprites/test.png")
    SCREEN.fill((0,0,0))

    # use font pygame
    FONT = pygame.font.Font("./fonts/game_over.ttf", 200)

    # show splash screen png
    # showSplashScreen()

    # show title screen after splash screen
    showTitleScreen()

if __name__ == "__main__":
    main()