from colorama import Fore, Back, Style, init
import re

class Grid:
    def __init__(self):
        self.grid = [[0] * 1000 for _ in range(1000)]
        # self.total_brightness = 0

    def totalBrightness(self, action, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1): #iterate over each row within the specified range
            for y in range(start_y, end_y + 1): #iterate over each column within the specified range, for each row
                if action == "turn on":
                    self.grid[x][y] += 1
                elif action == "turn off":
                    self.grid[x][y] = max(0, self.grid[x][y] - 1)
                elif action == "toggle":
                    self.grid[x][y] += 2

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

    def count_lit_lights(self):
        return sum(sum(row) for row in self.grid)

    def count_total_brightness(self):
        return sum(sum(row) for row in self.grid)

def main():
    grid = Grid()
    with open("input.txt", "r") as file:
        instructions = file.readlines()
        for instruction in instructions:
            action, start_x, start_y, end_x, end_y = grid.parse_instruction(instruction)
            grid.totalBrightness(action, start_x, start_y, end_x, end_y)

    # lit_lights = grid.count_lit_lights()
    total_brightness = grid.count_total_brightness()
    print(f"{Fore.GREEN}Total number of lit lights: {total_brightness}")

if __name__ == "__main__":
    main()
