
# here we solve to find dublicate number in given list - 
# Approach - Floyd's Tortoise and Hare (Cycle Detection)
# Two pointers (slow and fast) are used to detect a cycle in the array.
# Once a cycle is detected, we find the entry point of the cycle, which is the duplicate number.
# Time Complexity: O(n)
# Space Complexity: O(1)


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
