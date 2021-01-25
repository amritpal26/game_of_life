import pygame
from config import Config

BLACK = Config.get_config("colors")["BLACK"]
WHITE = Config.get_config("colors")["WHITE"]

TILESIZE = Config.get_config("tile_size")

class Cell(pygame.sprite.Sprite):

    def __init__(self, sprite_groups, x, y, tile_size):
        self.groups = sprite_groups

        pygame.sprite.Sprite.__init__(self, sprite_groups)
        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size

        self.kill(BLACK)

    def revive(self, color=WHITE):
        self.is_alive = True
        self.image.fill(color)

    def kill(self, color=BLACK):
        self.is_alive = False
        self.image.fill(color)
