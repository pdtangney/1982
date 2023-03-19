import os

import pygame
from settings import Settings


class Enemy(pygame.sprite.Sprite):
    """Generate an enemy."""
    def __init__(self, game, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.settings = game.settings
        self.create_enemy(x, y, img)
        self.counter = 0

    def create_enemy(self, x, y, img):
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(self.settings.colors('ALPHA'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        distance = 40
        speed = 5

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter > distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1
