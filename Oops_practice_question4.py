
# Solve oops problems - 

def tsum(num, target):
     
    n = len(num)
    
    for i in range(n-1):
        for j in range(i+1, n-1):
            if num[i]+num[j] == target: 
                print(num[i], num[j])
                return True
    return False

num = [5,6,3,2,4,5]
target = 10
tsum(num, target)


def thsum(num,sum):
         
        n = len(num)
        
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    if num[i] + num[j] + num[k] == sum:
                        print(num[i],num[j],num[k])
                        return True
        return False
    
num = [2,3,4,5,6,7,8,9,0]
sum = 10
thsum(num, sum)
