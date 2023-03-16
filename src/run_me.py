"""
Main module for 1982: 8-bit life. Call this file with python3 to run
the game.
"""
import sys

import pygame

from settings import Settings
class MainGame:
    """Overall class to manage 1982: 8-bit life assets and behaviour."""

    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_rez)
        pygame.display.set_caption("1982: 8-bit Life")

    def run_game(self):
        """Start the main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    bit_life = MainGame()
    bit_life.run_game()
