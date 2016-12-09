class Problem:
    def __init__(self, inp):
        self.data = inp.read().strip()

    @staticmethod
    def parse(string, version=1):
        result = 0
        while True:
            pre, _, rest = string.partition("(")
            result += len(pre)
            if rest == "":
                break
            a, post = rest.split(")", 1)
            chars, times = list(map(int, a.split("x")))
            sublen = len(post[:chars]) if version == 1 else Problem.parse(post[:chars], version)
            result += sublen * times
            string = post[chars:]
        return result

    def step1(self):
        return Problem.parse(self.data, version=1)

    def step2(self):
        return Problem.parse(self.data, version=2)
