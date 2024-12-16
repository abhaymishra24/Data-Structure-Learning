
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
# def removeDuplicates(arr, nums):
    
#     k = 2

#     for i in range(2, len(nums)):
#         if nums[i] != nums[k - 2]:
#             nums[k] = nums[i]
#             k += 1 

#     return k

# arr = [8,8,9,3,4,5]
# nums = len(arr)
# print(removeDuplicates(arr,nums))

# solve once again this problem - 

# def removedubli(arr, num):
    
#     n = 2
    
#     for i in range(2, len(num)):
#         if num[i] != num[n-2]:
#             num[n] = num[i]
#             n += 1
            
#     return n

# arr = [4,5,6,7,7,8,9]
# num = len(arr)
# print(removedubli(arr, num))
    
# here I solve a same problem with help of set - 

def remove_duplicates_set(arr):
    return list(set(arr))

# Example usage
arr = [10, 20, 20, 30, 40, 40, 50]
result = remove_duplicates_set(arr)
print(result)  # Output: [40, 10, 20, 30, 50] (order may vary)

