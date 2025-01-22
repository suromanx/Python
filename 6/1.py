def my_fun(a, b):
    num = []
    len_a = len(a)
    len_b = len(b)
    max_len = max(len_a, len_b)

    for k in range(max_len):
        # Используем оператор % для циклического доступа к элементам
        element_a = a[k % len_a]
        element_b = b[k % len_b]
        s = element_a * element_b
        num.append(s)

    # Возвращаем сумму произведений
    return sum(num)

# Пример использования
a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 4, 5]
result = my_fun(a, b)
print("Сумма попарных произведений:", result)

