import re
import itertools


class Problem:
    def __init__(self, inp):
        self.data = []
        for line in inp.read().strip().split("\n"):
            r = re.split("[\[\]]", line)
            self.data.append((r[0::2], r[1::2]))

    @staticmethod
    def has_abba(s):
        for i in range(len(s) - 3):
            if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
                return True
        return False

    @staticmethod
    def has_bab(s):
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] == s[i + 2]:
                yield s[i:i + 3]

    def step1(self):
        return len(list(filter(lambda l: any(map(Problem.has_abba, l[0]))
                                         and not any(map(Problem.has_abba, l[1])), self.data)))

    def step2(self):
        count = 0
        for l in self.data:
            hypernet_babs = list(itertools.chain.from_iterable(map(Problem.has_bab, l[1])))
            for bab in itertools.chain.from_iterable(map(Problem.has_bab, l[0])):
                if bab[1] + bab[0] + bab[1] in hypernet_babs:
                    count += 1
                    break
        return count
