
# Here we solve basic recursion question

# def fn(n):
#     if n>0:
#         fn(n-1)
#         print(n, end=' ')

# def fnreverse(n):
#     if n>0:
#         print(n, end=' ')
#         fnreverse(n-1)
         
# def fnodd(n):
#     if n>0:
#         fnodd(n-1)
#         print(2*n-1, end=' ')

# def fneven(n):
#     if n>0:
#         fneven(n-1)
#         print(2*n, end=' ')

# def fnoddr(n):
#     if n>0:
#         print(2*n-1, end=' ')
#         fnoddr(n-1)
        

# def fnevenr(n):
#     if n>0:
#         print(2*n, end=' ')
#         fnevenr(n-1)
              
# fnevenr(10)

# Here we solve some basic mathmetics question by recursion-

def sumn(n):
    if n==0:
        return 0
    return n + sumn(n-1)

def sumodd(n):
    if n==1:
        return 1
    return 2*n-1 + sumodd(n-1)

def sumeven(n):
    if n==0:
        return 0
    return 2*n + sumeven(n-1)

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

def factSq(n):
    if n==1:
        return 1
    return n*n + factSq(n-1)

print("print the answer = ",factSq(5))