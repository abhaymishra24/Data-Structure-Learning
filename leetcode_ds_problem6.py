
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