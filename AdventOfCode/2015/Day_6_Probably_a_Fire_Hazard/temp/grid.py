class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = value
        else:
            print("Invalid coordinates.")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        else:
            print("Invalid coordinates.")
            return None

# Create a 1000x1000 grid
grid = Grid(10, 10)

# Set some values in the grid
grid.set_value(0, 0, 1)
grid.set_value(0, 9, 1)
grid.set_value(9, 9, 1)
grid.set_value(9, 0, 1)


# Print the grid
grid.print_grid()

# Get a value from the grid
print(grid.get_value(0, 0))
print(grid.get_value(0, 9))
print(grid.get_value(9, 9))
print(grid.get_value(9, 0))

print(grid.get_value(1000, 1000))  # This should print an error message
