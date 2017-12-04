"""
@ Divide And Conquer(Merge Sort): O(NlogN) time

@ Explanation: count the pairs of left & right part separately, and sort them in the meanwhile.
               then count the intersect pairs which satisfy the requirement.
               (Intersect means select one from left and the other from right)
               As left & right are already sorted, use two pointers to count. And merge sort this two array.

@ For more info: see MergeSort/count-of-range-sum.md
"""


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0
        prefixSum = [0]
        for val in nums:
            prefixSum.append(prefixSum[-1] + val)
        return self.merge(prefixSum, lower, upper, 0, len(prefixSum) - 1)

    def merge(self, nums, lower, upper, start, end):
        if start >= end:
            return 0
        mid = (end - start) / 2 + start
        res = 0
        res += self.merge(nums, lower, upper, start, mid)
        res += self.merge(nums, lower, upper, mid + 1, end)
        p1, p2 = start, start
        # 1. count res
        for i in range(mid + 1, end + 1):
            # 1.1 update p1
            while p1 <= mid and nums[p1] < nums[i] - upper:
                p1 += 1
            # 2.1 update p2
            while p2 <= mid and nums[p2] <= nums[i] - lower:
                p2 += 1
            res += max(0, p2 - p1)
        # 2. merge
        newArr = []
        pl, pr = start, mid + 1
        while pl <= mid and pr <= end:
            if nums[pl] < nums[pr]:
                newArr.append(nums[pl])
                pl += 1
            else:
                newArr.append(nums[pr])
                pr += 1
        while pl <= mid:
            newArr.append(nums[pl])
            pl += 1
        while pr <= end:
            newArr.append(nums[pr])
            pr += 1
        nums[start: end + 1] = newArr
        return res

so = Solution()
print so.countRangeSum([-2, 5, -1], -2, 2)
