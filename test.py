import pygame
from pygame.locals import *
counter = 2
screen = pygame.display.set_mode((500,500))
pygame.init()
while 1:
    pygame.event.get()
    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]:
        if counter % 2:
            screen.blit(pygame.image.load("images/kek.png"),(0,0))
            pygame.display.flip()
        else:
            screen.blit(pygame.image.load("images/plain.png"),(0,0))
            pygame.display.flip()
        counter = counter + 1
        pygame.time.delay(100)
