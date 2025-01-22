my_text = ('раз два три четыре')
answer_dict = {}
for key in my_text:
    if key not in answer_dict:
        modified_text = my_text.replace(key, '')
        answer_dict[key] = modified_text

for key,value in answer_dict.items():
    print(f'{key}:{value}')
