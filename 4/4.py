my_set = set(k for k in range(1,51) if (k % 3 == 0)^(k % 4 == 0))
print(my_set)