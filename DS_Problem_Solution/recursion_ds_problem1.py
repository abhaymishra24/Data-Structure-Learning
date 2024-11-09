
# Here we solve basic recursion question

# def fn(n):
#     if n>0:
#         fn(n-1)
#         print(n, end=' ')

# def fnreverse(n):
#     if n>0:
#         print(n, end=' ')
#         fnreverse(n-1)
         
# def fnodd(n):
#     if n>0:
#         fnodd(n-1)
#         print(2*n-1, end=' ')

# def fneven(n):
#     if n>0:
#         fneven(n-1)
#         print(2*n, end=' ')

# def fnoddr(n):
#     if n>0:
#         print(2*n-1, end=' ')
#         fnoddr(n-1)
        

# def fnevenr(n):
#     if n>0:
#         print(2*n, end=' ')
#         fnevenr(n-1)
              
# print("print the answer: ",fnevenr(10))

# # Here we solve some basic mathmetics question by recursion-

# def sumn(n):
#     if n==0:
#         return 0
#     return n + sumn(n-1)

# def sumodd(n):
#     if n==1:
#         return 1
#     return 2*n-1 + sumodd(n-1)

# def sumeven(n):
#     if n==0:
#         return 0
#     return 2*n + sumeven(n-1)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n-1)

# def factSq(n):
#     if n==1:
#         return 1
#     return n*n + factSq(n-1)

# print("print the answer = ",factSq(5))

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