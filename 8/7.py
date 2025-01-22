from itertools import zip_longest

class MyClass:
    def __init__(self,numbers):
        self.numbers = numbers

def my_fun(value_1,value_2):
    new_list = [a+b for a,b in zip_longest(value_1.numbers,value_2.numbers,fillvalue=0 )]
    return MyClass(new_list)

obj_1 = MyClass([1,2,3,4])

obj_2 = MyClass([5,6])

result = my_fun(obj_1,obj_2)

print(result.numbers)

