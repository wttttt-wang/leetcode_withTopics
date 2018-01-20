"""
Subarray Sum Equals K
@ Prefix Sum + Hash: When comes to sub-array sum, please remember prefix sum! Ball ball you.
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        res, occurs = 0, {0: 1}
        prefix = 0
        for val in nums:
            prefix += val
            res += occurs.get(prefix - k, 0)
            occurs[prefix] = occurs.get(prefix, 0) + 1
        return res

