
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

def longeststring(a):
    
    n = len(a)
    res = 0
    
    for i in range(n):
        v = [False] * 256
        
        for j in range(i,n):
            if v [(ord(a[j]))] == True:
                break
            else:
                res = max(res,j-i+1)
                v[(ord(a[j]))] = True
                
    return res

a = "abhaybhiaabhay"
print(longeststring(a))          

# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/?envType=daily-question&envId=2024-12-10

class Solution(object):
    def maximumLength(self, s):

        if len(set(s))==len(s):
            return -1
        for i in range(len(s)-3,-1,-1):
            d = {}
            count = 0
            for j in range(i,len(s)):
                if len(set(s[count:j+1]))==1:
                    if s[count:j+1] not in d:
                        d[s[count:j+1]]=1
                    else:
                        d[s[count:j+1]]+=1
                        if d[s[count:j+1]]==3:
                            return len(s[count:j+1])
                count+=1
        return -1
          