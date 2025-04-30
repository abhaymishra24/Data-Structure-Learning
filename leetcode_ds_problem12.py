
def findnumber(nums):
    n = len(nums)
    count = 0
    for num in nums:
        if len(str(abs(num))) % 2 == 0:
            count += 1
    return count

f = findnumber()
nums = [12, 345, 2, 6, 7896]
print(f.findnumber(nums))  # Output: 2 (12 and 7896 have an even number of digits)


def findNumbers(nums):
        n = len(nums)
        count = 0

        for n in nums:

            if len(str(abs(n))) % 2 == 0:
                count += 1

        return count
