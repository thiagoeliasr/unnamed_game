
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
        self.path = [self.x, self.end]
        self.vel = 3

    def draw(self, win):
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

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
