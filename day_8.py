class Problem:
    WIDTH = 50
    HEIGHT = 6

    def __init__(self, inp):
        self.data = [[False] * Problem.WIDTH for i in range(Problem.HEIGHT)]
        for instructions in list(map(lambda row: row.split(" "), inp.read().strip().split("\n"))):
            if instructions[0] == "rect":
                w, h = list(map(int, instructions[1].split("x")))
                for r in range(h):
                    self.data[r][:w] = [True] * w
            if instructions[0] == "rotate":
                rotate = int(instructions[4])
                col_or_row = int(instructions[2][2:])
                if instructions[1] == "column":
                    column = [self.data[i][col_or_row] for i in range(6)]
                    column = column[-rotate:] + column[:-rotate]
                    for i in range(6):
                        self.data[i][col_or_row] = column[i]
                if instructions[1] == "row":
                    self.data[col_or_row] = self.data[col_or_row][-rotate:] + self.data[col_or_row][:-rotate]

    def step1(self):
        return sum(map(sum, self.data))

    def step2(self):
        return '\n' + '\n'.join(map(lambda row: ''.join(map(lambda v: "#" if v else ".", row)), self.data))
