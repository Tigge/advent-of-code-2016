import itertools
import hashlib


class Problem:
    def __init__(self, inp):
        self.data = inp.read().strip().encode("ascii")

    @staticmethod
    def find_hashes(startswith, content):
        password = ""
        m = hashlib.md5(content)
        for i in itertools.count():
            n = m.copy()
            n.update(str(i).encode("ascii"))
            digest = n.hexdigest()
            if digest.startswith(startswith):
                yield digest

    def step1(self):
        return ''.join(map(lambda digest: digest[5], itertools.islice(Problem.find_hashes("00000", self.data), 8)))

    def step2(self):
        password = ["_"] * 8
        for digest in Problem.find_hashes("00000", self.data):
            pos = int(digest[5], 16)
            if pos < len(password) and password[pos] == "_":
                password[pos] = digest[6]
                if "_" not in password:
                    return ''.join(password)
