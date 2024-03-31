import hashlib

class PuzzleSolver:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.flag = '' #positive number

    def hashingInp(self,hme):
        md5 = hashlib.md5(hme.encode('utf-8'))
        return md5.hexdigest()

    def miningCoin(self,puzzle_input):
        i = 1
        while True:
            hme = puzzle_input + str(i)
            # print(f"hme: {hme}")
            hvalue = self.hashingInp(hme)
            if hvalue.startswith("00000"):
                return i 
            i += 1

    def solve(self):
        self.flag = self.miningCoin(self.puzzle_input)
        return self.flag

if __name__ == "__main__":
    puzzle_input = "yzbqklnj"
    solver = PuzzleSolver(puzzle_input)
    result = solver.solve()
    print("\033[1;32mLowest Positive Number:\033[0m",result)
