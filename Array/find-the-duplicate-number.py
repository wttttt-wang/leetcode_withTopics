"""
Find the Duplicate Number
@ Array
@ Requirements: O(1) space, time < O(N ^ 2), no modification to origin array
@ Solutions: 1. binary search on result: O(NlogN) time
             2. linked list: like finding circle in an graph (See 'LinkedList/find-the-duplicate-number')
             3. index: see solution below, code it talks.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = None
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val] < 0:
                res = val
                break
            nums[val] = -nums[val]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])   # revert to origin
        return res

