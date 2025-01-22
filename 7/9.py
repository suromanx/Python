def main():

    name_1 = input('Введите имя файла (с расширением, например, file.txt): ')

    try:

        with open(name_1, 'r', encoding='utf-8') as mf:
            content = mf.readlines()

        print('File content')
        for line in content:
            print(line,end='')

        copy_name = f'copy_{name_1}'
        with open(copy_name,'w',encoding= 'utf-8') as copy_file:
            for index, line in enumerate(content, start=1):
                copy_file.write(f'{index}: {line}')
        print(f'\nКопия файла {name_1} created as {copy_name}.')
    except FileNotFoundError:
        print(f'Error file {name_1} does not exist')
    except Exception as e:
        print(f'Error occured {e}')
if __name__ == "__main__":
    main()