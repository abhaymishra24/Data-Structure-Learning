
# Remove Duplicates from Sorted Array -

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

# same code without comments - 

def removedubli(arr):
    if not arr:
        return arr  
 
    unique_elements = []
    
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)   

    return unique_elements

arr = [4, 5, 6, 7, 7, 8, 9]
result = removedubli(arr)
print(result) 

# same code in set method without comment - 

def remove_duplicates_set(arr):
    return list(set(arr))

arr = [10, 20, 20, 30, 40, 40, 50]
result = remove_duplicates_set(arr)
print(result) 
