class Alpha :
    pass
class Bravo:
    pass
MyClass = Alpha

A = MyClass()

MyClass = Bravo
B = MyClass()

Alpha = Bravo

C = Alpha()

MyClass = A.__class__

D = MyClass()

print('Обьект a:',type(A).__name__)

print('Обьект b:',type(B).__name__)

print('Обьект c:',type(C).__name__)

print('Обьект d:',type(D).__name__)

MyClass.__name__ = 'First'
Bravo.__name__='Second'


print()
print('Обьект a:',type(A).__name__)

print('Обьект b:',type(B).__name__)

print('Обьект c:',type(C).__name__)

print('Обьект d:',type(D).__name__)