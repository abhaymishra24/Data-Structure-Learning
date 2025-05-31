
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

# Example usage
if __name__ == "__main__":
    input_string = "Hello world hello"
    result = count_each_string(input_string)
    print(result)  # Output: {'hello': 2, 'world': 1}
    
