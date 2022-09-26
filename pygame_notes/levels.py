import pygame
#music
from pygame import mixer
import random
import math
import time





def levelOne():
    global playerY
    global playerX
    global bulletY
    global bulletX
    global bulletState
    global enemyY
    global enemyX
    global enemyDeltaY
    global enemyDeltaX
    global score


    a = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while a:
        screen.fill((0, 0, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False
                #exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and bulletState == "ready":
                    mixer.Sound('atariAsteroids default.wav').play()
                    bulletX = playerX
                    bulletY = playerY
                    bullet(bulletX, bulletY)

# player movement
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
        # Player restrictions
        if left:
            playerX -= .4
        if right:
            playerX += .4
        if up:
            playerY -= .4
        if down:
            playerY += .4




        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        #Enemy restrictions/movement


        for i in range(enemyNum):

        # Game over text
            if (isOver(playerX, playerY, enemyX[i], enemyY[i])) or (enemyY[i] > 600):
                for j in range(enemyNum):
                    enemyY[j] = 2000
                    o = True
                break

            enemyX[i] += enemyDeltaX[i]
            if enemyX[i] >= 750:
                    enemyDeltaX[i] = -.3
                    enemyY[i] += enemyDeltaY[i]
            if enemyX[i] <= 0:
                    enemyDeltaX[i] = .3
                    enemyY[i] += enemyDeltaY[i]

            if collision(bulletX, bulletY, enemyX[i], enemyY[i]):
                bulletY = playerY
                bulletState = "ready"
                score += 1
                print(score)
                mixer.Sound('Arcade Explo A.wav').play()

                enemyX[i] = random.randint(5, 750)
                enemyY[i] = -2000 #random.randint(50, 200)
                enemyDeltaY[i] = 0

            enemy(enemyX[i], enemyY[i], i)
        if o:
            displayOver()
#bullet conditions
        if bulletState == "fire":

            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

#collision




        player(playerX, playerY)

        displayScore(textX, textY)

    #window needs to update
        pygame.display.update()

