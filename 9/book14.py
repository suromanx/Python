class Alpha:
    def __getattr__(self, name):
        return len(name)

class Bravo:
    def show(self,x):
        print('Method show(): ', x)

    def __getattr__(self, name):
        if len(name)<5:
            return lambda x:print('First method:',x)
        else:
            return lambda x: print('Второй метод',x*x)

print('Обьект А класса Alpha')
A = Alpha()
A.value = 'Alpha'
print(A.value)
print()
print(A.color)
print('Field myattribute:', A.myattribute)
print()
B = Bravo()
B.show(10)
B.hi(10)
B.display(10)