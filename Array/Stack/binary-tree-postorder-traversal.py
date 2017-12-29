"""
Binary Tree Postorder Traversal
@ Stack (Non-recursion)
@ O(N) space
"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        # 1. initialize stack   (node, visited)
        while root:
            stack.append([root, False])
            root = root.left
        while stack:
            node, visited = stack[-1]
            if visited:
                stack.pop()
                res.append(node.val)
            else:
                tmp = node.right
                stack[-1][1] = True
                while tmp:
                    stack.append([tmp, False])
                    tmp = tmp.left
        return res

