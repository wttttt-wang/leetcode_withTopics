"""
Populating Next Right Pointers in Each Node II
@ Tree: (I came up with an amazing solution > <)
        The key point is to use dummy node which makes the solution really neat.
"""


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        prev = root
        while prev:
            dummy = TreeLinkNode(0)  # dummy of current level
            tmp = dummy
            while prev:
                if prev.left:
                    tmp.next = prev.left
                    tmp = tmp.next
                if prev.right:
                    tmp.next = prev.right
                    tmp = tmp.next
                prev = prev.next
            prev = dummy.next
