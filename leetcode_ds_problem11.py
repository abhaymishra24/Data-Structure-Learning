
# here we solve leed code (Easy) problem - 

# Given an integer array nums, return the number of subarrays of length 3 such that the sum of
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
print(s.countSubarrays(nums))  # Output: 0
