__author__ = "ben"

import pygame
size = 800, 600

pygame.init()

screen = pygame.display.set_mode(size)
test = pygame.image.load("1.png").convert()
bg = pygame.image.load("placeholder.png").convert()
screen.blit(bg, (800,600))
screen.blit(test, (100,0))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "Click!"

pygame.quit()
