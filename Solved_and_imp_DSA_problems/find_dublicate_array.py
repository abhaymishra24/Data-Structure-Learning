
# here we solve to find dublicate in given list - 


def find_dublicate(num):
    
    slow = num[0]
    fast = num[0]
    
    while True:
        slow = num[slow]
        fast = num[num[fast]]
        
        if slow == fast:
            break
        
    slow = num[o]
    
    while slow != fast:
        slow = num[slow]
        fast = num[fast]
        
    return slow


num = [2,3,4,5,5,6,7]
res = find_dublicate(num)
    

