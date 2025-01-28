class Alpha:
    code = 123
    def __init__(self,num):
        print('Constructor #1')
        self.number = num
        print('Object created')
        self.show()

    def show(self):
        print('Method 1')
        print('Class:', self.__class__.__name__)
        print('Code Class', self.__class__.code)
        print("Number field", self.number)

class Bravo(Alpha):
    code = 456

class Charlie(Bravo):
    def __init__(self,num,txt):
        print('Constructor #2')
        self.number = num
        self.name = txt
        print('New object')
        self.show()
    def show(self):
        print('Method 2')
        print('Class', self.__class__.__name__)
        print('Code of class', self.__class__.code)
        print('Number field', self.number)
        print('Name field', self.name)
class Delta(Charlie):
    code = 789


A = Alpha(100)
print()
A.code = 321
print('After A.code=321 command')
A.show()
print('b ->')
B = Bravo(200)
print()
print('charlie ->')
print()
C = Charlie(300,'C')
print()
D = Delta(400,'D')


