
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

