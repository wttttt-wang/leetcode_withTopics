"""
Max Points on a Line
@ Math + Hash: 1. Two points determine a line: y = a * x + b
               2. Fix one point, to get the max points by counting each a.
                  To avoid division related accuracy, use two number to stand for a. (Also avoid divide 0)
                  And we must consider same points.
@ Note: The way to calculate GCD
"""


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        res = 1
        for i in range(len(points)):
            cntMap, repeat, tmpMax = {}, 0, 0  # a1: {a2: cnt}, count for same point as points[i]
            for j in range(i + 1, len(points)):
                a1, a2 = points[i].x - points[j].x, points[i].y - points[j].y
                if a1 == 0 and a2 == 0:
                    repeat += 1  # Attention here: important!!!
                    continue
                gcd = self.getGcd(a1, a2)
                if gcd:
                    a1 /= gcd
                    a2 /= gcd
                if a1 not in cntMap:
                    cntMap[a1] = {a2: 1}
                else:
                    if a2 not in cntMap[a1]:
                        cntMap[a1][a2] = 0
                    cntMap[a1][a2] += 1
                tmpMax = max(tmpMax, cntMap[a1][a2])
            res = max(res, tmpMax + repeat + 1)
        return res

    def getGcd(self, a, b):
        return a if not b else self.getGcd(b, a % b)
