class Alpha:
    def display(self):
        print('Method Alpha')
        print('Field code: ', self.code)

    def show(self):
        self.display()
class Bravo(Alpha):
    def display(self):
        print('Method from Bravo')
        print('Name field: ', self.name)

A = Alpha()
A.code = 123

B = Bravo()
B.name = 'B'

A.show()
print()
B.show()
