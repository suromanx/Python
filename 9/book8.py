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
        super().show()
        Charlie.show(self)
        super(Bravo, self).show()


def display(MyClass):
    print("Ingeritance for " + MyClass.__name__ + ":")
    k = 1
    for s in MyClass.__mro__:
        print("[" + str(s) + "]", s.__name__)
        k += 1


display(Alpha)
A = Alpha(100)
print()
A.show()
print()
display(Bravo)
B = Bravo(200)
print()
B.show()
print()
display(Charlie)
print()
C = Charlie(300)
C.show()
print()
display(Delta)
print()
D = Delta(400)
print()
D.show()
