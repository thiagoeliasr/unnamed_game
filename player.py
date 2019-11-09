
class player(object):

    def __init__(self, x, y, width, height, assets):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.assets = assets

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.assets.left[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.assets.right[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.assets.char, (self.x, self.y))

    def move(self, pygame, screen_width, screen_height):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT] and self.x < screen_width - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not(self.isJump):
            """
            if keys[pygame.K_UP] and self.y > self.vel:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y < screen_height - self.height - self.vel:
                self.y += self.vel
            """

            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.left = False
                self.right = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1

                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


