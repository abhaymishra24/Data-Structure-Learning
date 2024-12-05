
# Here we solve two sum of given number - 

def sum(a,b):

    print(a+b)

sum(5,6)

def sum(nums, target):
    
    n=len(nums)

    for i in range(n-1):

        for j in range(i+1, n):

            if nums[i] + nums[j] == target:
                return [i,j]
             
    return[] 

nums=[4,6,7,8]
target=10
result=(sum(nums,target))
print(result)   

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
            print(f"first accurnce:{first}, last accurnce:{last}")
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
            print("first acuurnce:{first}, last acuurance:{last}")
        else:
            print("not found")
            

        