import pygame
import random
import time
import threading
# from pygame.examples.sprite_texture import sprite

from settings import *
from utils import resource_path

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)

        original_image = pygame.image.load(resource_path("assets/sprites/SimpleEnemies Bat_Idle_0.png")).convert_alpha()
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.hitbox = self.rect.inflate(0, -26)
        self.loop_phase = 0
        self.last_animation_time = 0
        self.last_movement_time = 0

        self.obstacles = obstacle_sprites

    def animation_loop(self):

        image_path = f"assets/sprites/SimpleEnemies Bat_Idle_{self.loop_phase}.png"

        # Load → convert → scale
        image_surface = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(image_surface, (64, 64))

        self.loop_phase = (self.loop_phase + 1) % 4




    def random_movement_input(self):
            enemy_direction = random.randint(0,3)
            if enemy_direction == 0:
                self.direction.y = -1
            elif enemy_direction == 1:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if enemy_direction == 2:
                self.direction.x = -1
            elif enemy_direction == 3:
                self.direction.x = 1
            else:
                self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
    
            self.hitbox.x += self.direction.x * speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * speed
            self.collision('vertical')
            self.rect.center = self.hitbox.center


    def update(self):
        now = time.time()
        if now - self.last_animation_time >= .1:
            self.animation_loop()
            self.last_animation_time = now  # reset timer
        if now - self.last_movement_time >= .5:
            self.random_movement_input()
            self.last_movement_time = now  # reset timer
        self.move(self.speed)

    def collision(self, direction):
        for sprite in self.obstacles:
            if direction == 'horizontal':
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        for sprite in self.obstacles:
            if direction == 'vertical':
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom


