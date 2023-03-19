"""
1982: 8:bit Life is a  1980's style platformer game.
Main module for 1982: 8-bit Life. Call this file with python3 to run
the game.
"""
import sys

import pygame

from settings import Settings
from player import Player

class MainGame:
    """Overall class to manage 1982: 8-bit life assets and behaviour."""

    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()
        self.settings = Settings()
        self._initialize_display()
        self.player_one = Player(self)

    def _initialize_display(self):
        """Set up the game display to its initial settings."""
        self.screen = pygame.display.set_mode(self.settings.screen_rez)
        pygame.display.set_caption("1982: 8-bit Life")

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_input_events()
            self.player_one.update()
            self._update_screen()

    def _check_input_events(self):
        """Respond to keyboard, mouse and game controller events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check and respond to keyboard keypresses."""
        if (event.key == self.settings.quit_game_key or
            event.key == pygame.K_ESCAPE):
            self.quit()
        elif event.key == pygame.K_RIGHT:
            self.player_one.moving_right = True

    def _check_keyup_events(self, event):
        """Check and respond to keyboard key releases."""
        if event.key == pygame.K_RIGHT:
            self.player_one.moving_right = False

    def _update_screen(self):
        """Update objects on screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player_one.blitme()
        pygame.display.flip()

    def quit(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    bit_life = MainGame()
    bit_life.run_game()
