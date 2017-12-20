"""
3Sum Closest
@ Two Pointers
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        res, diff = None, None
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right]
                tmpSum = tmp + nums[i]
                if diff is None or abs(target - tmpSum) < diff:
                    res = tmpSum
                    diff = abs(target - tmpSum)
                if tmp == target - nums[i]:
                    return target
                if tmp < target - nums[i]:
                    left += 1
                else:
                    right -= 1
        return res
