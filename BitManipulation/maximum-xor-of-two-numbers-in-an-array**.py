"""
Maximum XOR of Two Numbers in an Array
@ HashMap + Bit Manipulation: The basic idea is, from high to low bit, check whether this bit can be set 1.
                              The way to check is, check if current prefix can xor to current tmpRes.
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, mask = 0, 0
        for i in range(31, -1, -1):
            # 1. get the high bits of each number
            mask |= (1 << i)
            tmpSet = set()
            for n in nums:
                tmpSet.add(n & mask)
            # 2. in each iteration, check if there are pair(s) whose left(high) bits can XOR to a bigger res.
            # i.e. check if current bit can be set to 1
            tmpRes = res | (1 << i)  # update current bit to 1
            for pre in tmpSet:
                if tmpRes ^ pre in tmpSet:
                    res = tmpRes
                    break
        return res

