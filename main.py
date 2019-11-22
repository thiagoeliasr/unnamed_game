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
mainAssets = assets(pygame).mainAssets()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Glorious Unnamed Game")

font = pygame.font.Font("fonts/Abibas.ttf", 35)
fontSmall = pygame.font.Font("fonts/Abibas.ttf", 25)

textHealth = font.render("Health: ", True, (255, 255, 255))
textDied = font.render("You Died", True, (255, 0, 0))
textNewGame = fontSmall.render("Press ENTER to start a new game", True, (255, 255, 0))

man = player(pygame, 200, 410, 64, 64, assets(pygame).getMan())

def initEnemies():
    global enemies
    enemies = []
    for x in range(5):
        xInit = (random.randint(1, 20)) * 5 * -1
        if x % 2 == 0:
            xInit = screen_width + (x + 1) * 5

        goblin = enemy(pygame, xInit, 410, 64, 64, 450, assets(pygame).getEnemy())
        goblin.vel = random.randint(1, 4)
        enemies.append(goblin)

def resetGame():
    man.life = 100
    man.x = 200
    initEnemies()

def redrawGameWindow():
    global enemies

    if man.life < 1:
        win.fill((0, 0, 0))
        win.blit(textDied, [screen_width // 2 - textDied.get_width() // 2, screen_height // 2 - textDied.get_height() //2])
        win.blit(textNewGame, [screen_width // 2 - textNewGame.get_width() // 2, screen_height // 2 - textNewGame.get_height() // 2 + 80])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
            resetGame()

    else:
        win.blit(mainAssets.bg, (0, 0))
        man.draw(win)
        for goblin in enemies:
            goblin.draw(win, man)

        textHealthValue = font.render(str(man.life), True, (255, 255, 255))
        win.blit(textHealth, [10, 10])
        win.blit(textHealthValue, [textHealth.get_width() + 10, 10])

    pygame.display.update()


#mainLoop
run = True
initEnemies()
while run:
    global enemies
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

    redrawGameWindow()

pygame.quit()
