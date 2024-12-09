
# here we solve normel code -

def second_largest_sorting(numbers):
    numbers.sort(reverse=True)
    return numbers[1]

numbers = [12, 45, 2, 41, 31, 10, 45, 65, 78]
second_largest = second_largest_sorting(numbers)
print("Second largest number:", second_largest)
