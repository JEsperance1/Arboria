import pygame, sys
from settings import *
from level import Level
from tile import Tile
from debug import debug


class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            pygame.display.set_caption('Arboria')
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
