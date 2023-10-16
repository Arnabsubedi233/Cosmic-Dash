import pygame
import Cosmic_Dash
import buttons

pygame.init()

from pygame.locals import (
        RLEACCEL
    )

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE =  (255,255,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

clock = pygame.time.Clock()

while run == True:
    screen.fill((0, 0, 20))
    clock.tick(60)






   



