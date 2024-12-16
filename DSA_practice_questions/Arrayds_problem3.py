
# Remove Duplicates from Sorted Array -

def removedubli(arr, num):
    
    n = 2
    
    for i in range(n-2, len(num)):
        if num[i] != num[n-2]:
            num[n] = num[i]
            n += 1
            
    return n

arr = [4,5,6,7,7,8,9]
num = len(arr)
print(removedubli(arr, num))