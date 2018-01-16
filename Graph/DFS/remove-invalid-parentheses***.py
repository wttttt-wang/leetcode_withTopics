"""
Remove Invalid Parentheses
@ DFS: 1. how to check if current substring is valid? --> cntLeft & cntRight.
          Once cntRight > cntLeft: should remove ')'
          cntLeft > cntRight finally: redundant '('
       2. remove duplicates: always remove the first one of a series of consecutive ')'
       3. to unify the situation of both '(' > ')' and '(' < ')'
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.helper(s, results, 0, 0, ['(', ')'])
        return results

    def helper(self, s, results, startInd, startY, parentheses):
        # startInd is the start index to cnt '(' and ')'
        # startY is the start index where we can remove redundant parentheses --> to remove duplicates
        # 1. use parentheses to unify the situation both '(' > ')' and '(' < ')'
        cnt = 0
        for i in range(startInd, len(s)):
            if s[i] == parentheses[0]:
                cnt += 1
            elif s[i] == parentheses[1]:
                cnt -= 1
            if cnt < 0:
                for k in range(startY, i + 1):
                    # pay attention to remove duplicates
                    if s[k] == parentheses[1] and (k == startY or s[k - 1] != parentheses[1]):
                        self.helper(s[:k] + s[k + 1:], results, i, k, parentheses)
                return
        if parentheses[0] == '(':
            self.helper(s[::-1], results, 0, 0, [')', '('])   # should reverse then check when '(' > ')'
        else:
            results.append(s[::-1])  # no invalid pattern


so = Solution()
print so.removeInvalidParentheses("(()")
