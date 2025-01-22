class MyClass:
    def set(self,n):
        self.number = n
    def show(self):
        print('Поле number = ',self.number)

obj = MyClass()

print('Наличие поля obj',hasattr(obj,'number'))

try:
    obj.show()

except AttributeError:
    print('Поля нету у него')

obj.number = 123

obj.show()
obj.set(321)
obj.show()