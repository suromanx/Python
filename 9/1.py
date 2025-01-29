class Alpha:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def display(self):
        print(self.value)


class Bravo(Alpha):
    def __init__(self,value,new_value):
        super().__init__(value)
        self.a_value = new_value
    def set_a_value(self,new_value):
        self.a_value = new_value
    def display(self):
        super().display()
        print(self.a_value)

class Charlie(Bravo):
    def __init__(self,value,new_value,extra_value):
        super().__init__(value,new_value)
        self.extra_value = extra_value

    def set_extra_value(self,extra_value):
        self.extra_value = extra_value

    def display(self):
        super().display()
        print(self.extra_value)

if __name__ =='__main__':
    obj = Charlie(value=10,new_value='Hello', extra_value='world')

    obj.display()

    obj.set_value(20)
    obj.display()