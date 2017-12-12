"""
Permutation Sequence
@ Math: Find the law
"""
import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = []
        k -= 1
        candidates = range(1, n + 1)
        factor = math.factorial(n - 1)
        for i in range(n - 1, 0, -1):
            ind = k / factor
            result.append(str(candidates[ind]))
            candidates.pop(ind)  # update candidates
            k %= factor
            factor /= i
        result.append(str(candidates[0]))
        return "".join(result)


so = Solution()
print so.getPermutation(5, 7)
