"""
Reverse Pairs
@ Explanation: almost the same as 'count-of-range-sum' & 'count-of-smaller-numbers-after-self'
               @ Merge Sort + @ Two pointers
"""


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Solution1: merge sort
        return self.merge(nums, 0, len(nums) - 1)

    def merge(self, nums, start, end):
        if start >= end:
            return 0
        res = 0
        mid = (end - start) / 2 + start
        res += self.merge(nums, start, mid)
        res += self.merge(nums, mid + 1, end)
        # 1. cnt
        pr = mid + 1
        for pl in range(start, mid + 1):
            while pr <= end and nums[pl] > 2 * nums[pr]:
                pr += 1
            res += pr - mid - 1
        # 2. merge
        mergeArr = []
        pl, pr = start, mid + 1
        while pl <= mid and pr <= end:
            if nums[pl] < nums[pr]:
                mergeArr.append(nums[pl])
                pl += 1
            else:
                mergeArr.append(nums[pr])
                pr += 1
        while pl <= mid:
            mergeArr.append(nums[pl])
            pl += 1
        while pr <= end:
            mergeArr.append(nums[pr])
            pr += 1
        nums[start:end + 1] = mergeArr
        return res

