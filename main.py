import pygame
import random
from player import player
from enemy import enemy
from assets import assets

pygame.init()

screen_width = 900
screen_height = 500
fps = 60

clock = pygame.time.Clock()
win = pygame.display.set_mode((screen_width, screen_height))
level = pygame.Surface((screen_width, screen_height))

mainAssets = assets(pygame).mainAssets((screen_width, screen_height))

level.blit(mainAssets.bgCloudBack, (0, 0))
level.blit(mainAssets.bgCloudFront, (0, 0))
level.blit(mainAssets.bgBack, (0, 0))
level.blit(mainAssets.bgFront, (0, 0))

ground = assets(pygame).getGroundBlock()

for x in range(0, screen_width, 48):
    level.blit(ground.img, (x, screen_height - ground.h))

pygame.display.set_caption("The Glorious Unnamed Game")

font = pygame.font.Font("fonts/Abibas.ttf", 35)
fontSmall = pygame.font.Font("fonts/Abibas.ttf", 25)

textHealth = font.render("Health: ", True, (255, 255, 255))
textScore = fontSmall.render("Score: ", True, (255, 0, 0))
textDied = font.render("You Died", True, (255, 0, 0))
textNewGame = fontSmall.render("Press ENTER to start a new game", True, (255, 255, 0))

man = player(pygame, (screen_width - (screen_width / 2) - 65), screen_height - 106, 64, 64, assets(pygame).getMan())

def newEnemy(x):
    xInit = (random.randint(1, 20)) * 5 * -1
    if x % 2 == 0:
        xInit = screen_width + (x + 1) * 5

    e = enemy(pygame, xInit, screen_height - 102, 64, 64, 450, assets(pygame).getEnemy())
    e.vel = random.randint(1, 4)
    return e

def initEnemies():
    global enemies
    enemies = []
    for x in range(5):
        enemies.append(newEnemy(x))

def resetGame():
    man.life = 100
    man.x = (screen_width - (screen_width / 2)) - 64
    man.score = 0
    initEnemies()

def redrawGameWindow():

    if man.life < 1:
        win.fill((0, 0, 0))
        win.blit(textDied, [screen_width // 2 - textDied.get_width() // 2, screen_height // 2 - textDied.get_height() //2])
        win.blit(textNewGame, [screen_width // 2 - textNewGame.get_width() // 2, screen_height // 2 - textNewGame.get_height() // 2 + 80])

        txtFinalScore = font.render("Final Score: {}".format(man.score), True, (255, 0, 0))
        win.blit(txtFinalScore, [screen_width // 2 - txtFinalScore.get_width() // 2, screen_height // 2 - txtFinalScore.get_height() // 2 + 120])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
            resetGame()

    else:
        # Drawing bg images
        win.blit(level, win.get_rect())

        man.draw(win)

        for goblin in enemies:
            goblin.draw(win, man)

        textHealthValue = font.render(str(man.life), True, (255, 255, 255))
        win.blit(textHealth, [10, 10])
        win.blit(textHealthValue, [textHealth.get_width() + 10, 10])

        textScoreValue = fontSmall.render(str(man.score), True, (255, 0, 0))
        win.blit(textScore, [10, 50])
        win.blit(textScoreValue, [textScore.get_width() + 10, 50])

    pygame.display.update()


#mainLoop
run = True
initEnemies()
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False

    man.move(screen_width, screen_height)
    for goblin in enemies:
        man.checkHit(goblin.x, goblin.y, goblin.strength)
        goblin.checkHit(man) # Checking if this goblin was hit by any of player's bullets
        if goblin.life < 1:
            enemies.pop(enemies.index(goblin))

    if len(enemies) < 5:
        for x in range(0, len(enemies) - 1):
            enemies.append(newEnemy(x))

    redrawGameWindow()

pygame.quit()
