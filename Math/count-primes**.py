"""
Count Primes
@ Math + Hash: 1. The most naive solution is check each number one by one.
                  1.1 for a given number, check if prime --> check if divisible by x < n -->  x < sqrt(n) if enough
               2. Optimization: mark as non-prime by multiply former numbers.
                                i.e. for 2 we can mark 2 * 2, 2 * 3, ... as non-prime
                                2.1 A tricky is for a non-prime number, we don't need to multiply it.
                                    e.g. for 4: 4 * 2 is marked by 2, 4 * 3 is marked by 2. etc...
                                2.2 Another tricky is for a prime number x, we only need to multiply from x.
                                    e.g. for 5: 5 * 2, 5 * 3... is already marked.
                                2.3 terminating loop condition can be p < sqrt(n)
@ Note: 1 is not prime
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        isPrime = [1] * n
        endCond = int(math.sqrt(n))
        for i in range(2, endCond + 1):
            if isPrime[i]:
                j = i
                while j * i < n:
                    isPrime[j * i] = 0
                    j += 1
        return sum(isPrime) - 2

