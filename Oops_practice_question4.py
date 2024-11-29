
# Solve oops problems - 

# here print two sum of product -

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

# here print thee sum of product -

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
sum = 20
thsum(num, sum)

# here print four sum of product -

def fsum(num, tar):
    
    n = len(num)
    
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if num[i]+num[j]+num[k]+num[l] == tar:
                        print(f"four sum is:{num[i]},{num[j]},{num[k]},{num[l]} number of tar")
                        return True
    
    return False

num = [4,5,6,7,8,9,3,2,9]
tar = 25
fsum(num, tar)

                        
                     