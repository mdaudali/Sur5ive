__author__ = "ben"

import pygame, pygame.gfxdraw
size = 800, 600

GREEN         = (   0, 255,   0)
RED           = ( 255,   0,   0)

class Shuttle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("1.png")
        self.x = 270
        self.y = 400
        self.rect = self.image.get_rect()



pygame.init()

screen = pygame.display.set_mode(size)
bg = pygame.image.load("placeholder.png").convert()
#player = Shuttle()
vertices = 3


all_sprites_list = pygame.sprite.Group()
#all_sprites_list.add(player)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "Click!"


    screen.blit(bg, (0, 0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()
