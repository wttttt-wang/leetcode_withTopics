"""
K-diff Pairs in an Array
@ Sort + Two pointers: The two pointers in below solution goes somewhat weired. orz.
                       (Try to consider nums=[1, 1, 1, 2, 2])
@ Also see 'Hash/k-diff-pairs-in-an-array'
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        left, right, res = 0, 1, 0
        while left < len(nums) and right < len(nums):
            right = max(right, left + 1)
            while right < len(nums) and nums[right] - nums[left] < k:
                right += 1
            if left < right < len(nums) and nums[right] - nums[left] == k:
                res += 1
            left += 1
            while left < len(nums) and nums[left] == nums[left - 1]:
                left += 1
        return res


so = Solution()
print so.findPairs([1,1,1,2,2], 0)
