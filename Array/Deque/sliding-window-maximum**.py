"""
Sliding Window Maximum
@ Deque
@ Note: The common solution may be using @Heap, which is O(NlogK) time & need to remove target number from heap.
        Using a monotone deque can solve this by O(N) time & O(K) space.
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque, results = [], []
        for i in range(len(nums)):
            if i >= k:
                if deque[0] == nums[i - k]:
                    deque.pop(0)
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            if i >= k - 1:
                results.append(deque[0])
        return results


