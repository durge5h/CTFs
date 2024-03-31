import string

class PuzzleSolver:
    def __init__(self, file_input):
        self.file_input = file_input
        self.flag = [] # nice string

    def worker(self,santaString):
        vowels = 'aeiou'
        disallowed = ['ab', 'cd', 'pq', 'xy']
        
        if sum(1 for line in santaString if line in vowels) < 3:
            return False
        if not any(santaString[i] == santaString[i+1] for i in range(len(santaString) - 1)):
            return False
        # if all(substring not in variable for substring in disallowed)
        if any(substring in santaString for substring in disallowed):   
            return False
        return True

    def naughtyOrnice(self,santaString):
        if self.worker(santaString):
            self.flag.append(santaString)

    def solve(self):
        with open(self.file_input, "r") as f:
            data = f.read().strip().split('\n')
            for line in data:
                self.naughtyOrnice(line)

if __name__ == "__main__":
    file_input = "./input.txt"
    solver = PuzzleSolver(file_input)
    result = solver.solve()
    print("\033[1;32mNumber Of Nice String:\033[0m",len(solver.flag))