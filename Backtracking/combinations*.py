"""
Combinations
@ Backtracking: This is a typical application for backtracking.
    Two conditions for backtrack: 1. the stack length is already k;
    2. the current value is too large for the rest slots to fit.
@ Note: Using ascending order to make sure the uniqueness of each combination
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        results = []
        stack = []
        x = 1   # x is the next element to add
        while True:
            if len(stack) == k:
                results.append(stack[:])
            if len(stack) == k or x > n - k + len(stack) + 1:
                if not stack:
                    return results
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

