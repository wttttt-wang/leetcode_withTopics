"""
Largest Number
@ Sort: The sort way is really tricky
@ Corner case: start with '0'!!!!!!! --> indicates all zeros(For they are sorted)
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ""
        results = [str(ele) for ele in nums]
        results.sort(cmp=lambda x, y: -1 if x + y > y + x else 1)
        if results[0] == '0':   # This indicates that there are all zeros.
            return '0'   # Corner case: start with '0' --> obviously all 0s
        return "".join(results)
