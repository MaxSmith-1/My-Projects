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
screen = pygame.display.set_mode((800,800))


#title
pygame.display.set_caption("Casino")

#title image
icon = pygame.image.load('seven.png')
pygame.display.set_icon(icon)

#background images
background = pygame.image.load('newMCBackground.png')

#machine image
machine = pygame.image.load('actualMachine.png')


#background sound
mixer.music.load('4 - Pigstep (Mono Mix).mp3')
mixer.music.play(-1)


#images
creeper = pygame.image.load('icons8-minecraft-creeper-96.png')
gapple = pygame.image.load('icons8-minecraft-golden-apple-96.png')
diamond = pygame.image.load('icons8-minecraft-diamond-96.png')


#fonts
font = pygame.font.Font('Minecraft.ttf', 32)
eFont = pygame.font.Font('Minecraft.ttf', 64)
class Creeper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        screen.blit(creeper, (self.x, self.y))

class Gapple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        screen.blit(gapple, (self.x, self.y))

class Diamond:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        screen.blit(diamond, (self.x, self.y))



def spin(x,y):

    spinNum = random.randint(0,10)


    if spinNum <= 5:
        Creeper(x,y).display()
    if spinNum > 5 and spinNum < 8:
        Gapple(x,y).display()
    if spinNum >= 8:
        Diamond(x,y).display()





#running a window
isCreeper1 = False
isGapple1 = False
isDiamond1 = False


isCreeper2 = False
isGapple2 = False
isDiamond2 = False


isCreeper3 = False
isGapple3 = False
isDiamond3 = False

balance = 1000
bet = 100
win = 0

creeperBonus = False
gappleBonus = False
diamondBonus = False
smallBonus = False
bigBonus = False


def determine():
    global balance
    global win

    global creeperBonus
    global gappleBonus
    global diamondBonus
    global smallBonus
    global bigBonus

    if isCreeper1 and isCreeper2 and isCreeper3:
        win = 200

        creeperBonus = True
    if isGapple1 and isGapple2 and isGapple3:
        win = 400

        gappleBonus = True
    if isDiamond1 and isDiamond2 and isDiamond3:
        win = 600
        diamondBonus = True
    if isGapple1 and isDiamond2 and isGapple3:
        win = 800
        smallBonus = True
    if isDiamond1 and isGapple2 and isDiamond3:
        win = 2000
        bigBonus = True

    balance += win




def game():
    global isCreeper1
    global isGapple1
    global isDiamond1

    global isCreeper2
    global isGapple2
    global isDiamond2

    global isCreeper3
    global isGapple3
    global isDiamond3

    global balance
    global bet
    global win

    b = True

    s = False
    while b:

        screen.fill((0, 0, 10))
        screen.blit(background, (0, 0))

        screen.blit(machine, (0,200))

        instructions = font.render(("Press Space to Spin"), True, (0,100,0))
        screen.blit(instructions, (240,70))

        balanceBox = font.render(("Balance: $" + str(balance)), True, (0,100,0))
        screen.blit(balanceBox, (10, 210))

        betBox = font.render(("Bet: $" + str(bet)), True, (0, 100, 0))
        screen.blit(betBox, (10, 595))





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    s = True
                    balance -= bet

        spin(125, 360)
        spin(360, 360)
        spin(593, 360)

        if s:
            if balance > 0:
                num = random.randint(1,4)
                if (num == 1) or (num == 2):
                    isCreeper1 = True
                if num == 3:
                    isGapple1 = True
                if num == 4:
                    isDiamond1 = True

                numTwo = random.randint(1,4)
                if (numTwo == 1) or (numTwo == 2):
                    isCreeper2 = True
                if numTwo == 3:
                    isGapple2 = True
                if numTwo == 4:
                    isDiamond2 = True

                numThr = random.randint(1,4)
                if (numThr == 1) or (numThr == 2):
                    isCreeper3 = True

                elif numThr == 3:
                    isGapple3 = True

                elif numThr == 4:
                    isDiamond3 = True



                b = False
                determine()
                rest()
            if balance <= 0:
                yikesBox = eFont.render('Insufficient Funds', True, (150, 0, 0))
                screen.blit(yikesBox, (150, 360))
                if balance <= 0:
                    balance = 0


        pygame.display.update()



def rest():



    global isCreeper1
    global isGapple1
    global isDiamond1

    global isCreeper2
    global isGapple2
    global isDiamond2

    global isCreeper3
    global isGapple3
    global isDiamond3

    global balance
    global bet
    global win

    a = True



    while a:


        screen.fill((0, 0, 10))
        screen.blit(background, (0, 0))

        screen.blit(machine, (0, 200))

        instructions = font.render(("Press Space to Spin"), True, (0, 100, 0))
        screen.blit(instructions, (240, 70))

        balanceBox = font.render(("Balance: $" + str(balance)), True, (0,100,0))
        screen.blit(balanceBox, (10, 210))

        betBox = font.render(("Bet: $" + str(bet)), True, (0, 100, 0))
        screen.blit(betBox, (10, 595))






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    a = False
                    isCreeper1 = False
                    isGapple1 = False
                    isDiamond1 = False

                    isCreeper2 = False
                    isGapple2 = False
                    isDiamond2 = False

                    isCreeper3 = False
                    isGapple3 = False
                    isDiamond3 = False


                    print(str(win))
                    win = 0

                    game()


        if isCreeper1:
            Creeper(125,360).display()
        if isCreeper2:
            Creeper(360,360).display()
        if isCreeper3:
            Creeper(593,360).display()

        if isGapple1:
            Gapple(125,360).display()
        if isGapple2:
            Gapple(360,360).display()
        if isGapple3:
            Gapple(593,360).display()

        if isDiamond1:
            Diamond(125,360).display()
        if isDiamond2:
            Diamond(360,360).display()
        if isDiamond3:
            Diamond(593,360).display()

        if win > 0:
            print('yes')
            winBox = font.render(("Win: $" + str(win)), True, (0, 100, 0))
            screen.blit(winBox, (240, 595))




        pygame.display.update()




game()