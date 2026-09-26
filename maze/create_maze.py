from typing import List

class CreateMaze:
    def __init__(self, bit_grid: List[List[int]]) -> None:
        self.bit_grid = bit_grid
        self.grid: List[List[List[bool]]] = [[[False for _ in range(5)] for x in y]for y in self.bit_grid]

    def creator(self) -> None:
        self.grid = self.bit_gird.copy()
        for y in range(len(self.bit_grid)):
            for x in self.bit_grid[y]:
                cell = self.bit_grid[x][y]
                if cell & 1:
                    # we have a north wall
                    self.grid[y][self.bit_grid[y].index(x)[0]] = True
                if cell & 2:
                    # we have a east wall
                    self.grid[y][self.bit_grid[y].index(x)[1]] = True
                if cell & 4:
                    # we have a sout wall
                    self.grid[y][self.bit_grid[y].index(x)[2]] = True
                if cell & 8:
                    # we have a west wall
                    self.grid[y][self.bit_grid[y].index(x)[3]] = True
