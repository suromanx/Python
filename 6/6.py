def my_fun(f,n):
    def value_acc():
        value = 0
        for i in range(n):
            value += f()
        return value
    return value_acc

def fun():
    return 5

my_result = my_fun(fun,6)

print(my_result())


