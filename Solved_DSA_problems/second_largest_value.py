
# # here we solve second largest value - 

# # find out second largest number using sorting array

# def second_largest_sorting(numbers):
#     numbers.sort(reverse=True)
#     return numbers[1]

# numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]
# second_largest = second_largest_sorting(numbers)
# print("Second largest number:", second_largest)

# # same question solve with comments - 

# def second_largest_sorting(numbers):
#     # Sort the list of numbers in descending order (largest to smallest)
#     numbers.sort(reverse=True)
    
#     # Return the second element in the sorted list, which is the second largest number
#     return numbers[1]

# # Example list of numbers
# numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]

# # Call the function to find the second largest number
# second_largest = second_largest_sorting(numbers)

# # Print the result
# print("Second largest number:", second_largest)

# # solve once again - 

# def second_largest_sorting(numbers):
#     numbers.sort(reverse=True)
#     return numbers[1]

# numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]
# second_largest = second_largest_sorting(numbers)
# print("Second largest number:", second_largest)

# # solve again with same method - 

# def second_large_valu(num):
    
#     num.sort(reverse=True)
#     return num[1]

# num = [23,45,67,89]
# second_value = second_large_valu(num)
# print(f"the number is = {second_value}")

# # here solve once again - 

# def second_large(n):
    
#     num.sort(reverse=True)
#     return num[1]

# num = [2,3,4,5,6,7]
# second = second_large(num)
# print(second)

# # solve again tis one - 

# def sec_large(n):
    
#     n.sort(reverse=True)
#     return n[1]

# n = [3,4,5,8,9]
# value = sec_large(n)
# print(value)

# practice again - 

def sum_calculate(nums, target):
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        print(nums[i], nums[j], nums[k])
                        return True
                        
        return False

nums = [1,2,3,4,5,6,7]
target = 9
sum_calculate(nums, target)
