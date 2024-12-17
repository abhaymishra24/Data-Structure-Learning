
# first and last accurence sorted code - 

def findFirstAndLast(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n):
        if (x != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
 
    if (first != -1):
        print("First Occurrence = ", first,
              " \nLast Occurrence = ", last)
    else:
        print("Not Found")
 
 
# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)


# Here solve the code by myself-

def flacc(arr, x, n):
    first = -1
    last = -1

    for i in range(0, x):

        if(n != arr[i]):
            continue
        if (first == -1): 
            first = i
        last = i

    if (first != -1):
        
        print("first accurnce:",first, 
                " \nlast accurnce:",last)
    else:   
        print("not found")
        
arr = [1,2,3,4,4,4,6,6]
x=len(arr)
n=6
flacc(arr,x,n)

#  here solved again -

def acc(arr, a, n):
    first = -1
    last = -1
    
    for i in range(0, a):
        
        if (n != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
        
    if (first != -1): 
        print(f"first acuurnce:{first}, last acuurance:{last}")
    else: 
        print("not found")
            
arr = [9,4,5,7,3,4,2,2,5]
a = len(arr)
n = 2
acc(arr, a, n)   
    

# here we solve once again this question -

def accur(arr, t, n):
    
    f = -1
    l = -1
    
    for i in range(0, t):
        
        if (n != arr[i]):
            continue
        if (f == -1):
            f = i
        l = i
    
    if (f != -1):
        print((f), (l))
    else:
        print("not found")
        
arr = [4,5,6,7,8,4,9,3,8]
t = len(arr)
n = 8
accur(arr, t, n)
            
# here solve again this question - 

def acurrence(arr, number, tar):
    
    first = -1
    last = -1
    
    for i in range(0, number):
        if (number != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
        
    if (first != -1):
        print((first), (last))
    else:
        print("Not found")
        
arr = [5,6,7,8,9,0,0,3]
number = len(arr)
tar = 0
acurrence(arr, number, tar)

# Using list methods: You can use the index() method to find the first occurrence
# and a combination of len() and index() methods to find the last occurrence.

def first_and_last_occurrence(arr, target):
    first_occurrence = arr.index(target)
    last_occurrence = len(arr) - 1 - arr[::-1].index(target)
    return first_occurrence, last_occurrence

# Example usage:
arr = [1, 2, 3, 4, 2, 5, 6, 2, 7, 8]
target = 2
first, last = first_and_last_occurrence(arr, target)
print(f"First occurrence of {target} is at index {first}")
print(f"Last occurrence of {target} is at index {last}")

#Explanation:

# arr.index(target) returns the index of the first occurrence of target in the list arr.

# arr[::-1].index(target) reverses the list and then finds the index of the first occurrence of target in the reversed list.

# len(arr) - 1 - arr[::-1].index(target) calculates the index of the last occurrence of target in the original list.