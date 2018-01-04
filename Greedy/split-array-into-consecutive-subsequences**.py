"""
Split Array into Consecutive Subsequences
@ Greedy: For a given number, first append to existing sub-sequence then as a starter.
          We maintain an 'appendNum' to hold all numbers that can be appended to check if a number can be as a appender.
          We maintain the 'freqs' to hold the current frequency of each number to check if a number can be as a starter.
"""


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        appendNum, freqs = {}, {}
        for v in nums:
            freqs[v] = freqs.get(v, 0) + 1
        for v in nums:
            if freqs[v] == 0:
                continue  # means this value has already been processed before
            freqs[v] -= 1
            # 1. check if can be appended, this is with higher priority (greedy)
            if appendNum.get(v, 0) > 0:
                appendNum[v] -= 1
                appendNum[v + 1] = appendNum.get(v + 1, 0) + 1
            # 2. check if can as a starter, need to update appendNum
            elif freqs.get(v + 1, 0) > 0 and freqs.get(v + 2, 0) > 0:
                appendNum[v + 3] = appendNum.get(v + 3, 0) + 1
                freqs[v + 1] -= 1
                freqs[v + 2] -= 1
            else:
                return False
        return True
