

def movezero(nums):
    
    n = len(nums)
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[j] == 0:
                print(nums[i])
                continue
            if nums[i] == 0:
                print(nums[j])
                
    return nums

nums = [0,1,0,3,12]
movezero(nums)