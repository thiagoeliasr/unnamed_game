from projectile import projectile

class player(object):

    def __init__(self, pygame, x, y, width, height, assets):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.walkCount = 0
        self.assets = assets
        self.standing = True
        self.bullets = []
        self.pygame = pygame
        self.life = 100
        self.shootCount = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        self.shootCount += 1
        if self.shootCount > 5:
            self.shootCount = 0

        if not(self.standing):
            if self.left:
                win.blit(self.assets.left[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.assets.right[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.assets.right[0], (self.x, self.y))
            else:
                win.blit(self.assets.left[0], (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw(win, self.pygame)

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def checkHit(self, x, y, strength):
        if x > (self.x - 10) and x < (self.x + 10) and self.life > 0:
            if y < self.y + 15:
                self.life -= strength
                if self.life < 0:
                    self.life = 0

    def move(self, screen_width, screen_height):
        keys = self.pygame.key.get_pressed()

        for bullet in self.bullets:
            if bullet.x < screen_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                self.bullets.pop(self.bullets.index(bullet))

        facing = 1
        if self.left:
            facing = -1

        if keys[self.pygame.K_SPACE]:
            if len(self.bullets) < 5:
                if self.shootCount == 0:
                    self.bullets.append(
                        projectile(
                            round(self.x + self.width // 2),
                            round(self.y + self.height // 2),
                            3,
                            (0, 0, 0),
                            facing
                        )
                    )

        if keys[self.pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
        elif keys[self.pygame.K_RIGHT] and self.x < screen_width - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0

        if not(self.isJump):
            if keys[self.pygame.K_UP]:
                self.isJump = True
                self.left = False
                self.right = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -8:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1

                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 8


