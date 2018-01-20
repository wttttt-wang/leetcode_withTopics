"""
Contains Duplicate
@ Hash
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        occurs = set()
        for val in nums:
            if val in occurs:
                return True
            occurs.add(val)
        return False
