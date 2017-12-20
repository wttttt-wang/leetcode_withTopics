"""
Container With Most Water
@ Two pointers: The point is to find a smart way of scan to cut off the useless cases
                and meanwhile guarantee the max value can be reached through the rest of cases.
                The way is start from (0, len(height) - 1), and throw the smaller one in each round.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        while left <= right:
            res = max(res, min(height[left], height[right]) * (right - left + 1))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
