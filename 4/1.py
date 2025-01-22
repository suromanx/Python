from random import *
nums = set()

while len(nums) < 5:
    nums.add(randint(1,10))
while len(nums) < 15:
    nums.add(randint(10, 30))

result = list(nums)
print(result)
