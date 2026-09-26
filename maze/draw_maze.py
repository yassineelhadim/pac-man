import pygame as pyg
import time
from typing import List, Any
from .create_maze import CreateMaze

class Directions(enumerate):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

class MazeDrawer:
    def __init__(self, width: int, height: int, bit_grid: List[List[int]]) -> None:
        self.width = width
        self.height = height
        self.bit_grid = bit_grid
        self.draw_maze()

    def draw_maze(self) -> None:
        cell_size = 24
        pyg.init()
        maze = CreateMaze(self.bit_grid)
        screen = pyg.display.set_mode((self.width * 70, self.height * 70))
        self.draw(screen, self.bit_grid, cell_size)
        
        # rect_obj = py.draw.rect()
        # time.sleep()
    #     running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    # pygame.quit()
    # pygame.draw.line(surface, (0, 0, 255), (px, py), (px + tile_size, py), 2)

    def draw(self, screen: pyg.Surface, bit_grid: List[List[int]], cell_size: int) -> None:
        for y in range(len(bit_grid)):
            for x in range(len(bit_grid[y])):
                px = x * cell_size
                py = y * cell_size
                wall = bit_grid[y][x]
                if wall & 1:
                    pyg.draw.line(screen, (0, 0, 255), (px, py), (px + cell_size, py), 3)
                if wall & 2:
                    pyg.draw.line(screen, (0, 0, 255), (px + cell_size, py), (px + cell_size, py + cell_size), 3)
                if wall & 4:
                    pyg.draw.line(screen, (0, 0, 255), (px, py + cell_size), (px + cell_size, py + cell_size), 3)
                if wall & 8:
                    pyg.draw.line(screen, (0, 0, 255), (px, py), (px, py + cell_size), 3)
        # screen.fill((0, 0, 0))
        pyg.display.flip()
        time.sleep(100)