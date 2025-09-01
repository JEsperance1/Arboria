import pygame
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
from ground import Ground
from debug import debug
from utils import resource_path

class Level:
    def __init__(self):
        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.player
        self.enemy

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == '':
                    #Ground((x, y), ([self.visible_sprites]))
                    pass
                elif column == 'x':
                    #Ground((x, y), (self.obstacle_sprites, self.visible_sprites))
                    Tile((x, y), (self.obstacle_sprites, self.visible_sprites))
                elif column == 'p':
                    #Ground((x, y), (self.obstacle_sprites, self.visible_sprites))
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                elif column == 'e':
                    #Ground((x, y), (self.obstacle_sprites, self.visible_sprites))
                    self.enemy = Enemy((x, y), [self.visible_sprites], self.obstacle_sprites)

                else:
                    #render more walkable ground
                    pass

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.halfwidth = self.display_surface.get_width() // 2
        self.halfheight = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load(resource_path("assets/tilemaps/snow-home.png")).convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.center):
            self.offset.x = player.rect.centerx - self.halfwidth
            self.offset.y = player.rect.centery - self.halfheight
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)
