import pygame
from settings import *
from tile import Tile
from player import Player
from ground import Ground
from debug import debug
from utils import resource_path

class Level:
    def __init__(self):
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.create_map()
        self.player

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'x':
                    Ground((x, y), (self.obstacle_sprites, self.visible_sprites))
                    Tile((x, y), (self.obstacle_sprites, self.visible_sprites))
                elif column == '':
                    #Ground((x, y), ([self.obstacle_sprites], [self.visible_sprites]))
                    pass
                elif column == 'p':
                    self. player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

                else:
                    #render more walkable ground
                    pass

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        debug(self.player.direction)
