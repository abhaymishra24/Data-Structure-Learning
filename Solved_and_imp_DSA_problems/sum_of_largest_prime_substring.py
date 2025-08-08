
class Solution(object):    
    def sumOfLargestPrimes(self, s):
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

# practice again - 

