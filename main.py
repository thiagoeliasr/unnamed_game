import pygame
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
textHealth = font.render("Health: ", True, (255, 255, 255))

man = player(pygame, 200, 410, 64, 64, assets(pygame).getMan())
goblin = enemy(pygame, 100, 410, 64, 64, 450, assets(pygame).getEnemy())

def redrawGameWindow():
    win.blit(mainAssets.bg, (0, 0))
    # win.fill((0, 0, 0))
    man.draw(win)
    goblin.draw(win, man)

    textHealthValue = font.render(str(man.life), True, (255, 255, 255))
    win.blit(textHealth, [10, 10])
    win.blit(textHealthValue, [textHealth.get_width() + 10, 10])

    pygame.display.update()


#mainLoop
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False

    man.move(screen_width, screen_height)
    redrawGameWindow()

pygame.quit()
