
# Here we solve two sum of given number - 

def sum(a,b):

    print(a+b)

sum(5,6)

def sum(nums, target):
    
    n=len(nums)

    for i in range(n-1):

        for j in range(i+1, n):

            if nums[i] + nums[j] == target:
                return [i,j]
             
    return[] 

nums=[4,6,7,8]
target=10
result=(sum(nums,target))
print(result)   


# Here we solve best time to sell stock using recursion function (leetcode question)


def max_profit(prices):
    # Helper function for recursion
    def helper(day, holding):
        # Base case: if we reach the end of the prices list
        if day >= len(prices):
            return 0
        
        # If we are holding a stock
        if holding:
            # Option 1: Sell the stock today
            sell_today = prices[day] + helper(day + 1, False)
            # Option 2: Do nothing and hold the stock
            hold_today = helper(day + 1, True)
            return max(sell_today, hold_today)
        else:
            # If we are not holding a stock
            # Option 1: Buy the stock today
            buy_today = -prices[day] + helper(day + 1, True)
            # Option 2: Do nothing and stay without stock
            skip_today = helper(day + 1, False)
            return max(buy_today, skip_today)

    # Start recursion from day 0 and not holding any stock
    return helper(0, False)

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", max_profit(prices))


# first and last accurence sorted 

def findFirstAndLast(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n):
        if (x != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
 
    if (first != -1):
        print("First Occurrence = ", first,
              " \nLast Occurrence = ", last)
    else:
        print("Not Found")
 
 
# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)
