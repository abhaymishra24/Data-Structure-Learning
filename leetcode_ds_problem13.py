
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
    
    def sumOfThreeLargestUniquePrimesFromSubstrings(s):
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        unique_primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                num_str = s[i:j]
                if num_str.isdigit():
                    num = int(num_str)
                    if is_prime(num):
                        unique_primes.add(num)
        largest_primes = sorted(unique_primes, reverse=True)[:3]
        return sum(largest_primes)