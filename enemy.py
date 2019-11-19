
class enemy(object):

    def __init__(self, pygame, x, y, width, height, end, assets):
        self.pygame = pygame
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.assets = assets
        self.walkCount = 0
        self.path = self.x
        self.vel = 2
        self.life = 100
        self.strength = 10

    def draw(self, win, player):
        self.path = player.x
        self.move()
        assetCount = len(self.assets.left) + len(self.assets.right)

        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.assets.right[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.assets.left[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1


        fontLabel = self.pygame.font.Font("fonts/Abibas.ttf", 10)
        health = fontLabel.render("Health: ", True, (255, 0, 0))
        healthValue = fontLabel.render(str(self.life), True, (255, 0, 0))
        win.blit(health, [self.x + 20, self.y - 10])
        win.blit(healthValue, [self.x + 60, self.y - 10])


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
