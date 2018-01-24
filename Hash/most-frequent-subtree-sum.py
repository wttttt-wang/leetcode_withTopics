"""
Most Frequent Subtree Sum
@ Hash + Tree
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    _maxOccur = 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        maps = {}
        self._maxOccur = 0
        self.helper(root, maps)
        return [key for key in maps if maps[key] == self._maxOccur]

    def helper(self, root, maps):
        if not root:
            return 0
        left, right = self.helper(root.left, maps), self.helper(root.right, maps)
        tmpVal = left + right + root.val
        maps[tmpVal] = maps.get(tmpVal, 0) + 1
        self._maxOccur = max(self._maxOccur, maps[tmpVal])
        return tmpVal


