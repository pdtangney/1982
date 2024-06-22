"""The main game module"""

import os
import sys

import pygame

from settings import Settings
from player import Player
from level import Level


class Game:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game and create some assets."""
        pygame.init()
        self.settings = Settings()
        self._initialize_display()
        self.level = Level(self)
        self.add_player_one()
        self.generate_level_one()

    def _initialize_display(self):
        """Set up the game display."""
        self.screen = pygame.display.set_mode(
                (self.settings.screen_resolution))
        self.background = pygame.image.load(os.path.join(
            self.settings.GAME_DIR, 'images', 'wide-stage.png')).convert()
        self.background_rect = self.background.get_rect()
        pygame.display.set_caption("Block Party")

    def generate_level_one(self):
        """Create the first level."""
        # Generate the ground using the tile method.
        tile_width = 64
        tile_height = 64
        ground_tile_count = self.settings.screen_resolution[0] // tile_width
        ground_location = []
        for i in range(ground_tile_count):
            ground_location.append(i * tile_width)

        self.ground_list = self.level.generate_ground(1, ground_location,
                                                      tile_width, tile_height)

        self.platform_list = self.level.platform(1, tile_width, tile_height)

        self.loot_list = self.level.loot(1)

        # Create an enemy at x, y
        self.e_loc = [1030, self.settings.screen_resolution[1]-368]
        self.enemy_list = self.level.enemies(1, self.e_loc, 'enemy4.png')

    def add_player_one(self):
        """Create the first player."""
        self.player_list = pygame.sprite.Group()
        self.p1 = Player(self)
        self.p1.rect.x = 0
        self.p1.rect.y = 0
        self.player_list.add(self.p1)

    def run_game(self):
        """The main game loop."""
        while True:
            self._check_input_events()
            self.p1.jump()
            self._check_enemy_collisions()
            self._scroll_world()
            self._update_screen()

    def _check_input_events(self):
        """Check for keyboard, mouse and gamepad events."""
        keys = pygame.key.get_pressed()
        if keys[self.settings.p1_left]:
            if keys[self.settings.p1_run]:
                self.p1.is_running = True
                self.p1.control(-self.p1.speed['running'], 0)
            else:
                self.p1.is_running = False
                self.p1.control(-self.p1.speed['walking'], 0)

        elif keys[self.settings.p1_right]:
            if keys[self.settings.p1_run]:
                self.p1.is_running = True
                self.p1.control(self.p1.speed['running'], 0)
            else:
                self.p1.is_running = False
                self.p1.control(self.p1.speed['walking'], 0)
        else:
            # Stop player from moving when no keys pressed.
            self.p1.control(0, self.settings.gravity)
            # So player can fall off a platform properly.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                    self.quit()
                elif event.key == self.settings.p1_jump:
                    self.p1.is_jumping = True

    def quit(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()

    def _check_enemy_collisions(self):
        hit_list = pygame.sprite.spritecollide(self.p1, self.enemy_list, False)
        if hit_list:
            self.p1.health -= 1
            print(f'Health: {self.p1.health}')

    def _scroll_world(self):
        # Scroll forward
        if (self.p1.rect.x < self.background_rect.right -
           (self.p1.rect.width * 2)):
            if self.p1.rect.x >= self.settings.forward_x:
                scroll = self.p1.rect.x - self.settings.forward_x
                self.background_rect.x -= scroll
                self.p1.rect.x = self.settings.forward_x
                for p in self.platform_list:
                    p.rect.x -= scroll
                for e in self.enemy_list:
                    e.rect.x -= scroll
                for loot in self.loot_list:
                    loot.rect.x -= scroll
        else:
            self.p1.rect.left = self.settings.forward_x

        # Scroll backward
        if self.p1.rect.left > self.background_rect.left:
            if self.p1.rect.x <= self.settings.backward_x:
                scroll = self.settings.backward_x - self.p1.rect.x
                self.background_rect.x += scroll
                self.p1.rect.x = self.settings.backward_x
                for p in self.platform_list:
                    p.rect.x += scroll
                for e in self.enemy_list:
                    e.rect.x += scroll
                for loot in self.loot_list:
                    loot.rect.x += scroll
        else:
            self.p1.rect.x = self.settings.backward_x

    def _update_screen(self):
        """Update the display."""
        self.screen.blit(self.background, self.background_rect)

        self.ground_list.draw(self.screen)
        self.platform_list.draw(self.screen)
        self.loot_list.draw(self.screen)

        self.enemy_list.draw(self.screen)
        for e in self.enemy_list:
            e.move()

        self.p1.update(self.ground_list, self.platform_list, self.loot_list)
        self.player_list.draw(self.screen)

        pygame.display.flip()
        pygame.time.Clock().tick(self.settings.fps)


if __name__ == '__main__':

    playing = Game()
    playing.run_game()
