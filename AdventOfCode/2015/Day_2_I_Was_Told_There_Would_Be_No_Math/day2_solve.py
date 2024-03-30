class PuzzleSolver:
    def __init__(self, file_input):
        self.file_input = file_input
        self.finalSA = 0

    def surfaceArea(self,data):
        self.data = data
        #sa = 2*l*w + 2*w*h + 2*h*l
        l,w,h = map(int, self.data.split('x'))
        # self.data = str(self.data.replace('x','*'))
        sa = (2*l*w + 2*w*h + 2*h*l) 
        sa = sa + min(l*w,w*h,h*l)  # the area of the smallest side(took time).
        # sa = math.sqrt(sa) # thought have to convert feet to sfeet, but SA has sfeet value already
        print(f"flag: {sa}")
        return sa

    def solve(self):
        with open(self.file_input, "r") as f:
            data = f.read().strip().split('\n')
            # data_len = len(data)
            for index,val in enumerate(data):
                self.finalSA += self.surfaceArea(data[index])
                # print(f"finalSA: {self.finalSA}")
                # exit()
        print(self.finalSA)

if __name__ == "__main__":
    file_input = "./input.txt"
    solver = PuzzleSolver(file_input)
    result = solver.solve()
    print("\033[1;32mResult:\033[0m",result)
