
# here we solve longest substring - 


# def longestUniqueSubstr(s):
#     n = len(s)
#     res = 0

#     for i in range(n):

#         # Initializing all characters as not visited
#         visited = [False] * 256

#         for j in range(i, n):

#             # If current character is visited
#             # Break the loop
#             if visited[ord(s[j])] == True:
#                 break

#             # Else update the result if this window is larger,
#             # and mark current character as visited.
#             else:
#                 res = max(res, j - i + 1)
#                 visited[ord(s[j])] = True

#     return res

# if __name__ == "__main__":
#     s = "geeksforgeeks"
#     print(longestUniqueSubstr(s))

# Here we try once again this code by itself - 


def triplet(arr, sum):
    n = len(arr)

    for i in range(n-2):

        for j in range(i+1,n-1):

            for k in range(j+1, n):

                if arr[i]+arr[j]+arr[k]==sum:

                    print(f"the number is:{arr[i]},{arr[j]},{arr[k]}")
                    return True
    
    return False

arr = [2,4,5,6,7,9,2]
sum=16
triplet(arr, sum)






























# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
        
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i] - prices[i-1]
        
#         return profit
