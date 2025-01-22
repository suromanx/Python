def fun(*txt):
    def inner_fun():
        answer = ''
        for i in range(0,len(txt),2):
            answer += txt[i]
        return answer
    return inner_fun


my_text = 'апролддлорпа'

result = fun(my_text)
print(result())