class Alpha:
    def __init__(self,lst):
        self.vals = []
        if type(lst) == list:
            for n in lst:
                self.vals.append(n)
    def __str__(self):
        return str(self.vals)

    def __pos__(self):
        x = self.vals[0]
        del self.vals[0]
        self.vals.append(x)
        return self

    def __neg__(self):
        x = self.vals[-1]
        del self.vals[-1]
        self.vals.insert(0,x)
        return self

    def __mul__(self, v):
        self.vals.append(v)
        return self

    def __rmul__(self,v):
        self.vals.insert(0,v)
        return self

    def __imul__(self, other):
        return self*other

A = Alpha([1,'a',2])
print(A)
print()
print(+A)
print(-A)
print(A*3)
print(4*A)
A*= 'Alpha'
print(A)
