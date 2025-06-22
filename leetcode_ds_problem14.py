
# def reverse_string():
    
#     s = ()
#     k = s.reversed()
#     print(k)  
 
# reverse_string()


def cal_num(a,b):
    
    sum = a+b
    print(sum)
    
cal_num(10, 40)

def cal_num2(m,n):
    
    return m-n

r =  cal_num2(33, 8)
print(r)
    
def cal_num3():
    
    n = int(input())
    return n*n
    
res = cal_num3()
print(res)


def len_str(s):
    
    return len(s)

s = len_str("Abhay Mishra")
print(s)


def len_list(elm):
    
    print(elm)
    
len_list([1,2,3,4,5,"Abay"])


def cal_fact(n):
    
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
cal_fact(6)

def converter(usd):
    
    inr = usd * 83
    print(usd, "USD = ", inr,"INR")
    
converter(20)

def convert(inr):
    
    usd = inr / 83
    print(inr, "INR = ", usd, "USD")
    
convert(1200)

