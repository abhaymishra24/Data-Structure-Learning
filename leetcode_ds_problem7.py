
def movezero(nums):
    
    last_zero = 0
    
    for i in range(len(nums)):
        
        if nums[i] != 0:
            nums[last_zero] = nums[i]
            last_zero += 1
            
    for i in range(last_zero, len(nums)):
        nums[i] = 0
        
    return nums

nums = [0,1,0,3,12]
r = movezero(nums)
print(r)