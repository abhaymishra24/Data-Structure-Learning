
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
    
# Find the Index of the First Occurrence in a String 

def find_first_occurrence(haystack: str, needle: str) -> int:
    # If needle is an empty string, return 0
    if needle == "":
        return 0
    
    # Length of the haystack and needle strings
    haystack_length = len(haystack)
    needle_length = len(needle)
    
    # Iterate through the haystack to find the needle
    for start in range(haystack_length - needle_length + 1):
        # Check if the substring matches the needle
        if haystack[start:start + needle_length] == needle:
            return start  # Return the starting index
    
    return -1  # Return -1 if needle is not found

# Example usage
haystack = "Hello, welcome to my world."
needle = "welcome"
index = find_first_occurrence(haystack, needle)
print(f"The index of '{needle}' is: {index}")

# same code without comment - 

def find_first_occurrence(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
 
    haystack_length = len(haystack)
    needle_length = len(needle)

    for start in range(haystack_length - needle_length + 1):
        
        if haystack[start:start + needle_length] == needle:
            return start  
    
    return -1   

haystack = "Hello, welcome to my world."
needle = "welcome"
index = find_first_occurrence(haystack, needle)
print(f"The index of '{needle}' is: {index}")