"""
The main setting module for 1982: 8-Bit Life.
Includes screen resolution, player keybindings,
player speed settings.

Contains class Settings. This class manages game settings. Most settings
are user configurable. Where they are not meant to be user configured,
it will be noted with a comment on the line preceding the setting.
"""

import os

import pygame


class Settings:
    """
    Manage settings for 1982: 8-bit Life.

    Methods in Settings:
        initialize_screen() - Set resolution, framerate.
        player_one_keybindings() - User configurable keyboard controls.
    """

    GAME_DIR = os.path.dirname(__file__)

    def __init__(self):
        """Initialize game settings.

           Calls the following public methods:
                initialize_screen()
                player_one_keybindings()
        """

        self.screen_resolution = (960, 540)
        self.fps = 40

        # Screen scrolling settings. The following lines ensure the
        # player stays in view when approaching the edge of the screen.
        self.forward_x = self.screen_resolution[0] - 100
        self.backward_x = 50

        # Misc player settings. Its is recommended that self.running
        # is to be set at least twice the speed of self.walking.
        self.walking = 10
        self.running = 20

        # General game world settings
        self.gravity = 3.2

        # Keyboard and gamepad bindings.
        self.player_one_keybindings()

    def player_one_keybindings(self):
        """Keybindings for player one, when using a keyboard."""
        self.p1_left = pygame.K_LEFT
        self.p1_right = pygame.K_RIGHT
        self.p1_jump = pygame.K_SPACE
        self.p1_run = pygame.K_LSHIFT

    def colors(self, color):
        """Calling this method returns a RGB tuple."""
        if color == 'BLUE':
            return (25, 25, 200)
        if color == 'BLACK':
            return (23, 23, 23)
        if color == 'WHITE':
            return (254, 254, 254)
        if color == 'ALPHA':
            return (0, 255, 0)
        return None
