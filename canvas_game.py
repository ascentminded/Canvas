#Credit: Code.pylet on youtube for the tutorials that helped me understand pygame

#On pycharm, mouse over "pycharm" and choose to download pygame package, if you don't already have it
import pygame

import sys,os
from pygame.locals import *

#The two variables that you need to change to suit your own game are here:
#If you store the background image 'stage.png' and the character image 'hero.png' in a folder called images in the home folder, it will work. Otherwise, change the file locations to suit your own arrangement.
stage = os.path.join('images', 'stage.png')
hero  = os.path.join('images', 'hero.png')


#initializing display
W, H = 1026,1026
HW, HH =W/2, H/2
AREA = W*H



CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("HAPPY EXPLORING!")
FPS = 500

# 'events' becomes relevant later on in the while loop (line 65)
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()



#colours
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

#setting background image (the .convert() is important here, but not for sprites)
bg = pygame.image.load(stage).convert()
bgWidth, bgHeight = bg.get_rect().size

#Player image and sprites:
player_image = pygame.image.load(hero)

stageWidth = bgWidth
stageHeight = bgHeight
stagePosX = 0
stagePosY = 0
#if the character reaches the end of the image, the screen shouldn't keep scrolling to keep them at the centre, y'know? Unfortunately, there are still a few problems (you can see the right end of the image if you move close enough to the left,etc)
startScrollingPosX = HW
startScrollingPosY = HH

# 'circle' is a holdover from the initial draft of this code, where the sprite was a simple white circle, made using a draw function. circleRadius is nevertheless a good constant to set the position of the sprite, so it was left in
circleRadius = 25
circlePosX = circleRadius
circlePosY = circleRadius

playerPosX = HW
playerPosY = HH
#playerPosY = 2308.5
playerVelocityX = 0
playerVelocityY = 0
#I'm making a variable v, which you can change the value of speed everywhere to make the sprite move faster or slower, to taste/convenience
v = 2

#the following is a standard chunk of code, mapping buttons to movement.
# events (line 22) was used to define the escape button. There are Key-down and key-up (mentioned there), which shows whether you hold it down or just click it. Here, we use get_pressed() instead, i believe.
while True:
    events()
    k=pygame.key.get_pressed()
    if k[K_RIGHT]:
        playerVelocityX= v
    elif k[K_LEFT]:
        playerVelocityX= -v

    elif k[K_UP]:
        playerVelocityY = -v
    elif k[K_DOWN]:
        playerVelocityY = v
    else:
        playerVelocityX = 0
        playerVelocityY = 0

    playerPosX += playerVelocityX

#all the edge cases, preventing the sprite from moving off the left end of the background onto the right end, etc
    if playerPosX > stageWidth-circleRadius:
        playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius - 300:
        playerPosX = circleRadius - 300
    if playerPosX < startScrollingPosX - 300:
        circlePosX = playerPosX-stageWidth - 300
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX-stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX

    playerPosY += playerVelocityY
    if playerPosY > stageHeight -circleRadius:
        playerPosY = stageHeight - circleRadius
    elif playerPosY < circleRadius:
        playerPosY = circleRadius
    elif playerPosY < startScrollingPosY:
        circlePosY = playerPosY - stageHeight
    elif playerPosY > stageHeight - startScrollingPosY:
        circlePosY = playerPosY - stageHeight + H
    else:
        circlePosY = startScrollingPosY
        stagePosY += -playerVelocityY

#crucial, this is what we use to draw the image and sprite onto the screen.
    rel_x = stagePosX % bgWidth
    rel_y = stagePosY % bgHeight
    DS.blit(bg,(rel_x - bgWidth,rel_y - bgHeight))
    if rel_x < W and rel_y < H:
        DS.blit(bg, (rel_x,rel_y))
    elif rel_x >= W and rel_y < H:
        DS.blit(bg,(rel_x - bgWidth,rel_y))
    elif rel_x < W and rel_y >= H:
        DS.blit(bg, (rel_x, rel_y - bgHeight))
    else:
        DS.blit(bg, (rel_x - bgWidth, rel_y - bgHeight))



    DS.blit(player_image, (circlePosX, circlePosY))
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
#And that's it!