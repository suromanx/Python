class MyClass:
    def __init__(self, value):
        self.value = value
        self.next = None


def my_fun(num):
    if num <= 0:
        return None

    val_1 = MyClass(1)
    val_2 = val_1
    for i in range(2, num + 1):
        val_2.next = MyClass(i)
        val_2 = val_2.next
    return val_1


num = 5
result = my_fun(num)
while result is not None:
    print(result.value)
    result = result.next
