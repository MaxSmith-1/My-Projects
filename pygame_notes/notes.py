xMovement = [[pygame.KEYDOWN, -1], [pygame.KEYUP, 1]]
    yMovement = [[pygame.K_RIGHT, -1], [pygame.K_LEFT, 1]]
    #player drawn
    player(playerX, playerY)
    for i in xMovement:
        if event.type == i[0]:
            playerX += i[1]
            player(playerX, playerY)
        else:
            print("nothing")
    for i in yMovement:
        if event.type == i[0]:
            playerY += i[1]
            player(playerX, playerY)
        else:
            print("nothing")

if score >= 20:
    c = False
    level += 1
    levelFour()