"""
First Missing Positive
@ Array, Index-based: The key point is to put the element to it's right position.
                      And the reason why the solution works is res should be in [1, len(res) + 1]
@ V1: O(N) time & O(N) space
  V2: O(N) time & O(1) space: Please pay attention to when to increase i.
"""


class SolutionV2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                if 1 <= nums[i] <= len(nums):
                    ind = nums[i] - 1
                    if nums[i] == nums[ind]:
                        i += 1  # Attention: This is important or it will TLE!!!
                    else:
                        nums[i], nums[ind] = nums[ind], nums[i]
                else:
                    i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        flag = [False] * (len(nums) + 1)
        for val in nums:
            if 1 <= val <= len(nums) + 1:
                flag[val - 1] = True
        for i in range(len(flag)):
            if not flag[i]:
                return i + 1
