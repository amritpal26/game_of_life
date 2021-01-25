from config import Config
from cell import Cell

BLACK = Config.get_config("colors")["BLACK"]
WHITE = Config.get_config("colors")["WHITE"]

class Board:
    def __init__(self, sprite_groups, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(sprite_groups, x, y) for x in range(width)] for y in range(height)]

    def toggle_cell(self, row, col):
        cell = self.cells[row][col]
        if cell.is_alive:
            cell.dead()
        else:
            cell.birth()

    def next_generation(self):
        alive_table = [[False for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            prev_y = y-1
            next_y = (y+1) % self.height
            for x in range(self.width):
                prev_x = x-1
                next_x = (x+1) % self.width

                neighbours_count = \
                    self.cells[prev_y][prev_x].is_alive + \
                    self.cells[prev_y][x].is_alive + \
                    self.cells[prev_y][next_x].is_alive + \
                    self.cells[y][prev_x].is_alive + \
                    self.cells[y][next_x].is_alive + \
                    self.cells[next_y][prev_x].is_alive + \
                    self.cells[next_y][x].is_alive + \
                    self.cells[next_y][next_x].is_alive
                
                if self.cells[y][x].is_alive and neighbours_count in [2,3]:
                    alive_table[y][x] = True
                elif neighbours_count == 3:
                    alive_table[y][x] = True
        
        for y, cell_rows in enumerate(self.cells):
            for x, cell in enumerate(cell_rows):
                if alive_table[y][x]:
                    cell.birth(WHITE)
                else:
                    cell.dead(BLACK)
    