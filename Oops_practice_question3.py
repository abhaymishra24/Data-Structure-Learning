
# First Question -

name = 'Bob'
age = 25
print('{0} is {1} years old and {0} likes Python.'.format(name, age))


# Second Question -

import re
text = 'The quick brown fox jumps over the lazy dog'
pattern = r'\b\w{5}\b'
matches = re.findall(pattern, text)
print(len(matches))