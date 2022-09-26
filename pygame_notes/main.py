#Goals: 9 levels, easter egg?


import pygame
#music
from pygame import mixer
import random
import math
import time

#initialize pygame, always do this

pygame.init()


#creates window, width x height, starts at top left corner
screen = pygame.display.set_mode((800,600))

mercury = pygame.image.load("pxArt (2).png")
venus = pygame.image.load("pxArt (10).png")
earth = pygame.image.load("pxArt (9).png")
mars = pygame.image.load("pxArt (11).png")
jupiter = pygame.image.load("pxArt (12).png")
saturn = pygame.image.load("pxArt (13).png")
uranus = pygame.image.load("pxArt (14).png")
neptune = pygame.image.load("pxArt (15).png")
pluto = pygame.image.load("pxArt (16).png")
#title
pygame.display.set_caption("Space Journey")

#title image
icon = pygame.image.load('rocket (1).png')
pygame.display.set_icon(icon)

#background images
bi = pygame.image.load
#background sound
mixer.music.load('Interstellar Main Theme - Extra Extended - Soundtrack by Hans Zimmer.ogg')
mixer.music.play(-1)

#player
playerImg = pygame.image.load('rocket (1).png')
playerX = 400
playerY = 500


def player(x, y):
    #draws image
    screen.blit(playerImg, (x,y))

#enemy

enemyNum = 6
enemyNumTwo = 20
enemyNumThree = 35

enemyImg = []
enemyX = []
enemyY = []
enemyDeltaX = []
enemyDeltaY = []
def enemyList(num):
    global enemyImg
    global enemyX
    global enemyY
    global enemyDeltaX
    global enemyDeltaY



    for i in range(num):
        enemyImg.append(pygame.image.load('aircraft.png'))
        enemyX.append(random.randint(5,750))
        enemyY.append(random.randint(50,200))
        enemyDeltaX.append(1)
        enemyDeltaY.append(50)


def enemy(x,y, i):
   screen.blit(enemyImg[i], (x,y))


#bullet
#ready state means you cannot see the bullet on teh screen
#fire - the bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletY = 0
bulletX = 0
bulletDeltaY = 4
bulletState = "ready"

def bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 10, y))


def collision(ex,ey,bx,by):
    distance = math.sqrt((math.pow((ex-bx), 2)) + (math.pow((ey - by), 2)))
    if distance <= 20:
        return True

    else:
        return False

def isOver(px,py,ex,ey):
    distance = math.sqrt((math.pow((ex-px), 2)) + (math.pow((ey - py), 2)))
    if distance <= 10:
        return True
    else:
        return False




#display the score

score = 0
level = 1
font = pygame.font.Font('OriginTech personal use.ttf', 32)

textX = 20
textY = 20

def displayScore(x,y):
    scoreVal = font.render(("Score: " + str(score)), True, (200,200,50))
    levVal = font.render(("Level: " + str(level)), True, (200,200,50))
    screen.blit(scoreVal, (x,y))
    screen.blit(levVal, (x, y+50))

#game over display

fontOver = pygame.font.Font('OriginTech personal use.ttf', 59)


def displayOver():
    overVal = fontOver.render("GAME OVER", True, (255, 0, 0))
    screen.blit(overVal, (400, 300))

#running a window
def mainmenu(x,y):

    b = True
    while b:
        screen.fill((0, 0, 10))
        menu = fontOver.render("Space Journey", True, (255,50,0))
        menu2 = fontOver.render("Press Any Key to Play", True, (255,100, 0))
        screen.blit(menu, (100,100))
        screen.blit(menu2, (x-80,y+300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b = False

            if event.type == pygame.KEYDOWN:
                b = False

                intro()
        pygame.display.update()

introFont = pygame.font.Font('OriginTech personal use.ttf', 20)
def intro():
    e = True
    while e:
        screen.fill((0, 0, 10))

        message2 = introFont.render("A mysterious army has invaded our solar system", True, (255,50,0))
        message3 = introFont.render("Push them back to save us all (ANY KEY TO ADVANCE)", True, (255, 50, 0))



        screen.blit(message2, (100, 100))

        screen.blit(message3, (100, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                e = False
            if event.type == pygame.KEYDOWN:
                e = False
                levelOne()

        pygame.display.update()

easterImg = pygame.image.load('aircraft.png')
def easterEgg():
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
    global enemyNum
    global level
    global l
    global screen


    left = False
    right = False
    up = False
    down = False
    playerX = 50
    playerY = 150
    r = True
    while r:
        screen.fill((0, 0, 10))
        screen.blit(pygame.image.load('mars_city.jpg'), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False

            if event.type == pygame.KEYDOWN:
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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
            #easterEggTwo()
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        player(playerX, playerY)
        screen.blit(easterImg, (400, 150))
        pygame.display.update()

def closing():
    f = True
    while f:
        screen.fill((0, 0, 10))

        endmessage = introFont.render("Enemies Defeated...Return to Base ", True, (255, 50, 0))
        endmessageTwo = introFont.render("For 'peace in out time,' look harder next time...", True, (255, 50, 0))

        screen.blit(endmessage, (100, 100))

        screen.blit(endmessageTwo, (200, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = False
        pygame.display.update()



def createEnemy(num):
    global bulletY
    global bulletX
    global score
    global bulletState
    enemyList(num)
    for i in range(num):

        # Game over text
        if (isOver(playerX, playerY, enemyX[i], enemyY[i])) or (enemyY[i] > 600):
            for j in range(num):
                enemyY[j] = 2000
                o = True
                displayOver()


        enemyX[i] += enemyDeltaX[i]
        if enemyX[i] >= 750:
            enemyDeltaX[i] = -1
            enemyY[i] += enemyDeltaY[i]
        if enemyX[i] <= 0:
            enemyDeltaX[i] = 1
            enemyY[i] += enemyDeltaY[i]

        if collision(bulletX, bulletY, enemyX[i], enemyY[i]):
            bulletY = playerY
            bulletState = "ready"
            score += 1
            print(score)
            mixer.Sound('Arcade Explo A.wav').play()

            enemyX[i] = random.randint(5, 750)
            enemyY[i] = -2000  # random.randint(50, 200)
            enemyDeltaY[i] = 0

        enemy(enemyX[i], enemyY[i], i)


def exit():
    pygame.quit()

l = False

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
    global enemyNum
    global level
    global l
    global screen


    a = True
    o = False
    left = False
    right = False
    up = False
    down = False


    while a:

        screen.fill((0, 0, 10))
        screen.blit(mercury, (0, 0))


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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8




        if playerX >= 750:
            playerX = 750
            #easterEgg()
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        #Enemy restrictions/movement




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



        createEnemy(enemyNum)
        player(playerX, playerY)

        displayScore(textX, textY)


        if score == 6:
            a = False
            level += 1
            levelTwo()

    #window needs to update
        pygame.display.update()


def levelTwo():
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
    global enemyNum
    global level
    global l
    global screen




    c = True
    o = False
    left = False
    right = False
    up = False
    down = False


    while c:
        screen.fill((0, 0, 10))
        screen.blit(venus, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement
        createEnemy(enemyNumTwo)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 20:
            c = False
            level+= 1
            levelThree()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()



def levelThree():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(earth, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(30)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 30:
            c = False
            level+= 1
            levelFour()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelFour():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(mars, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            easterEgg()
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(40)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 40:
            c = False
            level += 1
            levelFive()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelFive():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(jupiter, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(50)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 50:
            c = False
            level += 1
            levelSix()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelSix():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(saturn, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(60)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 60:
            c = False
            level += 1
            levelSeven()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelSeven():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(uranus, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(70)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 70:
            c = False
            level += 1
            levelEight()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelEight():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(neptune, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(80)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 80:
            c = False
            level += 1
            levelNine()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


def levelNine():
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
    global enemyNum
    global level
    global l
    global screen

    c = True
    o = False
    left = False
    right = False
    up = False
    down = False

    while c:
        screen.fill((0, 0, 10))
        screen.blit(pluto, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                # exit()

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
            playerX -= 1.8
        if right:
            playerX += 1.8
        if up:
            playerY -= 1.8
        if down:
            playerY += 1.8

        if playerX >= 750:
            playerX = 750
        if playerX <= 0:
            playerX = 0
        if playerY >= 550:
            playerY = 550
        if playerY <= 0:
            playerY = 0
        # Enemy restrictions/movement

        createEnemy(90)
        if o:
            displayOver()
        # bullet conditions
        if bulletState == "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletDeltaY

        if bulletY < 1:
            bulletY = playerY
            bulletState = "ready"

        # collision

        if score >= 90:
            c = False
            level += 1
            closing()
        player(playerX, playerY)

        displayScore(textX, textY)

        pygame.display.update()


mainmenu(100,100)

