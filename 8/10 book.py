class MyClass:

    def __init__(self, val):
        if type(val) == int:
            self.number = val

        elif type(val) == str:
            self.name = val
        elif type(val) == float:
            self.value = val
        else:
            self.data = val

    def show(self):
        L = ['number', 'name', 'value', 'data']
        for s in L:
            if s in dir(self):
                print(s, "=", self.__dict__[s])
                break
        else:
            print('Strange Object')

A = MyClass(123)
A.show()

del A.number

A.show()

B = MyClass("Обьект B")
B.show()

C = MyClass(2.5)
C.show()

D = MyClass([1,2,3])
D.show()
