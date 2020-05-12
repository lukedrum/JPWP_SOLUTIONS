import math

import pygame

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(" :-) ")
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (800, 600))


posx = 200
posy = 300

window.blit(bg, (0, 0))
colorcircle = (255, 0, 0)
colorcircle_centre = (255, 255, 255)
size = 15
pygame.draw.circle(window, colorcircle, (posx, posy), size)
pygame.draw.circle(window, colorcircle_centre, (400, 300), 15)
pygame.display.update()
vel = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            posx -= vel

        if keys[pygame.K_RIGHT]:
            posx += vel

        if keys[pygame.K_UP]:
            posy -= vel

        if keys[pygame.K_DOWN]:
            posy += vel

        distance = math.sqrt(((posx - 400)**2) + ((posy -300)**2))
        if distance < (size + 15):
            colorcircle_centre = (255,0,0)

    window.blit(bg, (0, 0))
    pygame.draw.circle(window, colorcircle_centre, (400, 300), 15)
    pygame.draw.circle(window, colorcircle, (posx, posy), 15)
    pygame.display.flip()



pygame.quit()