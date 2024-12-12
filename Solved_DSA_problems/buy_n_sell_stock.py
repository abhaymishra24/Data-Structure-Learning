

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


def maxProfit(prices):
    # Initialize variables
    min_price = float('inf')  # Set to infinity initially
    max_profit = 0  # Maximum profit initialized to 0

    # Iterate through each price in the list
    for price in prices:
        # Update min_price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate profit if selling at current price
        current_profit = price - min_price
        # Update max_profit if current profit is greater
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5


# here we solve without comments -

def maxProfit(prices):
    min_price = float('inf')   
    max_profit = 0 
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        current_profit = price - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   

# here solve once again-0

def maxProfit(prices):
    min_price = float('inf')   
    max_profit = 0 
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        current_profit = price - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   

# new code -

def maxProfit(prices):
    min_price = float('inf')   
    max_profit = 0 
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        current_profit = price - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   


# add new once code -

def maxProfit(prices):
    min_price = float('inf')   
    max_profit = 0 
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        current_profit = price - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   

