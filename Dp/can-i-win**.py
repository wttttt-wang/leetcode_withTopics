"""
Can I Win
@ Dp + MinMax: 1. given total, remaining can be calculated by un chosen numbers, so just need one variable for dp.
               2. use str/integer as key for memorization.
@ Corner case: sum(1 to maxChoosableInteger) < desiredTotal!!!
"""


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger <= 0 or (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal, memo)

    def helper(self, nums, total, memo):
        hashKey = str(nums)
        if hashKey not in memo:
            if nums and nums[-1] >= total:
                return True
            for i in range(len(nums)):
                if not self.helper(nums[:i] + nums[i + 1:], total - nums[i], memo):
                    memo[hashKey] = True
                    return True
            memo[hashKey] = False
        return memo[hashKey]
