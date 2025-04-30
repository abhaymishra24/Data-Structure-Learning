
def findnumber(self, nums):
    n = len(nums)

    count = 0
    for num in nums:
        if len(str(abs(num))) % 2 == 0:
            count += 1
    return count