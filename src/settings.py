"""
The settings module. Manages all of the settings for 1982: 8-bit Life.
This includes user-configurable such as !!!!!
and non-user configurable settings, such as  !!!!
"""

import pygame
class Settings:
    """Manaages most of the game settings here."""

    def __init__(self):
        """Initialize game settings."""

        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.screen_rez = (self.screen_w, self.screen_h)
        self.bg_color = (200, 230, 250)

        # Misc keybindings, OTHER THAN player keys
        self.quit_game_key = pygame.K_q
