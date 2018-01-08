"""
Palindrome Pairs
@ Hash: The problem itself is not that difficult, the key point is the corner cases.
@ Corner cases: 1. Each word can only be used once.
                2. There may exists empty string, so it's important to consider each word whether palindrome as a whole.
                3. Pay attention to removing duplicates for results. (For simplify, u can use hashSet of course.)
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words or len(words) < 2:
            return []
        results, occurs = [], {}
        for i in range(len(words)):
            occurs[words[i]] = i
        for ind in range(len(words)):
            w = words[ind]
            for i in range(len(w) + 1):  # Attention that '+ 1', for words may contains empty string
                str1, str2 = w[:i], w[i:]
                if self.isPalin(str1):
                    rever = str2[::-1]
                    if rever in occurs and occurs[rever] != ind:  # the index so as not to repeat itself
                        results.append([occurs[rever], ind])
                # check len(str) != 2 is very important for removing duplicate for results
                if len(str2) != 0 and self.isPalin(str2):
                    rever = str1[::-1]
                    if rever in occurs and occurs[rever] != ind:
                        results.append([ind, occurs[rever]])
        return results

    def isPalin(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

