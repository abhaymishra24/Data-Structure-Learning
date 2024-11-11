
# Here we solve two sum of given number - 

def sum(a,b):

    print(a+b)

sum(5,6)

def sum(nums, target):
    
    n=len(nums)

    for i in range(n-1):

        for j in range(i+1, n):

            if nums[i] + nums[j] == target:
                return [i,j]
             
    return[] 

nums=[4,6,7,8]
target=10
result=(sum(nums,target))
print(result)   