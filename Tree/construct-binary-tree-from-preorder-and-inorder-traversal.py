"""
Construct Binary Tree from Preorder and Inorder Traversal
@ Tree + DFS
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        root.left, root.right = self.buildTree(preorder[1: ind + 1], inorder[:ind]), self.buildTree(preorder[ind + 1:], inorder[ind + 1:])
        return root
