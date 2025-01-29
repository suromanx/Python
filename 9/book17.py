class Alpha:
    def __getitem__(self, index):
        return self.value[index]

    def __setitem__(self, index, val):
        self.value[index]=val

    def __delitem__(self, index):
        del self.value[index]

    def __str__(self):
        return str(self.value)
    def __len__(self):
        return len(self.value)

A = Alpha()
A.value = [100,200,300]
print(A)

for k in range(len(A)):
    print(A[k], end=" ")
print()
A[1] = 'A'
print(A)
del A[0]
print(A)