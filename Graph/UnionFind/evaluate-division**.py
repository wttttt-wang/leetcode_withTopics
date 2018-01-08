"""
Evaluate Division
@ Union Find: More info refer to the code itself.
@ Note that we can use math formula to calculate the factor (as in function union).
"""


class UnionFind(object):
    def __init__(self, equations, values):
        self.parents, self.factor = {}, {}
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            if a not in self.parents:
                self.parents[a], self.factor[a] = a, 1
            if b not in self.parents:
                self.parents[b], self.factor[b] = b, 1
            self.union(a, b, values[i])

    def union(self, a, b, val):
        p1, v1 = self.find(a)  # a = p1 * v1
        p2, v2 = self.find(b)  # b = p2 * v2
        self.parents[p1] = p2  # a = val * b
        self.factor[p1] = (v2 / v1) * val   # --> p1 = (v2 / v1) * val * p2

    def find(self, a):
        if self.parents.get(a, "") == a:
            return a, 1
        p1, v1 = self.find(self.parents[a])
        val = self.factor[a] * v1
        self.factor[a], self.parents[a] = val, p1
        return p1, val

    def calcu(self, a, b):
        if a not in self.parents or b not in self.parents:
            return -1.0   # this is somewhat weired, for that 'x/x = -1.0' as defined in this problem
        p1, v1 = self.find(a)
        p2, v2 = self.find(b)
        if p1 != p2:
            return -1.0
        else:
            return v1 / v2


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations:
            return [-1] * len(queries)
        union = UnionFind(equations, values)
        results = []
        for a, b in queries:
            results.append(union.calcu(a, b))
        return results
