

# # solve with pointer - 

# def movezero(nums):
    
#     last_zero = 0
    
#     for i in range(len(nums)):
        
#         if nums[i] != 0:
#             nums[last_zero] = nums[i]
#             last_zero += 1
            
#     for i in range(last_zero, len(nums)):
#         nums[i] = 0
        
#     return nums

# nums = [0,1,0,3,12]
# r = movezero(nums)
# print(r)

# # same question with different method - 

# # Using List Comprehension
# # This method creates a new list with non-zero elements followed by the appropriate number of zeros.

# def movezero(nums):
#     # Create a new list with non-zero elements followed by zeros
#     non_zero_elements = [num for num in nums if num != 0]
#     zero_count = len(nums) - len(non_zero_elements)
    
#     # Extend the list with zeros
#     return non_zero_elements + [0] * zero_count

# # Example usage
# nums = [0, 1, 0, 3, 12]
# r = movezero(nums)
# print(r)  # Output: [1, 3, 12, 0, 0]

# solve leetcode question - 