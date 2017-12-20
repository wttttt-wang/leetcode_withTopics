"""
Word Break II
@ Backtracking + dp
@ Note: Pruning unnecessary searching(recursion).  [This is really important!!!]
        For this problem, when left string cannot construct from wordDict, then it's impossible to construct a result.
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        # dp[i] stands for whether s[i:] can be construct by wordDict, to skip unnecessary recursion
        dp = self.canConstruct(s, wordDict)
        results = []
        self.helper(s, 0, wordDict, dp, [], results)
        return results

    def canConstruct(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # dp[i] = True if exists (s[i:j] in wordDict and dp[j])
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp

    def helper(self, s, startInd, wordDict, dp, result, results):
        if startInd == len(s):
            results.append(" ".join(result))
            return
        for i in range(startInd, len(s)):
            word = s[startInd: i + 1]
            if word in wordDict and dp[i + 1]:
                result.append(word)
                self.helper(s, i + 1, wordDict, dp, result, results)
                result.pop()


so = Solution()
print so.wordBreak("catsanddog", ["cats","and","dog","sand","cat"])
