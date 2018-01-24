"""
Construct Binary Tree from Inorder and Postorder Traversal
@ Tree + DFS
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder or len(postorder) != len(inorder):
            return
        root = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])
        root.left, root.right = self.buildTree(inorder[:ind], postorder[:ind]), self.buildTree(inorder[ind + 1:], postorder[ind: -1])
        return root
