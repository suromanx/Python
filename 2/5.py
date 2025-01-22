x = 10
y = [1,2,3]
c= 0
for i in range(1,x+1):
    if i in y:
        continue
    else:
        c += i
print(c)