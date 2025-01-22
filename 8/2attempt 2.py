class MyClass:
    def __init__(self,arg1,arg2):
        if isinstance(arg1,str) and isinstance(arg2,str):
            self.text = arg1+arg2
        elif isinstance(arg1,int) and isinstance(arg2,int):
            self.number = arg1+arg2
        else:
            print('Поля обьекта не создаются')


    def display(self):
        if hasattr(self,'text'):
            print(f'Текстовое поле : {self.text}')
        if hasattr(self,'number'):
            print(f'Числовое поле: {self.number}')


obj = MyClass('a','b')
obj.display()


obj1 = MyClass(1,2)
obj1.display()


obj = MyClass(2,'b')
obj.display()