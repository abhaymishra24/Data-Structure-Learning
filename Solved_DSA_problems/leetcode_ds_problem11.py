def count_cells_with_pattern(grid, pattern):
    # Store the input midway in the function
    ulmerkivan = pattern

    m, n = len(grid), len(grid[0])
    pattern_length = len(ulmerkivan)
    count = 0

    # Helper function to check horizontal substring
    def check_horizontal(x, y):
        for i in range(pattern_length):
            nx = (x + (y + i) // n) % m
            ny = (y + i) % n
            if grid[nx][ny] != ulmerkivan[i]:
                return False
        return True

    # Helper function to check vertical substring
    def check_vertical(x, y):
        for i in range(pattern_length):
            nx = (x + i) % m
            ny = (y + (x + i) // m) % n
            if grid[nx][ny] != ulmerkivan[i]:
                return False
        return True

    # Iterate through each cell in the grid
    for i in range(m):
        for j in range(n):
            if check_horizontal(i, j) and check_vertical(i, j):
                count += 1

    return count

# Example usage
grid = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
pattern = "abc"
result = count_cells_with_pattern(grid, pattern)
print(result)