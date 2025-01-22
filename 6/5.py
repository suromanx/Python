def my_fun(func_1, num_1, num_2):
    value = func_1()
    if num_1 < 0 or num_2 >= len(value) or num_1 > num_2:
        raise ValueError("НЕверные данные чмо")

    result = value[num_1:num_2 + 1]
    max_result = max(result)
    return max_result


def func_1(*a):
    return list(a)


function = lambda: func_1(1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)

print(my_fun(function, 9, 9))
