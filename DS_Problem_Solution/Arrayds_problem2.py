
# Problem number 1 - Array method 

# Data Structure problem in Array 

from array import * 

a1=array ('i', [23,24,12])

# for loop 

for i in a1:
    print(i)

for i in range (3):
    print(a1[i], end=" ")

# while loop

i=0

while i<len(a1):
    print(a1[i])
    i+=1

# here I solve DS array problem 

# Question is two sum of number -

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found 
    