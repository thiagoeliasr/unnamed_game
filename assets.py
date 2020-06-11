class Object(object):
    pass

class assets():

    def __init__(self, pygame):
        self.imgPath = 'images/'
        self.chImages = self.imgPath + 'character/'
        self.pygame = pygame

    def mainAssets(self, dimensions):
        obj = Object()
        obj.bgBack = self.pygame.image.load(self.imgPath + 'background/BGBack.png').convert_alpha()
        obj.bgBack = self.pygame.transform.scale(obj.bgBack, dimensions)
        obj.bgFront = self.pygame.image.load(self.imgPath + 'background/BGFront.png').convert_alpha()
        obj.bgFront = self.pygame.transform.scale(obj.bgFront, dimensions)
        obj.bgCloudBack = self.pygame.image.load(self.imgPath + 'background/CloudsBack.png').convert_alpha()
        obj.bgCloudBack = self.pygame.transform.scale(obj.bgCloudBack, dimensions)
        obj.bgCloudFront = self.pygame.image.load(self.imgPath + 'background/CloudsFront.png').convert_alpha()
        obj.bgCloudFront = self.pygame.transform.scale(obj.bgCloudFront, dimensions)

        return obj

    def getMan(self):
        obj = Object()
        obj.right = []
        obj.left = []

        for idx in range(9):
            obj.right.append(self.pygame.image.load("{}R{}.png".format(self.chImages, idx + 1)))
            obj.left.append(self.pygame.image.load("{}L{}.png".format(self.chImages, idx + 1)))

        obj.char = self.pygame.image.load(self.chImages + 'standing.png')

        return obj

    def getEnemy(self):
        obj = Object()
        obj.right = []
        obj.left = []

        for idx in range(11):
            obj.right.append(self.pygame.image.load("{}R{}E.png".format(self.chImages, idx + 1)))
            obj.left.append(self.pygame.image.load("{}L{}E.png".format(self.chImages, idx + 1)))

        obj.char = self.pygame.image.load(self.chImages + 'standing.png')

        return obj

    def getApple(self):
        obj = Object()
        obj.w = 16
        obj.y = 16
        obj.img = self.pygame.image.load(self.imgPath + 'items/apple.png')
        return obj

    def getGroundBlock(self):
        obj = Object()
        obj.w = 48
        obj.h = 48
        obj.img = self.pygame.image.load(self.imgPath + 'background/ground.png')
        return obj

