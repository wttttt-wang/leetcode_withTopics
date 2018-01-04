"""
Sort Characters By Frequency
@ Heap + Hash
@ Just like 'Heap/top-k-frequent-elements', we can also use Bucket Sort for this problem.
"""


from heapq import *


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        freqs = {}
        for v in s:
            freqs[v] = freqs.get(v, 0) + 1
        lar = nlargest(len(freqs), freqs, key=lambda x: freqs[x])
        res = []
        for k in lar:
            for j in range(freqs[k]):
                res.append(k)
        return "".join(res)

