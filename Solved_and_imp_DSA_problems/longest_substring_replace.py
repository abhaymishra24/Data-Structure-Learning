
# This function finds the length of the longest substring that can be obtained
# by replacing at most k characters in the given string s.

# Time Complexity: O(n)
# Space Complexity: O(1) - since the character set is limited (e.g., uppercase English letters)

# I used the sliding window technique to solve this problem.
# The idea is to maintain a window that can contain at most k characters that need to be replaced
# to make all characters in the window the same. We keep track of the frequency of each character
# in the current window and the count of the most frequent character. If the number of characters
# that need to be replaced (i.e., window size - count of most frequent character) exceeds k,
# we shrink the window from the left until it is valid again. We also keep track of the maximum
# window size encountered during the process.

def n_char(s,k):

    f = {}
    left = 0
    max_c = 0
    max_l = 0

    for right in range(len(s)):

        char = s[right]
        f[char] = f.get(char, 0)+1

        max_c = max(max_c, f[char])

        while (right - left+1) - max_c > k:

            f[s[left]] -= 1
            left += 1

        max_l = max(max_l, right - left + 1)

    return max_l

ch = "AABABBA"
k = 2
print(n_char(ch, k))


