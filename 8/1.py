class MyClass:
    def __init__(self,val_1,val_2):
        self.A = val_1
        self.B = val_2

    def my_fun(self):
        print(self.A)
        print(self.B)

obj = MyClass(20,30)

obj.my_fun()