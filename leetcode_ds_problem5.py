
# Reverse words in string - 

class Solution(object):
    def reverseWords(self, s):
        s.strip()
        words = s.split()
        return " ".join(reversed(words))
  
  
# Find the Index of the First Occurrence in a String  (leetcode, easy)