"""
@ Note Before: If u don't know BIT or have no idea of how to use BIT to solve this problem, please complete
               'BinaryIndexedTree/count-of-smaller-numbers-after-self' first.
@ BIT: After u get the prefixSum, the problem is almost the same as the problem I list upper side.
       But pay attention for a range sum, we need do double sum for BIT.
@ Note: U need to pay attention to the way how we got prefixSum.

@ For more Info: MergeSort/count-of-range-sum.md
"""


class BIT(object):
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def lowBit(self, n):
        return n & (-n)

    def add(self, ind, val):
        while ind <= self.n:
            self.arr[ind] += val
            ind += self.lowBit(ind)

    def sum(self, ind):
        res = 0
        while ind > 0:
            res += self.arr[ind]
            ind -= self.lowBit(ind)
        return res


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0
        sum_array = [upper, lower - 1]
        total = 0
        for num in nums:
            total += num
            sum_array += [total, total + lower - 1, total + upper]  # because every ind we search should be in bit
        # 1. discretization
        index = {}
        for i, x in enumerate(sorted(set(sum_array))):
            index[x] = i + 1

        tree = BIT(len(index))
        ans = 0
        for i in xrange(len(nums) - 1, -1, -1):
            tree.add(index[total], 1)  # need to add before sum, for pair of just one element also need to be considered
            total -= nums[i]
            ans += tree.sum(index[upper + total]) - tree.sum(
                index[lower + total - 1])  # lower <= a - b <= upper --> lower + b <= a <= upper + b
        return ans
