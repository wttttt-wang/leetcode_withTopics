"""
Range Sum Query - Mutable
@ Classical Segment Tree
"""


class SegTreeNode(object):
    def __init__(self, start, end, val):
        self.start, self.end = start, end
        self.val = val
        self.left, self.right = None, None


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, start, end):
        if start > end:
            return
        if start == end:
            return SegTreeNode(start, end, nums[start])
        mid = (end - start) / 2 + start
        left = self.buildTree(nums, start, mid)
        right = self.buildTree(nums, mid + 1, end)
        root = SegTreeNode(start, end, left.val + right.val)
        root.left, root.right = left, right
        return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if i < 0 or i > self.root.end:
            return
        self.add(i, val, self.root)

    def add(self, i, val, root):
        if root.start == root.end:
            root.val = val
        else:
            mid = (root.end - root.start) / 2 + root.start
            if i <= mid:
                self.add(i, val, root.left)
            else:
                self.add(i, val, root.right)
            root.val = root.left.val + root.right.val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < self.root.start:
            i = self.root.start
        if j > self.root.end:
            j = self.root.end
        return self.sumHelper(i, j, self.root)

    def sumHelper(self, i, j, root):
        if root.end == j and root.start == i:
            return root.val
        mid = (root.end - root.start) / 2 + root.start
        if j <= mid:
            return self.sumHelper(i, j, root.left)
        if i > mid:
            return self.sumHelper(i, j, root.right)
        return self.sumHelper(mid + 1, j, root.right) + self.sumHelper(i, mid, root.left)


