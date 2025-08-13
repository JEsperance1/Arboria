import pygame
from settings import *
from src.utils import resource_path


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        original_image = pygame.image.load(resource_path("assets/sprites/tile_161.png")).convert_alpha()
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
