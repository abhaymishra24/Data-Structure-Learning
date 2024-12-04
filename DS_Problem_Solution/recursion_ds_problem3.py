
# here we solve longest substring - 


def longestUniqueSubstr(s):
    n = len(s)
    res = 0

    for i in range(n):

        # Initializing all characters as not visited
        visited = [False] * 256

        for j in range(i, n):

            # If current character is visited
            # Break the loop
            if visited[ord(s[j])] == True:
                break

            # Else update the result if this window is larger,
            # and mark current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(s[j])] = True

    return res

if __name__ == "__main__":
    s = "geeksforgeeks"
    print(longestUniqueSubstr(s))

# Here we try once again this code by itself -

def longss(s):
    n=len(s)
    res = 0

    for i in range(n):

        visited=[False]*256

        for j in range(i,n):

            if visited[(ord(s[j]))]==True:
                break

            else: 
                res= max(res, j-i+1)
                visited[(ord(s[j]))]= True

    return res

if __name__== "__main__":
    s= "geeksforgeeks"   
    print(longss(s)) 


# agaian write code - 

def lncc(s):
    n=len(s)
    res = 0

    for i in range(n):

        visited = [False]* 256

        for j in range(i,n):

            if visited[(ord(s[j]))]==True:
                break
            else:
                res=max(res,j-i+1)
                visited[(ord(s[j]))]=True

    return res

if __name__=="__main__":
    s="geeksforgeeks"
    print(lncc(s))


# here we solve again this question - 

def longst(s):
    
    n = len(s)
    res = 0
    
    for i in range(n):
        visited = [False] * 265
        
        for j in range(i,n):
            if visited[(ord(s[j]))] == True:
                break
            else:
                res = max(res,j-i+1)
                visited[(ord(s[j]))] = True
                
    return res

if __name__== "__main__":
    s = "hellomy"
    print(longst(s))
    
# here solve once again this problem - 

def lt(s):
    n = len(s)
    res = 0
    
    for i in range(n):
        v = [False] * 265
        
        for j in range(i,n):
            if v[(ord(s[j]))] == True:
                break
            else:
                res = max(res, j-i+1)
                v[((ord(s[j])))] = True
                
    return res

s = "abcabcbb"
print(lt(s))

# here we solve again this question -

# def longeststring()


                 