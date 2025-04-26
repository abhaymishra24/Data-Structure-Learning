from collections import defaultdict, deque

# from collections import Counter

# def mostCommonResponse(responses):
#     # Flatten the responses after removing duplicates within each day's responses
#     all_responses = []
#     for daily_responses in responses:
#         all_responses.extend(set(daily_responses))
    
#     # Count the occurrences of each response
#     response_count = Counter(all_responses)
    
#     # Find the most common response
#     max_count = max(response_count.values())
#     most_common = [response for response, count in response_count.items() if count == max_count]
    
#     # Return the lexicographically smallest response in case of a tie
#     return min(most_common)

# # Example usage
# responses = [
#     ["apple", "banana", "apple"],
#     ["banana", "orange", "banana"],
#     ["apple", "orange", "orange"]
# ]
# print(mostCommonResponse(responses))  # Output: "banana"


def baseUnitConversion(n, conversions):
    MOD = 10**9 + 7
    graph = defaultdict(list)
    
    # Build the graph
    for source, target, factor in conversions:
        graph[source].append((target, factor))
        graph[target].append((source, 1.0 / factor))
    
    # BFS to calculate conversion factors relative to unit 0
    base_conversion = [-1.0] * n
    base_conversion[0] = 1
    queue = deque([0])
    
    while queue:
        current = queue.popleft()
        for neighbor, factor in graph[current]:
            if base_conversion[neighbor] == -1:
                base_conversion[neighbor] = (base_conversion[current] * factor) % MOD
                queue.append(neighbor)
    
    return base_conversion

# Example usage
n = 4
conversions = [
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 4]
]
print(baseUnitConversion(n, conversions))  # Example output