class Alpha:
    def __init__(self,num):
        self.code = num
        print('Value to field "code" has been assigned')

    def show(self):
        print("Field code: ", self.code)

class Bravo(Alpha):
    def __init__(self,num,txt):
        super().__init__(num)
        self.name = txt
        print('Value to the field "name" has been assigned')

    def show(self):
        super().show()
        print('Name Field: ', self.name)

class Charlie(Bravo):
    def __init__(self,num,txt,val):
        super().__init__(num,txt)
        self.value = val
        print('Value to the field "name" has been assigned')

    def show(self):
        super().show()
        print('Value field: ', self.value)
print('Object A')
print()
A = Alpha(100)
A.show()
print()
print('Object B')
print()
B = Bravo(200,"B")
print('B.show() executed')
B.show()
print('Object C')
print('')
C = Charlie(300,'C',[1,2,3])
print()
C.show()
