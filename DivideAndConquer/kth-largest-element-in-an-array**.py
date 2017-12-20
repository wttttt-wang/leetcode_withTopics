"""
Kth Largest Element in an Array
@ Quick Select  (Divide And Conquer)
@ O(N) time:  T(N) = O(N) + T(N/2) = O(N) + O(N/2) + O(N/4) + ... + O(1) --> O(N) on average
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k <= 0 or len(nums) < k:
            return
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k + 1)   # quick select

    def helper(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        midVal = nums[(end - start) / 2 + start]
        while left <= right:
            while left <= right and nums[left] < midVal:
                left += 1
            while left <= right and nums[right] > midVal:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k > left - start:
            return self.helper(nums, left, end, k - left + start)
        if k <= right - start + 1:
            return self.helper(nums, start, right, k)
        return nums[left - 1]
