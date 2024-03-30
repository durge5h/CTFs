class PuzzleSolver:
    def __init__(self, file_input):
        self.file_input = file_input

    def solve(self):
        with open(self.file_input, "r") as f:
            data = f.read()
            data_len = len(data)
            flag = 0 + 1  # as loop start from 0
            for i in range(data_len):
                if data[i] == '(':
                    flag += 1
                else:
                    flag -= 1
            return flag

if __name__ == "__main__":
    file_input = "./input.txt"
    solver = PuzzleSolver(file_input)
    result = solver.solve()
    print("\033[1;32mResult:\033[0m",result)
