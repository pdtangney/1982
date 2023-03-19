import pygame


class Settings:
    """Manage settings for block party."""
    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screenX = 960
        self.screenY = 540
        self.resolution = (self.screenX, self.screenY)
        self.fps = 40

        self.p1_is_running = False
        self.walking = 10
        self.running = 20

        # General game world settings
        self.gravity = 3.2
        self.forwardX = self.screenX - 100
        self.backwardX = 50

        # Keyboard and gamepad bindings.
        self._player_one_keybindings()

    def _player_one_keybindings(self):
        """Keybindings for player one."""
        self.p1_speed = self.walking
        self.p1_left = pygame.K_LEFT
        self.p1_right = pygame.K_RIGHT
        self.p1_jump = pygame.K_SPACE
        self.p1_run = pygame.K_LSHIFT

    def colors(self, color):
        if color == 'BLUE':
            return (25, 25, 200)
        elif color == 'BLACK':
            return (23, 23, 23)
        elif color == 'WHITE':
            return (254, 254, 254)
        elif color == 'ALPHA':
            return (0, 255, 0)
