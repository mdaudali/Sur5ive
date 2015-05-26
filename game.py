__author__ = "ben"

import pygame
size = 800, 600

pygame.init()

screen = pygame.display.set_mode(size)
test = pygame.image.load("1.png").convert()
bg = pygame.image.load("placeholder.png").convert()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "Click!"
    screen.blit(bg, (0,0))
    screen.blit(test, (0,0))
    pygame.display.flip()

pygame.quit()
