"""
Longest Consecutive Sequence
@ Explanation: HashSet. O(N) time & O(N) space
@ Tricky
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        numSet = set(nums)
        res = 1
        for val in set(nums):
            tmpCnt = 1
            tmpVal = val + 1
            while tmpVal in numSet:
                numSet.remove(tmpVal)
                tmpCnt += 1
                tmpVal += 1
            while val - 1 in numSet:
                numSet.remove(val - 1)
                tmpCnt += 1
                val -= 1
            res = max(res, tmpCnt)
        return res
