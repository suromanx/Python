class ALpha:
    def __call__(self,n):
        s = 0
        for k in range(len(self.nums)):
            s+= self.nums[k]**n
        return s

class Bravo:
    def __call__(self,x,y):
        return self.num*x+self.val*y

A = ALpha()
A.nums = [1,2,3]
print(A(1))
print(A(2))

B =Bravo()
B.num = 2
B.val = 3

print(B(5,1))
print(B(3,4))