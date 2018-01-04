"""
Kth Smallest Element in a Sorted Matrix
@ Binary Search on result
@ Note: The key point is the result should be in matrix. This may require some tricky on binary search:
        1. find the right-most val where there are (k - 1) numbers that are <= val
        2. how to return the final result? Need to consider duplicates
           --> return left if self.cntSmallerEqual(left, matrix) >= k else right
@ Also see 'Heap/Kth Smallest Element in a Sorted Matrix'
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0] or k <= 0:
            return None
        # binary search: O((m + n) * log(max - min)) time
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right - 1:
            mid = (right - left) / 2 + left
            cnt = self.cntSmallerEqual(mid, matrix)  # find right-most
            if cnt <= k - 1:
                left = mid
            else:
                right = mid
        # Attention: This is really tricky. When there are only two candidates, ......left...right...
        # Because we also count equal numbers in, so...
        return left if self.cntSmallerEqual(left, matrix) >= k else right

    def cntSmallerEqual(self, val, matrix):
        n = len(matrix[0])
        row, col = len(matrix) - 1, 0
        res = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= val:
                res += (row + 1)
                col += 1
            else:
                row -= 1
        return res

