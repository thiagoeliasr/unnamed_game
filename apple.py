
class apple(object):

    def __init__(self, pygame, x, y, width, height, assets):
        self.pygame = pygame
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.assets = assets
        self.walkCount = 0
        self.path = self.x
        self.strength = 30
        self.hitbox = (self.x - (width/2), self.y - (height/2), self.width, self.height)
        self.visible = False

    def draw(self, win, player):
        if self.visible:
            image = self.pygame.transform.scale(self.assets.img, (self.width, self.height))
            win.blit(image, (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 2, 16, 16)
            self.hitbox = (self.x, self.y, self.width, self.height)
            # self.pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def checkEaten(self, player):
        if player.y - player.height < self.hitbox[1] + self.hitbox[3] and player.y + player.height > self.hitbox[1]:
            if player.x + player.width > self.hitbox[0] and player.x - player.width < self.hitbox[0] + self.hitbox[2]:
                self.eaten(player)

    def eaten(self, player):
        if player.life < 100 and self.visible:
            player.life = 100 if player.life + self.strength > 100 else player.life + self.strength

        self.visible = False



