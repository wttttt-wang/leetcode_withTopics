"""
Max Sum of Rectangle No Larger Than K
@ Binary Search: O(min(m, n) ^ 2 * max(m, n) * log(max(m, n))), O(max(m, n)) space
  This can be divided into two sub-problems:
  1. sub-rectangle with maximum sum in a given matrix
  2. sub-array with maximum sum(<= target) in a given array
"""


class Solution(object):
    def maxSumSubmatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m > n:
            return self.maxSumSubmatrix(map(list, zip(*matrix)), target)
        res = -sys.maxint
        for r1 in range(m):
            sumArr = [0] * n
            for r2 in range(r1, m):
                # update sumArr: add matrix[r2]
                for j in range(n):
                    sumArr[j] += matrix[r2][j]

                curSum, tmpArr = 0, [0, sys.maxint]  # prefixSum
                for k in range(n):
                    curSum += sumArr[k]
                    ind = bisect.bisect_left(tmpArr, curSum - target)
                    res = max(res, curSum - tmpArr[ind])
                    bisect.insort(tmpArr, curSum)
        return res


