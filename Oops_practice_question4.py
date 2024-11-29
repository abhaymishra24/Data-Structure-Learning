

def tsum(num, target):
     
    n = len(num)
    
    for i in range(n-1):
        for j in range(i+1, n-1):
            if num[i]+num[j] == target:
                 
                # print(num[i], num[j])
                # return True
    return []

# num = [5,6,3,2,4,5]
# target = 10
# tsum(num, target)