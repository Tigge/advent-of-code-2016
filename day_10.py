class Problem:
    def __init__(self, inp):
        do = list(map(lambda line: line.split(" "), inp.read().strip().split("\n")))
        self.data = {"bot": {}, "output": {}}

        def update(typ: str, num: str, val: int):
            self.data[typ][num] = val if typ == "output" else sorted(self.data["bot"].get(num, []) + [val])

        while len(do) > 0:
            pending = []
            for l in do:
                if l[0] == "value":
                    update(l[4], l[5], int(l[1]))
                elif l[0] == "bot" and l[1] in self.data["bot"] and len(self.data["bot"][l[1]]) == 2:
                    update(l[5], l[6], self.data["bot"][l[1]][0])
                    update(l[10], l[11], self.data["bot"][l[1]][1])
                else:
                    pending.append(l)
            do = pending

    def step1(self):
        for bot, values in self.data["bot"].items():
            if values == [17, 61]:
                return bot

    def step2(self):
        return self.data["output"]["0"] * self.data["output"]['1'] * self.data["output"]['2']
