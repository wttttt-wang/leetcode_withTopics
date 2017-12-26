"""
Create Maximum Number
@ Greedy
@ The way is to iterate over all possible i + j == k then merge them.
@ Note the way of select k elements to construct a maximum sub array:
    drop len(nums) - k elements rather than select k elements (refer to Greedy/remove-k-digits)
"""


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        return max(self.merge(self.maxK(nums1, i), self.maxK(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))

    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]

    def maxK(self, nums, k):
        drop = len(nums) - k   # drop len(nums) - k elements rather than select k elements
        out = []
        for val in nums:
            while drop and out and out[-1] < val:
                out.pop()
                drop -= 1
            out.append(val)
        return out[:k]
