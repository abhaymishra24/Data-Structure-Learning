
# print count each and every string in a string - 

def count_each_string(s):
    words = s.split()  # Split the string into words
    count_dict = {}  # Dictionary to hold word counts

    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in count_dict:
            count_dict[word] += 1  # Increment count if word already exists
        else:
            count_dict[word] = 1  # Initialize count if word is new

    return count_dict