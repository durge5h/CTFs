from colorama import Fore, Back, Style, init
import re
import numpy as np
import time

class Grid:
    def __init__(self):
        self.grid = [[False] * 1000 for _ in range(1000)]
        self.grid2 = np.full((1000, 1000),0)

    def parse_instruction(self, instruction):
        pattern = r"([a-z ]+) (\d+),(\d+) through (\d+),(\d+)"
        match = re.match(pattern, instruction)
        action, start_x, start_y, end_x, end_y = match.groups()
        start_x, start_y, end_x, end_y = map(int, [start_x, start_y, end_x, end_y])
        return action, start_x, start_y, end_x, end_y

    def apply_instruction(self, action, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1): #iterate over each row within the specified range
            for y in range(start_y, end_y + 1): #iterate over each column within the specified range, for each row
                if action == "turn on":
                    self.grid[x][y] = True
                elif action == "turn off":
                    self.grid[x][y] = False
                elif action == "toggle":
                    self.grid[x][y] = not self.grid[x][y]

    def apply_instruction_fast_way(self, action, start_x, start_y, end_x, end_y):
        if action == "turn on":
            self.grid2[start_x:start_y+1, end_x:end_y+1] = 1
        elif action == "turn off":
            self.grid2[start_x:start_y+1, end_x:end_y+1] = 0
        elif action == "toggle":
            self.grid2[start_x:start_y+1, end_x:end_y+1] = 1 - self.grid2[start_x:start_y+1, end_x:end_y+1]


    def count_lit_lights(self):
        # return sum(sum(row) for row in self.grid)
        return self.grid2.sum()

def main():
    grid = Grid()
    with open("input.txt", "r") as file:
        instructions = file.readlines()
        for instruction in instructions:
            action, start_x, start_y, end_x, end_y = grid.parse_instruction(instruction)
            grid.apply_instruction_fast_way(action, start_x, start_y, end_x, end_y)

    lit_lights = grid.count_lit_lights()
    print(f"{Fore.GREEN}Total number of lit lights: {lit_lights}")

if __name__ == "__main__":
    main()
