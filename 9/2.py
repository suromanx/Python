class Alpha:
    def __init__(self,int,text,float):
        self.int = int
        self.text = text
        self.float = float

    def __str__(self):
        print(self.text)

    def __float__(self):
        print(self.float)
    def __int__(self):
        print(self.int)

    def __bool__(self):
        print(bool(self.int))


if __name__ == '__main__':
    obj = Alpha(10,'hello',3.14)

    print(obj.int)
    print(obj.float)
    print(obj.__bool__())
    print(obj.text)