def fun(n):
    for i in range(1,n+1):
        num = 2 ** i
        yield num

n = 5
for i in fun(n):
    print(i)