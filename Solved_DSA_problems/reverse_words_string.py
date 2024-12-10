
# Reverse words in string - 

class Solution(object):
    def reverseWords(self, s):
        s.strip()
        words = s.split()
        return " ".join(reversed(words))

# Reverse words in string 

def reverse_words(input_string: str) -> str:
    # Split the input string into a list of words
    words = input_string.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list back into a string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Example usage
input_string = "Hello, welcome to my world."
reversed_string = reverse_words(input_string)
print(f"Original String: '{input_string}'")
print(f"Reversed Words String: '{reversed_string}'")

# same code without comment - 

def reverse_words(input_string: str) -> str:
     
    words = input_string.split()
    
    reversed_words = words[::-1]
    
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

input_string = "Hello, welcome to my world."
reversed_string = reverse_words(input_string)
print(f"Original String: '{input_string}'")
print(f"Reversed Words String: '{reversed_string}'")