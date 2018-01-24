"""
Binary Tree Paths
@ Tree + DFS
"""


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        results = []
        self.helper(root, results, [str(root.val)])
        return results

    def helper(self, root, results, result):
        if not root.left and not root.right:
            results.append("->".join(result))
            return
        if root.left:
            result.append(str(root.left.val))
            self.helper(root.left, results, result)
            result.pop()
        if root.right:
            result.append(str(root.right.val))
            self.helper(root.right, results, result)
            result.pop()
