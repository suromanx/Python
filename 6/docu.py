def show(txt):
    'Это функция show() с одним аргументом'
    print(txt)
print(show.__doc__)
def display(a,b):
    'Это функция дисплей с 2 аргументами'
    print([1],a)
    print([2], b)
def hello():
    print('Hi there')



f = show


def show(txt:"Text" = 'Show Func()') -> 'No Result':
    print(txt)
show()
print(show.__annotations__)
print()
for k in show.__annotations__:
    print(k,'-', show.__annotations__[k])