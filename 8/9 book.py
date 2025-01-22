def F(Alpha):
    class Bravo:
        value = Alpha()
    Bravo.__name__ = "My"+Alpha.__name__
    return Bravo
@F
class Charlie:
    def __init__(self):
        self.number = 123
    def show(self):
        print('Поле number',self.number)

obj = Charlie()
obj.value.show()

print("Класс обьекта obj",obj.__class__.__name__)
print("Класс поля value",obj.value.__class__.__name__)


