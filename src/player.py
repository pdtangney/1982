import os

import pygame


class Player(pygame.sprite.Sprite):
    """Create a human player."""
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.settings = game.settings

        # Load the player images
        self.create_player()

        # Initialize movement settings
        self.moveX = 0
        self.moveY = 0

        # Initialize player stats
        self.health = 10
        self.score = 0

        self.mass = 1
        self.velocity = 10
        self.isJumping = True

    def create_player(self):
        """Create an animated player."""
        self.images = []
        self.imagesXReverse = []

        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) +
                                    '.png')).convert_alpha()
            img.set_colorkey(self.settings.colors('ALPHA'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        for i in self.images:
            img = pygame.transform.flip(i, True, False)
            img.set_colorkey(self.settings.colors('ALPHA'))
            self.imagesXReverse.append(img)
        self.animation = 4  # Animation cycles = number of animation images.
        self.frame = 0  # Count animation frames

    def control(self, x, y):
        """Control player movement."""
        self.moveX = x
        self.moveY += y

    def gravity(self):
        """Put gravity into effect if the player is jumping."""
        if self.isJumping:
            self.moveY += self.settings.gravity

    def jump(self):
        if self.isJumping:
            if self.velocity > 0:  # Fall down
                force = (0.5 * self.mass * (self.velocity * self.velocity))
            else:   # Jump up in air
                force = -(0.5 * self.mass * (self.velocity * self.velocity))
            self.velocity -= 1
            self.moveY = -force  # Jump height

    def update(self, ground_list, plat_list, loot_list):
        """Update the player's position on-screen."""
        self.rect.x += self.moveX
        self.rect.y += self.moveY

        # Animated moving left
        if self.moveX < 0:
            self.frame += 1
            if self.frame > 3 * self.animation:
                self.frame = 0
            self.image = self.imagesXReverse[self.frame // self.animation]

        # Animated moving right
        if self.moveX > 0:
            self.frame += 1
            if self.frame > 3 * self.animation:
                self.frame = 0
            self.image = self.images[self.frame // self.animation]

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.moveY = 0
            self.rect.bottom = g.rect.top
            self.velocity = 10
            self.isJumping = False

        # Falling into the abyss
        if self.rect.y > self.settings.screenY:
            self.health -= 1
            self.rect.x = 64  # Tile size
            self.rect.y = 64

        loot_hit_list = pygame.sprite.spritecollide(self, loot_list, False)
        for loot in loot_hit_list:
            loot_list.remove(loot)
            self.score += 1

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.isJumping = False
            self.moveY = 0
            self.velocity = 10

            # Don't let player get on the platform from below.
            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.moveY += self.settings.gravity
        else:
            # Fall off the platform
            self.moveY += self.settings.gravity
