class MyClass:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.next = None  # Ссылка на следующий узел

    def create_chain(self, num):
        head = MyClass(1)  # Создаем первый узел
        current = head  # Указываем на текущий узел

        for i in range(2, num + 1):
            current.next = MyClass(i)  # Создаем новый узел и связываем его с текущим
            current = current.next  # Перемещаемся на новый узел
        return head  # Возвращаем ссылку на первый узел

    def insert_val(self,value,head):
        new_code = MyClass(value)

        if head is None:
            new_code = head

        new_code.next = head
        return new_code

    def delete_val(self,head,value):

        if head is None:
            return None

        if head.value == value:
            return head.next

        current = head

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return head
            current = current.next

        print(f"Значение {value} не найдено в списке.")
        return head

    def __str__(self):
        return str(self.value)  # Определяем, как узел будет представлен в виде строки


# Пример использования
num = 5
obj = MyClass(num)

head = obj.create_chain(num)  # Создаем цепочку узлов

# Вывод значений узлов
print("Исходный список:")
result = head
while result is not None:
    print(result)  # Печатаем значение узла
    result = result.next  # Переходим к следующему узлу

# Вставка нового узла
value_to_insert = 0
head = obj.insert_val(value_to_insert, head)  # Вставляем значение в начало списка
print(f"\nСписок после вставки {value_to_insert}:")
result = head
while result is not None:
    print(result)  # Печатаем значение узла
    result = result.next  # Переходим к следующему узлу

# Удаление узла
value_to_delete = 3
head = obj.delete_val(head, value_to_delete)  # Удаляем узел со значением 3
print(f"\nСписок после удаления {value_to_delete}:")
result = head
while result is not None:
    print(result)  # Печатаем значение узла
    result = result.next  # Переходим к следующему узлу
