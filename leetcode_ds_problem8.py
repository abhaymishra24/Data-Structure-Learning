
# find out minimum length of string after operation - 

# Approach 1: Using Hash Map

class Solution(object):
    def minimumLength(self, s):
        
        # Step 1: Count the frequency of each character in the string
        char_frequency_map = Counter(s)

        # Step 2: Calculate the number of characters to delete
        delete_count = 0
        for frequency in char_frequency_map.values():
            if frequency % 2 == 1:
                # If frequency is odd, delete all except one
                delete_count += frequency - 1
            else:
                # If frequency is even, delete all except two
                delete_count += frequency - 2

        # Step 3: Return the minimum length after deletions
        return len(s) - delete_count
        

# Approach 1: Using Hash Map

def minimumLength(self, s: str) -> int:
        arr = [0] * 26
        
        # Counting the char
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        # Applying the rules
        for i in range(26):
            while arr[i] >= 3:
                arr[i] -= 2
        
        # Counting the length of final string
        length = sum(arr)
        
        return length