"""Module representing the player."""
import os

import pygame


class Player(pygame.sprite.Sprite):
    """Create a human player."""

    def __init__(self, game_instance):
        pygame.sprite.Sprite.__init__(self)
        self.settings = game_instance.settings
        self.image = None
        self.current_frame = None

        # Load the player images
        self.create_player()

        # Initialize movement settings
        self.move_x = 0
        self.move_y = 0

        # Initialize player stats
        self.health = 10
        self.score = 0

        self.mass = 1
        self.velocity = 10
        self.is_jumping = False
        self.is_running = False
        self.speed = {
                      'walking': self.settings.walking,
                      'running': self.settings.running,
                      }

    def create_player(self):
        """Create an animated player."""
        self.images = []
        self.images_x_axis_reversed = []

        # 5 frames of animation
        for i in range(1, 5):
            self.image = pygame.image.load(os.path.join(
                self.settings.GAME_DIR, 'images', 'hero' + str(i) +
                '.png')).convert_alpha()
            self.image.set_colorkey(self.settings.colors('ALPHA'))
            self.images.append(self.image)
            self.rect = self.image.get_rect()
            # Create the reversed images, for walking to the left
            reverse_image = pygame.transform.flip(self.image, True, False)
            reverse_image.set_colorkey(self.settings.colors('ALPHA'))
            self.images_x_axis_reversed.append(reverse_image)
        # Animation cycles = number of animation images.
        self.total_frames = len(self.images)
        self.current_frame = 0

    def control(self, x, y):
        """
        Control player movement.

        Arguments: x, y are the axes.
        """
        self.move_x = x
        self.move_y += y

    def jump(self):
        """Code for jumping."""
        if self.is_jumping:
            self.move_y += self.settings.gravity
            if self.velocity > 0:  # Fall down
                force = 0.5 * self.mass * (self.velocity * self.velocity)
            else:   # Jump up in air
                force = -0.5 * self.mass * (self.velocity * self.velocity)
            self.velocity -= 1
            self.move_y = -force  # Jump height

    def update(self, ground_list, plat_list, loot_list):
        """Update the player's position and check for collisions."""
        self.rect.x += self.move_x
        self.rect.y += self.move_y

        self._animate_frames()
        self._collide_with_ground(ground_list)
        self._collide_with_lootbox(loot_list)
        self._collide_with_platform(plat_list)

    def _jump_reset(self):
        """Reset some values when no longer jumping."""
        self.is_jumping = False
        self.move_y = 0
        self.velocity = 10

    def _animate_frames(self):
        """Go through the animation cycle."""
        multiplier = 3
        self.current_frame += 1
        if self.current_frame > multiplier * self.total_frames:
            self.current_frame = 0
        # Animated moving left
        if self.move_x < 0:
            self.image = self.images_x_axis_reversed[
                    self.current_frame // self.total_frames]
        elif self.move_x > 0:
            # Animated moving right
            self.image = self.images[self.current_frame // self.total_frames]

    def _collide_with_ground(self, ground_list):
        """Has player hit the ground?"""
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for ground in ground_hit_list:
            self._jump_reset()
            self.rect.bottom = ground.rect.top

    def _collide_with_platform(self, plat_list):
        """Has the player come in contact with a platform?"""
        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for platform in plat_hit_list:
            self._jump_reset()

            # Don't let player get on the platform from below.
            if self.rect.bottom < platform.rect.bottom:
                self.rect.bottom = platform.rect.top
        # Fall off the platform
        self.move_y += self.settings.gravity

    def _collide_with_lootbox(self, loot_list):
        """Has the player hit a loot box?"""
        loot_hit_list = pygame.sprite.spritecollide(self, loot_list, False)
        for loot in loot_hit_list:
            loot_list.remove(loot)
            self.score += 1
