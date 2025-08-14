import pygame
from pygame.examples.sprite_texture import sprite

from settings import *
from utils import resource_path

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)

        original_image = pygame.image.load(resource_path("assets/sprites/hero.png")).convert_alpha()
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacles = obstacle_sprites

    def input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
            else:
                self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical')


    def update(self):
        self.input()
        self.move(self.speed)

    def collision(self, direction):
        for sprite in self.obstacles:
            if direction == 'horizontal':
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        for sprite in self.obstacles:
            if direction == 'vertical':
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom


