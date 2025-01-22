class MyClass:
    def __init__(self):
        self.value = 123
        print('Создaется обьект',self.value)
    def __del__(self):
        print('Удаляется обьект',self.value)

    def set(self,n):
        self.value=n
    def show(self):
        print('поле обьекта',self.value)

obj = MyClass()

obj.show()

obj.set(100)

print('1')
MyClass.show(obj)
MyClass.set(obj,200)
print('2')
obj.show()
print('3')
MyClass.__init__(obj)
print()
MyClass.__del__(obj)
print()

obj.show()
obj.value  = 321
print()
obj.show()
print('final')
obj.__init__()
obj.__del__()
obj.show()