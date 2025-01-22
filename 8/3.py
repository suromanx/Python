class MyClass:
    def __init__(self,list1):
        if not isinstance(list1,list):
            raise ValueError('Аргумент должен быть списком')
        self.A = [item for item in list1 if isinstance(item, (int, float))]
    def show_list(self):
        self.new_list = []
        for s in self.A:
            if isinstance(s,(int,float)):
                self.new_list.append(s)
        print(f'Создан новый список', self.new_list)

    def show(self):
        if hasattr(self,'new_list') and self.new_list:
            print(f'List of numbers : {self.new_list}')
        else:
            print(f'List is empty or hasnt been created' )


    def average(self):
        if not hasattr(self, 'new_list') or not self.new_list:
            print("Невозможно вычислить среднее значение: список пуст или не создан.")
            return
        sum1 = sum(self.new_list)
        length = len(self.new_list)
        average = sum1 / length
        print(f'Длина списка равна {length}, среднее значение равно {average}')

obj = MyClass([2342, "abc", 4.5, 100, None])
obj.show_list()  # Создан новый список: [2342, 4.5, 100]
obj.show()       # Список чисел: [2342, 4.5, 100]
obj.average()    # Длина списка: 3, Среднее значение: 7