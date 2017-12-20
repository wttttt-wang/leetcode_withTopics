"""
Trapping Rain Water
@ Two pointers
@ Note: the key point is the water is determined by the smaller outer column.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    res += (leftMax - height[left])
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    res += (rightMax - height[right])
                else:
                    rightMax = height[right]
                right -= 1
        return res
