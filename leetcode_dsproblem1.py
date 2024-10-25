
#  Here solution of Python based on List two sum-

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
    
# Here solution of Python based on Array tow sum-
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [] 
