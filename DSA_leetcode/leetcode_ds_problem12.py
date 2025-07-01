
# LeetCode Problem 1295: Find Numbers with Even Number of Digits:
# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

s = Solution()
nums = [34, 444, 22, 890, 11, 2]
print(s.findNumbers(nums))  # Output: 2 (12 and 7896 have an even number of digits) 


class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

s = Solution()
nums = [34, 444, 22, 890, 11, 2]
print(s.findNumbers(nums))


# LeetCode Problem: Build Array from Permutation
class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]

s = Solution()
nums = [0, 2, 1, 5, 3, 4]
print(s.buildArray(nums))  # Output: [0, 1, 2, 4, 5, 3]