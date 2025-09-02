
# This function finds the length of the longest substring that can be obtained
# by replacing at most k characters in the given string s.

# Time Complexity: O(n)
# Space Complexity: O(1) - since the character set is limited (e.g., uppercase English letters)


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


