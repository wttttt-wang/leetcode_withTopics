"""
Unique Binary Search Trees II
@ Tree + Recursion
"""


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        results = []
        for i in range(start, end + 1):
            ls, rs = self.helper(start, i - 1), self.helper(i + 1, end)
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    results.append(root)
        return results
