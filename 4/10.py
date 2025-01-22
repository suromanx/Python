dict_1= {'a':1,'b':2,'c':3}
dict_2= {'b':3,'c':4,'d':5}

my_intersections = set(dict_1.keys()).intersection(set(dict_2.keys()))
new_dict = {}
for key in my_intersections:
    new_dict[key] = dict_1[key],dict_2[key]
print(new_dict)