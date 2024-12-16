
# Remove Duplicates from Sorted Array - leetcode (easy) 

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        
        return k
    
# Remove Duplicates from Sorted Array II - leetcode (medium)

# class Solution:
def removeDuplicates(arr, nums):
    
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1 

    return k

arr = [8,8,9,3,4,5]
nums = len(arr)
print(removeDuplicates(arr,nums))

# solve once again this problem - 

def removedubli(arr, num):
    
    