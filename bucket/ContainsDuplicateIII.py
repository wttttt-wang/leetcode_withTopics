"""
@ Bucket: bucketing to t buckets, so it's guaranteed that there are at most one value in each bucket,
        or it will return True directly.

@ Corner case: Big Number for nums[i] + k will overflow. But for python u don't need to consider overflow.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k < 1 or t < 0:
            return False
        buckets = {}
        for i in range(len(nums)):
            bucket = nums[i]/ (t + 1)  # the diff in each bucket is at most t, so t + 1 elements in each bucket at most.
            if bucket in buckets or (bucket - 1 in buckets and nums[i] - buckets[bucket - 1] <= t) or (bucket + 1 in buckets and buckets[bucket + 1] - nums[i] <= t):
                return True
            if i >= k:
                lastBucket = nums[i - k] / (t + 1)
                buckets.pop(lastBucket)
            buckets[bucket] = nums[i]
        return False

