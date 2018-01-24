"""
Path Sum II
@ Tree + DFS
"""


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        self.helper(root, sum - root.val, results, [root.val])
        return results

    def helper(self, root, target, results, result):
        if not root.left and not root.right:
            if target == 0:
                results.append(result[:])
            return
        if root.left:
            result.append(root.left.val)
            self.helper(root.left, target - root.left.val, results, result)
            result.pop()
        if root.right:
            result.append(root.right.val)
            self.helper(root.right, target - root.right.val, results, result)
            result.pop()
