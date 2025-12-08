
# return array from function in python - 

def array():
    
    arr = [2,3,4,1,2]
    return arr

res = array()
print(res)

# return array by user - 

def array_input():
    # Prompt the user to enter the number of elements in the array
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    
    # Loop to get each element from the user
    for i in range(n):
        num = int(input("Enter the element: "))
        arr.append(num)  # Add the entered element to the array
    
    return arr  # Return the populated array

res = array_input()  # Call the function and store the result
print(res)  # Print the resulting array


