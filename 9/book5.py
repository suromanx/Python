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
        print('Const #2')
        self.number = num
        self.name = txt
        print('New object')
        self.show