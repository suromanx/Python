class MyClass:
    def __init__(self,n='Белый'):
        self.name = n
        print('Создан обьект',self.name)
    def __del__(self):
        print('Удален Обьект',self.name)

def create(n):
    obj = MyClass(n)

A = MyClass()
B = MyClass('Красный')
C = MyClass('Blue')
create('Yellow')
C.name = 'Green'

del A
del B
del C
