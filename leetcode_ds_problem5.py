
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

# count vowel num in range - ( Use prefix sum method Algo)

def count_string_num(words, queries):
    
        n = len(words)
        Prefix = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            Prefix[i + 1] = Prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                Prefix[i + 1] += 1

        ANS = []
        for query in queries:
            ANS.append(Prefix[query[1] + 1] - Prefix[query[0]])

        return ANS
    