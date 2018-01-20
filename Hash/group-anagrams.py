"""
Group Anagrams
@ Hash: The key point is to determine the hash key. Either by sorting or counting is acceptable.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        maps = {}
        for s in strs:
            tmp = self.mapTo(s)
            if tmp not in maps:
                maps[tmp] = []
            maps[tmp].append(s)
        return maps.values()

    def mapTo(self, s):
        res = [0] * 26
        for c in s:
            res[ord(c) - ord('a')] += 1
        return tuple(res)
