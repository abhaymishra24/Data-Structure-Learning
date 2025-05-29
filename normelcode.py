
# here we solve normel code -

# find out second largest number using sorting array

def second_largest_sorting(numbers):
    numbers.sort(reverse=True)
    return numbers[1]

numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]
second_largest = second_largest_sorting(numbers)
print("Second largest number:", second_largest)

# same question solve with comments - 

def second_largest_sorting(numbers):
    # Sort the list of numbers in descending order (largest to smallest)
    numbers.sort(reverse=True)
    
    # Return the second element in the sorted list, which is the second largest number
    return numbers[1]

# Example list of numbers
numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]

# Call the function to find the second largest number
second_largest = second_largest_sorting(numbers)

# Print the result
print("Second largest number:", second_largest)


# Contains Dublicates II -

def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False

# Same code with comments - 

def containsNearbyDuplicate(self, nums, k):
    # Create an empty dictionary to store the last index of each number
    dic = {}
    
    # Iterate over the list 'nums' with both index 'i' and value 'v'
    for i, v in enumerate(nums):
        # Check if the number 'v' is already in the dictionary
        # and whether the difference between the current index 'i'
        # and the last recorded index of 'v' is less than or equal to 'k'
        if v in dic and i - dic[v] <= k:
            # If both conditions are true, we found a duplicate
            # within the specified range, so return True
            return True
        
        # Update the dictionary with the current index of the number 'v'
        dic[v] = i
    
    # If no such duplicates were found within the range, return False
    return False