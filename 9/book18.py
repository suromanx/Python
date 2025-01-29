class Fibs:
    def __getitem__(self, item):
        a = 1
        b = 1

        for k in range(item-2):
            a,b = b, a+b
        return b

A = Fibs()

for k in range(1,15):
    print(A[k], end=" ")
