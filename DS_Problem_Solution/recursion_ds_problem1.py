
# Here we solve basic recursion question

def fn(n):
    if n>0:
        fn(n-1)
        print(n, end=' ')

def fnreverse(n):
    if n>0:
        print(n, end=' ')
        fnreverse(n-1)
         
def fnodd(n):
    if n>0:
        fnodd(n-1)
        print(2*n-1, end=' ')

def fneven(n):
    if n>0:
        fneven(n-1)
        print(2*n, end=' ')

def fnoddr(n):
    if n>0:
        print(2*n-1, end=' ')
        fnoddr(n-1)
        

def fnevenr(n):
    if n>0:
        print(2*n, end=' ')
        fnevenr(n-1)
              
fnevenr(10)


