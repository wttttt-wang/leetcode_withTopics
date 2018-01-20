"""
Split Array Largest Sum
@ Binary Search + Greedy
"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums:
            return 0
        left, right = -sys.maxint, 0  # maxVal, sumVal
        for val in nums:
            left = max(left, val)
            right += val
        while left < right - 1:
            mid = (right - left) / 2 + left
            satis = self.satisfy(nums, mid, m)
            if satis:
                right = mid
            else:
                left = mid
        return left if self.satisfy(nums, left, m) else right

    def satisfy(self, nums, target, m):
        cnt, currSum = 1, 0
        for val in nums:
            if currSum + val > target:
                cnt += 1
                currSum = val
                if cnt > m:
                    return False
            else:
                currSum += val  # greedy: add as more numbers into one split as possible
        return cnt <= m

