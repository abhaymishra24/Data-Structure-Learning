
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

# Using reversed() Function

def reverse_string(s):
    return ''.join(reversed(s))

# Example
print(reverse_string("Hello"))

# Using Recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Example
print(reverse_string("Hello"))

# Using Stack (List)        
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str 

# Example
print(reverse_string("Hello"))


# Using List Comprehension
def reverse_string(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])
# Example
print(reverse_string("Hello"))


# practice again -

