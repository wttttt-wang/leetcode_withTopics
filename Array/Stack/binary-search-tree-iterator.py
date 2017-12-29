"""
Binary Search Tree Iterator
@ Stack
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        node = res.right
        while node:
            self.stack.append(node)
            node = node.left
        return res.val


root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
so = BSTIterator(root)
while so.hasNext():
    print so.next()

