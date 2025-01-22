class MyClass:
    def __init__(self,txt,num):
        self.A = txt
        self.B = num

    def my_fun(self):
        if type(self.A) == str and type(self.B) == str:
            P = [self.A + self.B]
            print(P)
        elif type(self.A) == int and type(self.B) == int:
            E = [self.A + self.B]
            print(E)
        else:
            print('Ничего не создается')

obj = MyClass(4,2)
obj_1 = MyClass('a','s')

obj.my_fun()
obj_1.my_fun()
