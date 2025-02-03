class Alpha:
    def __init__(self):
        self.list_1 = [2,3,4,5]

    def __add__(self,other):
        if isinstance(other,Alpha):
            new_list = self.list_1 + other.list_1
            new_obj = Alpha()
            new_obj.list_1 = new_list
            return new_obj
        else:
            raise TypeError('error')


    def __str__(self):
        return str(self.list_1)
if __name__ == '__main__':
    obj1 = Alpha()
    obj2 = Alpha()

    result = obj1+obj2

    print(result)

