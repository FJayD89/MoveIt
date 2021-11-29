import math
from blockClass import OptimalBlock

import pygame
from math import gcd


pygame.display.set_caption('TestWindow')
# icon = pygame.image.load('icon.png')  32x32
# pygame.display.set_icon(icon)
aim = pygame.image.load('C:/Users/tl/Pictures/PxlArt/aim.png')
pygame.init()
screenHeight = 600
screenWidth = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

playerX = screenWidth/2
playerY = screenHeight/2
playerMove = [0.5, 0]
snake = []
length = 0
boardBlocks = []
vertical = 0


def playerUpdate():
    global playerX, playerY

    # move
    if playerX == screenWidth*(2 + 2*playerMove[0])/4:
        playerMove[0] = - playerMove[0]
    playerX += playerMove[0]
    playerY += playerMove[1]

    # draw
    screen.blit(aim, (playerX, playerY))


def drawGrid(width, height):
    for i in range(1, width):
        pygame.draw.line(screen, 0, [i*100, 0], [i*100, 600])
    for i in range(1, height):
        pygame.draw.line(screen, 0, [0, i*100], [800, i*100])


bg = (0, 0, 100)
running = True
while running:

    # default bg = dark blue
    bg = (0, 0, 100)

    # get the mouse position
    pos = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mouse pressed actions
    if pygame.mouse.get_pressed(3)[0]:
        # dark green
        bg = (0, 100, 0)
    else:
        if length >= 2:
            importantCoords = []
            a = [0,0]
            for i in range(length):
                importantCoords.append(snake[i][vertical])
            head = max(importantCoords)
            a[vertical] = head
            a[1-vertical] = snake[0][1-vertical]
            boardBlocks.append(OptimalBlock(length, vertical, a[0], a[1], 'a'))
        snake = []
        length = 0


    # set the bg
    screen.fill(bg)

    # draw stuff on it:

    drawGrid(int(screenWidth/100), int(screenHeight/100))

    # bg based on mPos
    # bg = (0, pos[0]*255/800, pos[1]*255/600)

    for block in boardBlocks:
        for tile in range(block.length):
            x = block.x + (1 - vertical)*tile
            y = block.y + vertical*tile
            pygame.draw.rect(screen, (0, 0, 0), (x * 100, y * 100, 100, 100))

    x = math.floor(pos[0]/100)
    y = math.floor(pos[1]/100)
    if not [x, y] in snake:
        if length < 2:
            snake.append([x, y])
            length += 1
        if length == 2:
            vertical = abs(snake[0][1] - snake[1][1])
        if length >= 2:
            if snake[-1][1 - vertical] == [x, y][1 - vertical]:
                snake.append([x, y])
                length += 1

    for [x, y] in snake:
        pygame.draw.rect(screen, (0, 0, 0), (x*100, y*100, 100, 100))

    playerUpdate()

    # screen.blit(screen)

    pygame.display.update()


# if __name__ == '__main__':
