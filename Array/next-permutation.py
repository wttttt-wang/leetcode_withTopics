"""
Next Permutation
@ Array
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        # 1. find the first nums[i] < nums[i + 1] from right to left
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                # 2.find the minimum nums[j] > nums[i - 1](j >= i), as nums[i:] is descending we find from right to left
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        break
                # nums[i:] is still descending after exchange, to make it ascending, just need exchange
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break
            i -= 1
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
