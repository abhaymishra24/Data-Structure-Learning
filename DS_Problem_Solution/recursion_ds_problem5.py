
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