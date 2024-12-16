
# Remove Duplicates from Sorted Array -

# def removedubli(arr, num):
    
#     n = 2
    
#     for i in range(n-2, len(num)):
#         if num[i] != num[n-2]:
#             num[n] = num[i]
#             n += 1
            
#     return n

# arr = [4,5,6,7,7,8,9]
# num = len(arr)
# print(removedubli(arr, num))

# same code with correction - 

def removedubli(arr):
    if not arr:
        return arr  # Return an empty list if input is empty

    # Initialize a new list to hold unique elements
    unique_elements = []
    
    # Iterate through each element in arr
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)  # Add only unique elements

    return unique_elements

# Example usage
arr = [4, 5, 6, 7, 7, 8, 9]
result = removedubli(arr)
print(result)  # Output: [4, 5, 6, 7, 8, 9]
