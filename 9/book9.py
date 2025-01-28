class MyClass:
    def __init__(self,val):
        self.value = val

    def __str__(self):
        return 'Field '+ str(self.value)
    def __bool__(self):
        if type(self.value) == int:
            return True
        else:
            return False

    def _
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
print('Object A')
A = MyClass(100)
print(A)
print('Num', int(A))
print('A - 1 = ', int(A)-1)
print()
print('Object B')
B =MyClass('B')
print(B)
print('Num',int(B))
print("B + 1 = ", int(B)+1)


