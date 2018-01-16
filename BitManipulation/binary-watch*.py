"""
 Binary Watch
 @ Bit Manipulation
"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        results = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    results.append('{}:{}'.format(h, m) if m >= 10 else '{}:0{}'.format(h, m))
        return results

