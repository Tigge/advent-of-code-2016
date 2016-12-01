class Problem:
    def __init__(self, inp):
        self.data = list(map(lambda x: x.strip(), inp.read().split(",")))

    @staticmethod
    def rectilinear_distance(position):
        return abs(position[0]) + abs(position[1])

    @staticmethod
    def walk(instructions):
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        TURNS = {"L": -1, "R": 1}
        location = (0, 0)
        yield location
        direction = 0
        for instruction in instructions:
            direction = (direction + TURNS[instruction[0]]) % len(DIRS)
            steps = int(instruction[1:])
            moments = DIRS[direction]
            for i in range(steps):
                location = (location[0] + moments[0], location[1] + moments[1])
                yield location

    def step1(self):
        values = Problem.walk(self.data)
        final = list(values)[-1]
        return Problem.rectilinear_distance(final)

    def step2(self):
        positions = {}
        for position in Problem.walk(self.data):
            if position in positions:
                return Problem.rectilinear_distance(position)
            positions[position] = True
