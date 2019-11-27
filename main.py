import pygame
import random
from player import player
from enemy import enemy
from assets import assets

class main():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('The Glorious Unnamed Game')

        self.screen_width = 900
        self.screen_height = 500
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.level = pygame.Surface((self.screen_width, self.screen_height))
        self.mainAssets = assets(pygame).mainAssets((self.screen_width, self.screen_height))
        self.level.blit(self.mainAssets.bgCloudBack, (0, 0))
        self.level.blit(self.mainAssets.bgCloudFront, (0, 0))
        self.level.blit(self.mainAssets.bgBack, (0, 0))
        self.level.blit(self.mainAssets.bgFront, (0, 0))
        self.ground = assets(pygame).getGroundBlock()
        self.dificultyMultiplier = 0.4

        for x in range(0, self.screen_width, 48):
            self.level.blit(self.ground.img, (x, self.screen_height - self.ground.h))

        self.font = pygame.font.Font("fonts/Abibas.ttf", 35)
        self.fontSmall = pygame.font.Font("fonts/Abibas.ttf", 25)

        self.textHealth = self.font.render("Health: ", True, (255, 255, 255))
        self.textScore = self.fontSmall.render("Score: ", True, (255, 0, 0))
        self.textDied = self.font.render("You Died", True, (255, 0, 0))
        self.textNewGame = self.fontSmall.render("Press ENTER to start a new game", True, (255, 255, 0))

        self.man = player(pygame, (self.screen_width - (self.screen_width / 2) - 65), self.screen_height - 106, 64, 64, assets(pygame).getMan())
        self.enemies = []

    def newEnemy(self, x):
        xInit = (random.randint(1, 20)) * 5 * -1
        if x % 2 == 0:
            xInit = self.screen_width + (x + 1) * 5

        e = enemy(pygame, xInit, self.screen_height - 102, 64, 64, 450, assets(pygame).getEnemy())
        e.vel = random.randint(1, 4) * self.dificultyMultiplier
        return e

    def initEnemies(self):
        self.enemies = []
        for x in range(5):
            self.enemies.append(self.newEnemy(x))

    def resetGame(self):
        self.man.life = 100;
        self.man.x = (self.screen_width - (self.screen_width / 2)) - 64
        self.man.score = 0
        self.dificultyMultiplier = 0.4
        self.initEnemies()

    def redraw(self):
        if self.man.life < 1:
            self.win.fill((0, 0, 0))
            self.win.blit(self.textDied, [self.screen_width // 2 - self.textDied.get_width() // 2, self.screen_height // 2 - self.textDied.get_height() //2])
            self.win.blit(self.textNewGame, [self.screen_width // 2 - self.textNewGame.get_width() // 2, self.screen_height // 2 - self.textNewGame.get_height() // 2 + 80])

            txtFinalScore = self.font.render("Final Score: {}".format(self.man.score), True, (255, 0, 0))
            self.win.blit(txtFinalScore, [self.screen_width // 2 - txtFinalScore.get_width() // 2, self.screen_height // 2 - txtFinalScore.get_height() // 2 + 120])

            keys = pygame.key.get_pressed()
            if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                self.resetGame()

        else:
            # Drawing bg images
            self.win.blit(self.level, self.win.get_rect())

            self.man.draw(self.win)

            for goblin in self.enemies:
                goblin.draw(self.win, self.man)

            textHealthValue = self.font.render(str(self.man.life), True, (255, 255, 255))
            self.win.blit(self.textHealth, [10, 10])
            self.win.blit(textHealthValue, [self.textHealth.get_width() + 10, 10])

            textScoreValue = self.fontSmall.render(str(self.man.score), True, (255, 0, 0))
            self.win.blit(self.textScore, [10, 50])
            self.win.blit(textScoreValue, [self.textScore.get_width() + 10, 50])

        pygame.display.update()

    def run(self):
        run = True
        self.initEnemies()
        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

            self.man.move(self.screen_width, self.screen_height)

            for goblin in self.enemies:
                self.man.checkHit(goblin.x, goblin.y, goblin.strength)
                goblin.checkHit(self.man) # Checking if this goblin was hit by any of player's bullets
                if goblin.life < 1:
                    self.enemies.pop(self.enemies.index(goblin))

            if len(self.enemies) < 5:
                for x in range(0, len(self.enemies) - 1):
                    self.enemies.append(self.newEnemy(x))

            if self.man.score % 10 == 0:
                self.man.score += 1 # Alternate solution for this 😂
                self.dificultyMultiplier += 0.1

            self.redraw()

        pygame.quit()


main().run()
