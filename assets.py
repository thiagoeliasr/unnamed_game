class Object(object):
    pass

class assets():

    def __init__(self, pygame):
        self.imgPath = 'images/'
        self.chImages = self.imgPath + 'character/'
        self.pygame = pygame

    def mainAssets(self):
        obj = Object()
        obj.bg = self.pygame.image.load(self.imgPath + 'bg.png')

        return obj

    def getMan(self):
        obj = Object()

        obj.right = [
            self.pygame.image.load(self.chImages + 'R1.png'),
            self.pygame.image.load(self.chImages + 'R2.png'),
            self.pygame.image.load(self.chImages + 'R3.png'),
            self.pygame.image.load(self.chImages + 'R4.png'),
            self.pygame.image.load(self.chImages + 'R5.png'),
            self.pygame.image.load(self.chImages + 'R6.png'),
            self.pygame.image.load(self.chImages + 'R7.png'),
            self.pygame.image.load(self.chImages + 'R8.png'),
            self.pygame.image.load(self.chImages + 'R9.png')
        ]

        obj.left = [
            self.pygame.image.load(self.chImages + 'L1.png'),
            self.pygame.image.load(self.chImages + 'L2.png'),
            self.pygame.image.load(self.chImages + 'L3.png'),
            self.pygame.image.load(self.chImages + 'L4.png'),
            self.pygame.image.load(self.chImages + 'L5.png'),
            self.pygame.image.load(self.chImages + 'L6.png'),
            self.pygame.image.load(self.chImages + 'L7.png'),
            self.pygame.image.load(self.chImages + 'L8.png'),
            self.pygame.image.load(self.chImages + 'L9.png')
        ]

        obj.char = self.pygame.image.load(self.chImages + 'standing.png')

        return obj

    def getEnemy(self):
        obj = Object()

        obj.right = [
            self.pygame.image.load(self.chImages + 'R1E.png'),
            self.pygame.image.load(self.chImages + 'R2E.png'),
            self.pygame.image.load(self.chImages + 'R3E.png'),
            self.pygame.image.load(self.chImages + 'R4E.png'),
            self.pygame.image.load(self.chImages + 'R5E.png'),
            self.pygame.image.load(self.chImages + 'R6E.png'),
            self.pygame.image.load(self.chImages + 'R7E.png'),
            self.pygame.image.load(self.chImages + 'R8E.png'),
            self.pygame.image.load(self.chImages + 'R9E.png'),
            self.pygame.image.load(self.chImages + 'R10E.png'),
            self.pygame.image.load(self.chImages + 'R11E.png')
        ]

        obj.left = [
            self.pygame.image.load(self.chImages + 'L1E.png'),
            self.pygame.image.load(self.chImages + 'L2E.png'),
            self.pygame.image.load(self.chImages + 'L3E.png'),
            self.pygame.image.load(self.chImages + 'L4E.png'),
            self.pygame.image.load(self.chImages + 'L5E.png'),
            self.pygame.image.load(self.chImages + 'L6E.png'),
            self.pygame.image.load(self.chImages + 'L7E.png'),
            self.pygame.image.load(self.chImages + 'L8E.png'),
            self.pygame.image.load(self.chImages + 'L9E.png'),
            self.pygame.image.load(self.chImages + 'L10E.png'),
            self.pygame.image.load(self.chImages + 'L11E.png')
        ]

        obj.char = self.pygame.image.load(self.chImages + 'standing.png')

        return obj

