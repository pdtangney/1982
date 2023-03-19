"""
The main setting module for 1982: 8-Bit Life.
Includes screen resolution, player keybindings,
player speed settings.

Contains class Settings. This class manages game settings. Most settings
are user configurable. Where they are not meant to be user configured,
it will be noted with a comment on the line preceding the setting.
"""

import pygame


class Settings:
    """
    Manage settings for 1982: 8-bit Life.

    Methods in Settings:
        initialize_screen() - Set resolution, framerate.
        player_one_keybindings() - User configurable keyboard controls.
    """
    def __init__(self):
        """Initialize game settings.

           Calls the following public methods:
                initialize_screen()
                player_one_keybindings()
        """
        self.initialize_screen()

        # Misc player settings. Its is recommended that self.running
        # is to be set at least twice the speed of self.walking.
        self.walking = 10
        self.running = 20
        # By default p1 is not running:
        self.p1_is_running = False
        self.p1_speed = self.walking

        # General game world settings
        self.gravity = 3.2
        # Screen scrolling settings. The following lines ensure the
        # player stays in view when approaching the edge of the screen.
        self.forward_x = self.screen_x - 100
        self.backward_x = 50

        # Keyboard and gamepad bindings.
        self.player_one_keybindings()

    def initialize_screen(self):
        """
        Set up the initial screen settings.
        self.screen_x, self,screen_y are the width, height of
        the screen.
        self.fps sets the frame-rate.

        """
        self.screen_x = 960
        self.screen_y = 540
        self.resolution = (self.screen_x, self.screen_y)
        self.fps = 40

    def player_one_keybindings(self):
        """Keybindings for player one, when using a keyboard."""
        self.p1_left = pygame.K_LEFT
        self.p1_right = pygame.K_RIGHT
        self.p1_jump = pygame.K_SPACE
        self.p1_run = pygame.K_LSHIFT
