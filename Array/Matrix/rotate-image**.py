"""
Rotate Image
@ Array: Two steps for rotate a matrix: 1. reverse up to down 2. swap the symmetry (swap matrix[i][j], matrix[j][i])
@ If rotate anticlockwise: 1. reverse left to right 2. swap the symmetry
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0] or len(matrix) != len(matrix[0]):
            return
        n = len(matrix)
        # step1: up-down
        for i in range(n / 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        # step2: symmetric swap
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
