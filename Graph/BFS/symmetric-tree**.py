"""
Symmetric Tree
@ BFS: The key point is always put the two nodes(subtree) that should symmetric together.
       And then, in each round pop them to check recursively.
       And note that they way we put the nodes into queue.
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            if len(queue) < 2:
                return False
            n1, n2 = queue.pop(0), queue.pop(0)
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                queue.append(n1.right)
                queue.append(n2.left)
                queue.append(n1.left)
                queue.append(n2.right)
            if (not n1 and n2) or (not n2 and n1):
                return False
        return True
