
# Function to find and print longest 
# substring without repeating characters.


def findLongestSubstring(string):
 
    n = len(string) 
 
    # starting point of current substring. 
    st = 0
 
    # maximum length substring without 
    # repeating characters. 
    maxlen = 0
 
    # starting index of maximum 
    # length substring. 
    start = 0
 
    # Hash Map to store last occurrence 
    # of each already visited character. 
    pos = {} 
 
    # Last occurrence of first
    # character is index 0 
    pos[string[0]] = 0
 
    for i in range(1, n): 
 
        # If this character is not present in hash, 
        # then this is first occurrence of this 
        # character, store this in hash. 
        if string[i] not in pos: 
            pos[string[i]] = i 
 
        else:
            # If this character is present in hash then 
            # this character has previous occurrence, 
            # check if that occurrence is before or after 
            # starting point of current substring. 
            if pos[string[i]] >= st: 
 
                # find length of current substring and 
                # update maxlen and start accordingly. 
                currlen = i - st 
                if maxlen < currlen: 
                    maxlen = currlen 
                    start = st 
 
                # Next substring will start after the last 
                # occurrence of current character to avoid 
                # its repetition. 
                st = pos[string[i]] + 1
             
            # Update last occurrence of 
            # current character. 
            pos[string[i]] = i 
         
    # Compare length of last substring with maxlen 
    # and update maxlen and start accordingly. 
    if maxlen < i - st: 
        maxlen = i - st 
        start = st 
     
    # The required longest substring without 
    # repeating characters is from string[start] 
    # to string[start+maxlen-1]. 
    return string[start : start + maxlen] 
 
# Driver Code
if __name__ == "__main__": 
 
    string = "GEEKSFORGEEKS"
    print(findLongestSubstring(string)) 
 

# here I write code the question without comment-

def findLongestSubstring(string):
 
    n = len(string)     
    st = 0
    maxlen = 0
    start = 0
 
    pos = {} 

    pos[string[0]] = 0
 
    for i in range(1, n): 
     
        if string[i] not in pos: 
            pos[string[i]] = i 
 
        else:
             
            if pos[string[i]] >= st: 
  
                currlen = i - st 
                if maxlen < currlen: 
                    maxlen = currlen 
                    start = st 
   
                st = pos[string[i]] + 1
             
            pos[string[i]] = i 
         
    if maxlen < i - st: 
        maxlen = i - st 
        start = st 
     
    return string[start : start + maxlen] 
 
if __name__ == "__main__": 
 
    string = "GEEKSFORGEEKS"
    print(findLongestSubstring(string)) 
    
    
# Here the different solution - 

def findLongestSubstring(s: str) -> str:
    char_index_map = {}
    start = 0
    max_length = 0
    longest_substring = ""

    for end in range(len(s)):
        if s[end] in char_index_map:
            # Move the start pointer to the right of the last occurrence of s[end]
            start = max(start, char_index_map[s[end]] + 1)

        # Update the last seen index of the character
        char_index_map[s[end]] = end
        
        # Calculate the length of the current substring
        current_length = end - start + 1
        
        # Update max_length and longest_substring if we found a longer one
        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:end + 1]

    return longest_substring

# Example usage:
input_string = "abcabcbb"
result = findLongestSubstring(input_string)
print(f"The longest substring without repeating characters is: '{result}'")

# sloved this question in both method - 

def longst():
    
 