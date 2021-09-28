import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500, 500)) # initialises game window
    surface.fill((66, 135, 245)) # values from 0 to 255
    pygame.display.flip() # flip to update screen

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:# can find list of event types online
                running = False
