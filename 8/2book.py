class Myclass:
    def set(self,n):
        self.number = n

    def show(self):
        print(self.number)

A = Myclass()
B = Myclass()

A.set(100)
B.set(200)

A.show()
B.show()

A.number = 123
B.number = 321

A.show()
B.show()
