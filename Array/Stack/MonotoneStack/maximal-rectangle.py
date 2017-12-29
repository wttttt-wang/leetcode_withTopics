"""
Maximal Rectangle
@ Stack: Can be treated as the extension of 'Stack/MonotoneStack/largest-rectangle-in-histogram'
@ O(N ^ 2) time  &  O(N) space
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, self.maxHistogram([int(h) for h in heights]))
        return res

    def maxHistogram(self, heights):
        if not heights:
            return 0
        heights.append(0)
        stack, res = [], 0
        for i in range(len(heights)):
            if stack and heights[i] < heights[stack[-1]]:
                while stack and heights[stack[-1]] > heights[i]:
                    val = heights[stack.pop()]
                    leftInd = stack[-1] if stack else -1
                    res = max(res, (i - leftInd - 1) * val)
            stack.append(i)
        return res


so = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print so.maximalRectangle(matrix)
