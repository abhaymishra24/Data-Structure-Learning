
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
    
    # Another example
    input_string2 = "This is a test. This test is simple."
    result2 = count_each_string(input_string2)
    print(result2)
    
# print count each and every string in list - 

def count_each_string_in_list(lst):
    count_dict = {}  # Dictionary to hold word counts

    for word in lst:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in count_dict:
            count_dict[word] += 1  # Increment count if word already exists
        else:
            count_dict[word] = 1  # Initialize count if word is new

    return count_dict

# Example usage
if __name__ == "__main__":
    input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result_list = count_each_string_in_list(input_list)
    print(result_list)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
    
    # Another example
    input_list2 = ["cat", "dog", "cat", "bird", "dog", "cat"]
    result_list2 = count_each_string_in_list(input_list2)
    print(result_list2)  # Output: {'cat': 3, 'dog': 2, 'bird': 1}
    
    
def count_each_string_in_list(lst):
    count_string = {}
    for string in lst:
        if string in count_string:
            count_string[string] += 1
        else:
            count_string[string] = 1
            
    return count_string

# Example usage
if __name__ == "__main__":
    input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result_list = count_each_string_in_list(input_list)
    print(result_list)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
    
    # Another example
    input_list2 = ["cat", "dog", "cat", "bird", "dog", "cat"]
    result_list2 = count_each_string_in_list(input_list2)
    print(result_list2)  # Output: {'cat': 3, 'dog': 2, 'bird': 1}
    