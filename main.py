import pygame
from player import player
from assets import assets

pygame.init()

screen_width = 500
screen_height = 500
fps = 60

clock = pygame.time.Clock()
mainAssets = assets(pygame).mainAssets()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Glorious Unnamed Game")

man = player(200, 410, 64, 64, assets(pygame).getMan())

def redrawGameWindow():
    global walkCount
    win.blit(mainAssets.bg, (0, 0))
    man.draw(win)
    pygame.display.update()

#mainLoop
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False

    man.move(pygame, screen_width, screen_height)

    redrawGameWindow()

pygame.quit()
