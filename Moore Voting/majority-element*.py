"""
Majority Element
@ Moore Voting
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        res, cnt = None, 0
        for val in nums:
            if res and res != val:
                cnt -= 1
            else:
                res = val
                cnt += 1
            if cnt == 0:
                res = val
                cnt = 1
        return res
