def my_fun(my_list, my_doc):
    var_value = [val for val in my_list if isinstance(val, int) and val > 0]
    var_txt = [val for val in my_list if isinstance(val, str)]

    MyNewClass = type(my_doc,(object,),{})
    obj = MyNewClass()

    for name,value in zip(var_txt,var_value):
        setattr(obj,name,value)
    return obj

my_class = 'NameOfMyClass'
my_values = [10, 'name', 20, 'age', 39, 'height']

answer = my_fun(my_values, my_class)

print(answer.name)
