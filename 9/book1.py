class Alpha:
    def __init__(self):
        self.set(100)
        print('Обьект класса альфа',self.number)


    def set(self,n):
        self.number = n

    def show(self):
        print(self.__class__.__name__, self.number)


class Bravo(Alpha):
    def __init__(self):
        self.set(200)
        print(self.number)

A = Alpha()
A.set(123)
A.show()

##Производный класс

print()
B = Bravo()
B.set(234)
B.show()