
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

def second_largest_sort(lst):
    lst.sort()   
    return lst[-2]   


li = []
n = int(input("Enter size of list: "))
for i in range(n):
    e = int(input("Enter element of list: "))
    li.append(e)

print("Second largest in", li, "is", second_largest_sort(li))

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
