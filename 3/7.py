my_list = [1,4,5,2,5,5,10]
def d (my_list):
    max_value = max(my_list)
    max_index = my_list.index(max_value)
    answer = [max_value,max_index]
    return answer


x = d(my_list)
print(x)
