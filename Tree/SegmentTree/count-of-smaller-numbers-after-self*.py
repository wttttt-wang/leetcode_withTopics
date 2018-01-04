"""
Count of Smaller Numbers After Self
@ Segment Tree: Almost the same usage like BIT.
@ Note: Segment tree is not the most recommended way to solution this problem as far as I'm concerned.
        But this is of course a way for learning segment tree.
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = [0] * len(nums)
        # 1. discretization: This is important, set and then sort.(Because we want to count smaller, so sort is necessary!)
        dis = {}
        for i, j in enumerate(sorted(set(nums))):
            dis[j] = i
        segtree = SegmentTree([0] * len(dis))
        print dis
        for i in range(len(nums) - 1, -1, -1):
            ind = dis[nums[i]]
            print nums[i], ind
            res[i] = segtree.rangeSum(0, ind - 1)
            segtree.add(ind, 1)
        return res


class SegmentTree(object):
    def __init__(self, nums):
        self.root = self.construct(nums, 0, len(nums) - 1)

    def construct(self, nums, start, end):
        if start > end:
            return
        if start == end:
            return SegNode(start, end, nums[start])
        mid = (end - start) / 2 + start
        left, right = self.construct(nums, start, mid), self.construct(nums, mid + 1, end)
        root = SegNode(start, end, left.val + right.val)
        root.left, root.right = left, right
        return root

    def add(self, ind, val):
        if ind < self.root.start or ind > self.root.end:
            return
        self.addHelper(ind, val, self.root)

    def addHelper(self, ind, val, root):
        if root.start == root.end:
            root.val += val
        else:
            mid = (root.end + root.start) / 2
            if ind <= mid:
                self.addHelper(ind, val, root.left)
            else:
                self.addHelper(ind, val, root.right)
            root.val = root.left.val + root.right.val

    def rangeSum(self, left, right):
        if left > self.root.end or right < self.root.start:
            return 0
        return self.rangeHelper(left, right, self.root)

    def rangeHelper(self, left, right, root):
        if root.start == root.end or (left <= root.start and right >= root.end):
            return root.val
        mid = (root.start + root.end) / 2
        if right <= mid:
            return self.rangeHelper(left, right, root.left)
        if left > mid:
            return self.rangeHelper(left, right, root.right)
        return self.rangeHelper(left, mid, root.left) + self.rangeHelper(mid + 1, right, root.right)


class SegNode(object):
    def __init__(self, s, e, val):
        self.val, self.start, self.end = val, s, e
