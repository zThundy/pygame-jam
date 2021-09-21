import sys, pygame

size = width, height = 550, 550
name = "Prova"

def main(args):
    pygame.init()
    DISPLAY = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(name)
    pygame.display.set_icon("./sprites/test.png")

    # use font pygame
    font = pygame.font.Font("./fonts/game_over.ttf", 100)
    
    # get player skin
    player = pygame.image.load("./sprites/pg.png")
    print("ciao")
