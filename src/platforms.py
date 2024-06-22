import os

import pygame
from settings import Settings


class Platform(pygame.sprite.Sprite):
    def __init__(self, xLocation, yLocation, image):
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()
        self.image = pygame.image.load(os.path.join(self.settings.GAME_DIR,
                                                    'images', image)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(self.settings.colors('ALPHA'))
        self.rect = self.image.get_rect()
        self.rect.x = xLocation
        self.rect.y = yLocation
