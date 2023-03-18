""" Module to manange player instances."""
import pygame

class Player:
    """
    Class to manage a player instance.
    Takes an instance of MainGame in order to get the current screen
    resolution.
    """

    def  __init__(self, bit_life):
        """Create a human player instance."""
        self.screen = bit_life.screen
        self.screen_rect = bit_life.screen.get_rect()
        self._create_player()

        # Movment flags
        self.moving_right = False

    def _create_player(self):
        """Create a player instance. """
        self.image = pygame.image.load('images/hero1.png')
        self.rect = self.image.get_rect()

        # Set players starting location
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the player to the screen at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the player's position based on the movement flags."""
        if self.moving_right:
            self.rect.x += 1
