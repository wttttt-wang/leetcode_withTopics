"""
@ Binary Indexed Tree: O(NlogN) time
@ Explanation: In BIT, store the frequency of each element.
               Then the required result of ind i is the count of elements which is smaller then nums[i].

@ Optimization: discretization --> remove duplicates and sort nums, then we get a mapping from origin elements to new ind.
                As a result, we optimize space from O(max(nums) - min(nums)) to O(N)
"""


class BIT(object):
    def __init__(self, length):
        self.arr = [0] * length
        self.n = length

    def lowBit(self, x):
        return x & (-x)

    def add(self, ind, val):
        while ind < self.n:
            self.arr[ind] += val
            ind += self.lowBit(ind)

    def sumBefore(self, ind):
        res = 0
        while ind:
            res += self.arr[ind]
            ind -= self.lowBit(ind)
        return res


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        results = [0] * len(nums)
        discretization = {}
        for i, j in enumerate(sorted(set(nums))):
            discretization[j] = i + 1
        bit = BIT(len(discretization))
        for i in range(len(nums) - 1, -1, -1):
            ind = discretization[nums[i]]
            results[i] = bit.sumBefore(ind - 1)
            bit.add(ind, 1)
        return results
