def new_sum(*a):
    result = []
    max_v = max(a)
    min_v = min(a)
    avg_v = sum(a) / len(a)
    result = [max_v,min_v,avg_v]
    return result

result = new_sum(10, 20, 30, 40, 50)
print(result)  # Вывод: [30.0, 50, 10]


