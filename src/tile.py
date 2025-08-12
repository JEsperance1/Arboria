import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        original_image = pygame.image.load("/Users/jordanesperance/PycharmProjects/ArboriaAttempt1/.venv/Sprites/LPCsnowTrees.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
