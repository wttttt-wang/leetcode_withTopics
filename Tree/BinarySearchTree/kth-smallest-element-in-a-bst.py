"""
Kth Smallest Element in a BST
@ Binary Search Tree:
@ 1. V1: The key point is to construct sorted array according to BST's features.
  2. V2: (preferred): And for follow-up, we can cache cntNodes for each node.
                      Therefore, for each update & search, we need O(h) time.
"""


class SolutionV2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        leftCnt = self.cntNodes(root.left)
        if k == leftCnt + 1:
            return root.val
        if k <= leftCnt:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - leftCnt - 1)

    def cntNodes(self, root):
        return self.cntNodes(root.left) + self.cntNodes(root.right) + 1 if root else 0


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while k > 1:
            node = stack.pop()
            if node.right:
                tmp = node.right
                while tmp:
                    stack.append(tmp)
                    tmp = tmp.left
            k -= 1
        if stack:
            return stack[-1].val
