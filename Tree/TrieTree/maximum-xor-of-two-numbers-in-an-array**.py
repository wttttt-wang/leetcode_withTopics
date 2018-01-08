"""
Maximum XOR of Two Numbers in an Array
@ Trie Tree: The key point is for each number in nums, to search the max xor.
@ Note: 'BitManipulation/maximum-xor-of-two-numbers-in-an-array' is recommended for solving this problem.
"""


class TrieNode(object):
    def __init__(self):
        self.children = [None, None]  # 0bit, 1bit


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution2: trie tree
        # 1. initialize trie, insert num to tree
        root = TrieNode()
        for num in nums:
            self.insert(num, root)
        # 2. search for res
        res = 0
        for num in nums:
            tmpRes, tmpRoot = 0, root
            for i in range(31, -1, -1):
                currBit = (num >> i) & 1
                if tmpRoot.children[currBit ^ 1]:
                    tmpRes += (1 << i)
                    tmpRoot = tmpRoot.children[currBit ^ 1]
                else:
                    tmpRoot = tmpRoot.children[currBit]
            res = max(tmpRes, res)
        return res

    def insert(self, val, root):
        for i in range(31, -1, -1):
            currBit = (val >> i) & 1
            if not root.children[currBit]:
                root.children[currBit] = TrieNode()
            root = root.children[currBit]

