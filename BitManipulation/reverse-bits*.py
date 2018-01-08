"""
Reverse Bits
@ Bit Manipulation
@ Follow up: If the function is called multi-times, then we can use global cache.
             What's more, we can split n to several parts to increase the hit ratio.
"""


class Solution:
    global_cache = {0: 0}
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n not in self.global_cache:
            res = 0
            for i in range(32):
                res = (res << 1) + (n & 1)
                n >>= 1
            self.global_cache[n] = res
        return self.global_cache[n]

