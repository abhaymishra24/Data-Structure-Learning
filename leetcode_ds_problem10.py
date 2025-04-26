from collections import Counter

def mostCommonResponse(responses):
    # Flatten the responses after removing duplicates within each day's responses
    all_responses = []
    for daily_responses in responses:
        all_responses.extend(set(daily_responses))
    
    # Count the occurrences of each response
    response_count = Counter(all_responses)
    
    # Find the most common response
    max_count = max(response_count.values())
    most_common = [response for response, count in response_count.items() if count == max_count]
    
    # Return the lexicographically smallest response in case of a tie
    return min(most_common)

# Example usage
responses = [
    ["apple", "banana", "apple"],
    ["banana", "orange", "banana"],
    ["apple", "orange", "orange"]
]
print(mostCommonResponse(responses))  # Output: "banana"