import pygame
from config import Config

BLACK = Config.get_config("colors")["BLACK"]
WHITE = Config.get_config("colors")["WHITE"]

TILESIZE = Config.get_config("tile_size")

class Cell(pygame.sprite.Sprite):

    def __init__(self, sprite_groups, x, y):
        self.groups = sprite_groups

        pygame.sprite.Sprite.__init__(self, sprite_groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.dead(BLACK)

    def birth(self, color=WHITE):
        self.is_alive = True
        self.image.fill(color)

    def dead(self, color=BLACK):
        self.is_alive = False
        self.image.fill(color)
