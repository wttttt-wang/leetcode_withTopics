"""
Counting Bits
@ Bit Manipulation: SolutionV1 of O(32n) time is really trivial.
                    Refer to SolutionV2 with actually O(N) time: f[i] = f[i >> 1] + (i & 1) (This is really tricky)
@ Note to add parentheses when necessary!
"""


class SolutionV2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        results = [0] * (num + 1)
        for i in range(1, num + 1):
            results[i] = results[i >> 1] + (i & 1)
        return results


class SolutionV1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        results = []
        for val in range(num + 1):
            cnt = 0
            for i in range(32):
                cnt += (val & 1)
                val >>= 1
            results.append(cnt)
        return results
