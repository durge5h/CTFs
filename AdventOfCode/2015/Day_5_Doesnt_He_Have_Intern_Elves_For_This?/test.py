import string

class PuzzleSolver:
    def __init__(self, file_input):
        self.file_input = file_input
        self.flag = []  # List to store nice strings

    def worker(self, line):
        vowels = 'aeiou'
        disallowed = ['ab', 'cd', 'pq', 'xy']

        # Condition 1: Check for at least three vowels
        if sum(1 for char in line if char in vowels) < 3:
            return False

        # Condition 2: Check for at least one letter that appears twice in a row
        if not any(line[i] == line[i + 1] for i in range(len(line) - 1)):
            return False

        # Condition 3: Check for disallowed substrings
        if any(substring in line for substring in disallowed):
            return False

        # If all conditions are met, return True (nice string)
        return True

    def naughtyOrNice(self, line):
        if self.worker(line):
            self.flag.append(line)

    def solve(self):
        with open(self.file_input, "r") as f:
            data = f.read().strip().split('\n')
            for line in data:
                self.naughtyOrNice(line)

if __name__ == "__main__":
    file_input = "./input.txt"
    solver = PuzzleSolver(file_input)
    solver.solve()
    print("\033[1;32mResult:\033[0m", len(solver.flag))
