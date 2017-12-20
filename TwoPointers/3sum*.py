"""
3Sum
@ Two pointers
@ Note: Pay attention to how to remove duplicates.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right]
                if tmp == -nums[i]:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1   # to skip duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return results

