class Problem:
    def __init__(self, inp):
        self.data = list(map(lambda l: (int(l[0:5]), int(l[5:10]), int(l[10:15])), inp.read()[:-1].split("\n")))

    @staticmethod
    def valid(t):
        return t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]

    def step1(self):
        return len(list(filter(lambda v: v, map(Problem.valid, self.data))))

    def step2(self):
        valid = 0
        for i in range(len(self.data)):
            col, row = i % 3, (i // 3) * 3
            valid += 1 if Problem.valid((self.data[row][col], self.data[row + 1][col], self.data[row + 2][col])) else 0
        return valid
