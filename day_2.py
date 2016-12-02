class Problem:
    def __init__(self, inp):
        self.data = inp.read().strip().split("\n")

    @staticmethod
    def walk(keypad, position, instructions):
        MOVES = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
        for instruction in instructions:
            for letter in instruction:
                new_position = (position[0] + MOVES[letter][0], position[1] + MOVES[letter][1])
                if new_position[0] < 0 or new_position[1] < 0:
                    continue
                if new_position[0] >= len(keypad) or new_position[1] >= len(keypad):
                    continue
                new_number = keypad[new_position[1]][new_position[0]]
                if new_number == "-":
                    continue
                position = new_position
            yield keypad[position[1]][position[0]]

    def step1(self):
        keypad = [["1", "2", "3"],
                  ["4", "5", "6"],
                  ["7", "8", "9"]]
        return ''.join(Problem.walk(keypad, (1, 1), self.data))

    def step2(self):
        keypad = [["-", "-", "1", "-", "-"],
                  ["-", "2", "3", "4", "-"],
                  ["5", "6", "7", "8", "9"],
                  ["-", "A", "B", "C", "-"],
                  ["-", "-", "D", "-", "-"]]
        return ''.join(Problem.walk(keypad, (1, 1), self.data))
