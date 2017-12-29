"""
Binary Tree Preorder Traversal
@ Stack  + Binary Tree  Nothing special
"""


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, stack = [], []
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop().right
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
        return res
