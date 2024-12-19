
# Remove Duplicates from Sorted Array - leetcode (easy) 

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        
        return k
  
# here I solve a same problem with help of set - 

def remove_duplicates_set(arr):
    return list(set(arr))

# Example usage
arr = [10, 20, 20, 30, 40, 40, 50]
result = remove_duplicates_set(arr)
print(result)  # Output: [40, 10, 20, 30, 50] (order may vary)

# same code in set method without comment - 

def remove_duplicates_set(arr):
    return list(set(arr))

arr = [10, 20, 20, 30, 40, 40, 50]
result = remove_duplicates_set(arr)
print(result) 

# remove dublicates code with correction - 

def removedubli(arr):
    if not arr:
        return arr  
 
    unique_elements = []
    
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)   

    return unique_elements

arr = [4, 5, 6, 7, 7, 8, 9]
result = removedubli(arr)
print(result)   

# solve problem with help of set - 

def remove_dublicate(arr):
    
    return list(set(arr))

arr = [3,4,5,6,7,8,8,9,9]
result = remove_dublicate(arr)
print(result)

# here solve once again this problem - 

def dubli(arr):
    
    return list(set(arr))

arr = [3,4,5,6,7,8,8,8,9,4,4]
r = dubli(arr)
print(r)

# solve this problem once again -

def dublicates(arr):
    return list(set(arr))

arr = [8,6,7,7,8,9,9,0,0]
rr = dublicates(arr)
print(rr)

# same question solve once agian - 

def rdubli(arr):
    return list(set(arr))

arr = [5,5,6,7,8,8,9]
res = rdubli(arr)
print(res)

# solve this question - 

def dar(a):
    return list(set(a))

a = [6,7,8,9,4,4,5,5,7,0,0]
b = dar(a)
print(b)