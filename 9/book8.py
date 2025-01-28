class Alpha():
    def __init__(self, num):
        self.code = num

    def show(self):
        print('Class code: ', self.code)


class Bravo(Alpha):
    def show(self):
        print('Class Bravo: ', self.code)
        super().show()


class Charlie(Alpha):
    def show(self):
        print('Class Charlie: ', self.code)
        super(Charlie, self).show()


class Delta(Bravo, Charlie):
    def show(self):
        print('Class Delta: ', self.code)
        print('1')
        super().show()
        print('2')
        Charlie.show(self)
        print('3')
        super(Bravo, self).show()


print()


def display(MyClass):
    print("Inheritance for " + MyClass.__name__ + ":")
    k = 1
    for s in MyClass.__mro__:
        print("[" + str(s) + "]", s.__name__)
        k += 1


display(Delta)
D = Delta(400)
print()
D.show()
