"""
Random Pick Index
@ Reservoir Sampling
"""


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        candi, pv = None, 1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(1, pv) == 1:
                    candi = i
                pv += 1
        return candi
