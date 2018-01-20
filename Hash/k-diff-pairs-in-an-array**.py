"""
K-diff Pairs in an Array
@ Hash: The key point is how to remove duplicates.
        And we should also pay attention to k == 0.
@ Also see 'TwoPointers/k-diff-pairs-in-an-array'
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < 2 or k < 0:
            return 0
        occurs, res = {}, 0
        for val in nums:
            occurs[val] = occurs.get(val, 0) + 1
        for key in occurs:
            if k == 0:
                if occurs[key] > 1:
                    res += 1
            else:
                if key + k in occurs:
                    res += 1
        return res
