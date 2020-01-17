import pygame
from pygame.locals import *
import random
pygame.init()

randomNumber = random.randint(1,450)
randomNumber2 = random.randint(1,450)
x = 0
squareCount = 0
beenHere = 0

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

colour = RED

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AIM training | Score: 0")
screen.fill(BLACK)
pygame.display.flip()

pygame.time.set_timer(USEREVENT + 1, 750)

done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        print(event)
    if event.type == pygame.QUIT:
        done = True
    if event.type == USEREVENT + 1:
        screen.fill(BLACK)
        randomNumber = random.randint(1,450)
        randomNumber2 = random.randint(1,450)
        mySquare = pygame.draw.rect(screen,colour,(randomNumber,randomNumber2,55,55),5)
        squareCount = squareCount + 1
        if squareCount == 50:
            done == True
        pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN:
        y, z = pygame.mouse.get_pos()
        is_inside = mySquare.collidepoint(y, z)
        if is_inside and colour == RED:
            x = x+1
            text = str(x)
            pygame.display.set_caption("AIM training | Score " + text)
            colour = RED

clock.tick(20)
pygame.quit()
