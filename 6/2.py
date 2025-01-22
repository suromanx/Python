def my_sum(list):
    newest_list = [k for k in list if k % 2 != 0]
    return newest_list


list = [2, 3, 4, 6, 6, 3, 5, 7]

result = my_sum(list)
print(result)
