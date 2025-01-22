class Alpha:
    pass
class Bravo:
    name = ('Bravo')
    def display():
        print('Поле name',Bravo.name)
    def show(self):
        print('Поле value',self.value)
    def __init__(self):
        self.value = 123
A = Alpha()
B = Bravo()
print('1')
print('class ALpha')
n =1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+":",Alpha.__dict__[s])

print()
print('Obj A',A.__dict__)

print('Obj B',B.__dict__)

Bravo.display()
Alpha.display = Bravo.display()

del Bravo.display
B.show()

B.show()

A.color = 'red'

B.show= lambda : print('Обьект B',B.value)
print()

print('Alpha class')

n = 1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+": ",Alpha.__dict__[s])
    n+=1

print('Bravo class')

n = 1
for s in Bravo.__dict__:
    print("["+str(n)+"] "+s+": ",Bravo.__dict__[s
    ])
    n+=1


print('Obj A',A.__dict__)

print('Obj B',B.__dict__)

Alpha.display()
Bravo.show()
B.show()