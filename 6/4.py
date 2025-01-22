def my_fun(text,*numbers):
    result_text = ''
    for num in numbers:
        result_text += text[num]
    return result_text

text = 'ФБВГДЕ'
numbers = [1,2,4,5]

answer = my_fun(text,*numbers)
print(answer)