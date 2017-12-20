"""
Median of Two Sorted Arrays
@ Divide And Conquer
@ Note: Pay attention to the way of handling index.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tmp = len(nums1) + len(nums2)
        if tmp % 2:
            return self.findK(nums1, nums2, tmp / 2 + 1)
        else:
            return (self.findK(nums1, nums2, tmp / 2) + self.findK(nums1, nums2, tmp / 2 + 1)) / 2.0

    def findK(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findK(nums2, nums1, k)  # unify to len(nums1) <= len(nums2) for better encoding
        # 1. recursion exit
        if not nums1:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(k / 2, len(nums1))
        p2 = k - p1
        if nums1[p1 - 1] < nums2[p2 - 1]:
            return self.findK(nums1[p1:], nums2, p2)
        else:
            return self.findK(nums1, nums2[p2:], p1)

