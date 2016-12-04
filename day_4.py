import itertools


class Problem:
    def __init__(self, inp):
        def parse(string):
            return {
                "encrypted": string[:-11],
                "checksum": string[-6:-1],
                "sector": int(string[-10:-7])
            }
        self.data = list(map(parse, inp.read().strip().split("\n")))

    @staticmethod
    def rotate(char, rotations):
        return ' ' if char == '-' else chr((ord(char) - ord('a') + rotations) % 26 + ord('a'))

    def step1(self):
        count = 0
        for item in self.data:
            encrypted_sort = sorted(item["encrypted"].replace("-", ""))
            encrypted_group = [list(g) for k, g in itertools.groupby(encrypted_sort)]
            encrypted_group_sort = sorted(encrypted_group, key=lambda x: len(x), reverse=True)
            for i, checksum_letter in enumerate(item["checksum"]):
                if encrypted_group_sort[i][0] != checksum_letter:
                    break
            else:
                count += item["sector"]
        return count

    def step2(self):
        for item in self.data:
            decrypted = ''.join((map(lambda c: Problem.rotate(c, item["sector"]), item["encrypted"])))
            if decrypted == "northpole object storage":
                return item["sector"]