class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        queue = [""]
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        # Solution2: BFS
        for i in range(len(digits)):
            while queue and len(queue[0]) == i:
                tmp = queue.pop(0)
                for char in mapping[digits[i]]:
                    queue.append(tmp + char)
        return queue


so = Solution()
print so.letterCombinations("25")
