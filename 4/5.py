eneven = [k for k in range(1,16) if k % 2 != 0]
my_set = set()
for i in range(len(eneven)-1):
    a,b = eneven[i],eneven[i+1]
    my_set.add((a,b))
print(eneven)
print()
print(my_set)