"""
Contiguous Array
@ PrefixSum + Hash (+ Math): Two solution, all using 'prefixSum'
@ Solution1: Treat 0 as -1, then problem becomes 'find longest subarray which sum == 0'
@ Solution2: Using prefixSum, transform math equations:
             (pre[i] - pre[j]) * 2 == j - i --> pre[i] * 2 - i == pre[j] * 2 - j
             (Should pay more attention to the index!)
"""


class Solution2(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maps, prefix = {1: -1}, 0  # map 'prefix * 2 - i' to leftmost ind
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            mapKey = prefix * 2 - i
            if mapKey in maps:
                res = max(res, i - maps[mapKey])
            if mapKey not in maps:
                maps[mapKey] = i
        return res
