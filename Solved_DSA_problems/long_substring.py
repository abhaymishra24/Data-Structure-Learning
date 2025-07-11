
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

# same question solve with new method - 

def longest_unique_substring(s):
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(f"The length of the longest substring without repeating characters is: {longest_unique_substring(s)}")

# xplanation:
# char_map: A dictionary to store the last index of each character.

# max_length: Keeps track of the length of the longest substring found.

# start: The start index of the current substring.

# Steps:

# Iterate over each character in the string with the end pointer.

# If the character is already in the map and the start pointer is less than or equal to the character's index, update the start pointer.

# Update the last index of the character in the map.

# Calculate the current length of the substring and update max_length if it’s greater than the previous max_length.

# This approach ensures we traverse the string only once, making it efficient with a time complexity of O(n).

