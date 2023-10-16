import pygame
import buttons
import game


pygame.init()

from pygame.locals import (
        RLEACCEL
    )

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE =  (255,255,255)

play_img = pygame.image.load("images/playbutton.png")
play_button = buttons.Button(250,125,play_img,0.5)

settings_img = pygame.image.load("images/settingsbutton.png")
settings_img = buttons.Button(250,250,settings_img,0.5)

exit_img = pygame.image.load("images/button_quit.png")
exit_button = buttons.Button(250,375,exit_img,0.5)




screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

clock = pygame.time.Clock()

while run == True:
    screen.fill((0, 0, 20))
    clock.tick(60)

    if play_button.draw(screen):
        game.game()
        run = False
    if settings_img.draw(screen):
        pass
    if exit_button.draw(screen):
        run = False

        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    pygame.display.flip()
