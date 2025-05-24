
# solve find out angle of triangle -

# str = " My name is money. I power full in every moment."

# print(str.index("m"))

# a = 5
# b = 12
# c = 15

# print(max(a,b,c))


# def primeoflargenumber(s):
    
#     s = input()
    
#     s = int(s)
    
#     s = set(s)
    
class Solution(object):    
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        s = [int(i) for i in s if i.isdigit()]
        primes = []
        
        for num in s:
            if num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
        
        if not primes:
            return 0
        
        return sum(sorted(primes, reverse=True)[:2])
    
# Example usage:
# solution = Solution()
# result = solution.sumOfLargestPrimes("My name is 5 12 15 and 7")
# print(result)  # Output should be the sum of the two largest prime numbers found in the string    
# Example usage:
# solution = Solution()     
# result = solution.sumOfLargestPrimes("My name is 5 12 15 and 7")
# print(result)  # Output should be the sum of the two largest prime numbers found in the string
    
