
# here we solve leed code (Easy) problem - 

# Given an integer array nums, return the number of subarrays of length 3 such that the sum of
# the first and third numbers equals exactly half of the second number.

# here solution is - 

# class Solution(object):
#     def countSubarrays(self, nums):
#         n = len(nums)
#         ans = 0
#         for i in range(1, n - 1):
#             if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
#                 ans += 1
#         return ans
    
# s = Solution()
# nums = [1, 2, 3, 4, 5]
# print(s.countSubarrays(nums))  # Output: 0



def sum(n, t):
    
    k = len(n)
    
    for i in range(k-4):
        for j in range(i+1, k-3):
            for l in range(j+1, k-2):
                for m in range(l+1, k-1):
                    for p in range(m+1, k):
                        if n[i] + n[j] + n[l] + n[m] + [p] == t:
                            print(n[i], n[j], n[l], n[m], n[p])
                            return True
    
    return False

n = [3,4,5,6,7,8,9]
t = 25
sum = (n,t)
                