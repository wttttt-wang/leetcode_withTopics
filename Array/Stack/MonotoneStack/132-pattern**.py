"""
132 Pattern
@ Stack(Monotone Stack) + Greedy: To find s1 < s3 < s2, the key point is to first find the maximum s3 where
                                  exists s2 > s3 (greedy), when found s3, the problem is to find s1 < s2.
                                  Find max s3 where s2 > s3, we can use monotone stack.
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        stackS2, s3 = [], -sys.maxint  # s3 if the max val where exists s2 > s3
        # iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            while stackS2 and stackS2[-1] < nums[i]:
                s3 = stackS2.pop()
            stackS2.append(nums[i])
        return False
