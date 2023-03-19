import pygame

from enemy import Enemy
from platforms import Platform


class Level:
    """Manage level generation."""
    def __init__(self, game):
        """Retrieve game settings."""
        self.settings = game.settings
        self.res = self.settings.resolution

    def generate_ground(self, level, groundLoc, tw, th):
        """
        Generate the ground using the tile method.
        tw, th are the dimentions of the tile.
        groundLoc is the location of the ground.
        """
        ground_list = pygame.sprite.Group()

        if level == 1:
            for i in range(len(groundLoc)):
                ground = Platform(groundLoc[i],
                                  self.settings.screenY - th,
                                  'tile-ground.png')
                ground_list.add(ground)

        if level == 2:
            print('level ' + str(level))

        return ground_list

    def platform(self, level, tw, th):
        """
        Generate platforms for each level.
        tw, th, are the width and height of the tile sprites.
        """
        platform_list = pygame.sprite.Group()
        platform_location = []

        if level == 1:
            # Xloc,, yloc, len of platform
            platform_location.append((300, self.res[1] - th - 128, 4))
            platform_location.append((900, self.res[1] - th - 128, 5))
            platform_location.append((1030, self.res[1] - th - 256, 4))
            print(platform_location)
            # For every item in platform_location
            for i in range(len(platform_location)):
                # Generate a platform[i][2] wide
                for j in range(platform_location[i][2]):
                    plat = Platform((platform_location[i][0]+(j*tw)),
                                    platform_location[i][1], 'tile.png')
                    platform_list.add(plat)

        if level == 2:
            print('level ' + str(level))

        return platform_list

    def loot(self, level):
        loot_list = pygame.sprite.Group()

        if level == 1:
            loot = Platform(64 * 10, self.res[1]-64 * 5, 'loot_1.png')
            # Xlocation, y location (tx*9, ty*5)
            # This is expressed as multiples of tile size. You can also,
            # Hard-code the locations
            loot_list.add(loot)

        if level == 2:
            print('level ' + str(level))

        return loot_list

    def enemies(self, level, location, img):
        """Generate enemies for each level."""
        enemy_list = pygame.sprite.Group()

        if level == 1:
            enemy = Enemy(self, location[0], location[1], img)
            enemy_list.add(enemy)

        if level == 2:
            print('level ' + str(level))

        return enemy_list
