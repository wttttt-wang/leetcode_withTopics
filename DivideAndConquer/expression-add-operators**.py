"""
Expression Add Operators
@ Divide And Conquer, not like expression-add-operators, we cannot consider this problem by split the num.
@ Corner cases: 1. overflow (should be considered even though automatically handled by python)
                2. number cannot start with '0' apart from '0' itself
                3. need to consider the priority of calculators.
                        Btw, this solution handles priority with a really amazing way.
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        results = []
        self.helper(num, 0, "", results, 0, 0, target)
        return results

    def helper(self, num, start, result, results, calcuVal, formerVal, target):
        if start == len(num):
            if calcuVal == target:
                results.append(result)
            return
        for i in range(start, len(num)):
            if i != start and num[start] == '0':  # corner case: cannot start with '0'
                continue
            tmp = num[start:i + 1]  # for python, u don't need to consider overflow, but please pay attention to it.
            if start == 0:
                self.helper(num, i + 1, tmp, results, calcuVal + int(tmp), int(tmp), target)
            else:
                self.helper(num, i + 1, result + "+" + tmp, results, calcuVal + int(tmp), int(tmp), target)
                self.helper(num, i + 1, result + "-" + tmp, results, calcuVal - int(tmp), -int(tmp), target)
                self.helper(num, i + 1, result + "*" + tmp, results, calcuVal - formerVal + formerVal * int(tmp),
                            formerVal * int(tmp), target)  # need to calculate multiply first

