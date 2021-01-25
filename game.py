import pygame, sys
from itertools import cycle
from config import Config
from board import Board

BLACK = Config.get_config("colors")["BLACK"]
WHITE = Config.get_config("colors")["WHITE"]
GREY = Config.get_config("colors")["GREY"]
RED = Config.get_config("colors")["RED"]

WIDTH = Config.get_config("screen_width")
HEIGHT = Config.get_config("screen_height")
TITLE = Config.get_config("app_title")
TILESIZES = cycle(Config.get_config("tile_sizes"))

FPS = Config.get_config("frames_per_second")
GPS = Config.get_config("generations_per_second")

FONT = Config.get_config("font")
FONTSIZE = Config.get_config("font_size")

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.next_generation_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.next_generation_event, 1000//GPS)

        self.tile_size = next(TILESIZES)
        self.is_paused = True
        self.show_menu = True
        self.show_grid = True
        self.menu_font = pygame.font.SysFont(FONT, FONTSIZE)
    
    def new(self):
        self.grid_width = int(WIDTH / self.tile_size)
        self.grid_height = int(HEIGHT / self.tile_size)
        self.all_sprites = pygame.sprite.Group()
        self.board = Board(self.all_sprites, self.grid_width, self.grid_height, self.tile_size)
        self.previous_mouse_motion = None

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw_grid(self):
        for x in range(0, WIDTH, self.tile_size):
            pygame.draw.line(self.screen, GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, self.tile_size):
            pygame.draw.line(self.screen, GREY, (0, y), (WIDTH, y))

    def blit(self, position, text, color=RED):
        text_surface = (self.menu_font.render(text, False, color))
        self.screen.blit(text_surface, (FONTSIZE, FONTSIZE*position))

    def draw_menu(self):
        self.blit(0, f"{TITLE}")
        self.blit(1, f"   F1:  Show / Hide menu")
        self.blit(2, f"space:  Run / Pause (Current: {'paused)' if self.is_paused else 'running)'}")
        self.blit(3, f"    g:  Show / Hide grid (Current: {'shown)' if self.show_grid else 'hidden)'}")
        self.blit(4, f"    t:  Change Tile Size ({self.tile_size} - {self.grid_width}x{self.grid_height})")
        self.blit(5, f"    r:  Reset Tiles")
        self.blit(6, f"  LMB:  Revive dead cell")
        self.blit(7, f"  RMB:  Kill living cell")
        self.blit(8, f"ESC|q:  Quit")
        self.blit(int(HEIGHT/FONTSIZE) - 1, f"Developed by Amritpal Singh")

    def draw(self):
        self.all_sprites.draw(self.screen)
        if self.show_grid:
            self.draw_grid()
        if self.show_menu:
            self.draw_menu()
        pygame.display.flip()

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.show_menu = not(self.show_menu)
                elif event.key == pygame.K_SPACE:
                    self.is_paused = not(self.is_paused)
                elif event.key == pygame.K_g:
                    self.show_grid = not(self.show_grid)
                elif event.key == pygame.K_r:
                    self.is_paused = True
                    self.new()
                elif event.key == pygame.K_t:
                    self.tile_size = next(TILESIZES)
                    self.new()
                elif event.key in [pygame.K_ESCAPE, pygame.K_q]:
                    self.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                row = y // self.tile_size
                col = x // self.tile_size
                if event.button == 1:
                    self.board.revive_cell(row, col)
                elif event.button == 3:
                    self.board.kill_cell(row, col)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] != event.buttons[2]:
                buttons = event.buttons
                x, y = event.pos
                row = y // self.tile_size
                col = x // self.tile_size
                if (buttons[0], buttons[2], row, col) != self.previous_mouse_motion:
                    if buttons[0] == 1:
                        self.board.revive_cell(row, col)
                    else:
                        self.board.kill_cell(row, col)
                    self.previous_mouse_motion = (buttons[0], buttons[2], row, col)
            elif event.type == self.next_generation_event and not self.is_paused:
                self.board.next_generation()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.listen_events()
            self.draw()


game = Game()
game.new()
game.run()