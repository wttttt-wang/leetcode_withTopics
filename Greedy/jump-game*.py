"""
Jump Game
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        end = 0
        for i in range(len(nums)):
            if i > end:
                return end
            end = max(i + nums[i], end)
        return True


so = Solution()
print so.canJump([2, 5, 0, 0])
