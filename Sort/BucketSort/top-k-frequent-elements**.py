"""
Top K Frequent Elements
@ Bucket Sort: N buckets for frequency <= N.  O(N) time & O(N) space
@ Also see 'Heap/top-k-frequent-elements'
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        freqs, buckets, results = {}, [[] for _ in range(len(nums) + 1)], []
        for v in nums:
            freqs[v] = freqs.get(v, 0) + 1
        for key in freqs:
            buckets[freqs[key]].append(key)
        for i in range(len(buckets) - 1, -1, -1):
            if len(results) == k:
                return results
            results += buckets[i]
        return results[:k] if len(results) > k else results

