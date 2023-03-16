""" Module to manange player instances."""
import pygame

class Player:
    """Class to manage a player instance."""

    def  __init__(self, bit_life):
        """Create a human player instance."""
        self.screen = bit_life.screen
        self.screen_rect = bit_life.screen.get_rect()

        self.image = pygame.image.load('images/hero1.png')
        self.rect = self.image.get_rect()

        # Set players starting location
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the player to the screen at its current location."""
        self.screen.blit(self.image, self.rect)
