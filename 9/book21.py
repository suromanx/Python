class MyClass:
    def __init__(self,*vals):
        L = []
        for v in vals:
            if type(v) == int:
                if v<10 and v>0:
                    L.append(v)
        self.digits = L
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]

        else:
            raise StopIteration

A = MyClass(2,"A",12,7,-3,"Hello",9,5,"Alpha")

try:
    while True:
        print(next(A),end=' ')

except StopIteration:
    print()


B=MyClass(5,"B",1.2,11,-1,"Hi",8,4,"Bravo",3)

for s in B:
    print(s,end=' ')
print()