"""
Next Greater Element II
@ Monotone Stack + Circular Array: For circular array, the first thing we can consider is to do 'nums += nums'
                                   Also, for this problem, we can not repeat num by just appending stack, see V2.
"""


class SolutionV2(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        results = [-1] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            stack.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                results[i] = stack[-1]
            stack.append(nums[i])
        return results


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        results, n, stack = [], len(nums), []
        nums += nums
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if i < n:
                results.append(stack[-1] if stack else -1)
            stack.append(nums[i])
        return results[::-1]
