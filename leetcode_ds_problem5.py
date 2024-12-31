
# Reverse words in string - 

class Solution(object):
    def reverseWords(self, s):
        s.strip()
        words = s.split()
        return " ".join(reversed(words))
  
  
# Find the Index of the First Occurrence in a String  (leetcode, easy)

class Solution(object):
    def strStr(self, haystack, needle):
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                return i
        # if we exit the loop, return -1        
        return -1

# same code without comment - 

class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    

# write code here for leet code - 

# find out minimum cost for ticket - 

def minimum_cost_ticket(self, days, costs):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    