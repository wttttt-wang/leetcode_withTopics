"""
Substring with Concatenation of All Words
@ Two pointers (Sliding window)  +  Hash: Using w times sliding windows can cover all different combinations.
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        # sliding window, using Two pointers
        l, k, w = len(s), len(words), len(words[0])
        occurs, results = {}, []
        for w1 in words:
            occurs[w1] = occurs.get(w1, 0) + 1
        for i in range(w):
            # w times sliding window, will cover all different answers
            occurNum, currentOccurs = 0, {}  # reset count
            left = i
            for right in range(i, l - w + 1, w):
                tmpWord = s[right: right + w]
                if tmpWord in occurs:
                    currentOccurs[tmpWord] = currentOccurs.get(tmpWord, 0) + 1
                    occurNum += 1
                    while currentOccurs[tmpWord] > occurs[tmpWord]:
                        currentOccurs[s[left: left + w]] -= 1
                        left += w
                        occurNum -= 1
                    if occurNum == k:
                        results.append(left)
                        currentOccurs[s[left: left + w]] -= 1
                        occurNum -= 1
                        left += w
                else:
                    currentOccurs = {}
                    occurNum = 0
                    left = right + w
        return results


so = Solution()
print so.findSubstring("barfoobar", ["foo","bar"])
