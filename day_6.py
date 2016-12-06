class Problem:
    def __init__(self, inp):
        self.data = [{}, {}, {}, {}, {}, {}, {}, {}]
        for line in inp.read().strip().split("\n"):
            for i, char in enumerate(line):
                self.data[i][char] = self.data[i].get(char, 0) + 1

    def step1(self):
        return ''.join(map(lambda m: sorted(m.items(), key=lambda y: y[1], reverse=True)[0][0], self.data))

    def step2(self):
        return ''.join(map(lambda m: sorted(m.items(), key=lambda y: y[1])[0][0], self.data))
