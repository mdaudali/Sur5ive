__author__ = 'mohammed'
import pygame
#import game
import button

pygame.init()
size = width, height = 800, 600 # screen size
screen = pygame.display.set_mode(size) # sets the screen size
# menu = pygame.image.load("menuart.png").convert() # gets menu code and converts into optimised format
# logo = pygame.image.load("logo.png").convert() # same for logo
# logo.set_colorkey(button.BLACK)
rocket_1 = pygame.image.load("1.png").convert()
rocket_2 = pygame.image.load("2.png").convert()
rocket_3 = pygame.image.load("3.png").convert()
rocket_4 = pygame.image.load("4.png").convert()
rocket_state = 0
btn = button.Button("Testing sizes", 200, 350,400,50) # creates button with text
btn2 = button.Button("Yay!", 200, 410, 400, 50 )
while 1:
    mouse = pygame.mouse.get_pos() # gets mouse position for mouseover
    for event in pygame.event.get(): # checks for special events such as quit and click
        if event.type == pygame.QUIT: pygame.quit() # if quit event, quit pygame
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            if btn.rect.collidepoint(mouse): # checks if mouse is over the button
                print("button one clicked")
                #game.game()
    # screen.blit(menu, [0,0]) # draws menu on screen
    # screen.blit(logo, [133.5,56.5]) # draws logo on screen
    btn.draw(mouse, screen) # draws button on screen
    btn2.draw(mouse, screen)
    if rocket_state <= 25:
        screen.blit(rocket_1, [0,0])
    elif rocket_state <= 50:
        screen.blit(rocket_2, [0,0])
    elif rocket_state <= 75:
        screen.blit(rocket_3, [0,0])
    elif rocket_state <= 100:
        screen.blit(rocket_4, [0,0])
    else:
        rocket_state = 0
    rocket_state = rocket_state + 1
    pygame.display.flip() # updates screen

    #HELLO workld