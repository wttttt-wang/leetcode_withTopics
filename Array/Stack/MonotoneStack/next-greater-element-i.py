"""
Next Greater Element I
@ Monotone Stack
"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums or not nums:
            return []
        maps, stack = {}, []   # stack is decreasing
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            maps[nums[i]] = stack[-1] if stack else -1
            stack.append(nums[i])
        return [maps[val] for val in findNums]

