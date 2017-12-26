"""
Gas Station
@ Greedy  + Math: 1. Math: if sum(gas - cost) >= 0  -->  there exists a solution(exists an index that starts from this index
                     can make sure sum always >= 0)
                  2. Greedy: starts from i, sum first become negative at j
                     so: (diff[i] + diff[i + 1] + ... + diff[j]) < 0  & (diff[i] + ... + diff[j - 1]) >= 0
                     then: we only need to start from j when find next solution
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        ind, sumFromInd, total = 0, 0, 0
        for i in range(len(gas)):
            sumFromInd += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if sumFromInd < 0:
                ind = i + 1   # greedy here
                sumFromInd = 0
        return ind if total >= 0 else -1
