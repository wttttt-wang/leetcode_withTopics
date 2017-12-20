"""
Restore IP Addresses
@ Note: This is actually not that hard.
@ Edge case: cannot start from '0' except only one element('0')
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.helper(s, 0, [], results)
        return results

    def helper(self, s, startInd, result, results):
        if startInd == len(s):
            if len(result) == 4:
                results.append(".".join(result))
            return
        if len(result) >= 4:
            return
        for i in range(3):
            if startInd + i >= len(s) or (i > 0 and s[startInd] == '0'):
                break
            tmp = s[startInd: startInd + i + 1]
            if int(tmp) > 255:
                continue
            result.append(tmp)
            self.helper(s, startInd + i + 1, result, results)
            result.pop()
