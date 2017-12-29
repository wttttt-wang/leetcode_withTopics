"""
Largest Rectangle in Histogram
@ Stack(Monotone Stack): The key point is to consider for each column i, calculate the area of height=heights[i]
                         So the problem convert to be find the closest column that smaller than heights[i] -->
                         This can be solved by using monotone stack.
@ Note: Do not forget to handle the left non-descending stack elements.  --> It's really tricky by adding tailing 0.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return False
        stack = []  # non-descending stack
        res = 0
        heights.append(0)   # This is important(and really tricky)! for handling left ascending columns
        for i in range(len(heights)):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)   # append index rather than value
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    val = heights[stack.pop()]    # calculate for current column with ind = stack.pop() & height = val
                    leftInd = stack[-1] if stack else -1
                    res = max(res, (i - leftInd - 1) * val)
                stack.append(i)
        return res


so = Solution()
heights = [2, 1, 5, 6, 2, 3]
print so.largestRectangleArea(heights)
