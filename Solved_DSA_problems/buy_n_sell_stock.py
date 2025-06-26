
# here we solve stock sell and buy cases - 

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

prices =  [3,4,6,7,9,8,2]
print(maxProfit(prices))

# practice again - 

   