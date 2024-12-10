

# here we solve second largest value - 

# with the help of (sorting value)

def second_largest_sort(lst):
    lst.sort()  # Sort the list in ascending order
    return lst[-2]  # Return the second last element

# Input from user
li = []
n = int(input("Enter size of list: "))
for i in range(n):
    e = int(input("Enter element of list: "))
    li.append(e)

print("Second largest in", li, "is", second_largest_sort(li))

# here we solve same question with diffenet method - 

# solve this question with the (Removing the Maximum Element)

def second_largest_remove_max(lst):
    max_value = max(lst)  # Find the maximum value
    lst.remove(max_value)  # Remove it from the list
    return max(lst)  # Return the new maximum, which is the second largest

# Input from user
li = []
n = int(input("Enter size of list: "))
for i in range(n):
    e = int(input("Enter element of list: "))
    li.append(e)

print("Second largest in", li, "is", second_largest_remove_max(li))


# Here solved without comment -

# with the help of (sorting value)

def second_largest_sort(lst):
    lst.sort()   
    return lst[-2]   

li = []
n = int(input("Enter size of list: "))
for i in range(n):
    e = int(input("Enter element of list: "))
    li.append(e)

print("Second largest in", li, "is", second_largest_sort(li))


# solve this question with the (Removing the Maximum Element)

def second_largest_remove_max(lst):
    max_value = max(lst)   
    lst.remove(max_value)  
    return max(lst)   
 
li = []
n = int(input("Enter size of list: "))
for i in range(n):
    e = int(input("Enter element of list: "))
    li.append(e)

print("Second largest in", li, "is", second_largest_remove_max(li))

# solve second largest number with the help of Hashmap - 

def second_largest(numbers):
    # Use a set to store unique numbers
    unique_numbers = set(numbers)

    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers

    # Convert the set back to a list and sort it
    sorted_numbers = sorted(unique_numbers)

    # Return the second largest number
    return sorted_numbers[-2]

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
result = second_largest(numbers)

if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("There are not enough unique numbers to determine the second largest.")


# same code without comments - 

def second_largest(numbers):
   
    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        return None   

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers[-2]

numbers = [12, 35, 1, 10, 34, 1]
result = second_largest(numbers)

if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("There are not enough unique numbers to determine the second largest.")
