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
        self.initialize_display()
        self.level = Level(self)
        self.add_player_one()
        self.generate_level_one()

    def initialize_display(self):
        """Set up the game display."""
        self.screen = pygame.display.set_mode((self.settings.resolution))
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load(os.path.join(
                                        'images', 'wide-stage.png')).convert()
        self.background_rect = self.background.get_rect()
        pygame.display.set_caption("Block Party")
        self.clock = pygame.time.Clock()

    def generate_level_one(self):
        """Create the first level."""
        res = self.settings.resolution
        # Generate the ground using the tile method.
        ground_location = []

        # Tile dimentions
        tw = 64
        th = 64
        tiles = self.settings.screenX // tw
        for i in range(tiles):
            ground_location.append(i * tw)

        self.ground_list = self.level.generate_ground(1, ground_location,
                                                      tw, th)

        self.platform_list = self.level.platform(1, tw, th)

        self.loot_list = self.level.loot(1)

        # Create an enemy at x, y
        self.e_loc = [1030, res[1]-368]
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
            self.p1.gravity()
            self._check_enemy_collisions()
            self._scroll_world()
            self._update_screen()

    def _check_input_events(self):
        """Check for keyboard, mouse and gamepad events."""
        if self.settings.p1_is_running:
            self.settings.p1_speed = self.settings.running
        else:
            self.settings.p1_speed = self.settings.walking

        keys = pygame.key.get_pressed()
        if keys[self.settings.p1_left]:
            if keys[self.settings.p1_run]:
                self.settings.p1_is_running = True
                self.p1.control(-self.settings.p1_speed, 0)
            else:
                self.settings.p1_is_running = False
                self.p1.control(-self.settings.p1_speed, 0)

        elif keys[self.settings.p1_right]:
            if keys[self.settings.p1_run]:
                self.settings.p1_is_running = True
                self.p1.control(self.settings.p1_speed, 0)
            else:
                self.settings.p1_is_running = False
                self.p1.control(self.settings.p1_speed, 0)
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
                    self.p1.isJumping = True

    def quit(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()

    def _check_enemy_collisions(self):
        hit_list = pygame.sprite.spritecollide(self.p1, self.enemy_list, False)
        for enemy in hit_list:
            self.p1.health -= 1
            print(f'Health: {self.p1.health}')

    def _scroll_world(self):
        # Scroll forward
        if (self.p1.rect.x < self.background_rect.right -
           (self.p1.rect.width * 2)):
            if self.p1.rect.x >= self.settings.forwardX:
                scroll = self.p1.rect.x - self.settings.forwardX
                self.background_rect.x -= scroll
                self.p1.rect.x = self.settings.forwardX
                for p in self.platform_list:
                    p.rect.x -= scroll
                for e in self.enemy_list:
                    e.rect.x -= scroll
                for l in self.loot_list:
                    l.rect.x -= scroll
        else:
            self.p1.rect.left = self.settings.forwardX

        # Scroll backward
        if self.p1.rect.left > self.background_rect.left:
            if self.p1.rect.x <= self.settings.backwardX:
                scroll = self.settings.backwardX - self.p1.rect.x
                self.background_rect.x += scroll
                self.p1.rect.x = self.settings.backwardX
                for p in self.platform_list:
                    p.rect.x += scroll
                for e in self.enemy_list:
                    e.rect.x += scroll
                for l in self.loot_list:
                    l.rect.x += scroll
        else:
            self.p1.rect.x = self.settings.backwardX

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
        self.clock.tick(self.settings.fps)


if __name__ == '__main__':

    playing = Game()
    playing.run_game()
