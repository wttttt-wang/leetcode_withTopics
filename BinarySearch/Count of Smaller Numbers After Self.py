"""
@ Binary Search: The simplest method of this problem is to sort the right part and then binary search.
@ Time Complexity: O(N ^ 2) time as arr.insert() will cause O(N) time.  O(N) additional space to store sortedArr.
@ Nothing special
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        results = []
        tailArr = []
        for i in range(len(nums) - 1, -1, -1):
            cnt = self.cntSmaller(nums[i], tailArr)
            results.append(cnt)
            tailArr.insert(len(tailArr) - cnt, nums[i])  # this may result in O(N) time
        results.reverse()
        return results

    def cntSmaller(self, val, arr):
        if not arr:
            return 0
        # that is to find the right-most element which >= val
        left, right = 0, len(arr) - 1
        while left < right - 1:
            mid = (right - left) / 2 + left
            if arr[mid] >= val:
                left = mid
            else:
                right = mid
        if arr[right] >= val:
            return len(arr) - right - 1
        if arr[left] >= val:
            return len(arr) - right
        return len(arr) - left
