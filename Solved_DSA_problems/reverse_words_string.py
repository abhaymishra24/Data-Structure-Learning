
def reverse_string(s):
    return s[::-1]

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)

# Using a Loop (Manual Reversal)

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example
print(reverse_string("Hello"))

