

import pygame
import pygame.gfxdraw
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

scale = 5

gameDisplay = pygame.display.set_mode((200*scale,100*scale))
gameDisplay.fill(black)

# pixAr = pygame.PixelArray(gameDisplay)
# pixAr[10][20] = green

# pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
#
pygame.draw.rect(gameDisplay, white, (90*scale,40*scale,20*scale,20*scale))
#
pygame.draw.circle(gameDisplay, white, (160*scale,50*scale), 15*scale)

# pygame.draw.polygon(gameDisplay, white, ((25,75),(76,125),(250,375),(400,25),(60,540)))

def check_Obstacle(x, y):
#   For square
    if x>=90 and x<=110 and y>=40 and y<=60:
        return  True
#   For Circle
    if (x-160)**2 + (y-50)**2 < 15**2:
        return True
    else:
        return False

# if check_Obstacle(109,60):
#     print("Obstacle detected!!")
# else:
#     print("No Obstacle!!")

def draw_Explored_Nodes(x,y):
    pygame.gfxdraw.pixel(gameDisplay,x,y,red)
    pygame.display.update()
    # return None
# for  x in range (50):
#     for y in range (100):
#         draw_Explored_Nodes(x,y)
        # time.sleep()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


