class ALpha:
    def __getattr__(self, name):
        return "There's no such attribute"

    def __delattr__(self, name):
        if name == 'number':
            print('Delete is forbidden!!')
        else:
            object.__delattr__(self,name)

A = ALpha()

A.value = 'Object A'
print(A.value)
del A.value
A.number = 123
print(A.number)

del A.number
print()
del A.__dict__['number']
print(A.number)

