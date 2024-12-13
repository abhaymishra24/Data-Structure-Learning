
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
        
arr = [4,5,6,7,8,8,9,3]
t = len(arr)
n = 8
accur(arr, t, n)
            
# here solve again this question - 

