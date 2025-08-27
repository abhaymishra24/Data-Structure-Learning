
# here we solve to find dublicate number in given list - 
# Approach - Floyd's Tortoise and Hare (Cycle Detection)
# Two pointers (slow and fast) are used to detect a cycle in the array.
# Once a cycle is detected, we find the entry point of the cycle, which is the duplicate number.
# Time Complexity: O(n)
# Space Complexity: O(1)


def find_dublicate(num):                    
    
    # intialize both pointers to the start of the array
    slow = num[0]                          
    fast = num[0]
    
    # Move slow pointer by one step and fast pointer by two steps
    # Continue until they meet inside the cycle
    
    while True:
        slow = num[slow]
        fast = num[num[fast]]
        
        # When both pointers meet, a cycle is detected
        # Break the loop
        # This meeting point is guaranteed due to the presence of a duplicate number
        
        if slow == fast:
            break
        
    # To find the entry point of the cycle (duplicate number)
    # Reset one pointer to the start of the array
    
    slow = num[0]
    
    # Move both pointers one step at a time until they meet again
    # The meeting point is the duplicate number
    while slow != fast:
        slow = num[slow]
        fast = num[fast]
    # Return the duplicate number
    return slow


num = [1, 3, 4, 2, 2]
res = find_dublicate(num)
print(res)

# solve this problem again -

def find_dublicate(num):
    
    slow = num[0]
    fast = num[0]
    
    while True:
        slow = num[slow]
        fast = num[num[fast]]
        
        if slow == fast:
            break
        
    slow = num[0]
    
    while slow != fast:
        slow = num[slow]
        fast = num[fast]
        
    return slow


num = [3,1,3,4,2]
res = find_dublicate(num)
print(res)


# solve this problem again -

write code here for find dublicate number in given list - 

def find_dub(arr):
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break

    slow = arr[0]

    while slow != fast:

        slow = arr[slow]
        fast = arr[fast]

    return slow

arr = [3,3,3,3,3]
result = find_dub(arr)
print(result)