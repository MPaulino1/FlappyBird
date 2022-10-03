import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Pipe(Obj):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

    def update(self, *args):
        self.rect[0] -= 4

        if self.rect[0] <= - 100:
            self.kill()


class Coin(Obj):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= 4

        if self.rect[0] <= - 100:
            self.kill()

    def anim(self):
        self.ticks = (self.ticks + 1) % 6

        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")


class Bird(Obj):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)
        self.ticks = 0
        self.grav = 1
        self.vel = 4

        self.pts = 0
        self.play = True

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.vel += self.grav
        self.rect[1] += self.vel

        if self.vel >= 10:
            self.vel = 10

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.vel -= 5

        if self.rect[1] <= 0:
            self.rect[1] = 0
            self.vel = 4

        if self.rect[1] >= 420:
            self.rect[1] = 420

    def anim(self):
        self.ticks = (self.ticks + 1) % 4

        self.image = pygame.image.load("assets/bird" + str(self.ticks) + ".png")

    def collision_pipes(self, group):
        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.play = False

    def collision_coins(self, group):
        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            self.pts += 1


class Text:
    def __init__(self, size, text):
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))