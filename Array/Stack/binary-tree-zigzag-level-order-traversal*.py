"""
Binary Tree Zigzag Level Order Traversal
@ Stack
"""


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, stack = [], [root]
        reverFlag = True
        while stack:
            res.append([n.val for n in stack])
            tmpRes = []
            if reverFlag:
                while stack:
                    node = stack.pop()
                    if node.right:
                        tmpRes.append(node.right)
                    if node.left:
                        tmpRes.append(node.left)
            else:
                while stack:
                    node = stack.pop()
                    if node.left:
                        tmpRes.append(node.left)
                    if node.right:
                        tmpRes.append(node.right)
            reverFlag = not reverFlag
            stack = tmpRes
        return res
