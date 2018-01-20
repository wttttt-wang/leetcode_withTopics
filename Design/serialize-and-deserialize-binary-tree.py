"""
Serialize and Deserialize Binary Tree
@ Design + Tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = [str(root.val)]
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                res.append(str(node.left.val))
            else:
                res.append('#')
            if node.right:
                queue.append(node.right)
                res.append(str(node.right.val))
            else:
                res.append('#')
        print res
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(",")
        res = TreeNode(data[0])
        queue, ind = [res], 1
        while queue:
            node = queue.pop(0)
            if data[ind] != '#':
                node.left = TreeNode(int(data[ind]))
                queue.append(node.left)
            ind += 1
            if data[ind] != '#':
                node.right = TreeNode(int(data[ind]))
                queue.append(node.right)
            ind += 1
        return res


so = Codec()
root = TreeNode(-1)
root.left, root.right = TreeNode(0), TreeNode(1)
str1 = so.serialize(root)
print so.deserialize(str1)
