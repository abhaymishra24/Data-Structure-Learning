
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

# Explanation:
# This code uses a regular expression to find all five-letter words in the text. Let's break down the pattern r'\b\w{5}\b':
# - \b represents a word boundary
# - \w represents any word character (letter, digit, or underscore)
# - {5} specifies exactly 5 occurrences of the previous pattern (\w)
# The re.findall() function returns all non-overlapping matches of the pattern in the string. In this text, there are three five-letter words: 'quick', 'brown', and 'jumps'. Therefore, len(matches) returns 3.

