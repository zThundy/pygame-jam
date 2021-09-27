import pygame, random
from pygame.locals import *
from events import *
from utils import *

CLOCK = pygame.time.Clock()

coords = {
    "1": (55, 150),
    "2": (213, 150),
    "3": (355, 150),
    "4": (55, 245),
    "5": (213, 245),
    "6": (355, 245),
    "7": (55, 340),
    "8": (213, 340),
    "9": (355, 340),

    "0": (213, 435),
    "ok": (213, 515),
}

number_string = ""
secret_code = "7355608"
def keyPadInteraction(SCREEN, mouseX, mouseY, sounds, cb = False):
    global number_string

    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/tasti.png")
    image = pygame.transform.scale(image, (512, 600))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))

    # pygame.draw.rect(s, (255, 0, 0), (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2, image.get_width(), image.get_height()), 1)
    for index in coords:
        # pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + coords[index][0], (SCREEN.get_height()/2 - image.get_height()/2) + coords[index][1], 100, 75), 1)
        if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + coords[index][0], (SCREEN.get_height()/2 - image.get_height()/2) + coords[index][1], 100, 75):
            sounds.playSound("./sounds/tasks/click.wav")
            if len(number_string) < 15 and index != "ok":
                number_string += index
            else:
                if number_string == secret_code:
                    sounds.playSound("./sounds/tasks/correct_task.wav")
                    number_string = ""
                    if cb:
                        cb("keypad")
                else:
                    sounds.playSound("./sounds/tasks/wrong_task.wav")
                    number_string = ""

    FONT = pygame.font.Font("./fonts/game_over.ttf", 100)
    main_title = FONT.render(number_string, True, (0, 0, 0))
    s.blit(main_title, ((SCREEN.get_width()/2 - image.get_width()/2) + 100, (SCREEN.get_height()/2 - image.get_height()/2) + 45))

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)

def boardInteraction(SCREEN, mouseX, mouseY, sounds, cb = False):
    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/post_it.png")
    image = pygame.transform.scale(image, (256, 256))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))
    
    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)

bin_opened = False
folder_1_opened = False
web_opened = False
def computerInteractions(SCREEN, mouseX, mouseY, sounds, cb = False):
    global bin_opened
    global folder_1_opened
    global web_opened
    bin = False

    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    s.fill((0, 0, 0, 200))
    
    pc = pygame.image.load("./sprites/rooms/room_elements/pc/desktop_sfondo.png")
    pc = pygame.transform.scale(pc, (900, 600))
    s.blit(pc, (SCREEN.get_width()/2 - pc.get_width()/2, SCREEN.get_height()/2 - pc.get_height()/2))
    
    image = pygame.image.load("./sprites/rooms/room_elements/pc/cestino.png")
    image = pygame.transform.scale(image, (45, 45))
    s.blit(image, ((SCREEN.get_width()/2 - pc.get_width()/2) + 80, (SCREEN.get_height()/2 - pc.get_height()/2) + 60))
    
    image = pygame.image.load("./sprites/rooms/room_elements/pc/cartella_desktop.png")
    image = pygame.transform.scale(image, (70, 70))
    s.blit(image, ((SCREEN.get_width()/2 - pc.get_width()/2) + 140, (SCREEN.get_height()/2 - pc.get_height()/2) + 250))
    
    image = pygame.image.load("./sprites/rooms/room_elements/pc/cartella_desktop_piena.png")
    image = pygame.transform.scale(image, (70, 70))
    s.blit(image, ((SCREEN.get_width()/2 - pc.get_width()/2) + 210, (SCREEN.get_height()/2 - pc.get_height()/2) + 150))
    
    image = pygame.image.load("./sprites/rooms/room_elements/pc/cartella_desktop_piena.png")
    image = pygame.transform.scale(image, (70, 70))
    s.blit(image, ((SCREEN.get_width()/2 - pc.get_width()/2) + 280, (SCREEN.get_height()/2 - pc.get_height()/2) + 90))
    
    image = pygame.image.load("./sprites/rooms/room_elements/pc/logo_internet.png")
    image = pygame.transform.scale(image, (70, 70))
    s.blit(image, ((SCREEN.get_width()/2 - pc.get_width()/2) + 450, (SCREEN.get_height()/2 - pc.get_height()/2) + 170))

    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - pc.get_width()/2) + 140, (SCREEN.get_height()/2 - pc.get_height()/2) + 250, 45, 45):
        sounds.playSound("./sounds/tasks/mouse_click.wav")
        folder_1_opened = True
        bin_opened = False
        web_opened = False
    
    if folder_1_opened:
        bin = pygame.image.load("./sprites/rooms/room_elements/pc/folder_interfaccia.png")
        bin = pygame.transform.scale(bin, (500, 500))
        s.blit(bin, (SCREEN.get_width()/2 - bin.get_width()/2, SCREEN.get_height()/2 - bin.get_height()/2))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - bin.get_width()/2) + 15, (SCREEN.get_height()/2 - bin.get_height()/2) + 15, 10, 10))

    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - pc.get_width()/2) + 80, (SCREEN.get_height()/2 - pc.get_height()/2) + 60, 45, 45):
        sounds.playSound("./sounds/tasks/mouse_click.wav")
        bin_opened = True
        folder_1_opened = False
        web_opened = False
    
    if bin_opened:
        bin = pygame.image.load("./sprites/rooms/room_elements/pc/bin_interfaccia.png")
        bin = pygame.transform.scale(bin, (500, 500))
        s.blit(bin, (SCREEN.get_width()/2 - bin.get_width()/2, SCREEN.get_height()/2 - bin.get_height()/2))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - bin.get_width()/2) + 15, (SCREEN.get_height()/2 - bin.get_height()/2) + 15, 10, 10))

    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - pc.get_width()/2) + 450, (SCREEN.get_height()/2 - pc.get_height()/2) + 170, 45, 45):
        sounds.playSound("./sounds/tasks/mouse_click.wav")
        bin_opened = False
        folder_1_opened = False
        web_opened = True
    
    if web_opened:
        bin = pygame.image.load("./sprites/rooms/room_elements/pc/web_interfaccia.png")
        bin = pygame.transform.scale(bin, (500, 500))
        s.blit(bin, (SCREEN.get_width()/2 - bin.get_width()/2, SCREEN.get_height()/2 - bin.get_height()/2))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - bin.get_width()/2) + 15, (SCREEN.get_height()/2 - bin.get_height()/2) + 15, 10, 10))

    if bin and checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - bin.get_width()/2) + 15, (SCREEN.get_height()/2 - bin.get_height()/2) + 15, 10, 10):
        sounds.playSound("./sounds/tasks/mouse_click.wav")
        bin_opened = False
        folder_1_opened = False
        web_opened = False

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)

pixel_counter = 0
green_cable = "None"
red_cable = "None"
yellow_cable = "None"
def serverInteraction_1(SCREEN, mouseX, mouseY, sounds, cb = False):
    global pixel_counter
    global green_cable
    global red_cable
    global yellow_cable

    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/server_rack_interface.png")
    image = pygame.transform.scale(image, (768, 768))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))

    # first led row
    if pixel_counter > 50 and pixel_counter < 70:
        pygame.draw.rect(s, (0, 0, 255), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    if pixel_counter > 80 and pixel_counter < 95:
        pygame.draw.rect(s, (255, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    if random.randint(0, pixel_counter) >= random.randint(0, pixel_counter):
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    # second led row
    if pixel_counter > 50 and pixel_counter < 90:
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 348, 36, 36))
    if pixel_counter > 10 and pixel_counter < 100:
        pygame.draw.rect(s, (255, 150, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 348, 36, 36))
    if green_cable != "Plugged" and red_cable != "Plugged" and yellow_cable != "Plugged":
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
    if green_cable == "Plugged" and red_cable != "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
    if green_cable == "Plugged" and red_cable == "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))


    pygame.draw.rect(s, (255, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 396, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
    # check if green cable is plugged in
    if green_cable == "Plugged_1" or green_cable == "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))
    # check if red cable is plugged in
    if red_cable == "Plugged_1" or red_cable == "Plugged":
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))
    # check if yellow cable is plugged in
    if yellow_cable == "Plugged_1" or yellow_cable == "Plugged":
        pygame.draw.rect(s, (255, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 396, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))

    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if green_cable == "None":
            green_cable = "Plugged_1"
        elif green_cable == "Plugged_1":
            green_cable = "None"
        elif green_cable == "Plugged_2":
            green_cable = "Plugged"
    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if red_cable == "None":
            red_cable = "Plugged_1"
        elif red_cable == "Plugged_1":
            red_cable = "None"
        elif red_cable == "Plugged_2":
            red_cable = "Plugged"
    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 396, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if yellow_cable == "None":
            yellow_cable = "Plugged_1"
        elif yellow_cable == "Plugged_1":
            yellow_cable = "None"
        elif yellow_cable == "Plugged_2":
            yellow_cable = "Plugged"
    
    if pixel_counter > 100:
        pixel_counter = 0
    
    pixel_counter += 1

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)

def serverInteraction_2(SCREEN, mouseX, mouseY, sounds, cb = False):
    global pixel_counter
    global green_cable
    global red_cable
    global yellow_cable

    s = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), SRCALPHA)
    image = pygame.image.load("./sprites/rooms/room_elements/server_rack_interface.png")
    image = pygame.transform.scale(image, (768, 768))
    s.fill((0, 0, 0, 200))
    s.blit(image, (SCREEN.get_width()/2 - image.get_width()/2, SCREEN.get_height()/2 - image.get_height()/2))

    # first led row
    if pixel_counter > 50 and pixel_counter < 70:
        pygame.draw.rect(s, (0, 0, 255), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    if pixel_counter > 80 and pixel_counter < 95:
        pygame.draw.rect(s, (255, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    if random.randint(0, pixel_counter) >= random.randint(0, pixel_counter):
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 180, 36, 36))
    # second led row
    if pixel_counter > 50 and pixel_counter < 90:
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 348, 36, 36))
    if pixel_counter > 10 and pixel_counter < 100:
        pygame.draw.rect(s, (255, 150, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 348, 36, 36))
    if green_cable != "Plugged" and red_cable != "Plugged":
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
    if green_cable == "Plugged" and red_cable != "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
    if green_cable == "Plugged" and red_cable == "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 516, 36, 36))

    # check if green cable is plugged in
    if green_cable == "Plugged_2" or green_cable == "Plugged":
        pygame.draw.rect(s, (0, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))
    # check if red cable is plugged in
    if red_cable == "Plugged_2" or red_cable == "Plugged":
        pygame.draw.rect(s, (255, 0, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))
    # check if yellow cable is plugged in
    if yellow_cable == "Plugged_2" or yellow_cable == "Plugged":
        pygame.draw.rect(s, (255, 255, 0), ((SCREEN.get_width()/2 - image.get_width()/2) + 396, (SCREEN.get_height()/2 - image.get_height()/2) + 660, 36, 280))

    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 468, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if green_cable == "None":
            green_cable = "Plugged_2"
        elif green_cable == "Plugged_2":
            green_cable = "None"
        elif green_cable == "Plugged_1":
            green_cable = "Plugged"
    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 540, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if red_cable == "None":
            red_cable = "Plugged_2"
        elif red_cable == "Plugged_2":
            red_cable = "None"
        elif red_cable == "Plugged_1":
            red_cable = "Plugged"
    if checkCollisionAndMouseClick(mouseX, mouseY, 3, 3, (SCREEN.get_width()/2 - image.get_width()/2) + 396, (SCREEN.get_height()/2 - image.get_height()/2) + 648, 36, 36):
        sounds.playSound("./sounds/tasks/cable_plug.wav")
        if yellow_cable == "None":
            yellow_cable = "Plugged_2"
        elif yellow_cable == "Plugged_2":
            yellow_cable = "None"
        elif yellow_cable == "Plugged_1":
            yellow_cable = "Plugged"
    
    if pixel_counter > 100:
        pixel_counter = 0
    
    pixel_counter += 1

    SCREEN.blit(s, (0, 0))
    # update display
    pygame.display.update()
    # limit the number of fps to prevent
    # problems :)
    CLOCK.tick(60)