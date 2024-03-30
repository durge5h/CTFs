class PuzzleSolver:
    def __init__(self, file_input):
        self.file_input = file_input
        self.flag = set() #visited house, Use a set to keep track of visited houses
        self.currentMoves = (0, 0) 

    def gettingDemensions(self,move):
        direction = move
        # self.currentMoves = (self.currentMoves[0] +1, self.currentMoves[1] + 1)
        if direction == ">":
            self.currentMoves = (self.currentMoves[0] + 1, self.currentMoves[1])
        elif direction == "<":
            self.currentMoves = (self.currentMoves[0] - 1, self.currentMoves[1])
        elif direction == "^":
            self.currentMoves = (self.currentMoves[0], self.currentMoves[1] + 1)
        elif direction == "v":
            self.currentMoves = (self.currentMoves[0], self.currentMoves[1] - 1)

    def housesReceived(self, move):
        # self.move = move
        self.gettingDemensions(move)
        # print(f"currentMoves: {self.currentMoves, type(self.currentMoves)}")
        self.flag.add(self.currentMoves)
        # print(f"Houses visited: {self.flag}")

    def solve(self):
        with open(self.file_input, "r") as f:
            # moves = f.readline()
            # print(type(moves[1]))
            moves = "^>v<"
            self.flag.add((0, 0)) # was tricky for me for no reason, adding before as Santa start at his starting location
            for move in moves:
                self.housesReceived(move)
                # exit()
            print(f"Houses visited: {self.flag}")

if __name__ == "__main__":
    file_input = "./input.txt"
    solver = PuzzleSolver(file_input)
    result = solver.solve()
    print("\033[1;32mHouses Visited by Santa is:\033[0m",len(solver.flag))
