
# LeetCode Problem 1295: Find Numbers with Even Number of Digits:
# Given an array nums of integers, return how many of them contain an even number of digits.


def findNumbers(nums):
        n = len(nums)
        count = 0
        for n in nums:

            if len(str(abs(n))) % 2 == 0:
                count += 1

        return count

