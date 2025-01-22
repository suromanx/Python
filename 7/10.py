def main():

    name_1 = 'a.txt'
    text_1 = 'Новый текст после извменения '
    text_1_upper = text_1.upper()
    with open(name_1, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            print('Что было до: ',line)
    try:
        with open(name_1,'w',encoding= 'utf-8') as file:
            file.write(text_1_upper)
        with open(name_1, 'r', encoding='utf-8') as file:
            content = file.readlines()
            for line in content:
                print('Что стало после: ',line,end='')
    except FileNotFoundError:
        print(f'Error file {name_1} does not exist')
    except Exception as e:
        print(f'Error occured {e}')
if __name__ == "__main__":
    main()