__author__ = 'mohammed'
import pygame
#import game
import button
pygame.init()

all_sprites_list = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
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
        if pygame.K_w in pressed:
            print("w is pressed")
        if pygame.K_s in pressed:
            print("s is pressed")
        if pygame.K_a in pressed:
            print("a is pressed")
        if pygame.K_d in pressed:
            print("d is pressed")
        self.x = self.rect.x
        self.image = pygame.image.load(str(self.state) + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x + 1


size = width, height = 800, 600 # screen size
screen = pygame.display.set_mode(size) # sets the screen size
# menu = pygame.image.load("menuart.png").convert() # gets menu code and converts into optimised format
# logo = pygame.image.load("logo.png").convert() # same for logo
# logo.set_colorkey(button.BLACK)
btn = button.Button("Testing sizes", 200, 350,400,50) # creates button with text
btn2 = button.Button("Yay!", 200, 410, 400, 50)
rocket12 = Player()
all_sprites_list.add(rocket12)
while 1:
    mouse = pygame.mouse.get_pos() # gets mouse position for mouseover
    for event in pygame.event.get(): # checks for special events such as quit and click
        if event.type == pygame.QUIT: pygame.quit() # if quit event, quit pygame
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            if btn.rect.collidepoint(mouse): # checks if mouse is over the button
                print("button one clicked")
    pressed = pygame.key.get_pressed()
                #game.game()
    # screen.blit(menu, [0,0]) # draws menu on screen
    # screen.blit(logo, [133.5,56.5]) # draws logo on screen
    screen.fill(button.BLACK) #resets screen
    btn.draw(mouse, screen) # draws button on screen
    btn2.draw(mouse, screen)
    all_sprites_list.update(pressed) #calls update
    all_sprites_list.draw(screen) #redraws image
    pygame.display.flip() # updates screen