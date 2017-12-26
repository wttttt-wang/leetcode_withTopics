"""
Remove K Digits
@ Greedy + Stack

"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res, cnt = [], 0
        listNum = list(num)
        for val in listNum:
            while cnt < k and res and res[-1] > val:
                res.pop()
                cnt += 1
            res.append(val)

        res = res[:len(listNum) - k]
        startInd = 0  # remove leading zeros!!!
        while startInd < len(res) and res[startInd] == '0':
            startInd += 1
        return "".join(res[startInd:]) if res and startInd < len(res) else '0'

