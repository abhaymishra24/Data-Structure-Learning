
# here we solve leed code (Easy) problem - 

# Question -  Given an integer array nums, return the number of subarrays of length 3 such that the sum of
# the first and third numbers equals exactly half of the second number.

# here solution is - 

class Solution(object):
    def countSubarrays(self, nums):
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
        return ans
    
s = Solution()
nums = [1, 2, 3, 4, 5]
print(s.countSubarrays(nums))   


# 2962 leetcode problem (Medium) - 

# Question: You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.

class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        max_count = 0

        for i in range(n):
            max_elem = nums[i]
            count = 0
            for j in range(i, n):
                if nums[j] == max_elem:
                    count += 1
                elif nums[j] > max_elem:
                    max_elem = nums[j]
                    count = 1
                if count >= k:
                    max_count += 1

        return max_count

# Example usage:
s = Solution()
nums = [1, 3, 2, 3, 3]
k = 2
print(s.countSubarrays(nums, k))   