

# Given an array arr[] of size n and an integer sum. Find if there’s a triplet in the array which sums up to the given integer sum.

# Function to find a triplet with a given sum in an array

def find3Numbers(arr, sum):
    n = len(arr)

    # Fix the first element as arr[i]
    for i in range(n - 2):

        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):

            # Now look for the third number
            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == sum:

                    # Triplet is found; print the triplet elements
                    print(f"Triplet is {arr[i]}, {arr[j]}, {arr[k]}")
                    return True

    # If no triplet is found, return false
    return False

# Driver code
arr = [1, 4, 45, 6, 10, 8]
sum = 22

find3Numbers(arr, sum)


# Here solve same question by me this triplet sum of array - 

def number3sum(arr, sum):                     # here first we define function and give two argument according question
    n = len(arr)                                 # here we find the length of arr

    for i in range (n-2):                        # here we put itteration for check first number of triplet
        
        for j in range (i+1, n-1):                 # here we put itteration for check second number of triplet

            for k in range (j+1, n):                 # here we put itteration for check third number of triplet

                if arr[i] + arr[j] + arr[k] == sum:    # here we give condition for check the sum of triple number equal to given value

                    print(f"triplet number:{arr[i]},{arr[j]},{arr[k]}")           # here print the number of triple number
                    return True
    
    return False

arr=[1, 4, 45, 6, 10, 8]                                    # give the number 
sum = 22                                                    # give the value of sum

number3sum(arr, sum)                                        # call the function for answer 

# Here solve once again this triplet problem - 

def triplet(arr, sum):
    n=len(arr)

    for i in range(n-2):

        for j in range(i+1,n-1):

            for k in range(j+1, n):

                if arr[i]+arr[j]+arr[k]==sum:

                    print(f"the number is:{arr[i]},{arr[j]},{arr[k]}")
                    return True
    
    return False

arr = [2,4,5,6,7,9,2]
sum=16
triplet(arr, sum)


# again solve - 

def tripletsum(arr, sum):
    
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[j] == sum:
                    print(f"print the number:{arr[i]},{arr[j]},{arr[k]}")
                    return True
                
    return False

arr = [8,9,4,5,6,6]
sum = 21
tripletsum(arr, sum)
    
# here we solve double sum product -

def Dsum(arr, sum):
    
    n = len(arr)
    
    for i in range(n-1):
        for j in range(i+1, n-1):
            if arr[i]+arr[j]==sum:
                print(f"the number is:{arr[i]},{arr[j]}")
                return True
            
    return False

arr = [8,9,2,3,6,2]
sum = 15
Dsum(arr, sum)

# again code triplet - 

def trips(arr, sum):
    
    m = len(arr)
    
    for i in range(m-2):
        for j in range(i+i, m-1):
            for k in range(j+1, m):
                if arr[i]+arr[j]+arr[k] == sum:
                    print(f"print:{arr[i]},{arr[j]},{arr[k]}")
                    return True
    return False

arr = [6,6,7,8,9,0,1,2]
sum = 17
trips(arr,sum)

# here solve once again double -

def Dsum(arr, sum):
    
    d = len(arr)
    
    for i in range(d-1):
        for j in range(i+1,d-1):
            if arr[i]+arr[j] == sum:
                print(f"Dsum number:{arr[i]},{arr[j]}")
                return True
    return False

arr = [6,7,3,2,4,5]
sum = 10
Dsum(arr, sum)

# one agian try this question -

def sut(num, t):
    
    n = len(num)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if num[i] + num [j] + num [k] == t:
                    print(f"number is here of t : {num[i]},{num[j]},{num[k]}. solve it.")
                    return True
    return False

num = [1,2,3,4,5,0,9,8,7]
t  = 17
sut(num,t)  

# here we solve this question once again - 

def sumtwonumber(num,pro):
    
    n = len(num)
    
    for i in range(n-1):
        for j in range(i,n):
            if num[i] + num[j] == pro:
                print(num[i],num[j])
                return True
    return False

num = [2,4,6,9,12,8]
pro = 14
sumtwonumber(num,pro)


# solve this question once again - 

def threenumber(arr, add):
    
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == add:
                    print(f"the number is of add:{arr[i]},{arr[j]},{arr[k]}.")
                    return True
                
    return False

arr = [2,3,4,5,6,7]
add = 12
threenumber(arr, add)


# here solve once again for two add number - 

def twonumber(a, ad):
    
    n = len(a)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] + a[j] == ad:
                print(f"number is for ad = {a[i]},{a[j]}.")
                return True
            
    return False

a = [3,4,5,6,7,8]
ad = 7
twonumber(a, ad)

# write this code once again - 

def add(num, tar):
    
    n = len(num)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if num[i] + num[j] + num[k] == tar:
                    print(f"the number is for tar here : {num[i]}, {num[j]}, {num[k]}. Thankyou:)")
                    return True
                
    return True

num = [3,4,5,6,7,8,9,8,7]
tar = 22
add(num, tar)


# here solve same question of three number sum product -

def tsum(number, goal):
    
    n = len(number)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == goal:
                    print(f"the number of goal is {number[i]},{number[j]},{number[k]}. thank you for reach the goal.")
                    return True
                
    return False

number = [9,8,9,9,3,2,4]
goal = 20
tsum(number, goal)

# solve this problem again - 

def addnum(number, tgt):
    
    n = len(number)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == tgt:
                    print(f"the number is - {number[i]} and {number[j]} and {number[k]}.")
                    return True
    
    return False

number = [3,4,5,6,7,8,9,0,2]
tgt = 15
addnum(number, tgt)

# solve again this problem with four number - 

def number(add, goal):
    
    n = len(add)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if add[i] + add[j] + add[k] + add[l] == goal:
                        print(f"The number for goal is - {add[i]} and {add[j]} and {add[k]} and {add[l]}.")
                        return True
                    
    return False

add = [3,4,5,6,7,8,9,8,2]
goal = 25
number(add, goal)

# solve this problem once again - 

def numb(ar, g):
    n = len(ar)
     
    for i in range(n-1):
        for j in range(i+1, n):
            if ar[i] + ar[j] == g:
                print(f"print the number is {ar[i]} and {ar[j]}.")
                return True
            
    return False

ar = [2,3,4,5,6]
g = 8
numb(ar, g)


# solve again 

def sum(a, t):
    
    l = len(a)
    
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if a[i] + a[j] + a[k] == t:
                    print(a[i], a[j], a[k])
                    return True
                
    return False

a = [2,3,4,5,6,7]
t = 10
sum(a, t)

# here solve again - 

def s(n, t):
    
    m = len(n)
    
    for i in range(m-2):
        for j in range(i+1, m-1):
            for k in range(j+1, m):
                if n[i] + n[j] + n[k] == t:
                    print(f"number is = {n[i]}, {n[j]}, {n[k]}.")
                    return True
    
    return False

n = [2,3,4,5,6,7,7]
t = 11
s(n, t)


# here solve once again - 

def sum(arr, target):
    
    n = len(arr)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        print(f"number of target is = {arr[i]},{arr[j]},{arr[k]},{arr[l]}.")
                        return True
                    
    return False

arr = [2,3,4,5,6,7,8,9]
target = 15
sum(arr, target)

# here solve once again - 

def sum(arr, taregt):
    
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == taregt:
                    print(f"the number - {arr[i]},{arr[j]},{arr[k]}.")
                    return True
                
    return False

arr = [2,3,4,5,6,7]
taregt = 12
sum(arr, taregt)

# write again same code -

def sum(arr, target):
    
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == taregt:
                    print(arr[i],arr[j], arr[k])
                    return True
                
    return False

arr = [3,4,5,6,7,8]
target = 12
sum(arr, target)

# solve once again - 

def sum(n, t):
    
    k = len(n)
    
    for i in range(k-4):
        for j in range(i+1, k-3):
            for l in range(j+1, k-2):
                for m in range(l+1, k-1):
                    for p in range(m+1, k):
                        if n[i] + n[j] + n[l] + n[m] + n[p] == t:
                            print(n[i], n[j], n[l], n[m], n[p])
                            return True
    
    return False

n = [3,4,5,6,7,8,9]
t = 25
sum(n,t)

# write once again this programm - 

def number(num, res):
    
    n = len(num)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if num[i] + num[j] + num[k] + num[l] == res:
                        print("number is of result: ", num[i], num[j], num[k], num[l])
                        return True
                    
    return False
num = [8, 5, 6, 7, 9 ,8,10]
res = 32
number(num, res)
  
# practice again -  


def nums_sum(num, r):
    
    n = len(num)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if num[i]+num[j]+num[k]+num[l] == r:
                        print(f"This is number of r:-{num[i]},{num[j]},{num[k]},{num[l]}.")
                        return True
                        
                        
    return False

num = [2,3,5,6,8,7,5,4,3]
r = 16
nums_sum(num,r)