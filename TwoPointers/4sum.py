"""
4Sum
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # same as 3 sum
            threeSum = self.threeSum(nums, i + 1, target - nums[i])
            results += [[nums[i]] + t for t in threeSum]
        return results


    def threeSum(self, nums, startInd, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or startInd >= len(nums):
            return []
        results = []
        for i in range(startInd, len(nums) - 2):
            if i > startInd and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right]
                if tmp == target - nums[i]:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1   # to skip duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp < target - nums[i]:
                    left += 1
                else:
                    right -= 1
        return results

