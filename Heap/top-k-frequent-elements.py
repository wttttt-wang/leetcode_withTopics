"""
Top K Frequent Elements
@ Heap + Hash: O(N) time & O(N) space
@ Also see 'Sort/BucketSort/top-k-frequent-elements'
"""


from heapq import *


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        freqs = {}
        for v in nums:
            freqs[v] = freqs.get(v, 0) + 1
        return nlargest(k, freqs, key=lambda x: freqs[x])
