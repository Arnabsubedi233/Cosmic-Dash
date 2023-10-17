import pygame
import buttons
import game


pygame.init()

 # Import pygame.locals for easier access to key coordinates
 # Updated to conform to flake8 and black standards
from pygame.locals import (
        RLEACCEL
    )
 # Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE =  (255,255,255)

#variables to hold buttons and images of buttons
play_img = pygame.image.load("images/playbutton.png")
play_button = buttons.Button(250,125,play_img,0.5)

settings_img = pygame.image.load("images/settingsbutton.png")
settings_img = buttons.Button(250,250,settings_img,0.5)

exit_img = pygame.image.load("images/button_quit.png")
exit_button = buttons.Button(250,375,exit_img,0.5)



# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#flag for mainloop
run = True
#clock for better frames
clock = pygame.time.Clock()

#main loop
while run == True:
    #fills screen colour
    screen.fill((0, 0, 20))
    clock.tick(60)

    #selection for if button press = true then executes command
    if play_button.draw(screen):
        game.game()
        run = False
    if settings_img.draw(screen):
        pass
    if exit_button.draw(screen):
        run = False

        

    #driver
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False

    #displays on screen
    pygame.display.flip()
