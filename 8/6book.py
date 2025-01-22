class MyClass:
    color = 'red'
    def set(txt):
        MyClass.color = txt
    def show ():
        print(MyClass.color)

MyClass.show()

MyClass.set('Green')

print(MyClass.color)

MyClass.color = 'Blue'
print()
MyClass.show()

print()

A = MyClass()
B = MyClass()

print('class', MyClass.color)
print('obj A', A.color)
print('obj b', B.color)
print()

A.color = 'white'
print('class', MyClass.color)
print('obj A', A.color)
print('obj b', B.color)
print()

MyClass.color = 'yellow'
print('class', MyClass.color)
print('obj A', A.color)
print('obj b', B.color)
print()

del A.color
print('class', MyClass.color)
print('obj A', A.color)
print('obj b', B.color)
print()
