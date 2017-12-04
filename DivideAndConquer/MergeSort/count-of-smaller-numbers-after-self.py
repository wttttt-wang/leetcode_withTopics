"""
@ Divide And Conquer(Merge Sort)
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        results = [0] * len(nums)
        self.mergeSort(list(enumerate(nums)), results)
        return results

    def mergeSort(self, nums, results):
        if not nums or len(nums) < 2:
            return nums
        mid = len(nums) / 2
        left = self.mergeSort(nums[:mid], results)
        right = self.mergeSort(nums[mid:], results)
        for i in range(len(nums) - 1, -1, -1):
            if not right or (left and left[-1][1] > right[-1][1]):
                results[left[-1][0]] += len(right)
                val = left.pop()
            else:
                val = right.pop()
            nums[i] = val
        return nums
