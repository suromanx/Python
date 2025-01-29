class Alpha:
    def __setattr__(self, name, value):
        if name == 'number' and type(value)!= int:
            res = 0

        else:
            res = value

        self.__dict__[name]=res

A = Alpha()
A.value = 'Object A'

print('A.value =', A.value)
print()
A.number = 123
print(A.number)
print()
A.number = 'hello'
print(A.number)
A.value = 321
print(A.value)
print()
A.__dict__['number']='Python'
print(A.number)