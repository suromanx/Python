class Alpha():
    code = 123
    def alpha(self):
        print('alpha',self.code)

class Bravo(Alpha):
    def bravo(self):
        print('bravo', self.code)

class Charlie(Bravo):
    def charlie(self):
        print('charlie', self.code)


def show(MyClass):
    print('Class', MyClass.__name__,end= ':\n')

    for s in MyClass.__mro__:
        print('<',s.__name__,'>',end='',sep = '')
    print()

show(Alpha)
show(Bravo)
show(Charlie)
print()
A = Alpha()
B = Bravo()
C = Charlie()
print('Object A')
A.alpha()
print('Object B')
B.alpha()
B.bravo()
print('Object C')
C.alpha()
C.bravo()
C.charlie()
#Assignment the value to the feild
Bravo.code = 321
print('Command Executed Bravo.code = 321')
print('Object C')
C.alpha()
C.bravo()
C.charlie()
print('Object A')
A.alpha()

