
# Solution in normel Array and function

# Solution number 1 -

def four_sum(nums, target):
    nums.sort()  # Sort the array to facilitate the search for unique quadruplets
    n = len(nums)
    quadruplets = set()  # Use a set to avoid duplicate quadruplets

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1  # Two pointers for the remaining two numbers
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    # Found a valid quadruplet
                    quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # Skip duplicates for the third number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the fourth number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

            # Skip duplicates for the second number
            while j + 1 < n - 2 and nums[j] == nums[j + 1]:
                j += 1

        # Skip duplicates for the first number
        while i + 1 < n - 3 and nums[i] == nums[i + 1]:
            i += 1

    return list(quadruplets)

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = four_sum(nums, target)
print(result)  # Output: All unique quadruplets that sum up to the target


# Solution number 2-

# Solution with class method in Array

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res     
     