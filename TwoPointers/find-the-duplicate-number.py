"""
Find the Duplicate Number
@ LinkedList: like finding circle.
@ Also see 'Array/find-the-duplicate-number' (recommended)
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        if slow != fast:
            return
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow