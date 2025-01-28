class Alpha:
    def __getattribute__(self, name):
        print("Alpha:запрос поля  ", name)
        return object.__getattribute__(self,name)

    def __getattr__(self, name):
        print(" Нет такого поля !")
        return 'Alpha '+name
class Bravo:
    def __getattribute__(self, name):
        print('Bravo:запрос  поля',name)

        try:
            res = object.__getattribute__(self,name)
        except AttributeError:
            res = 'Bravo: нет поля'+name
        return res

print("обьект A  класса Alpha")
A = Alpha()
A.value = 123
print(A.value)
print('eще раз',object.__getattribute__(A,'value'))
A.value = 321
print()
print('Поле value',A.value)
print(A.color)
print('Обьект B класса Bravo')
B = Bravo()
B.mylist = [2,3,4]
print(B.mylist)
print(object.__getattribute__(B,'mylist'))
B.mylist = ['A','B','C']
print(B.mylist)
print(B.myset)
