"""
Convert Sorted Array to Binary Search Tree
@ BST + DFS
"""


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, start, end):
        if start > end:
            return
        if start == end:
            return TreeNode(nums[start])
        mid = (end - start) / 2 + start
        root = TreeNode(nums[mid])
        root.left, root.right = self.helper(nums, start, mid - 1), self.helper(nums, mid + 1, end)
        return root
