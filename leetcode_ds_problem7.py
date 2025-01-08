

def movezero(nums):
    
    n = len(nums)
    
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                print(nums[i])
            else:
                print(nums[j])
                
    return nums

nums = [0,1,0,3,12]
movezero(nums)