
# here we solve to find dublicate in given list - 


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

    

