
# Best Time to Buy and Sell Stock - leetcode (easy)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         price = float('inf')
#         profit = 0

#         for i in prices:
#             price = min (i, price)
#             profit = max (profit, i - price)
             
#         return profit
    
    
# Best Time to Buy and Sell Stock II - leetcode (medium)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
        
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i] - prices[i-1]
        
#         return profit


 