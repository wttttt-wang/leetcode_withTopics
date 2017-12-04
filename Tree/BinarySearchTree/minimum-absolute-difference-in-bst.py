"""
Minimum Absolute Difference in BST
@ Explanation: This is aim at basic understanding not application of BST.
"""


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.res = sys.maxint
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        left, right = self.helper(node.left), self.helper(node.right)
        minVal, maxVal = node.val, node.val
        if left:
            self.res = min(self.res, node.val - left[1])
            minVal = left[0]
        if right:
            self.res = min(self.res, right[0] - node.val)
            maxVal = right[1]
        return [minVal, maxVal]

