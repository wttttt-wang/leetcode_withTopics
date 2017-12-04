"""
Reverse Pairs
@ Explanation: BIT. remember to add all the indices that needed to add / sum to allVals.
"""


class BIT(object):
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def lowBit(self, x):
        return x & (-x)

    def add(self, ind, val):
        while ind <= self.n:
            self.arr[ind] += val
            ind += self.lowBit(ind)

    def sum(self, ind):
        res = 0
        while ind:
            res += self.arr[ind]
            ind -= self.lowBit(ind)
        return res


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Solution2: BIT
        # 1. discretization
        allVals = []
        for val in nums:
            allVals.append(val)
            allVals.append(val / 2 + (0 if val % 2 else -1))
        mapped = {}
        for ind, val in enumerate(sorted(set(allVals))):
            mapped[val] = ind + 1
        bit = BIT(len(mapped))
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            ind = mapped[nums[i]]
            smaller = nums[i] / 2 + (0 if nums[i] % 2 else -1)
            res += bit.sum(mapped[smaller])
            bit.add(ind, 1)
        return res
