import pygame
from config import Config
from board import Board

BLACK = Config.get_config("colors")["BLACK"]
WHITE = Config.get_config("colors")["WHITE"]
GREY = Config.get_config("colors")["GREY"]

WIDTH = Config.get_config("screen_width")
HEIGHT = Config.get_config("screen_height")
TITLE = Config.get_config("app_title")
TILESIZE = Config.get_config("tile_size")

FPS = Config.get_config("frames_per_second")
GPS = Config.get_config("generations_per_second")

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_paused = True

        self.next_generation_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.next_generation_event, 1000//GPS)
    
    def new(self):
        grid_width = int(WIDTH / TILESIZE)
        grid_height = int(HEIGHT / TILESIZE)
        self.all_sprites = pygame.sprite.Group()
        self.board = Board(self.all_sprites, grid_width, grid_height)

    def quit(self):
        pygame.quit()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, GREY, (0, y), (WIDTH, y))

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pygame.display.flip()

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                    self.quit()
                elif event.key == pygame.K_SPACE:
                    self.is_paused = not(self.is_paused)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // TILESIZE
                col = x // TILESIZE
                self.board.toggle_cell(row, col)
            elif event.type == self.next_generation_event and not self.is_paused:
                self.board.next_generation()
                

        mouse_clicked = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        x = x // TILESIZE
        y = y // TILESIZE

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.listen_events()
            self.draw()


game = Game()
# while True:
game.new()
game.run()