class MyClass:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert_values(self,value):

        if value < self.value:
            if self.left is None:
                self.left = MyClass(value)
            else:
                self.left.insert_values(value)
        else:
            if self.right is None:
                self.right = MyClass(value)
            else:
                self.right.insert_values(value)

    def put_in_order(self):
        """Возвращает значения узлов в симметричном порядке (in-order)."""
        numerals = []
        if self.left:  # Если есть левый потомок, обходим его
            numerals += self.left.put_in_order()
        numerals.append(self.value)  # Добавляем значение текущего узла
        if self.right:  # Если есть правый потомок, обходим его
            numerals += self.right.put_in_order()
        return numerals



numerals = [3,4,2,4,5,3]
