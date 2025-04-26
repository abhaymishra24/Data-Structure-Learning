
## his is the question of leetcode - 

# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

# this is answer - 
class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(len(nums) - 1):
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False  # If they have the same parity, return False
        return True
 
 
#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

#There may be duplicates in the original array.

#Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.   

class Solution(object):
    def check(self, nums):
        count, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
                if count > 1: return False
        return True
    