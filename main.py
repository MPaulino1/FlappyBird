import pygame
from game import Game


class Main:
    def __init__(self):
        pygame.font.init()

        self.window = pygame.display.set_mode([360, 640])
        pygame.display.set_caption("Flappy Bird")

        self.loop = True
        self.fps = pygame.time.Clock()
        self.game = Game()

    def draw(self):
        self.game.updates()
        self.game.draw(self.window)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            self.fps.tick(30)
            pygame.display.update()


Main().update()
