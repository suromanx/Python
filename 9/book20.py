class Alpha:
    def __init__(self, *vals):
        L = []
        for v in vals:
            if type(v) == int:
                L.append(v)

        self.nums = L

    def __iter__(self):
        return Bravo(self.nums)


class Bravo:
    def __init__(self, nums):
        L = []
        for n in nums:
            if n < 10 and n >0:
                L.append(n)

        self.digits = L
        self.position = -1

    def __next__(self):
        self.position += 1
        if self.position < len(self.digits):
            return self.digits[self.position]

        else:
            raise StopIteration


A = Alpha(2, "A", 12, 7, -3, "Hello", 9, 5, "Alpha")
B = iter(A)

try:
    while True:
        print(next(B), end=" ")
except StopIteration:
    print()
