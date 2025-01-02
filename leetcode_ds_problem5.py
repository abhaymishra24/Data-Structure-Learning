
# # Reverse words in string - 

# class Solution(object):
#     def reverseWords(self, s):
#         s.strip()
#         words = s.split()
#         return " ".join(reversed(words))
  
  
# # Find the Index of the First Occurrence in a String  (leetcode, easy)

# class Solution(object):
#     def strStr(self, haystack, needle):
#         # makes sure we don't iterate through a substring that is shorter than needle
#         for i in range(len(haystack) - len(needle) + 1):
#             # check if any substring of haystack with the same length as needle is equal to needle
#             if haystack[i : i+len(needle)] == needle:
#                 # if yes, we return the first index of that substring
#                 return i
#         # if we exit the loop, return -1        
#         return -1

# # same code without comment - 

# class Solution(object):
#     def strStr(self, haystack, needle):
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1
    

# write code here for leet code - 

def count_string_num(words, queris):
    
    w = len(words)
    q = len(queris)
    
    for i in range(w-1):
        for j in range(q-1):
            if words[i] == queris[j]:
                print(len(queris))
                return True
            
    return False

words = ["aba", "bcb", "ece", "aa", "e"]
queris = [[0,2],[1,4],[1,1]]
count_string_num(words, queris)
            


