"""
Search in Rotated Sorted Array II
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        # since the worst case is alway O(N), I didn't use binary search
        for val in nums:
            if val == target:
                return True
        return False
