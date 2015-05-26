__author__ = "ben"

import pygame, pygame.gfxdraw
size = 800, 600
x,y = 300,400
angle = 10
GREEN         = (   0, 255,   0)
RED           = ( 255,   0,   0)

#class Shuttle(pygame.sprite.Sprite):
#    def __init__(self):
#        self.image = pygame.image.load("1.png")
 #       self.x = 270
 #       self.y = 400
 #       self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite):  # changes the image and can be moved. Use if you want.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = 1
        self.image = pygame.image.load("1.png").convert()
        self.rect = self.image.get_rect()
        self.state = 1
        self.no = 0
        self.x = 0
    def update(self, pressed):
        self.no = self.no + 1
        if self.no <= 2:
            self.state = 1
        elif self.no <= 4:
            self.state = 2
        elif self.no <= 6:
            self.state = 3
        else:
            self.no = 0
        self.x = self.rect.x
        self.image = pygame.image.load(str(self.state) + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.rotate(self.image, angle)
        print angle
    def spinLeft(self):
        global angle
        angle -= 5



pygame.init()

screen = pygame.display.set_mode(size)
bg = pygame.image.load("placeholder.png").convert()

player = Player()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
movespeed = 1  # Change this variable to alter the movement speed of the player.

done = False
while not done:
    global movespeed, Player, angle
    player = Player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "Click!"
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
            y -= movespeed
            print "w is pressed"
    if keys_pressed[pygame.K_s]:
            y += movespeed
            print "s is pressed"
    if keys_pressed[pygame.K_a]:
            x -= movespeed
            print "a is pressed"
    if keys_pressed[pygame.K_d]:
            x += movespeed
            print "d is pressed"
    if keys_pressed[pygame.K_q]:
            player.spinLeft()
            print "q is pressed"

    screen.blit(bg, (0, 0))
    all_sprites_list.update(keys_pressed)
    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()
